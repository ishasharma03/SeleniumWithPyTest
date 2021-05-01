from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="D:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")

driver.implicitly_wait(10) # wait for every element, has to be specified once
#time out = 10
#dynamic wait
#will be applied for all web elements
#global wait
#find element/elements
# not for title,url,alerts no web element

print(driver.title)

assert 'Welcome: Mercury Tours' in driver.title

ele_usename = driver.find_element_by_name("userName")
ele_pwd = driver.find_element_by_name("password")

ele_usename.send_keys("mercury")
ele_pwd.send_keys("mercury")

driver.close()