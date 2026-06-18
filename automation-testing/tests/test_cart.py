from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

class TestCartWorkflow:
    def setup_method(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        
        self.driver.get("https://www.saucedemo.com")
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")
        self.wait.until(EC.url_contains("inventory"))

    def teardown_method(self):
        self.driver.quit()

    def test_end_to_end_purchase(self):
        """TC_CB_01: Luồng mua hàng thành công từ đầu đến cuối"""
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver)
        
        inventory_page.add_backpack_to_cart()
        inventory_page.go_to_cart()
        self.wait.until(EC.url_contains("cart"))
        cart_page.click_checkout()
        
        self.wait.until(EC.url_contains("checkout-step-one"))
        cart_page.fill_shipping_info("Nguyen", "Van A", "100000")
        
        self.wait.until(EC.url_contains("checkout-step-two"))
        cart_page.click_finish()
        
        self.wait.until(EC.url_contains("checkout-complete"))
        assert cart_page.get_complete_header_text() == "Thank you for your order!"

    def test_remove_product_from_cart(self):
        """TC_CB_02: Xóa sản phẩm khỏi giỏ hàng thành công"""
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver)
        
        inventory_page.add_backpack_to_cart()
        inventory_page.go_to_cart()
        self.wait.until(EC.url_contains("cart"))
        
        cart_page.remove_backpack()
        assert len(inventory_page.get_cart_badges()) == 0

    def test_checkout_with_missing_info(self):
        """TC_CB_03: Hệ thống báo lỗi khi trống Zip Code"""
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver)
        
        inventory_page.add_backpack_to_cart()
        inventory_page.go_to_cart()
        self.wait.until(EC.url_contains("cart"))
        cart_page.click_checkout()
        
        self.wait.until(EC.url_contains("checkout-step-one"))
        cart_page.fill_shipping_info("Nguyen", "Van A", "")
        
        assert "Error: Postal Code is required" in cart_page.get_error_message()