from database import db


class InventoryManager:


    def get_stock(self, product_id):

        result = db.fetchone("""
        SELECT stock
        FROM products
        WHERE id=?
        """, (product_id,))


        if result:
            return result[0]

        return 0



    def increase_stock(self, product_id, quantity):

        current_stock = self.get_stock(product_id)

        new_stock = current_stock + quantity


        db.execute("""
        UPDATE products
        SET stock=?
        WHERE id=?
        """, (new_stock, product_id))


        print("✅ Stock Increased")



    def decrease_stock(self, product_id, quantity):

        current_stock = self.get_stock(product_id)


        if current_stock < quantity:

            print("❌ Not Enough Stock")

            return False


        new_stock = current_stock - quantity


        db.execute("""
        UPDATE products
        SET stock=?
        WHERE id=?
        """, (new_stock, product_id))


        print("✅ Stock Decreased")

        return True



    def stock_report(self):

        products = db.fetchall("""
        SELECT id, name, stock
        FROM products
        """)


        print("\n========== INVENTORY REPORT ==========")


        for product in products:

            print(
                f"ID: {product[0]} | "
                f"Name: {product[1]} | "
                f"Stock: {product[2]}"
            )



    def low_stock_alert(self, limit=20):

        products = db.fetchall("""
        SELECT id, name, stock
        FROM products
        WHERE stock <= ?
        """, (limit,))


        if products:

            print("\n⚠️ LOW STOCK ALERT")


            for product in products:

                print(
                    f"ID: {product[0]} | "
                    f"Name: {product[1]} | "
                    f"Stock: {product[2]}"
                )

        else:

            print("\n✅ All Products Stock Level Good")



    def check_inventory_status(self):

        products = db.fetchall("""
        SELECT name, stock
        FROM products
        """)


        print("\n📦 INVENTORY STATUS")


        for product in products:


            if product[1] <= 0:

                status = "OUT OF STOCK ❌"


            elif product[1] <= 20:

                status = "LOW STOCK ⚠️"


            else:

                status = "AVAILABLE ✅"



            print(
                f"{product[0]} : "
                f"{product[1]} units - {status}"
            )



inventory_manager = InventoryManager()