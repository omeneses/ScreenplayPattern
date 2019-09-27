from selenium.webdriver.common.by import By
from screenplay.base_page import BasePage 


class HomePage(BasePage):
    """A class for main page locators. All main page locators should come here"""
    SEARCH_CONTAINER = (By.ID, 'searchInput')
    SEARCH_BUTTON = (By.ID, 'searchButton')



