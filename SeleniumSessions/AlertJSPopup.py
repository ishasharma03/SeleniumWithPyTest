from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
# driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
#
# driver.find_element(By.CLASS_NAME, 'signinbtn').click()
#
# alert = driver.switch_to.alert
# print(alert.text)
# alert.accept()
#driver.switch_to.default_content()

driver.get("http://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()

alert = driver.switch_to.alert
print(alert.text)
alert.send_keys('Alohaaaa')
alert.accept()

driver.switch_to.default_content()

driver.quit()