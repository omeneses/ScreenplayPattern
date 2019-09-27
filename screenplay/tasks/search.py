from screenplay.actions.enter import Enter
from screenplay.actions.click import Click
from screenplay.user_interface.home_page import HomePage 
from screenplay.base_page import BasePage

import unittest


class Search():
    """
    Search a text in wikipedia
    """

    def test_search_text(self,driver,text):
        """
        Enter a text to search in wikipedia
        """
        Enter.write_text(self,driver,"ID",HomePage.SEARCH_CONTAINER[1],text)
        Click.click_on(self,driver,"ID",HomePage.SEARCH_BUTTON[1])