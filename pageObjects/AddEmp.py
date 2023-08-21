from selenium.webdriver.common.by import By


class AddEmp:
    Click_PIM_XPATH = (By.XPATH,
                             "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='PIM']")
    Click_Add_Button = (By.XPATH, "//button[normalize-space()='Add']")
    Text_FirstName_XPATH = (By.XPATH, "//input[@placeholder='First Name']")
    Text_MiddleName_XPATH = (By.XPATH, "//input[@placeholder='Middle Name']")
    Text_LastName_XPATH = (By.XPATH, "//input[@placeholder='Last Name']")
    Click_Save_Button = (By.XPATH, "//button[@type='submit']")
    # Click_EmpId_XPATH = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/input[1]")
    Text_PersonalDetails_XPATH = (By.XPATH, "//h6[normalize-space()='Personal Details']")
    Click_Add_Emp_XPATH = (By.XPATH, "//a[normalize-space()='Add Employee']")


    def __init__(self,driver):
        self.driver = driver


    def Click_PIM(self):
        self.driver.find_element(*AddEmp.Click_PIM_XPATH).click()

    def Add_Button(self):
        self.driver.find_element(*AddEmp.Click_Add_Button).click()

    def Enter_Firstname(self, firstname):
        self.driver.find_element(*AddEmp.Text_FirstName_XPATH).send_keys(firstname)

    def Enter_Middlename(self, middlename):
        self.driver.find_element(*AddEmp.Text_MiddleName_XPATH).send_keys(middlename)

    def Enter_Lastname(self, lastname):
        self.driver.find_element(*AddEmp.Text_LastName_XPATH).send_keys(lastname)

    # def Click_EmpId(self):
    #     self.driver.find_element(*AddEmp.Click_EmpId_XPATH).remove()

    def Click_Save(self):
        self.driver.find_element(*AddEmp.Click_Save_Button).click()

    def Click_AddEmployee(self):
        self.driver.find_element(*AddEmp.Click_Add_Emp_XPATH).click()


    def Add_Employee_Status(self):
        try:
            self.driver.find_element(*AddEmp.Text_PersonalDetails_XPATH)
            return True

        except:
            return False





