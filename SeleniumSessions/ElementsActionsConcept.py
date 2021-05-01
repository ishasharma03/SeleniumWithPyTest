from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://classic.crmpro.com/index.html")


username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
loginButton = driver.find_element(By.CLASS_NAME, 'btn.btn-small')

act_chain = ActionChains(driver)
act_chain.send_keys_to_element(username, 'ishasharma1415@gmail.com').perform()
act_chain.send_keys_to_element(password, 'test123')
act_chain.click(loginButton).perform()
time.sleep(3)

driver.quit()