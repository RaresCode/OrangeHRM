from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class loginpage():
    textbox_username_id = "txtUsername"
    textbox_password_id = "txtPassword"
    btn_login_id = "btnLogin"
    link_logout = "https://opensource-demo.orangehrmlive.com/index.php/auth/logout"
    
    def __init__(self, driver):
        self.driver = driver
        self.WebDriverWait = WebDriverWait(self.driver, 10)

    def setusername(self, username):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.textbox_username_id)))
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setpassword(self, password):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.textbox_password_id)))
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID , self.btn_login_id))).click()

    