from selenium.webdriver.common.by import By


class SearchCustomer:
    # Search Customer Page
    txtEmail_id = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"
    tblSearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, mail):
        self.driver.find_element(By.ID, self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(mail)

    def setFirstName(self, fname):
        self.driver.find_element(By.ID, self.txtFirstName_id).clear()
        self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.ID, self.txtLastName_id).clear()
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.ID, self.btnSearch_id).click()

    # def getNoOfRows(self):
    #     return len(self.driver.find_element(By.XPATH, self.tableRows_xpath))
    #
    # def getNoOfColumns(self):
    #     return len(self.driver.find_element(By.XPATH, self.tableColumns_xpath))

    # def searchCustomerByEmail(self, email):
    #     flag = False
    #     for r in range(1,self.getNoOfRows()+1):
    #         table = self.driver.find_element(By.XPATH, self.table_xpath)
    #         emailID = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text()
    #         if emailID == email:
    #             flag = True
    #             break
    #         return flag

    # def searchCustomerByName(self, Name):
    #     flag = False
    #     for r in range(1, self.getNoOfRows()+1):
    #         table = self.driver.find_element(By.XPATH, self.table_xpath)
    #         name = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text()
    #         if name == Name:
    #             flag = True
    #             break
    #         return flag

    def searchCustomerByEmail(self, email):
        flag = False
        emailResult = self.driver.find_element(By.XPATH, '//*[@id="customers-grid"]/tbody/tr/td[2]').text
        if emailResult == email:
            flag = True
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        nameResult = self.driver.find_element(By.XPATH, '//*[@id="customers-grid"]/tbody/tr/td[3]').text
        if nameResult == Name:
            flag = True
        return flag