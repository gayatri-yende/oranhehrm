from selenium.webdriver.common.by import By


class loginPage:

    Text_Username_XPATH = (By.XPATH, "//input[@placeholder='Username']")
    Text_Password_XPATH = (By.XPATH, "//input[@placeholder='Password']")
    Click_Login_Button= (By.XPATH, "//button[normalize-space()='Login']")
    Click_Menu_Button_XPATH= (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    Click_LogOut_Button= (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver


    def Enter_UserName(self, username):
        self.driver.find_element(*loginPage.Text_Username_XPATH).send_keys(username)


    def Enter_Password(self, password):
        self.driver.find_element(*loginPage.Text_Password_XPATH).send_keys(password)


    def Click_Login(self):
        self.driver.find_element(*loginPage.Click_Login_Button).click()

    def Click_MenuButton(self):
        self.driver.find_element(*loginPage.Click_Menu_Button_XPATH).click()

    def Click_LogOut(self):
        self.driver.find_element(*loginPage.Click_LogOut_Button).click()

    def Login_Status(self):
        try:
            self.driver.find_element(*loginPage.Click_Menu_Button_XPATH).click()
            return True

        except:
            return False







