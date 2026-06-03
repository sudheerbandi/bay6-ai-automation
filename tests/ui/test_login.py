def test_login_success( pages, page, config): 
    page.goto( config["web_url"] ) 
    pages.login.login( "admin", "password" ) 
    assert pages.login.verify_login()