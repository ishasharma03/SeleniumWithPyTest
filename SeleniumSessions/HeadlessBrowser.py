from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

options = webdriver.ChromeOptions()
options.headless = True
#driver = webdriver.Chrome(executable_path="dfxgfhfgjhgk", options=options)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(5)

driver.get("https://amazon.in")
print(driver.title)
