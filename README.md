# SauceDemo Testing Project — Manual & Automation

Dự án kiểm thử toàn diện cho website thương mại điện tử **[SauceDemo](https://www.saucedemo.com/)**, 
bao gồm **Manual Testing**, **Automation Testing (POM)** và **API Testing**.

- **Tester:** Lê Thị Hoài Linh
- **Thời gian:** 05/2026 – 06/2026
- **Công cụ:** Python · Selenium · Pytest · Postman · Jira

---

## 📋 Manual Testing

### Tổng quan kết quả

| Module | Total | Pass | Fail |
|--------|-------|------|------|
| Login | 10 | 9 | 1 |
| Product | 10 | 10 | 0 |
| Cart | 10 | 9 | 1 |
| Checkout | 16 | 15 | 1 |
| **TOTAL** | **46** | **43** | **3** |

### Phạm vi kiểm thử
- **Login:** Đăng nhập thành công/thất bại, tài khoản bị khóa, để trống field, truy cập URL trực tiếp khi chưa đăng nhập
- **Product:** Hiển thị danh sách, sort (A-Z / Z-A / giá tăng / giá giảm), xem chi tiết, thêm sản phẩm vào giỏ
- **Cart:** Thêm/xóa sản phẩm, badge hiển thị đúng số lượng, giá hiển thị đúng, checkout
- **Checkout:** Validation form (First Name / Last Name / Zip), tính tổng tiền, hoàn thành đơn hàng, reset giỏ hàng sau mua

### Tài liệu
- 📄 [Test Cases (Excel)](./test-plan/saucedemo_manual_testcases_v2.xlsx)
- 📄 [Test Plan](./test-plan/TestPlan.md)
- 📄 [Test Summary Report](./test-plan/TestSummaryReport.md)
- 🐞 [Jira Bug Report (PDF)](./jira-bug-report..pdf)

---

## 🐞 Bug Tracking (Jira)

| Jira ID | Bug ID | Mô tả | Severity | Status |
|---------|--------|-------|----------|--------|
| SCRUM-6 | BUG_01 | Ảnh sản phẩm hiển thị sai với problem_user | High | In Review |
| SCRUM-7 | BUG_02 | Sort sản phẩm không hoạt động với problem_user | Medium | In Review |
| SCRUM-8 | BUG_03 | Một số nút Add to cart bị lỗi với problem_user | High | In Review |
| SCRUM-9 | BUG_05 | Ô Last Name không nhập được khi checkout | High | In Review |
| SCRUM-10 | BUG_07 | Không thể hoàn thành checkout vì Last Name bị khóa | High | In Review |
| SCRUM-11 | BUG_08 | Hệ thống cho phép checkout khi giỏ hàng trống | Medium | In Review |

🔗 [Xem Jira Board](https://lehoailinh05.atlassian.net/jira/software/projects/SCRUM/boards/1/backlog)

---

## 🤖 Automation Testing (Page Object Model)

Framework kiểm thử tự động xây dựng từ đầu cho SauceDemo, áp dụng kiến trúc **Page Object Model (POM)**.

### Công nghệ
| Tool | Mục đích |
|------|----------|
| Python | Ngôn ngữ lập trình |
| Selenium WebDriver | Điều khiển trình duyệt |
| Pytest | Test runner |
| Page Object Model | Design pattern |
| `@pytest.mark.parametrize` | Data-Driven Testing |
| Pytest-HTML | Báo cáo kết quả |

### Các tính năng được kiểm thử
- **Authentication:** Đăng nhập thành công, sai password, tài khoản bị khóa, để trống field
- **Cart Workflow:** Thêm/xóa sản phẩm khỏi giỏ hàng
- **Checkout Flow:** Luồng End-to-End và validation form

### Cấu trúc thư mục
```text
├── automation-testing/
│   ├── pages/                  # POM — UI Locators & Actions
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── inventory_page.py
│   │   └── cart_page.py
│   └── tests/                  # Test Scripts
│       ├── test_login.py
│       ├── test_cart.py
│       └── test_checkout.py
├── test-plan/
│   ├── TestPlan.md
│   ├── TestSummaryReport.md
│   └── saucedemo_manual_testcases_v2.xlsx
├── api-testing/
│   └── saucedemo_api_collection.json
├── assets/
├── jira-bug-report.pdf
├── report.html
├── requirements.txt
└── README.md
```

### Kết quả — 7/7 test pass
![Kết quả test](assets/pass%20.png)

### Cài đặt và chạy
```bash
# Clone repo
git clone https://github.com/lehoailinh05/saucedemo-manual-automation-testing.git

# Cài thư viện
pip install -r requirements.txt

# Chạy test
pytest automation-testing/tests/ --html=report.html
```

---

## 🌐 API Testing (Postman)

Kiểm thử REST API bằng Postman cho các luồng: Đăng nhập, Giỏ hàng, Thông tin người dùng.

**File:** `api-testing/saucedemo_api_collection.json`

### Hướng dẫn sử dụng
1. Tải file `saucedemo_api_collection.json` từ thư mục `api-testing/`
2. Mở Postman → bấm **Import**
3. Kéo thả file `.json` vào
4. Chọn collection **SauceDemo API Testing** → bấm **Run**
