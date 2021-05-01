from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# options = Options()
# options.add_argument('--allow-running-insecure-content')
# options.add_argument('--ignore-certificate-errors')
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# desired_capabilities = DesiredCapabilities().CHROME.copy()
# desired_capabilities['acceptInsecureCerts'] = True
# driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=desiredCapabilities)

options = Options()
options.set_capability('acceptInsecureCerts', True)
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.implicitly_wait(10)

driver.get('https://expired.badssl.com/')
print(driver.find_element(By.TAG_NAME, 'h1').text)
