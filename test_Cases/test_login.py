import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login


class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homepagetitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login1":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("..//Screenshots//test_homepagetitle.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration1":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("..//Screenshots//test_login.png")
            self.driver.close()
            assert False

