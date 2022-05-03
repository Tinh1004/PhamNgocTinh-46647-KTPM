from utils.locators import *
from pages.login_page import LoginPage

class LogoutPage():
    def __init__(self,driver):
        self.locators = LogoutPageLocators
        self.driver = driver
    
    def click_hethong(self):
        self.driver.find_element(*self.locators.HE_THONG).click()
    
    def click_logout(self):
        self.driver.find_element(*self.locators.LOGOUT).click()
    
    def wait_logout(self):
        self.driver.implicitly_wait(10)

    def save_screenshot_page(self, _urlImage):
        self.driver.save_screenshot(_urlImage)
    
    def logout(self):
        self.click_hethong()
        self.save_screenshot_page(self.locators.Screen_He_Thong)
        self.click_logout()
        self.save_screenshot_page(self.locators.Screen_Logout)