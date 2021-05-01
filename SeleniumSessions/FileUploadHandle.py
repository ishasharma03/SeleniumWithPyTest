from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("http://cgi-lib.berkeley.edu/ex/fup.html")

driver.find_element(By.NAME, 'upfile').send_keys('D:\IMP_DOCS\CV\IshaSharma_Resume.docx')
# this will only work when type='file' is present

driver.find_element(By.XPATH, '/html/body/form/input[3]').click()