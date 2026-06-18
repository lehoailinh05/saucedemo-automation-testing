from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # --- Tập hợp các Locator (Bộ định vị phần tử) ---
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_CONTAINER = (By.CSS_SELECTOR, ".error-message-container")

    # --- Các hành động trên trang Login ---
    def login(self, username, password):
        """Điền thông tin và bấm đăng nhập"""
        if username:
            self.enter_text(self.USERNAME_INPUT, username)
        if password:
            self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        """Lấy thông báo lỗi hiển thị trên màn hình"""
        return self.find_element(self.ERROR_CONTAINER).text