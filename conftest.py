import pytest 

from playwright.sync_api import sync_playwright 
from config.config_manager import ConfigManager 
from core.page_factory import PageFactory 

@pytest.fixture(scope="session") 
def config(): 
    return ConfigManager.get_config() 

@pytest.fixture 
def browser(): 
    playwright = sync_playwright().start() 
    browser = playwright.chromium.launch( headless=False ) 
    
    yield browser 
    browser.close() 
    playwright.stop() 
    
@pytest.fixture 
def page(browser): 
    page = browser.new_page() 
    
    yield page 
    page.close() 

@pytest.fixture 
def pages(page): 
    return PageFactory(page)