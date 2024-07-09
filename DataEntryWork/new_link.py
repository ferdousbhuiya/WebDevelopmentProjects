from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Custom User-Agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

# Initialize Chrome WebDriver with custom User-Agent
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={user_agent}")
options.add_experimental_option('detach', True)

# Path to your ChromeDriver
driver = webdriver.Chrome(options=options)

try:
    # Access the Zillow page
    url = 'https://www.zillow.com/sunrise-fl/rentals/?searchQueryState=%7B"pagination"%3A%7B%7D%2C"mapBounds"%3A%7B"north"%3A26.219249711500723%2C"south"%3A26.07625085201194%2C"east"%3A-80.19997580615234%2C"west"%3A-80.39292319384765%7D%2C"isMapVisible"%3Atrue%2C"filterState"%3A%7B"fsba"%3A%7B"value"%3Afalse%7D%2C"fsbo"%3A%7B"value"%3Afalse%7D%2C"nc"%3A%7B"value"%3Afalse%7D%2C"fore"%3A%7B"value"%3Afalse%7D%2C"cmsn"%3A%7B"value"%3Afalse%7D%2C"auc"%3A%7B"value"%3Afalse%7D%2C"fr"%3A%7B"value"%3Atrue%7D%2C"ah"%3A%7B"value"%3Atrue%7D%2C"mp"%3A%7B"max"%3A1400%7D%2C"price"%3A%7B"max"%3A271648%7D%2C"beds"%3A%7B"min"%3A1%7D%2C"baths"%3A%7B"min"%3A1%7D%7D%2C"isListVisible"%3Atrue%2C"mapZoom"%3A12%2C"regionSelection"%3A%5B%7B"regionId"%3A54628%2C"regionType"%3A6%7D%5D%7D'
    driver.get(url)

    # Wait for the page to load
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Perform actions or extract data as needed
    print("Page loaded successfully")

finally:
    # Close the driver
    driver.quit()
