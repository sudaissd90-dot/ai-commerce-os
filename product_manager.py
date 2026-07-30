from database import db
from workflow_manager import workflow_manager
from product_analysis_agent import product_analysis_agent

print("🔥 PRODUCT MANAGER FILE LOADED")


class ProductManager:

    def __init__(self, database=None):
        self.database = database


    def add_product(self, name, price, stock):

        # Check Duplicate
        existing = db.fetchone("""
        SELECT * FROM products
        WHERE LOWER(name)=LOWER(?)
        """, (name,))


        if existing:
            print("\n⚠️ PRODUCT ALREADY EXISTS")
            print(f"Name: {name}")
            print("Action: Product Not Added")
            return None


        # Product Object
        product = {
            "name": name,
            "price": price
        }


        # AI Analysis
        analysis = product_analysis_agent.run(product)


        print("\n🧠 AI PRODUCT ANALYSIS")
        print(analysis)


        # Reject Weak Product
        if analysis["decision"] != "APPROVED ✅":
            print("\n❌ PRODUCT REJECTED BY AI")
            return None


        # Save Product
        db.execute("""
        INSERT INTO products(name, price, stock)
        VALUES (?, ?, ?)
        """, (name, price, stock))


        print("\n✅ PRODUCT SAVED TO DATABASE")
        print(f"Name : {name}")
        print(f"Price: ${price}")
        print(f"Stock: {stock}")


        # AI Listing Generation
        listing = workflow_manager.run_workflow(
            "auto_listing_workflow",
            product
        )


        print("\n🤖 AI GENERATED LISTING")
        print(listing)


        return listing



    def get_all_products(self):

        return db.fetchall("""
        SELECT * FROM products
        ORDER BY id DESC
        """)



    def search_product(self, name):

        return db.fetchone("""
        SELECT * FROM products
        WHERE LOWER(name)=LOWER(?)
        """, (name,))



    def update_stock(self, product_id, stock):

        db.execute("""
        UPDATE products
        SET stock=?
        WHERE id=?
        """, (stock, product_id))


        print("✅ Stock Updated")



    def delete_product(self, product_id):

        db.execute("""
        DELETE FROM products
        WHERE id=?
        """, (product_id,))


        print("✅ Product Deleted")



# Object
product_manager = ProductManager(db)