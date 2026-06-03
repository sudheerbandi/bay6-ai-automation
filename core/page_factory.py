from pages.login_page import LoginPage 
from pages.chatbot_page import ChatBotPage 

class PageFactory: 
    def __init__(self, page): 
        self.page = page 

    @property 
    def login(self): 
        return LoginPage(self.page) 

    @property 
    def chatbot(self): 
        return ChatBotPage(self.page) 