from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("http://www.londonfreelance.org/courses/frames/index.html")

#driver.switch_to.frame(2) # frame index
#driver.switch_to.frame('main') #frame name
frame_ele = driver.find_element(By.NAME, "main") #by creating frame element
driver.switch_to.frame(frame_ele)
header = driver.find_element(By.CSS_SELECTOR, 'body > h2')
print(header.text)

driver.switch_to.default_content()
driver.switch_to.parent_frame()
