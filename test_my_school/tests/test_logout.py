from tests.home_test import HomeTest
from pages.main import MainPage

from pages.logout_page import LogoutPage

class TestLogoutPage(HomeTest):

    def test_logout_page(self):
        driver = self.driver
        # login
        main = MainPage(driver)
        logout = main.logout_page()
        logout.logout()