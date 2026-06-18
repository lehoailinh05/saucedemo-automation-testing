from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
from pages.login_page import LoginPage

class TestLogin:
    def setup_method(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self):
        self.driver.quit()

    def test_login_success(self):
        """TC_LG_01: Đăng nhập thành công với tài khoản chuẩn"""
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")
        
        # Chờ URL chuyển hướng thành công sang trang sản phẩm
        self.wait.until(EC.url_contains("inventory"))
        assert "inventory" in self.driver.current_url

    @pytest.mark.parametrize(
        "username, password, expected_error",
        [
            ("standard_user", "wrongpass", "Username and password do not match"),
            ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out"),
            ("", "secret_sauce", "Username is required")
        ]
    )
    def test_login_failures(self, username, password, expected_error):
        """Gộp các kịch bản lỗi: Hệ thống phải hiển thị thông báo lỗi tương ứng"""
        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        
        # Lấy text lỗi từ trang thông qua lớp LoginPage đã tối ưu
        error_msg = login_page.get_error_message()
        assert expected_error in error_msg