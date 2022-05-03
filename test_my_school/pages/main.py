from utils.locators import *
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.thongbao_page import ThongBaoPage
from pages.doimatkhau_page import DoiMatKhauPage
from pages.search_tkb_page import SearchTKBPage

class MainPage():
    
    def __init__(self,driver):
        self.locators_thongbao = ThongBaoPageLocators
        self.locators_logout = LogoutPageLocators
        self.locators_doipass = DoiPassPageLocators
        self.locators_mainLogin = MainLoginPageLocators
        self.driver = driver
    
    def thongbao_page(self):
        login = LoginPage(self.driver)
        login.login(self.locators_mainLogin.INPUT_USERNAME, self.locators_mainLogin.INPUT_PASSWORD, self.locators_thongbao.Screen_Login, self.locators_thongbao.Screen_AfterLogin)
       
        self.driver.find_element(*self.locators_thongbao.THONG_BAO).click()
        self.driver.save_screenshot(self.locators_thongbao.Screen_ThongBao)
        
        return ThongBaoPage(self.driver)
    
    def search_tkb(self):
        tb_page = self.thongbao_page()
        tb_page.click_TimTKB_page()
        return SearchTKBPage(self.driver)
        
    
    def logout_page(self):
        login = LoginPage(self.driver)
        login.login(self.locators_mainLogin.INPUT_USERNAME, self.locators_mainLogin.INPUT_PASSWORD, self.locators_logout.Screen_Login, self.locators_logout.Screen_AfterLogin)
        return LogoutPage(self.driver)
    
    def doipass_page(self):
        login = LoginPage(self.driver)
        login.login(self.locators_mainLogin.INPUT_USERNAME, self.locators_mainLogin.INPUT_PASSWORD, self.locators_doipass.Screen_Login, self.locators_doipass.Screen_AfterLogin)

        logout = LogoutPage(self.driver)
        logout.click_hethong()
        logout.save_screenshot_page(self.locators_doipass.Screen_ClickHeThong)
        
        return DoiMatKhauPage(self.driver)
    
    