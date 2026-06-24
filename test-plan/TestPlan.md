# TEST PLAN — SAUCEDEMO E-COMMERCE

## 1. Thông tin dự án

| Hạng mục | Chi tiết |
|----------|----------|
| Dự án | SauceDemo E-commerce Website |
| Tester | Lê Thị Hoài Linh |
| Ngày bắt đầu | 03/06/2026 |
| Ngày kết thúc | 24/06/2026 |
| URL | https://www.saucedemo.com |
| Trạng thái | Completed |

---

## 2. Mục tiêu kiểm thử

Kiểm tra toàn bộ chức năng của website SauceDemo bao gồm đăng nhập, 
xem sản phẩm, giỏ hàng và thanh toán — đảm bảo hệ thống hoạt động 
đúng với các luồng nghiệp vụ chính trước khi phát hành.

---

## 3. Phạm vi kiểm thử

### In-scope (trong phạm vi)
- Chức năng Login / Logout
- Danh sách sản phẩm và Sort
- Giỏ hàng (thêm, xóa, kiểm tra badge)
- Checkout (validation form, tính tổng tiền, hoàn thành đơn)
- Kiểm thử với các loại user khác nhau (standard, locked, problem)
- API Testing các endpoint chính

### Out-scope (ngoài phạm vi)
- Thanh toán thực tế (payment gateway)
- Database / Backend trực tiếp
- Mobile app
- Performance / Load testing
- Cross-browser testing (chỉ test Chrome)

---

## 4. Môi trường kiểm thử

| Hạng mục | Chi tiết |
|----------|----------|
| Trình duyệt | Google Chrome (latest) |
| Hệ điều hành | Windows 10/11 |
| Manual Testing Tool | Excel, Jira |
| Automation Tool | Python, Selenium WebDriver, Pytest |
| API Tool | Postman |
| Bug Tracking | Jira (Project: SCRUM) |

---

## 5. Tài khoản test

| Username | Password | Loại | Mục đích |
|----------|----------|------|----------|
| standard_user | secret_sauce | User bình thường | Test luồng chính |
| locked_out_user | secret_sauce | User bị khóa | Test blocked login |
| problem_user | secret_sauce | User có lỗi | Test bug detection |

---

## 6. Các loại test thực hiện

| Loại test | Số lượng | Công cụ | Kết quả |
|-----------|----------|---------|---------|
| Manual Testing | 46 test cases | Excel + Jira | 43 Pass / 3 Fail |
| Automation Testing | 7 test cases | Pytest + Selenium | 7/7 Pass |
| API Testing | 20 requests | Postman | Completed |

---

## 7. Entry Criteria (Điều kiện bắt đầu test)

- Website SauceDemo accessible tại https://www.saucedemo.com
- Tài khoản test đã được xác nhận hoạt động
- Môi trường test đã cài đặt đầy đủ (Chrome, Python, Selenium, Postman)
- Test cases đã được thiết kế và review

## 8. Exit Criteria (Điều kiện kết thúc test)

- Tất cả 46 test cases đã được thực thi
- Tỷ lệ Pass ≥ 90% (đạt: 43/46 = 93%)
- Tất cả bug High đã được log trên Jira
- Test Summary Report đã hoàn thành

---

## 8. Rủi ro và giải pháp

| Rủi ro | Mức độ | Giải pháp |
|--------|--------|-----------|
| Website demo thay đổi UI | Medium | Cập nhật locator và test case khi cần |
| Một số bug là cố ý (problem_user) | Low | Đã xác định và document rõ trong bug report |
| Môi trường test không ổn định | Low | Chạy lại test, ghi nhận flaky test |
| Thiếu thời gian thực thi | Medium | Ưu tiên test case High priority trước |

---

## 9. Tài liệu liên quan

- 📄 [Test Cases](./saucedemo_manual_testcases_v2.xlsx)
- 📄 [Test Summary Report](./TestSummaryReport.md)
- 🐞 [Jira Bug Report](../jira-bug-report.pdf)
