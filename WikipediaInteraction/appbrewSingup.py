from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver_option = webdriver.ChromeOptions()
driver_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=driver_option)

driver.get('https://secure-retreat-92358.herokuapp.com')

first_name= driver.find_element(By.XPATH, value='/html/body/form/input[1]')
first_name.send_keys('Ferdouse')

last_name=driver.find_element(By.XPATH,value='/html/body/form/input[2]')
last_name.send_keys('Bhuiya')

email_field=driver.find_element(By.XPATH,value='/html/body/form/input[3]')
email_field.send_keys('ferdousbhuiya.ihs@gmail.com')

sign_up_button = driver.find_element(By.XPATH,value='/html/body/form/button')
sign_up_button.send_keys(Keys.ENTER)