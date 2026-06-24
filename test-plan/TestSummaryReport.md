# TEST SUMMARY REPORT — SAUCEDEMO E-COMMERCE

## 1. Tổng quan

| Hạng mục | Chi tiết |
|----------|----------|
| Dự án | SauceDemo E-commerce Website |
| Tester | Lê Thị Hoài Linh |
| Thời gian test | 03/06/2026 – 24/06/2026 |
| URL | https://www.saucedemo.com |
| Trình duyệt | Google Chrome |

---

## 2. Phạm vi đã test

- **Manual Testing:** 46 test cases (Login, Product, Cart, Checkout)
- **API Testing:** 20 requests (GET, POST, PUT, DELETE) bằng Postman
- **Automation Testing:** 7 test cases bằng Selenium + Pytest

---

## 3. Kết quả tổng hợp

| Loại test | Tổng | Pass | Fail | Pass Rate |
|-----------|------|------|------|-----------|
| Manual | 46 | 43 | 3 | 93.5% |
| API | 20 | 20 | 0 | 100% |
| Automation | 7 | 7 | 0 | 100% |

### Chi tiết Manual Testing theo module

| Module | Total | Pass | Fail | Pass Rate |
|--------|-------|------|------|-----------|
| Login | 10 | 9 | 1 | 90% |
| Product | 10 | 10 | 0 | 100% |
| Cart | 10 | 9 | 1 | 90% |
| Checkout | 16 | 15 | 1 | 93.75% |
| **TOTAL** | **46** | **43** | **3** | **93.5%** |

---

## 4. Bug Summary

| Bug ID | Jira ID | Mô tả | Severity | Status |
|--------|---------|-------|----------|--------|
| BUG_01 | SCRUM-6 | Ảnh sản phẩm hiển thị sai với problem_user | High | In Review |
| BUG_02 | SCRUM-7 | Sort sản phẩm không hoạt động với problem_user | Medium | In Review |
| BUG_03 | SCRUM-8 | Một số nút Add to cart bị lỗi với problem_user | High | In Review |
| BUG_05 | SCRUM-9 | Ô Last Name không nhập được khi checkout | High | In Review |
| BUG_07 | SCRUM-10 | Không thể hoàn thành checkout vì Last Name bị khóa | High | In Review |
| BUG_08 | SCRUM-11 | Hệ thống cho phép checkout khi giỏ hàng trống | Medium | In Review |

| Severity | Số lượng |
|----------|----------|
| High | 4 |
| Medium | 2 |
| **Total** | **6** |

---

## 5. Kết luận

| Hạng mục | Kết quả |
|----------|---------|
| Tổng test cases | 46 |
| Pass Rate | 93.5% |
| Exit Criteria (≥ 90%) | ✅ Đạt |
| Tổng bugs | 6 |
| High severity bugs | 4 |
| Trạng thái | Hoàn thành |

Hệ thống SauceDemo hoạt động ổn định ở các luồng nghiệp vụ chính
với `standard_user`. Các lỗi tập trung ở `problem_user` — user được
thiết kế có lỗi cố ý. Riêng BUG_08 (checkout giỏ trống) xảy ra với
tất cả user, cần ưu tiên xử lý trước khi release.

---

## 6. Rủi ro còn tồn đọng

| Rủi ro | Mức độ |
|--------|--------|
| Chưa test trên Firefox, Safari | Medium |
| Chưa test responsive trên mobile | Medium |
| Bugs của problem_user chưa được fix (trang demo cố định) | Low |

---

## 7. Tài liệu đính kèm

- 📄 [Test Cases](./saucedemo_manual_testcases_v2.xlsx)
- 📄 [Test Plan](./TestPlan.md)
- 🐞 [Jira Bug Report](../jira-bug-report..pdf)
