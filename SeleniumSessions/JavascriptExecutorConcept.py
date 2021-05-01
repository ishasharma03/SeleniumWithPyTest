from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://classic.crmpro.com/index.html')
# mobile_ele = driver.find_element(By.LINK_TEXT, 'Mobiles')

# driver.execute_script("arguments[0].click();", mobile_ele)

# title = driver.execute_script("return document.title")
# print(title)

#driver.execute_script("history.go(0);") #will refresh the page

#driver.execute_script("alert('Hello Selenium learner');")# this will generate alert

# innertext = driver.execute_script("return document.documentElement.innerText;")# will give all text used for web elements
# print(innertext)

# driver.execute_script("arguments[0].style.border = '3px solid red'", mobile_ele)

# form = driver.find_element(By.ID, 'hs-login')
# driver.execute_script("arguments[0].style.border = '3px solid red'", form)

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #will scroll down the end of page
# driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);") #will scroll up the page from down

# forgot_pass = driver.find_element(By.LINK_TEXT, "Forgot Password?")
# IandE = driver.find_element(By.XPATH, "//*[@id='details']/div/div/div[2]/div/div[6]/h3")
# driver.execute_script("arguments[0].scrollIntoView(true);", IandE)
#
# print(driver.execute_script("return navigator.userAgent;"))

#send keys
driver.execute_script("document.getElementById('username').value = 'abc@gmail.com")
