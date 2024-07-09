import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TwitterBot:
    def __init__(self, driver, email, username1, password, promised_down, promised_up):
        self.driver = driver
        self.email = email
        self.username1 = username1
        self.password = password
        self.promised_down = promised_down
        self.promised_up = promised_up
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net')
        time.sleep(20)
        #start_button = self.driver.find_element()
        start_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'))
        )
        start_button.click()

        time.sleep(50)  # Wait for the speed test to complete, adjust as necessary

        self.down = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                            '3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'))
        ).text
        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                           '3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        speed = [self.down, self.up]
        print(speed)
        return speed

    def tweet_at_provider(self):
        self.driver.get('https://x.com/i/flow/login')
        print(self.username1)
        print(self.password)
        username_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'))
        )
        username_field.send_keys(self.username1)

        next_button = self.driver.find_element(By.XPATH,
                                               '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div')
        next_button.click()

        password_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                            '2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'))
        )
        password_field.send_keys(self.password)

        login_button = self.driver.find_element(By.XPATH,
                                                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                '2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div')
        login_button.click()

        tweet_compose = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
                                            '3]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                            '1]/div/div/div/div/div/div/div/div/div/div/div/div['
                                            '1]/div/div/div/div/div/div[2]/div/div/div/div'))
        )

        tweet = f"AT&T, why is my internet speed {self.down}down/{self.up}up when I pay for {self.promised_down}down/{self.promised_up}up?"
        tweet_compose.send_keys(tweet)

        tweet_button = self.driver.find_element(By.XPATH,
                                                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
                                                '3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div['
                                                '2]/div/div/div/button/div/span/span')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()
