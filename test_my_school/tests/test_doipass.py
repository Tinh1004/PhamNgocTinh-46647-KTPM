from tests.home_test import HomeTest
from pages.main import MainPage

class TestDoiMatKhauPage(HomeTest):

    def test_login_page(self):
        driver = self.driver
        # login
        main = MainPage(driver)
        test_doipass = main.doipass_page()
        test_doipass.Click_doipass()


