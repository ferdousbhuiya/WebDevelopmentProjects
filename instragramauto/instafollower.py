import time
import os
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from dotenv import load_dotenv

load_dotenv()


class InstaFollower:
    def __init__(self, driver, username1, password, similar_account):
        self.driver = driver
        self.username1 = username1
        self.password = password
        self.similar_account = similar_account

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')

        # Wait for the login fields to load
        try:
            username_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'username'))
            )
        except TimeoutException:
            print("Login page did not load properly.")
            return

        password_field = self.driver.find_element(By.NAME, 'password')

        # Clear any autofilled text in the username field using backspace key
        username_field.send_keys(Keys.CONTROL + "a")
        username_field.send_keys(Keys.BACKSPACE)
        username_field.send_keys(self.username1)

        # Clear any autofilled text in the password field using backspace key
        password_field.send_keys(Keys.CONTROL + "a")
        password_field.send_keys(Keys.BACKSPACE)
        password_field.send_keys(self.password)

        # Wait for the login button and click it
        time.sleep(9.8)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()

        # Wait for the main page to load
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]'))
            )
        except TimeoutException:
            print("Login failed or took too long.")

    def find_followers(self):
        time.sleep(10.2)
        # Navigate to the similar account's followers page
        self.driver.get(f"https://www.instagram.com/{self.similar_account}/followers")

        time.sleep(10.1)
        # The xpath of the modal that shows the followers will change over time. Update yours accordingly.
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        try:
            modal = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, modal_xpath))
            )
        except TimeoutException:
            print("Followers modal did not load.")
            return

        for _ in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follows(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                cancel_button.click()


