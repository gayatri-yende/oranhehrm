import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

from Utilities import XLutils
from pageObjects.LoginPage import loginPage
from Utilities.readproperties import Readconfig
from Utilities.Logger import LogGenrator

class Test_Logins_ddt:

    Url = Readconfig.geturl()
    log = LogGenrator.loggen()
    path = "C:\\Users\\Success\\PycharmProjects\\OrangeHRM\\TestCases\\TestData\\LoginData.xlsx"



    def test_login_ddt_006(self, setup):
        self.driver = setup
        self.log.info("test_login_ddt_006 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this Url-->" +self.Url)
        self.lp = loginPage(self.driver)
        self.rows = XLutils.getrowCount(self.path, 'Sheet1')
        print("Numbers of rows are-->", self.rows)
        login_status = []
        for r in range(2, self.rows+1):
            self.username = XLutils.readData(self.path, 'Sheet1',r,2)
            self.password = XLutils.readData(self.path, 'Sheet1',r,3)

            self.log.info("Entering Username-->" + self.username)
            self.lp.Enter_UserName(self.username)
            self.log.info("Entering Password-->" + self.password)
            self.lp.Enter_Password(self.password)
            self.lp.Click_Login()
            self.log.info("Click on login button")
            time.sleep(2)


            if self.lp.Login_Status() == True:
                self.driver.save_screenshot("C:\\Users\\Success\\PycharmProjects\\OrangeHRM\\SceenShots\\"+self.username+self.password+"test_login_ddt_006-pass.png")

                self.lp.Click_MenuButton()
                self.log.info("Click on Menu button")

                self.lp.Click_LogOut()
                self.log.info("Click on logout button")
                login_status.append("Pass")
                XLutils.writeData(self.path, 'Sheet1', r, 4, "Pass")

            else:
                login_status.append("Fail")
                XLutils.writeData(self.path, 'Sheet1', r, 4, "Fail")
                self.driver.save_screenshot("C:\\Users\\Success\\PycharmProjects\\OrangeHRM\\SceenShots\\"+self.username+self.password+"test_login_ddt_006-fail.png")

        print(login_status)
        if "Fail" in login_status:
            self.log.info("test_login_ddt_006 is passed")
            assert True
        else:
            self.log.info("test_login_ddt_006 is Failed")
            assert False
        self.driver.close()
        self.log.info("test_login_ddt_006 is Completed")

