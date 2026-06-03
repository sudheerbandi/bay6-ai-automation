from pages.base_page import BasePage 
from locators.login_locators import LoginLocators 

class LoginPage(BasePage):
    def login(self, username, password): 
        self.fill( 
            LoginLocators.EMAIL_ID, username 
        ) 
        self.fill( 
            LoginLocators.PASSWORD_ID, password 
        ) 
        self.click( 
            LoginLocators.LOGIN_SUBMIT_NAME 
        ) 
    
    def verify_login(self): 
        return self.is_visible( 
            LoginLocators.HOME_PAGE 
        )