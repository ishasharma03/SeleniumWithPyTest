from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.maximize_window()

driver.get("https://www.spicejet.com/")
time.sleep(3)

ele_login = driver.find_element(By.ID, 'ctl00_HyperLinkLogin')
act_chains = ActionChains(driver)
act_chains = ActionChains(driver)
act_chains.move_to_element(ele_login).perform()

spice_members = driver.find_element(By.LINK_TEXT, "SpiceClub Members")
act_chains.move_to_element(spice_members).perform()

mem_login = driver.find_element(By.LINK_TEXT, "Member Login")
mem_login.click()

time.sleep(2)
driver.quit()