from utils.locators import *

class DoiMatKhauPage():
    def __init__(self,driver):
        self.locators = DoiPassPageLocators
        self.driver = driver
    
    def save_screenshot_page(self, _urlImage):
        self.driver.save_screenshot(_urlImage)
    
    def wait_doipass(self):
        self.driver.implicitly_wait(5)
    
    def Click_doipass(self):
        self.driver.find_element(*self.locators.DOI_PASS).click()
        self.save_screenshot_page(self.locators.Screen_DoiPass)
        # self.wait_doipass()

    
    