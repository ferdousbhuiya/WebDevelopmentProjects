import os
from dotenv import load_dotenv
from selenium import webdriver
from twitterBot import TwitterBot

# Load environment variables
load_dotenv()

# Get environment variables
TWITTEREMAIL = os.getenv('TWITTEREMAIL')
PASSWORD = os.getenv('PASSWORD')
USERNAME1 = os.getenv('USERNAME')
PROMISED_DOWN = 150
PROMISED_UP = 50

# Initialize the WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()

#Create an instance of the TwitterBot
bot = TwitterBot(driver, TWITTEREMAIL, PASSWORD, PROMISED_DOWN, PROMISED_UP, USERNAME1)
bot.get_internet_speed()
bot.tweet_at_provider()

# Quit the driver
driver.quit()
print(USERNAME1,PASSWORD)