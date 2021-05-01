from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.maximize_window()
# driver.get('https://app.hubspot.com/login')
# print(driver.title)
#
# wait = WebDriverWait(driver, 15)
# emailID = wait.until(ec.presence_of_element_located((By.ID, 'username')))
# emailID.send_keys('abc@gmail.com')
# print(driver.title)

'''
title_is
title_contains
url_contains
url_to_be
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present
'''

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.freshworks.com/')

wait = WebDriverWait(driver, 15)
footer_links = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul.footer-nav li')))
print(len(footer_links))

for e in footer_links:
    print(e.text)
