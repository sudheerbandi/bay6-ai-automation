import requests 
def test_security_headers(config): 
    response = requests.get( config["web_url"] ) 
    assert ( "X-Frame-Options" in response.headers ) 
    assert ( "Content-Security-Policy" in response.headers ) 