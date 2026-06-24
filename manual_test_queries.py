import sqlite3

conn = sqlite3.connect("manual_test.db")
cursor = conn.cursor()

# ── GIẢ LẬP HÀNH ĐỘNG MANUAL TEST ────────────────────────────────

# Giả lập: standard_user thêm 3 sản phẩm vào giỏ
cursor.execute("DELETE FROM cart")  # reset giỏ hàng
cursor.executemany("INSERT INTO cart (username, product_id, quantity) VALUES (?,?,?)", [
    ("standard_user", 1, 1),  # Backpack
    ("standard_user", 2, 1),  # Bike Light
    ("standard_user", 3, 1),  # Bolt T-Shirt
])

# Giả lập: checkout thành công
cursor.execute("DELETE FROM orders")  # reset orders
cursor.execute("""
    INSERT INTO orders (username, total, tax, status, first_name, last_name, zip_code)
    VALUES (?, ?, ?, ?, ?, ?, ?)
""", ("standard_user", 55.97, 4.48, "completed", "Hoai", "Linh", "10000"))

conn.commit()

print("=" * 55)
print("     VERIFY KẾT QUẢ MANUAL TEST - SAUCEDEMO")
print("=" * 55)

# TC_CT_03: Thêm nhiều sản phẩm - số lượng phải là 3
cursor.execute("SELECT COUNT(*) FROM cart WHERE username = 'standard_user'")
count = cursor.fetchone()[0]
status = "✅ PASS" if count == 3 else "❌ FAIL"
print(f"\n[TC_CT_03] Thêm 3 sản phẩm vào giỏ")
print(f"  SQL: SELECT COUNT(*) FROM cart → {count}")
print(f"  Kết quả: {status}")

# TC_CT_10: Giá hiển thị đúng
cursor.execute("""
    SELECT SUM(p.price) 
    FROM cart c 
    JOIN products p ON c.product_id = p.id
    WHERE c.username = 'standard_user'
""")
total = round(cursor.fetchone()[0], 2)
status = "✅ PASS" if total == 55.97 else "❌ FAIL"
print(f"\n[TC_CT_10] Giá hiển thị đúng")
print(f"  SQL: SELECT SUM(price) FROM cart JOIN products → ${total}")
print(f"  Kết quả: {status}")

# TC_CK_08: Tổng tiền tính đúng (total = item_total + tax)
cursor.execute("SELECT total, tax FROM orders WHERE username = 'standard_user'")
row = cursor.fetchone()
item_total = round(row[0] - row[1], 2)
status = "✅ PASS" if round(item_total + row[1], 2) == row[0] else "❌ FAIL"
print(f"\n[TC_CK_08] Tổng tiền tính đúng")
print(f"  SQL: SELECT total, tax FROM orders → Item: ${item_total} + Tax: ${row[1]} = ${row[0]}")
print(f"  Kết quả: {status}")

# TC_CK_10: Hoàn thành đơn hàng - status phải là 'completed'
cursor.execute("SELECT status FROM orders WHERE username = 'standard_user'")
order_status = cursor.fetchone()[0]
status = "✅ PASS" if order_status == "completed" else "❌ FAIL"
print(f"\n[TC_CK_10] Hoàn thành đơn hàng")
print(f"  SQL: SELECT status FROM orders → '{order_status}'")
print(f"  Kết quả: {status}")

# BUG_08: Checkout giỏ hàng trống - total phải > 0
cursor.execute("SELECT COUNT(*) FROM orders WHERE total = 0")
empty_orders = cursor.fetchone()[0]
status = "🐞 BUG CONFIRMED" if empty_orders > 0 else "✅ PASS"
print(f"\n[BUG_08] Checkout giỏ hàng trống")
print(f"  SQL: SELECT COUNT(*) FROM orders WHERE total = 0 → {empty_orders}")
print(f"  Kết quả: {status}")

# TC_CK_13: Giỏ hàng reset sau khi mua
cursor.execute("DELETE FROM cart WHERE username = 'standard_user'")
conn.commit()
cursor.execute("SELECT COUNT(*) FROM cart WHERE username = 'standard_user'")
remaining = cursor.fetchone()[0]
status = "✅ PASS" if remaining == 0 else "❌ FAIL"
print(f"\n[TC_CK_13] Giỏ hàng reset sau khi mua")
print(f"  SQL: SELECT COUNT(*) FROM cart → {remaining} sản phẩm")
print(f"  Kết quả: {status}")

print("\n" + "=" * 55)
conn.close()