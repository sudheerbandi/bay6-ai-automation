from pages.base_page import BasePage 
from locators.login_locators import LoginLocators 

class LoginPage(BasePage):
    def login(self, username, password):
        self.fill(LoginLocators.EMAIL, username)
        self.fill(LoginLocators.PASSWORD, password)
        self.click(LoginLocators.LOGIN_BUTTON)

    def verify_login(self):
        return self.is_visible(LoginLocators.TITLE)