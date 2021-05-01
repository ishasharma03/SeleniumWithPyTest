from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import xlrd
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.orangehrm.com/orangehrm-30-day-trial/')

url = driver.find_element(By.ID, 'Form_submitForm_subdomain')
fname = driver.find_element(By.ID, 'Form_submitForm_FirstName')
lname = driver.find_element(By.ID, 'Form_submitForm_LastName')
email = driver.find_element(By.ID, 'Form_submitForm_Email')
jobtitle = driver.find_element(By.ID, 'Form_submitForm_JobTitle')
empno = driver.find_element(By.ID, 'Form_submitForm_NoOfEmployees')
compname = driver.find_element(By.ID, 'Form_submitForm_CompanyName')
indus = driver.find_element(By.ID, 'Form_submitForm_Industry')
phno = driver.find_element(By.ID, 'Form_submitForm_Contact')
countt = driver.find_element(By.ID, 'Form_submitForm_Country')

wb = xlrd.open_workbook('DataFile.xlsx')
sheet1 = wb.sheet_by_name('Registration_Data')

rowCount = sheet1.nrows
coulumnCount = sheet1.ncols
print(rowCount, coulumnCount)

for curr_row in range(1, rowCount):
    urlValue = sheet1.cell_value(curr_row, 0)
    firstname = sheet1.cell_value(curr_row, 1)
    lastname = sheet1.cell_value(curr_row, 2)
    emailID = sheet1.cell_value(curr_row, 3)
    jobTitle = sheet1.cell_value(curr_row, 4)
    compnNme = sheet1.cell_value(curr_row, 5)
    phNo = sheet1.cell_value(curr_row, 6)
    totalEmp = sheet1.cell_value(curr_row, 7)
    indusName= sheet1.cell_value(curr_row, 8)
    country = sheet1.cell_value(curr_row, 9)

    url.clear()
    url.send_keys(urlValue)
    fname.clear()
    fname.send_keys(firstname)
    lname.clear()
    lname.send_keys(lastname)
    email.clear()
    email.send_keys(emailID)
    jobtitle.clear()
    jobtitle.send_keys(jobTitle)
    #empno.send_keys()
    compname.clear()
    compname.send_keys(compnNme)
    indus.clear()
    indus.send_keys(indusName)
    phno.clear()
    phno.send_keys(phNo)
    countt.clear()
    countt.send_keys(country)

    time.sleep(4)