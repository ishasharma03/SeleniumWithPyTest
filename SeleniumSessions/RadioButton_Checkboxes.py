from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="D:\Drivers\chromedriver_win32\chromedriver.exe")

# driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")
#
# total_count = driver.find_elements_by_class_name("checkbox")
# print(len(total_count))
# status = driver.find_element(By.ID, "isAgeSelected").is_selected()
# print(status)
#
# driver.find_element(By.ID, "isAgeSelected").click()


driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")

time.sleep(10)

total_count_radio = driver.find_elements(By.CLASS_NAME, 'radio-inline')
print(len(total_count_radio))
status_radio = driver.find_element_by_class_name("radio-inline").find_element_by_css_selector("input[value='Male']").is_selected()

print(status_radio)

driver.find_element_by_class_name("radio-inline").find_element_by_css_selector("input[value='Male']").click()

status_radio_1 = driver.find_element_by_class_name("radio-inline").find_element_by_css_selector("input[value='Female']").is_selected()

print(status_radio_1)

print(status_radio)

#driver.find_element_by_class_name("radio-inline").find_element_by_css_selector("input[value='5 - 15']").click()

#driver.find_element_by_class_name("radio-inline").find_element_by_css_selector("input[value='Female']").find_element_by_name("optradio").click()



