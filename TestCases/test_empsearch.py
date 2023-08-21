import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.AddEmp import AddEmp
from pageObjects.EmployeeSearchPage import EmployeeSearch
from pageObjects.LoginPage import loginPage
from Utilities.readproperties import Readconfig
from Utilities.Logger import LogGenrator


class Test_Search_EMp:

    Url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenrator.loggen()

    @pytest.mark.sanity
    def test_searchEmp_005(self, setup):
        self.driver = setup
        self.log.info("test_searchEmp_005 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this url-->" +self.Url)
        self.lp = loginPage(self.driver)
        self.lp.Enter_UserName(self.username)
        self.log.info("Entering Username-->" + self.username)
        self.lp.Enter_Password(self.password)
        self.log.info("Entering Password-->" + self.password)
        self.lp.Click_Login()
        self.log.info("Click on login button")
        self.ae = AddEmp(self.driver)
        self.ae.Click_PIM()
        self.log.info("Click on PIM button")
        self.es = EmployeeSearch(self.driver)
        self.es.Enter_EmpName("Paul")
        self.log.info("Entering Emp Name")
        time.sleep(2)
        self.es.Click_SearchButton()
        self.log.info("Clicking on Search Button")
        time.sleep(10)
        print(self.es.Search_Result())
        if self.es.Search_Result() == True:
            self.log.info("Search Found")
            self.lp.Click_MenuButton()
            self.log.info("Click on Menu button")
            self.lp.Click_LogOut()
            self.log.info("Click on logout button")
            assert True
            self.log.info("test_searchEmp_005 is Passed")
            assert True

        else:
            self.log.info("No Search Found")
            self.lp.Click_MenuButton()
            self.log.info("Click on Menu button")
            self.lp.Click_LogOut()
            self.log.info("Click on logout button")
            self.log.info("test_searchEmp_005 is failed")
            assert False


        self.driver.close()


