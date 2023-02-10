import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import Login
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.logger.info("******** Test_003_AddCustomer ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("******** Login Successful ********")

        self.logger.info("******** Starting Adding Customer Test ********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.addcust.clickOnAddnew()

        self.logger.info("******** Filling Customer Info ********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("George")
        self.addcust.setLastName("Ashraf")
        self.addcust.setDob("1/10/1988")        # Format D / MM / YYYY
        self.addcust.setCompanyName("QACompany")
        self.addcust.setAdminContent("This is for testing")
        self.addcust.clickOnSave()

        self.logger.info("******** Saving Customer Info ********")

        self.logger.info("******** Add Customer Validation started ********")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)

        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("******** Add Customer Test Passed ********")
        else:
            self.driver.save_screenshot("..//Screenshots//test_addCustomer.png")
            self.logger.error("******** Add Customer Test Failed ********")
            assert False

        self.driver.close()
        self.logger.info("******** Ending Add Customer Test ********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


