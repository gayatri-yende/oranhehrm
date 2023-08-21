import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

from pageObjects.LoginPage import loginPage
from Utilities.readproperties import Readconfig
from Utilities.Logger import LogGenrator

class Test_Logins:

    Url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenrator.loggen()

    def test_login_params_004(self, setup, getDataforlogin):
        self.driver = setup
        self.log.info("test_login_002 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this Url-->" +self.Url)
        self.lp = loginPage(self.driver)
        self.log.info("Entering Username-->" + getDataforlogin[0])
        self.lp.Enter_UserName(getDataforlogin[0])
        self.log.info("Entering Password-->" + getDataforlogin[1])
        self.lp.Enter_Password(getDataforlogin[1])
        self.lp.Click_Login()
        self.log.info("Click on login button")
        time.sleep(2)

        if self.lp.Login_Status() == True:
            if getDataforlogin[2] == "Pass":
                self.driver.save_screenshot("C:\\Users\\Success\\PycharmProjects\\OrangeHRM\\SceenShots\\test_login_002-pass.png")
                self.lp.Click_MenuButton()
                self.log.info("Click on Menu button")
                self.lp.Click_LogOut()
                self.log.info("Click on logout button")
                self.log.info("test_login_002 is passed")
                assert True

            else:
                self.log.info("test_login_002 is Failed")
                self.driver.save_screenshot(
                    "C:\\Users\\Success\\PycharmProjects\\OrangeHRM\\SceenShots\\test_login_002-fail.png")

                assert False
        else:
            if getDataforlogin[2] == "Fail":
                assert True

            else:
                self.log.info("test_login_002 is Failed")
                self.driver.save_screenshot(
                    "C:\\Users\\Success\\PycharmProjects\\OrangeHRM\\SceenShots\\test_login_002-fail.png")

                assert False


        self.driver.close()
        self.log.info("test_login_002 is Completed")

