from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
#provide credentials separated by : in url itself after https
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
