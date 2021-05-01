from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.amazon.com/")

total_links = driver.find_elements(By.TAG_NAME, 'a')

for i in total_links:
    print(i.text)
    print(i.get_attribute('href'))
