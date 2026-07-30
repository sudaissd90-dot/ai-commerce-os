class OrderManager:

    def __init__(self):
        self.orders = []

    def add_order(self, product, quantity, selling_price):

        total = quantity * selling_price

        order = {
            "product": product,
            "quantity": quantity,
            "selling_price": selling_price,
            "total": total,
            "status": "Pending"
        }

        self.orders.append(order)

        print("✅ Order Added")
        return order

    def complete_order(self, index):

        if index < len(self.orders):
            self.orders[index]["status"] = "Completed"
            print("✅ Order Completed")

    def get_orders(self):

        return self.orders