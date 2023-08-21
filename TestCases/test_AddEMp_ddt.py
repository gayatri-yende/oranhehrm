import time

from selenium.webdriver.common.by import By

from Utilities import XLutils
from pageObjects.AddEmp import AddEmp
from pageObjects.LoginPage import loginPage
from Utilities.readproperties import Readconfig
from Utilities.Logger import LogGenrator


class Test_AddEmp_DDT:

    Url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenrator.loggen()
    path = "C:\\Users\\Success\\PycharmProjects\\OrangeHRM\\TestCases\\TestData\\EmployeeList.xlsx"

    def test_AddEmp_ddt_005(self, setup):
        self.driver = setup
        self.log.info("test_AddEmp_ddt_005 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this url-->" +self.Url)
        # driver = webdriver.Chrome()
        # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # time.sleep(2)
        self.lp = loginPage(self.driver)
        self.lp.Enter_UserName(self.username)
        self.log.info("Entering Username-->" + self.username)
        self.lp.Enter_Password(self.password)
        self.log.info("Entering Password-->" + self.password)
        self.lp.Click_Login()
        self.log.info("Click on login button")
        self.ae = AddEmp(self.driver)
        self.rows = XLutils.getrowCount(self.path, 'Sheet1')
        print("Numbers of rows are-->", self.rows)

        self.ae.Click_PIM()
        self.log.info("Click on PIM button")
        self.ae.Add_Button()
        self.log.info("Click on Add button")
        time.sleep(2)
        status_List = []
        for r in range(2, self.rows+1):
            self.FirstName = XLutils.readData(self.path, 'Sheet1', r, 2)
            self.MiddleName = XLutils.readData(self.path, 'Sheet1', r, 3)
            self.LastName = XLutils.readData(self.path, 'Sheet1', r, 4)

            time.sleep(4)
            self.ae.Enter_Firstname(self.FirstName)
            self.log.info("Entering Firstname-->" + self.FirstName)
            self.ae.Enter_Middlename(self.MiddleName)
            self.log.info("Entering Middlename-->" + self.MiddleName)
            self.ae.Enter_Lastname(self.LastName)
            self.log.info("Entering Lastname-->" + self.MiddleName)
            time.sleep(2)
            # self.ae.Click_EmpId()
            self.ae.Click_Save()
            self.log.info("Click on save button")
            time.sleep(4)
            if self.ae.Add_Employee_Status() == True:
                self.ae.Click_AddEmployee()
                status_List.append("Pass")
                XLutils.writeData(self.path, 'Sheet1', r, 5,"Pass")
                self.driver.save_screenshot("C:\\Users\\Success\\PycharmProjects\\OrangeHRM\\SceenShots\\test_AddEmp_003-pass.png")

            else:
                status_List.append("Fail")
                XLutils.writeData(self.path, 'Sheet1', r, 5,"Fail")
                self.driver.save_screenshot("C:\\Users\\Success\\PycharmProjects\\OrangeHRM\\SceenShots\\test_AddEmp_003-fail.png")
        print(status_List)
        self.lp.Click_MenuButton()
        self.log.info("Click on Menu button")
        self.lp.Click_LogOut()
        self.log.info("Click on logout button")
        self.driver.close()
        self.log.info("Closing the browser")
        if "Fail" not in status_List:
            self.log.info("test_AddEmp_ddt_005 is passed")
            assert True
        else:
            self.log.info("test_AddEmp_ddt_005 is failed")
            assert False
        self.log.info("test_AddEmp_ddt_005 is Completed")

