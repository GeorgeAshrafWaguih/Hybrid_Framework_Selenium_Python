import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:

    baseURL = ReadConfig.getApplicationURL()
    path = './/TestData/LoginData.xlsx'
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("**************** Test_002_DDT_Login ****************")
        self.logger.info("**************** Verifying Login DDT Test ****************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in excel:", self.rows)

        list_status = []

        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.expected = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.set_username(self.user)
            self.lp.set_password(self.password)
            self.lp.click_login()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.expected == "Pass":
                    self.logger.info("**** Passed ****")
                    self.lp.click_logout()
                    list_status.append("Pass")
                elif self.expected == "Fail":
                    self.logger.info("**** Failed ****")
                    self.lp.click_logout()
                    list_status.append("Fail")
            elif act_title != exp_title:
                if self.expected == "Pass":
                    self.logger.info("**** Failed ****")
                    list_status.append("Fail")
                elif self.expected == "Fail":
                    self.logger.info("**** Passed ****")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("**** Login DDT test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** Login DDT test failed ****")
            self.driver.close()
            assert False

        self.logger.info("****** End of Login DDT Test ******")