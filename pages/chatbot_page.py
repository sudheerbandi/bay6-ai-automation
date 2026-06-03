from pages.base_page import BasePage 
from locators.chatbot_locators import ChatBotLocators 

class ChatBotPage(BasePage): 
    def ask_question(self, question): 
        self.fill( 
            ChatBotLocators.CHAT_INPUT, 
            question 
        ) 
        self.click( 
            ChatBotLocators.SEND_BUTTON 
        ) 
    
    def get_response(self): 
        return self.get_text( 
            ChatBotLocators.RESPONSE 
        )