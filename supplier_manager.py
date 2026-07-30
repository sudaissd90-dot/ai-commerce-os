import requests


class SupplierManager:


    def __init__(self):

        self.suppliers = {}



    def add_supplier(self, name, api_url, api_key):

        self.suppliers[name] = {

            "api_url": api_url,
            "api_key": api_key

        }

        print(f"✅ Supplier Added: {name}")



    def get_supplier(self, name):

        return self.suppliers.get(name)



    def list_suppliers(self):

        return list(self.suppliers.keys())



    def remove_supplier(self, name):

        if name in self.suppliers:

            del self.suppliers[name]

            print(f"✅ Supplier Removed: {name}")

        else:

            print("❌ Supplier Not Found")



    def is_connected(self, name):

        return name in self.suppliers



    # 🤖 AI Supplier Comparison

    def analyze_suppliers(self, product):


        suppliers = [


            {
                "name": "Supplier A",
                "cost": 8,
                "shipping": 3,
                "rating": 4.5
            },


            {
                "name": "Supplier B",
                "cost": 6,
                "shipping": 5,
                "rating": 4.2
            },


            {
                "name": "Supplier C",
                "cost": 10,
                "shipping": 2,
                "rating": 4.8
            }

        ]



        for supplier in suppliers:

            supplier["total_cost"] = (
                supplier["cost"] +
                supplier["shipping"]
            )



        best = min(
            suppliers,
            key=lambda x: x["total_cost"]
        )



        return {


            "product": product["name"],

            "supplier_analysis": suppliers,

            "recommended_supplier":
                best["name"],

            "best_cost":
                best["total_cost"],

            "decision":
                "BEST SUPPLIER SELECTED ✅"

        }




supplier_manager = SupplierManager()