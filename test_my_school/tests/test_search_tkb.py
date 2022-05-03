from tests.home_test import HomeTest
from pages.main import MainPage

class TestSearchTKBPage(HomeTest):

    def test_login_page(self):
        driver = self.driver
        # login
        main = MainPage(driver)
        test_search_tkb = main.search_tkb()
        test_search_tkb.search("ST19A1A")


