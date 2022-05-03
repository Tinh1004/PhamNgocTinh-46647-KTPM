from tests.home_test import HomeTest
from pages.login_page import LoginPage

class TestLoginPage(HomeTest):

    def test_login_page(self):
        driver = self.driver
        # login
        login = LoginPage(driver)
        login.login("46647", "tinh46647", 'img/login/login.png', 'img/login/afterLogin.png')

    
    def test_login_page_wrong_password(self):
        driver = self.driver
        # login
        login = LoginPage(driver)
        login.login("46647", "123456", 'img/login/login_1.png', 'img/login/afterLogin_1.png')

    
    def test_login_page_wrong_username(self):
        driver = self.driver
        # login
        login = LoginPage(driver)
        login.login("tinh", "tinh46647", 'img/login/login_2.png', 'img/login/afterLogin_2.png')

    def test_login_page_wrong_kitu(self):
        driver = self.driver
        # login
        login = LoginPage(driver)
        login.login("46647", "'a'", 'img/login/login_3.png', 'img/login/afterLogin_3.png')


    def test_login_page_wrong_detrong(self):
        driver = self.driver
        # login
        login = LoginPage(driver)
        login.login("", "", 'img/login/login_4.png', 'img/login/afterLogin_4.png')

    
    def test_login_page_wrong_SQL_Injection(self):
        driver = self.driver
        # login
        login = LoginPage(driver)
        login.login("46647", "' or 1=1 --", 'img/login/login_5.png', 'img/login/afterLogin_5.png')
