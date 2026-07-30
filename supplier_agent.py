from ai_agent_manager import ai_agent_manager


class SupplierAgent:

    def run(self, data=None):

        print("\n🔍 SUPPLIER AGENT RUNNING")


        products = [

            {
                "supplier": "AliExpress",
                "name": "Portable Electric Pump",
                "price": 35,
                "stock": 50
            },

            {
                "supplier": "CJ Dropshipping",
                "name": "Smart Pet Feeder",
                "price": 45,
                "stock": 50
            },

            {
                "supplier": "Spocket",
                "name": "LED Motion Sensor Light",
                "price": 20,
                "stock": 100
            },

            {
                "supplier": "AliExpress",
                "name": "Car Cleaning Kit",
                "price": 30,
                "stock": 50
            }

        ]


        print("\n========== SUPPLIER PRODUCTS ==========")

        for product in products:
            print(product)

        print("=======================================")


        return products



supplier_agent = SupplierAgent()


ai_agent_manager.register_agent(
    "supplier_agent",
    supplier_agent
)