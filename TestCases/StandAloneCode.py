import time

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# time.sleep(2)
driver.implicitly_wait(2)
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
# time.sleep(2)
driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()



