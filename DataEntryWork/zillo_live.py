import os
import re
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Custom User-Agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

# Initialize Chrome WebDriver with custom User-Agent
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={user_agent}")
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()

try:
    # Access the Zillow page
    url = 'https://www.zillow.com/sunrise-fl/rentals/?searchQueryState=%7B"pagination"%3A%7B%7D%2C"mapBounds"%3A%7B"north"%3A26.219249711500723%2C"south"%3A26.07625085201194%2C"east"%3A-80.19997580615234%2C"west"%3A-80.39292319384765%7D%2C"isMapVisible"%3Atrue%2C"filterState"%3A%7B"fsba"%3A%7B"value"%3Afalse%7D%2C"fsbo"%3A%7B"value"%3Afalse%7D%2C"nc"%3A%7B"value"%3Afalse%7D%2C"fore"%3A%7B"value"%3Afalse%7D%2C"cmsn"%3A%7B"value"%3Afalse%7D%2C"auc"%3A%7B"value"%3Afalse%7D%2C"fr"%3A%7B"value"%3Atrue%7D%2C"ah"%3A%7B"value"%3Atrue%7D%2C"mp"%3A%7B"max"%3A1400%7D%2C"price"%3A%7B"max"%3A271648%7D%2C"beds"%3A%7B"min"%3A1%7D%2C"baths"%3A%7B"min"%3A1%7D%7D%2C"isListVisible"%3Atrue%2C"mapZoom"%3A12%2C"regionSelection"%3A%5B%7B"regionId"%3A54628%2C"regionType"%3A6%7D%5D%7D'
    driver.get(url)

    # Wait for the page to load
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Get page source and parse HTML content using BeautifulSoup
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Print page source for verification (optional)
    #print(soup.prettify())

    # Extract rent prices
    #rent_prices = soup.find_all(name='span', class_='PropertyCardWrapper__StyledPriceLine')
    rent_prices = soup.find_all(By.XPATH, value='/html/body/div[1]/div/div[2]/div/div/div/div[1]/div[3]/ul/li[1]/div/div/article/div/div[1]/div[2]/div/span')

    # Clean the rent prices
    cleaned_rent_prices = []
    for span in rent_prices:
        price_text = span.get_text()
        # Use regular expression to extract the numeric value
        match = re.search(r'\$\d+(?:,\d+)?', price_text)
        if match:
            cleaned_price = match.group(0)  # Extract the matched dollar amount
            cleaned_rent_prices.append(cleaned_price)

    # Extract property addresses and links
    #property_wrappers = soup.find_all('div', class_='StyledPropertyCardDataWrapper')
    property_wrappers = soup.find_all(By.XPATH, value='/html/body/div[1]/div/div[2]/div/div/div/div[1]/div[3]/ul/li[1]/div/div/article/div/div[1]/div[3]')

    # Prepare lists for addresses and links
    addresses = []
    links = []

    # Iterate through each property wrapper to extract address and link
    for wrapper in property_wrappers:
        # Find the <a> element inside the current wrapper
        link_element = wrapper.find('a', class_='StyledPropertyCardDataArea-anchor')

        # Extract the address
        address = link_element.find('address').get_text(strip=True)
        addresses.append(address)

        # Extract the href attribute (link)
        href = link_element.get('href')
        links.append(href)

    # Print the results for each property (for verification)
    for i in range(len(cleaned_rent_prices)):
        print("Price:", cleaned_rent_prices[i])
        print("Address:", addresses[i])
        print("Link:", links[i])
        print()  # Separate each property with a blank line
    form_url = 'https://forms.gle/Ap2RiAewAaLys89s6'
    driver.get(form_url)
    time.sleep(10)  # Give time for the form to fully load (you can adjust this as needed)

    for i in range(len(cleaned_rent_prices)):
        # Fill in the price
        price_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        )
        price_field.send_keys(cleaned_rent_prices[i])

        # Fill in the address
        address_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        )
        address_field.send_keys(addresses[i])

        # Fill in the link
        link_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", link_field)
        link_field.send_keys(links[i])

        # Submit the form (assuming there's a submit button with class 'submit_button')
        submit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span'))
        )
        submit_button.click()

        submit_again = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'))
        )
        submit_again.click()

finally:
    # Quit the WebDriver session
    #driver.quit()
    driver.get('https://docs.google.com/spreadsheets/d/1hYr8k5r3T4g5zkU5bzE4P_QG6sDHHi1XrnLLlxKIwm4/edit?usp=sharing')
    print("Extraction is completed.")
