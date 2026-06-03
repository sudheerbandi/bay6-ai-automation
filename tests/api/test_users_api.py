from utilities.api_client import APIClient 
def test_get_users(config): 
    api = APIClient( config["api_url"] ) 
    response = api.get( "/users" ) 
    assert response.status_code == 200