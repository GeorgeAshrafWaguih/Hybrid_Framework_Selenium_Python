from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/")
username = driver.find_element(By.XPATH, '//*[@id="Email"]')
username.clear()
username.send_keys("admin@yourstore.com")
password = driver.find_element(By.XPATH, '//*[@id="Password"]')
password.clear()
password.send_keys("admin")
login = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button")
login.click()
lnkCustomers_menu_xpath = driver.find_element(By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p")
lnkCustomers_menu_xpath.click()
customermenuitem = driver.find_element(By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p")
customermenuitem.click()
Firstname = driver.find_element(By.ID, "SearchFirstName")
Firstname.send_keys("Victoria")
searchbutton = driver.find_element(By.ID, "search-customers")
searchbutton.click()
time.sleep(3)
result_name = driver.find_element(By.XPATH, '//*[@id="customers-grid"]/tbody/tr/td[3]')
print(result_name.text)
# addnewcustomer = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/form[1]/div/div/a")
# addnewcustomer.click()
# emailfield = driver.find_element(By.ID, "Email")
# emailfield.send_keys("test")
# passwordfield = driver.find_element(By.ID, "Password")
# passwordfield.send_keys("test")
# customerRole = driver.find_element(By.XPATH, '//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/div')
# customerRole.click()
# time.sleep(3)
# #listitemAdmin = driver.find_element(By.XPATH, '//*[@id="SelectedCustomerRoleIds_listbox"]/li[1]')
# #listitemAdmin.click()
#
# listitemVendor = driver.find_element(By.XPATH, '//*[@id="SelectedCustomerRoleIds_listbox"]/li[5]')
# #customerRole.click()
# time.sleep(3)
# listitemVendor.click()
# dob = driver.find_element(By.XPATH, '//*[@id="DateOfBirth"]')
# dob.click()
# company = driver.find_element(By.ID, "Company")
# company.send_keys("Test")
# save = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/form/div[1]/div/button[1]')
# save.click()
#
# time.sleep(3)