from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="D:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")

ele_usename = driver.find_element_by_name("userName")
ele_pwd = driver.find_element_by_name("password")

print((ele_usename).is_enabled())
print((ele_pwd).is_enabled())

print((ele_usename).is_displayed())
print((ele_pwd).is_displayed())

ele_usename.send_keys("mercury")
ele_pwd.send_keys("mercury")

driver.find_element_by_name("submit").click()
driver.find_element_by_link_text("Flights").click()

# roundTripRadio = driver.find_element_by_css_selector("input[value=roundtrip]")
# oneWayRadio = driver.find_element_by_css_selector("input[value=oneway]")
#
# print("Status of roundtrip radio button is", roundTripRadio.is_selected())
# print("Status of oneway radio button is", oneWayRadio.is_selected())
#
# driver.close()