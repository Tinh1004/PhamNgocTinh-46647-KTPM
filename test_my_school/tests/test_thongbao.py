from tests.home_test import HomeTest
from pages.main import MainPage

class TestLoginPage(HomeTest):

    def test_thongbao_page(self):
        driver = self.driver
        # login
        main = MainPage(driver)
        test_thongbao = main.thongbao_page()
        test_thongbao.click_thongbao_page()
    
    def test_TKB_page(self):
        driver = self.driver
        # login
        main = MainPage(driver)
        test_thongbao = main.thongbao_page()
        test_thongbao.click_TKB_page()
    
    def test_TimTKB_page(self):
        driver = self.driver
        # login
        main = MainPage(driver)
        test_thongbao = main.thongbao_page()
        test_thongbao.click_TimTKB_page()
    
    def test_LichThi_page(self):
        driver = self.driver
        # login
        main = MainPage(driver)
        test_thongbao = main.thongbao_page()
        test_thongbao.click_LichThi_page()
    
    def test_CapGT_page(self):
        driver = self.driver
        # login
        main = MainPage(driver)
        test_thongbao = main.thongbao_page()
        test_thongbao.click_CapGT_page()
    
    def test_VanBan_page(self):
        driver = self.driver
        # login
        main = MainPage(driver)
        test_thongbao = main.thongbao_page()
        test_thongbao.click_VanBan_page()
    

