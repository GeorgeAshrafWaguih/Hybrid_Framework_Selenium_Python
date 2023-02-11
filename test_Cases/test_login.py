import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_homepagetitle(self, setup):

        self.logger.info("**************** Test_001_Login ****************")
        self.logger.info("**************** Verifying Home Page Title ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.driver.close()
            self.logger.info("**************** Home page title test passed ****************")
            assert True
        else:
            self.driver.save_screenshot("..//Screenshots//test_homepagetitle.png")
            self.driver.close()
            self.logger.error("**************** Home page title test failed ****************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("**************** Verifying Login Test ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("**************** Login test passed ****************")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("..//Screenshots//test_login.png")
            self.driver.close()
            self.logger.error("**************** Login test failed ****************")
            assert False

