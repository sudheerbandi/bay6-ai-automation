from locust import HttpUser 
from locust import task 

class ChatbotUser(HttpUser): 
    @task 
    def chatbot_query(self): 
        self.client.post( 
            "/chat", 
            json={ 
                "message": 
                "What services do you offer?" 
            } 
        )