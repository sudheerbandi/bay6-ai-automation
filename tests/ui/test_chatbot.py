def test_chatbot_response( pages, page, config): 
    page.goto( config["web_url"] ) 
    pages.chatbot.ask_question( "What is Bay6 AI?" ) 
    response = ( pages.chatbot.get_response() ) 
    assert response is not None