from utils.locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ThongBaoPage():
    
    def __init__(self,driver):
        self.locators = ThongBaoPageLocators
        self.driver = driver

    def save_screenshot_page(self, _urlImage):
        self.driver.save_screenshot(_urlImage)
    
    def click_thongbao_page(self):
        self.driver.find_element(*self.locators.Click_ThongBao).click()
        self.save_screenshot_page(self.locators.Screen_ThongBao_1)
    
    def click_TKB_page(self):
        self.driver.find_element(*self.locators.Click_TKB).click()
        self.save_screenshot_page(self.locators.Screen_ThongBao_2)
    
    def click_TimTKB_page(self):
        self.driver.find_element(*self.locators.Click_TimTKB).click()
        self.save_screenshot_page(self.locators.Screen_ThongBao_3)
    
    def click_LichThi_page(self):
        self.driver.find_element(*self.locators.Click_LichThi).click()
        self.save_screenshot_page(self.locators.Screen_ThongBao_4)
    
    def click_CapGT_page(self):
        self.driver.find_element(*self.locators.Click_CapGT).click()
        self.save_screenshot_page(self.locators.Screen_ThongBao_5)
    
    def click_VanBan_page(self):
        self.driver.find_element(*self.locators.Click_VanBan).click()
        self.save_screenshot_page(self.locators.Screen_ThongBao_6)
    

