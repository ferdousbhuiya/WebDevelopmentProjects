from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=option)

driver.get('https://orteil.dashnet.org/experiments/cookie/')

clicked = driver.find_element(By.CSS_SELECTOR, value='#money').text
rate = driver.find_element(By.ID, value='cps').text
grandmother = driver.find_element(By.ID, value='buyGrandma')
factory = driver.find_element(By.ID, value="buyFactory")
cookie = driver.find_element(By.ID, value='cookie')
for i in range(1000):
    cookie.click()
    if int(clicked)==100:
        grandmother.click()

print(rate)

#driver.quit()
