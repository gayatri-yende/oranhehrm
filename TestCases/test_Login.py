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

    @pytest.mark.sanity
    def test_PageTitle_001(self, setup):
        self.driver = setup
        self.log.info("test_PageTitle_001 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this url-->" +self.Url)
        # driver = webdriver.Chrome()
        # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(2)
        if self.driver.title == "OrangeHRM":
            assert True
            self.log.info("test_PageTitle_001 is passed")
            self.log.info("Page Title is" +self.driver.title)
        else:
            self.log.info("test_PageTitle_001 is Failed")
            assert False



        self.driver.close()
        self.log.info("test_PageTitle_001 is Completed")

    @pytest.mark.sanity
    def test_login_002(self, setup):
        self.driver = setup
        self.log.info("test_login_002 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this Url-->" +self.Url)

        # driver = webdriver.Chrome()
        # # driver.implicitly_wait(6)
        # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.lp = loginPage(self.driver)
        self.log.info("Entering Username-->" + self.username)
        self.lp.Enter_UserName(self.username)
        self.log.info("Entering Password-->" + self.password)
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.lp.Enter_Password(self.password)
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.lp.Click_Login()
        self.log.info("Click on login button")
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(2)

        # try:
        #     login= self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
        #     print("login testcase is passed")
        #     self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
        #     self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
        #     login = True
        #     # assert True
        #     print(login)
        # except:
        #     print("login testcase is failed")
        #     login = False
        #     # assert False
        #     print(login)

        if self.lp.Login_Status() == True:
            self.driver.save_screenshot("C:\\Users\\Success\\PycharmProjects\\OrangeHRM\\SceenShots\\test_login_002-pass.png")

            self.lp.Click_MenuButton()
            self.log.info("Click on Menu button")

            self.lp.Click_LogOut()
            self.log.info("Click on logout button")
            self.log.info("test_login_002 is passed")
            assert True

        else:
            self.log.info("test_login_002 is Failed")
            self.driver.save_screenshot("C:\\Users\\Success\\PycharmProjects\\OrangeHRM\\SceenShots\\test_login_002-fail.png")

            assert False
        self.driver.close()
        self.log.info("test_login_002 is Completed")

        # def test_AddEmp_003(self, setup):
        #     self.driver = setup
        #
        #     # driver = webdriver.Chrome()
        #     # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        #     # time.sleep(2)
        #
        #     self.driver.implicitly_wait(4)
        #     self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        #     self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        #     self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        #     self.driver.find_element(By.XPATH,
        #                              "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='PIM']").click()
        #     self.driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        #     self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Credence")
        #     self.driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys("Credence")
        #     self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Credence")
        #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        #     time.sleep(4)
        #
        #     try:
        #         EMpAddd = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Personal Details']").text
        #         print(EMpAddd)
        #         print("login testcase is passed")
        #         self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
        #         self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
        #         addEmp = True
        #     except:
        #         print("login testcase is failed")
        #         addEmp = False
        #
        #     print(addEmp)
        #
        #     if addEmp == True:
        #         assert True
        #     else:
        #         assert False
        #
