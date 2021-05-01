from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="D:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.reddit.com/")

print(driver.get_cookies())

driver.add_cookie({'name':'isha', 'domain':'reddit.com', 'value':'python'})
#print(driver.get_cookies())

cookies = driver.get_cookies()
for cook in cookies:
    print(cook)
