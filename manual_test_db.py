import sqlite3

conn = sqlite3.connect("manual_test.db")
cursor = conn.cursor()

# ── TẠO BẢNG ──────────────────────────────────────────────────────

# Bảng users
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username  TEXT PRIMARY KEY,
        password  TEXT,
        role      TEXT
    )
""")

# Bảng products
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id    INTEGER PRIMARY KEY,
        name  TEXT,
        price REAL
    )
""")

# Bảng cart
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cart (
        id         INTEGER PRIMARY KEY AUTOINCREMENT,
        username   TEXT,
        product_id INTEGER,
        quantity   INTEGER DEFAULT 1
    )
""")

# Bảng orders
cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id         INTEGER PRIMARY KEY AUTOINCREMENT,
        username   TEXT,
        total      REAL,
        tax        REAL,
        status     TEXT,
        first_name TEXT,
        last_name  TEXT,
        zip_code   TEXT
    )
""")

# ── INSERT DỮ LIỆU MẪU ────────────────────────────────────────────

# Users
cursor.executemany("INSERT OR REPLACE INTO users VALUES (?,?,?)", [
    ("standard_user",   "secret_sauce", "standard"),
    ("locked_out_user", "secret_sauce", "locked"),
    ("problem_user",    "secret_sauce", "problem"),
])

# Products (6 sản phẩm của SauceDemo)
cursor.executemany("INSERT OR REPLACE INTO products VALUES (?,?,?)", [
    (1, "Sauce Labs Backpack",          29.99),
    (2, "Sauce Labs Bike Light",         9.99),
    (3, "Sauce Labs Bolt T-Shirt",      15.99),
    (4, "Sauce Labs Fleece Jacket",     49.99),
    (5, "Sauce Labs Onesie",             7.99),
    (6, "Test.allTheThings() T-Shirt",  15.99),
])

conn.commit()
print("✅ Tạo database thành công!")
conn.close()