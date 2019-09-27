"""
Description: Test module for module src/page_object_patter/base_page.py

@author: Paul Bodean
@date: 25/07/2017
"""
from screenplay.tasks.search import Search 
from screenplay.test_template import TestTemplate 


import unittest


class TestHomePage(TestTemplate):
    """
    Check page functionality
    """
    
    def test_search_a_text(self):
        """
        Check Home page buttons are displayed
        """
        Search.test_search_text(self, self.driver, "Python")

if __name__ == '__main__':
    unittest.main()
