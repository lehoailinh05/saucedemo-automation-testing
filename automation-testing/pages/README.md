# Ecommerce Automation Testing Framework (Page Object Model)

Dự án xây dựng framework kiểm thử tự động hoàn chỉnh từ đầu (Scratch) cho website thương mại điện tử **SauceDemo**, áp dụng kiến trúc thiết kế **Page Object Model (POM)** kết hợp với ngôn ngữ **Python** và thư viện **Selenium WebDriver**.

## 🚀 Các tính năng được kiểm thử
* **Authentication:** Đăng nhập thành công với tài khoản chuẩn, chặn đăng nhập khi sai password, khóa tài khoản hoặc để trống trường thông tin.
* **Cart Workflow:** Thêm sản phẩm vào giỏ hàng, xóa sản phẩm khỏi giỏ hàng trực tiếp.
* **Checkout Flow:** Luồng thanh toán End-to-End thành công và kiểm tra validation chặn lỗi khi điền thiếu thông tin cá nhân (First Name, Last Name, Zip Code).

## 🛠️ Công nghệ sử dụng
* **Ngôn ngữ:** Python
* **Công cụ cốt lõi:** Selenium WebDriver
* **Test Runner:** Pytest
* **Design Pattern:** Page Object Model (POM), Data-Driven Testing (`@pytest.mark.parametrize`)
* **Report:** Pytest-HTML

## 📁 Cấu trúc thư mục dự án
```text
├── automation-testing/
│   ├── pages/            # Tầng quản lý UI Locators và Actions (POM)
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── inventory_page.py
│   │   └── cart_page.py
│   └── tests/            # Tầng chứa kịch bản kiểm thử (Test Scripts)
│       ├── test_cart.py
│       ├── test_checkout.py
│       └── test_login.py
├── requirements.txt      # Danh sách thư viện cần thiết
└── README.md             # Tài liệu hướng dẫn dự án