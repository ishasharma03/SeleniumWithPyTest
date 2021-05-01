from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="D:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.linkedin.com/in/ishasharma0724/")

print(driver.title)
print(driver.page_source)
print(driver.current_url)

driver.close()

# driver = webdriver.Firefox(executable_path="D:\Drivers\geckodriver-v0.29.1-win64\geckodriver.exe")
#
# driver.get("https://www.linkedin.com/in/ishasharma0724/")
#
# print(driver.title)
#
# driver.close()