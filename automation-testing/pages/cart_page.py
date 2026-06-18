from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    # --- Tập hợp các bộ định vị (Locators) chuẩn hóa ---
    REMOVE_BACKPACK_BUTTON = (By.CSS_SELECTOR, "[data-test='remove-sauce-labs-backpack']")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "[data-test='checkout']")
    
    # Sử dụng bộ ID dạng gạch nối chuẩn của SauceDemo
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    ERROR_MESSAGE_BOX = (By.CSS_SELECTOR, "[data-test='error']")

    # --- Tập hợp các phương thức hành động (Actions) ---
    def remove_backpack(self):
        self.click(self.REMOVE_BACKPACK_BUTTON)

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def fill_shipping_info(self, first_name="", last_name="", postal_code=""):
        """Chỉ thực hiện nhập nếu có dữ liệu truyền vào để tránh kích hoạt lỗi sớm"""
        if first_name:
            self.enter_text(self.FIRST_NAME_INPUT, first_name)
        if last_name:
            self.enter_text(self.LAST_NAME_INPUT, last_name)
        if postal_code:
            self.enter_text(self.POSTAL_CODE_INPUT, postal_code)
        self.click(self.CONTINUE_BUTTON)

    def click_finish(self):
        self.click(self.FINISH_BUTTON)

    def get_complete_header_text(self):
        return self.find_element(self.COMPLETE_HEADER).text

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE_BOX).text