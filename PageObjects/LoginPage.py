
class loginpage():
    textbox_username_id = "txtUsername"
    textbox_password_id = "txtPassword"
    btn_login_id = "btnLogin"
    link_logout = "https://opensource-demo.orangehrmlive.com/index.php/auth/logout"
    
    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.btn_login_id).click()

    