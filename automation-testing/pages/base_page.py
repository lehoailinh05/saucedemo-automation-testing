from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        """Khởi tạo Driver và bộ đợi Explicit Wait"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """Đợi và trả về phần tử khi nó xuất hiện trên giao diện"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Đợi phần tử hiển thị rồi thực hiện click"""
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        """Xóa nội dung cũ và nhập văn bản mới"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)