from selenium import webdriver
from selenium.webdriver.common.by import By


option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=option)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_number = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/a[1]').text
print(f"Total number of articles: {article_number}")