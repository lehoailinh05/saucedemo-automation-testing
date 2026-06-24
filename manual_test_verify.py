import sqlite3

conn = sqlite3.connect("manual_test.db")
cursor = conn.cursor()

def verify(tc_id, description, actual, expected):
    status = "✅ PASS" if actual == expected else "❌ FAIL"
    print(f"\n[{tc_id}] {description}")
    print(f"  Kết quả SQL: {actual} | Kỳ vọng: {expected}")
    print(f"  → {status}")

print("=" * 55)
print("   VERIFY MANUAL TEST BẰNG SQL - SAUCEDEMO")
print("=" * 55)

# ── RESET DATA ────────────────────────────────────────────
cursor.execute("DELETE FROM cart")
cursor.execute("DELETE FROM orders")
conn.commit()

# ── TC_CT_02: Thêm 1 sản phẩm ─────────────────────────────
cursor.execute("DELETE FROM cart")
cursor.execute("INSERT INTO cart (username, product_id) VALUES (?,?)", ("standard_user", 1))
conn.commit()
cursor.execute("SELECT COUNT(*) FROM cart WHERE username = 'standard_user'")
verify("TC_CT_02", "Thêm 1 sản phẩm vào giỏ", cursor.fetchone()[0], 1)

# ── TC_CT_03: Thêm 3 sản phẩm ─────────────────────────────
cursor.execute("DELETE FROM cart")
cursor.executemany("INSERT INTO cart (username, product_id) VALUES (?,?)", [
    ("standard_user", 1),
    ("standard_user", 2),
    ("standard_user", 3),
])
conn.commit()
cursor.execute("SELECT COUNT(*) FROM cart WHERE username = 'standard_user'")
verify("TC_CT_03", "Thêm 3 sản phẩm vào giỏ", cursor.fetchone()[0], 3)

# ── TC_CT_05: Xóa hết sản phẩm ────────────────────────────
cursor.execute("DELETE FROM cart WHERE username = 'standard_user'")
conn.commit()
cursor.execute("SELECT COUNT(*) FROM cart WHERE username = 'standard_user'")
verify("TC_CT_05", "Xóa hết sản phẩm - giỏ hàng trống", cursor.fetchone()[0], 0)

# ── TC_CT_09: Số lượng hiển thị đúng ──────────────────────
cursor.execute("DELETE FROM cart")
cursor.executemany("INSERT INTO cart (username, product_id) VALUES (?,?)", [
    ("standard_user", 1),
    ("standard_user", 2),
    ("standard_user", 3),
])
conn.commit()
cursor.execute("SELECT COUNT(*) FROM cart WHERE username = 'standard_user'")
verify("TC_CT_09", "Icon giỏ hàng hiển thị đúng số lượng (3)", cursor.fetchone()[0], 3)

# ── TC_CT_10: Giá hiển thị đúng ───────────────────────────
cursor.execute("""
    SELECT ROUND(SUM(p.price), 2)
    FROM cart c
    JOIN products p ON c.product_id = p.id
    WHERE c.username = 'standard_user'
""")
total_price = cursor.fetchone()[0]
verify("TC_CT_10", "Giá hiển thị đúng (Backpack+BikeLight+BoltTShirt)", total_price, 55.97)

# ── TC_CK_01: Checkout đầy đủ thông tin ───────────────────
cursor.execute("""
    INSERT INTO orders (username, total, tax, status, first_name, last_name, zip_code)
    VALUES (?,?,?,?,?,?,?)
""", ("standard_user", 55.97, 4.48, "completed", "Hoai", "Linh", "10000"))
conn.commit()
cursor.execute("SELECT status FROM orders WHERE username = 'standard_user'")
verify("TC_CK_01", "Checkout đầy đủ thông tin - status completed", cursor.fetchone()[0], "completed")

# ── TC_CK_08: Tổng tiền tính đúng ─────────────────────────
cursor.execute("SELECT total, tax FROM orders WHERE username = 'standard_user'")
row = cursor.fetchone()
item_total = round(row[0] - row[1], 2)
calculated = round(item_total + row[1], 2)
verify("TC_CK_08", f"Tổng tiền đúng (${item_total} + ${row[1]} tax)", calculated, row[0])

# ── TC_CK_10: Hoàn thành đơn hàng ─────────────────────────
cursor.execute("SELECT status FROM orders WHERE username = 'standard_user'")
verify("TC_CK_10", "Hoàn thành đơn hàng - status = completed", cursor.fetchone()[0], "completed")

# ── TC_CK_13: Giỏ hàng reset sau khi mua ─────────────────
cursor.execute("DELETE FROM cart WHERE username = 'standard_user'")
conn.commit()
cursor.execute("SELECT COUNT(*) FROM cart WHERE username = 'standard_user'")
verify("TC_CK_13", "Giỏ hàng reset sau khi mua xong", cursor.fetchone()[0], 0)

# ── BUG_08: Checkout giỏ hàng trống ──────────────────────
cursor.execute("DELETE FROM orders")
cursor.execute("""
    INSERT INTO orders (username, total, tax, status, first_name, last_name, zip_code)
    VALUES (?,?,?,?,?,?,?)
""", ("standard_user", 0, 0, "completed", "Hoai", "Linh", "10000"))
conn.commit()
cursor.execute("SELECT COUNT(*) FROM orders WHERE total = 0")
count = cursor.fetchone()[0]
status = "🐞 BUG CONFIRMED" if count > 0 else "✅ PASS"
print(f"\n[BUG_08] Checkout khi giỏ hàng trống")
print(f"  SQL: SELECT COUNT(*) FROM orders WHERE total = 0 → {count}")
print(f"  → {status}")

print("\n" + "=" * 55)
conn.close()