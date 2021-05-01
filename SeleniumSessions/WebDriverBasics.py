from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.google.com/")

driver.implicitly_wait(5)

driver.find_element_by_name("q").send_keys("Isha")

matchList = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li span')

print(len(matchList))

for i in matchList:
    if i.text!="":
        print(i.text)
