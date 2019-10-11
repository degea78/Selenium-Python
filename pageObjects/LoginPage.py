class LoginPage():
    textbox_username_id = "username"
    textbox_password_id = "password"
    button_login_id = "loginButton"


    def __init__(self, driver):
        self.driver = driver
    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).send_keys("su")
    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).send_keys("su")
    def clickLogin(self):
        self.driver.find_element_by_id(self.button_login_id).click()
    def clickMainBth(self):
        self.driver.find_element_by_xpath("//a[@class='cat-nav-tab'][text()='Componente']").click()