from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://www.linkedin.com/jobs/')

signin_button = driver.find_element(By.XPATH, value='/html/body/nav/div/a[2]').click()
time.sleep(3)
user_name = driver.find_element(By.XPATH, value="/html/body/div/main/div[2]/div[1]/form/div[1]/input")
password =driver.find_element(By.XPATH, value='/html/body/div/main/div[2]/div[1]/form/div[2]/input')
user_name.send_keys('bvmghgjhmgkjgk@gmail.com')
password.send_keys('khukgjj)goipkhbjhfgd')
time.sleep(3)
driver.find_element(By.XPATH, value="/html/body/div/main/div[2]/div[1]/form/div[3]/button").click()

driver.find_element(By.XPATH, value='//*[@id="jobs-search-box-keyword-id-ember28"]').click()
input("Solve the captcha")
driver.find_element(By.ID, value='jobs-search-box-keyword-id-ember28').send_keys('Marketing executive')
driver.find_element(By.XPATH,value='//*[@id="jobs-search-box-location-id-ember28"]').send_keys('Florida',Keys.ENTER)
time.sleep(5)

driver.find_element(By.CLASS_NAME,value="artdeco-button__text").click()
#driver.find_element(By.CLASS_NAME,value='artdeco-button__text').click()




# driver.find_element(By.XPATH, value='//*[@id="ember434"]/span').click()
# driver.find_element(By.XPATH,value='//*[@id="radio-button-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3962066225-2871959978-multipleChoice"]/div[1]/label').click()
# driver.find_element(By.XPATH,value='//*[@id="ember443"]/span').click()
# driver.find_element(By.XPATH,value='//*[@id="ember453"]/span').click()

#jobs-search-box-keyword-id-ember28