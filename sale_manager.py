print("🔥 SALES MANAGER FILE LOADED")
class SalesManager:


    def __init__(self):

        self.sales = []



    def add_sale(self, product_name, quantity, selling_price):

        total = quantity * selling_price


        sale = {

            "product": product_name,
            "quantity": quantity,
            "selling_price": selling_price,
            "total": total

        }


        self.sales.append(sale)


        print(f"✅ Sale Added: {product_name}")
        print(f"💰 Sale Total: ${total}")



    def get_all_sales(self):

        return self.sales



    def total_revenue(self):

        return sum(
            sale["total"]
            for sale in self.sales
        )



# Object

sales_manager = SalesManager()

print("✅ SALES MANAGER OBJECT CREATED")