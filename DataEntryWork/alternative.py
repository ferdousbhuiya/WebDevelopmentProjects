import os
import re
import time
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Load environment variables
load_dotenv()

# Initialize Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()

try:
    # Fetch Zillow Clone webpage
    url = 'https://appbrewery.github.io/Zillow-Clone/'
    response = requests.get(url)
    response.raise_for_status()

    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract rent prices
    rent_prices = soup.find_all(name='span', class_='PropertyCardWrapper__StyledPriceLine')

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
    property_wrappers = soup.find_all('div', class_='StyledPropertyCardDataWrapper')

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

    # Save extracted data to CSV file
    # output_file = 'property_data.csv'
    # with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    #     fieldnames = ['Price', 'Address', 'Link']
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #     writer.writeheader()
    #     for i in range(len(cleaned_rent_prices)):
    #         writer.writerow({'Price': cleaned_rent_prices[i], 'Address': addresses[i], 'Link': links[i]})

    # Assuming the Google Form has fields named 'price_field', 'address_field', and 'link_field'
    form_url = 'https://forms.gle/vE1qSBByfuQx4RxY8'
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
    driver.quit()
    print("Extraction is completed. Data saved to 'property_data.csv'.")
