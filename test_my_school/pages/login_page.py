from utils.locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage():
    
    def __init__(self,driver):
        self.locators = LoginPageLocators
        self.driver = driver
    
    def enter_username(self, _username):
        username = self.driver.find_element(*self.locators.INPUT_USERNAME).send_keys(_username)
    
    def enter_password(self, _password):
        password = self.driver.find_element(*self.locators.INPUT_PASSWORD).send_keys(_password)
    
    def click_login(self):
        submit   = self.driver.find_element(*self.locators.SUBMIT_LOGIN)
        submit.click() 
    
    def wait_login_success(self):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//img[@id='Image1']"))
            )   
        except:
            # else quit
            self.driver.quit()
    
    def save_screenshot_page(self, _urlImage):
        self.driver.save_screenshot(_urlImage)
    
    def login(self, _username, _password, _login_screenshot, _after_screenshot):
        driver = self.driver
        # login
        self.enter_username(_username)
        self.enter_password(_password)
        self.save_screenshot_page(_login_screenshot)
        self.click_login()
        self.save_screenshot_page(_after_screenshot)
        self.wait_login_success()