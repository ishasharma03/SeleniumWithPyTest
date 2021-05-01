from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

# emp_nos = driver.find_element(By.ID, "Form_submitForm_NoOfEmployees")
# select = Select(emp_nos)
# select.select_by_value("26 - 50")
#
# emp_coun = driver.find_element_by_id("Form_submitForm_Country")
# select_coun = Select(emp_coun)
# select_coun.select_by_visible_text("India")

# If there are many drop down menus in page then we have to call Select again and again which is not good/
#intead create a create a function and call it.

# def dropdownSelector(theElement, theValue):
#     selectValue = Select(theElement)
#     selectValue.select_by_value(theValue)
#
#
# dropdownSelector(driver.find_element(By.ID, "Form_submitForm_NoOfEmployees"), "26 - 50")
# dropdownSelector(driver.find_element_by_id("Form_submitForm_Country"), "India")
#
# emp_coun = driver.find_element_by_id("Form_submitForm_Country")
# selectOptions = Select(emp_coun)
# sel = selectOptions.options
#
# for option in sel:
#     print(option.text)

country_list = driver.find_elements_by_xpath("//select[@name='Country']/option")
for country in country_list:
    print(country.text)
