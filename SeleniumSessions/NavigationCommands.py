from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="D:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.python.org")

print(driver.title)

driver.get("http://pavantestingtools.blogspot.in/")

print(driver.title)

driver.back()

print(driver.title)

driver.forward()

print(driver.title)

driver.refresh()

driver.close()