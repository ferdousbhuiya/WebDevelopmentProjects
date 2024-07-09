import os
from selenium import webdriver
from dotenv import load_dotenv
from instafollower import InstaFollower

load_dotenv()

SIMILAR_ACCOUNT = os.getenv('SIMILAR_ACCOUNT')
USERNAME1 = os.getenv('USERNAME1')
PASSWORD = os.getenv('PASSWORD')

if not SIMILAR_ACCOUNT or not USERNAME1 or not PASSWORD:
    print("Please make sure that SIMILAR_ACCOUNT, USERNAME1, and PASSWORD are set in your .env file.")
else:
    # Initialize the webdriver
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    instafollower = InstaFollower(driver, USERNAME1, PASSWORD, SIMILAR_ACCOUNT)

    instafollower.login()
    instafollower.find_followers()
    instafollower.follows()

    # Do not quit the driver if you want to keep the browser open
    # driver.quit()
