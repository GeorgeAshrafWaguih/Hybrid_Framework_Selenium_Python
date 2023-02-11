import pytest
import time
from pageObjects.LoginPage import Login
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("******** SearchCustomerByName_005 ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("******** Login successful ********")

        self.logger.info("******** Starting Search Customer by Email ********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("******** Searching Customer By Email ********")

        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(3)
        status = searchcust.searchCustomerByName("Victoria Terces")
        self.driver.close()
        assert status
        self.logger.info("******** SearchCustomerByName_005 Finished ********")
