from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="D:\Drivers\chromedriver_win32\chromedriver.exe")

#driver.maximize_window()

driver.get("https://www.seleniumeasy.com/test/input-form-demo.html")

time.sleep(10)

#To find all the input boxes present in web page

IB = driver.find_elements_by_class_name('form-control')

print(len(IB))

#How to provide value in text box

driver.find_element_by_name("first_name").send_keys("Isha")
driver.find_element_by_name("last_name").send_keys("Sharma")

#How to get the status

#is_displayed
#is_selected
#is_enabled