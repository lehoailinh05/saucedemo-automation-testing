from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

class TestCheckout:
    def setup_method(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        
        # Tiền điều kiện theo POM: Đăng nhập -> Thêm sản phẩm -> Vào giỏ hàng
        self.driver.get("https://www.saucedemo.com")
        login_page = LoginPage(self.driver)
        inventory_page = InventoryPage(self.driver)
        
        login_page.login("standard_user", "secret_sauce")
        self.wait.until(EC.url_contains("inventory"))
        
        inventory_page.add_backpack_to_cart()
        inventory_page.go_to_cart()
        self.wait.until(EC.url_contains("cart"))

    def teardown_method(self):
        self.driver.quit()

    def test_checkout_complete_flow(self):
        """TC_CO_01: Luồng hoàn thành thông tin thanh toán thành công"""
        cart_page = CartPage(self.driver)
        cart_page.click_checkout()
        
        # Điền đầy đủ thông tin hợp lệ thông qua CartPage POM
        self.wait.until(EC.url_contains("checkout-step-one"))
        cart_page.fill_shipping_info("John", "Doe", "12345")
        
        self.wait.until(EC.url_contains("checkout-step-two"))
        cart_page.click_finish()
        
        self.wait.until(EC.url_contains("checkout-complete"))
        assert cart_page.get_complete_header_text() == "Thank you for your order!"

    def test_checkout_empty_firstname(self):
        """TC_CO_02: Hệ thống chặn và báo lỗi khi trống First Name"""
        cart_page = CartPage(self.driver)
        cart_page.click_checkout()
        
        self.wait.until(EC.url_contains("checkout-step-one"))
        cart_page.fill_shipping_info(first_name="", last_name="Doe", postal_code="12345")
        
        assert "Error: First Name is required" in cart_page.get_error_message()

    def test_checkout_empty_lastname(self):
        """TC_CO_03: Hệ thống chặn và báo lỗi khi trống Last Name"""
        cart_page = CartPage(self.driver)
        cart_page.click_checkout()
        
        self.wait.until(EC.url_contains("checkout-step-one"))
        cart_page.fill_shipping_info(first_name="John", last_name="", postal_code="12345")
        
        assert "Error: Last Name is required" in cart_page.get_error_message()

    def test_checkout_empty_zipcode(self):
        """TC_CO_04: Hệ thống chặn và báo lỗi khi trống Zip/Postal Code"""
        cart_page = CartPage(self.driver)
        cart_page.click_checkout()
        
        self.wait.until(EC.url_contains("checkout-step-one"))
        cart_page.fill_shipping_info(first_name="John", last_name="Doe", postal_code="")
        
        assert "Error: Postal Code is required" in cart_page.get_error_message()