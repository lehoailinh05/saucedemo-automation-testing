from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    # --- Tập hợp các bộ định vị (Locators) ---
    ADD_TO_CART_BACKPACK = (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    # --- Tập hợp các phương thức hành động (Actions) ---
    def add_backpack_to_cart(self):
        """Thêm sản phẩm balo vào giỏ hàng"""
        self.click(self.ADD_TO_CART_BACKPACK)

    def get_cart_badge_count(self):
        """Lấy số lượng hiển thị trên biểu tượng giỏ hàng"""
        return self.find_element(self.CART_BADGE).text

    def get_cart_badges(self):
        """Tìm danh sách các thẻ số lượng giỏ hàng"""
        return self.driver.find_elements(*self.CART_BADGE)

    def go_to_cart(self):
        """Chuyển hướng người dùng vào trang giỏ hàng chi tiết"""
        self.click(self.CART_LINK)