from utils.locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SearchTKBPage():
    
    def __init__(self,driver):
        # self.locators = ThongBaoPageLocators
        self.driver = driver

    def enter_search(self, input_search):
        search = self.driver.find_element(By.XPATH, '//input[@name="ctl00$MainContent$Ttkb1"]')
        search.send_keys(input_search)
    
    def click_search(self):
        search_click = self.driver.find_element(By.XPATH, '//a[@id="MainContent_Lref1"]')
        search_click.click()
    
    def save_screenshot_page(self, _urlImage):
        self.driver.save_screenshot(_urlImage)
    
    def wait_search_success(self):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//th[contains(text(),"Thứ")]'))
            )   
        except:
            # else quit
            print("Không tìm thấy!!!")

        
    
    def search(self, input_search):
        self.enter_search(input_search)
        self.save_screenshot_page('input_search.png')
        self.click_search()
        self.wait_search_success()
        self.save_screenshot_page('after_search.png')
