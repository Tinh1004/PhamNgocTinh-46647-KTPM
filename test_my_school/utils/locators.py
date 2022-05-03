from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name
class MainLoginPageLocators(object):
    INPUT_USERNAME = "46647"
    INPUT_PASSWORD = "tinh46647"


class LoginPageLocators(object):
    INPUT_USERNAME = (By.XPATH, '//input[@name="User"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@name="Password"]')
    SUBMIT_LOGIN = (By.XPATH, '//a[@id="Lnew1"]')


class LogoutPageLocators(object):
    Screen_Login = 'img/logout/login.png'
    Screen_AfterLogin = 'img/logout/afterLogin.png'

    HE_THONG = (By.XPATH, '//a[contains(text(),"Hệ thống")]')
    LOGOUT = (By.XPATH, '//a[contains(text(),"Đăng xuất")]')
    Screen_He_Thong = 'img/logout/hethong.png'
    Screen_Logout = 'img/logout/logout.png'

class DoiPassPageLocators(object):
    Screen_Login = 'img/doimatkhau/login.png'
    Screen_AfterLogin = 'img/doimatkhau/afterLogin.png'
    Screen_ClickHeThong = 'img/doimatkhau/hethong.png'
    
    DOI_PASS = (By.XPATH, '//a[@href="doipass"]')
    Screen_DoiPass = 'img/doimatkhau/doipass_page.png'

class ThongBaoPageLocators(object):
    Screen_Login = 'img/thongbao/login.png'
    Screen_AfterLogin = 'img/thongbao/afterLogin.png'
    Screen_ThongBao = 'img/thongbao/thongbao.png'

    THONG_BAO = (By.XPATH, '//li/a[contains(text(),"Thông báo ")]')
    Click_ThongBao = (By.XPATH, '//a[@href="thongbao"]')
    Click_TKB = (By.XPATH, '//a[@href="tkb"]')
    Click_TimTKB = (By.XPATH, '//a[@href="timtkb"]')
    Click_LichThi = (By.XPATH, '//a[@href="lichthi"]')
    Click_CapGT = (By.XPATH, '//a[@href="capgt"]')
    Click_VanBan = (By.XPATH, '//a[@href="vanban"]')

    Screen_ThongBao_1 = 'img/thongbao/thongbao_1.png'
    Screen_ThongBao_2 = 'img/thongbao/thongbao_2.png'
    Screen_ThongBao_3 = 'img/thongbao/thongbao_3.png'
    Screen_ThongBao_4 = 'img/thongbao/thongbao_4.png'
    Screen_ThongBao_5 = 'img/thongbao/thongbao_5.png'
    Screen_ThongBao_6 = 'img/thongbao/thongbao_6.png'









