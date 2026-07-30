import sqlite3


class Database:

    def __init__(self):

        self.conn = sqlite3.connect("ai_enterprise.db")
        self.cursor = self.conn.cursor()

        self.create_tables()


    # ==========================
    # CREATE TABLES
    # ==========================

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            supplier TEXT,
            cost REAL,
            price REAL,
            stock INTEGER

        )
        """)


        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product TEXT,
            quantity INTEGER,
            total REAL

        )
        """)


        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT

        )
        """)


        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS suppliers (

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            rating REAL

        )
        """)


        self.conn.commit()



    # ==========================
    # EXECUTE QUERY
    # ==========================

    def execute(self, query, params=()):

        self.cursor.execute(query, params)

        self.conn.commit()



    # ==========================
    # FETCH ONE
    # ==========================

    def fetchone(self, query, params=()):

        self.cursor.execute(query, params)

        return self.cursor.fetchone()



    # ==========================
    # FETCH ALL
    # ==========================

    def fetchall(self, query, params=()):

        self.cursor.execute(query, params)

        return self.cursor.fetchall()



    # ==========================
    # CLEAR PRODUCTS
    # ==========================

    def clear_products(self):

        try:

            self.cursor.execute(
                "DELETE FROM products"
            )

            self.conn.commit()

            print("🗑️ Old Products Cleared")


        except Exception as e:

            print("Clear Products Error:", e)



    # ==========================
    # ADD PRODUCT
    # ==========================

    def add_product(self, product):

        try:

            self.cursor.execute("""
            INSERT INTO products
            (name, supplier, cost, price, stock)

            VALUES (?, ?, ?, ?, ?)

            """,
            (
                product.get("name"),
                product.get("supplier"),
                product.get("cost"),
                product.get("price"),
                product.get("stock")
            ))


            self.conn.commit()

            return True


        except Exception as e:

            print("Add Product Error:", e)

            return False



    # ==========================
    # GET PRODUCTS
    # ==========================

    def get_products(self):

        return self.fetchall(
            "SELECT * FROM products"
        )



    # ==========================
    # CLOSE DATABASE
    # ==========================

    def close(self):

        self.conn.close()



# ==========================
# GLOBAL DATABASE OBJECT
# ==========================

db = Database()