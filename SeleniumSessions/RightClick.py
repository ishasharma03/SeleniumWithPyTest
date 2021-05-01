from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")

right_click = driver.find_element(By.CSS_SELECTOR, 'p span')
act_chain = ActionChains(driver)
act_chain.context_click(right_click).perform()

time.sleep(2)

menu_options = driver.find_elements(By.CSS_SELECTOR, 'ul span')
for options in menu_options:
    print(options.text)
    if options.text == 'Copy':
        options.click()
        break

time.sleep(2)

driver.quit()