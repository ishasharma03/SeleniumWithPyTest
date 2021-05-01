from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
time.sleep(3)

driver.find_element(By.ID, "justAnInputBox").click()
time.sleep(3)

ele_list = driver.find_elements(By.CSS_SELECTOR, "span.comboTreeItemTitle")

def selectValuesInDropdown(theElementList, *theValue):
    for value in theValue:
        if value == 'all':
            for ele in theElementList:
                ele.click()
        else:
            for ele in theElementList:
                if ele.text == value:
                    ele.click()
                    break



# def selectValuesInDropdown(theElementList, *theValue):
#     if theValue == 'all':
#         try:
#             for ele in theElementList:
#                 ele.click()
#         except Exception as err:
#             print(err)
#     else:
#         for ele in theElementList:
#             for value in theValue:
#                 if ele.text == value:
#                     ele.click()
#                     break

#selectValuesInDropdown(ele_list, 'all')
selectValuesInDropdown(ele_list, "choice 2", "choice 6 2 1", "choice 7")
# selectValuesInDropdown(ele_list, "choice 6 2 1")
#selectValuesInDropdown(ele_list, "choice 7")
#selectValuesInDropdown(ele_list, "all")

# for ele in ele_list:
#     print(ele.text)
#     if ele.text == "choice 2":
#         ele.click()
#         break
