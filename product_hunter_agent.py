from ai_agent_manager import ai_agent_manager


class ProductHunterAgent:

    def run(self, data=None):

        print("\n🔍 PRODUCT HUNTER AGENT RUNNING")

        products = ai_agent_manager.run_agent(
            "supplier_agent"
        )

        if not products:
            print("❌ No Products Found")
            return []

        print(f"\n📦 Total Products Found: {len(products)}")

        sorted_products = sorted(
            products,
            key=lambda product: product["price"]
        )

        print("\n🏆 BEST PRODUCTS")

        for product in sorted_products:

            print(
                f"{product['name']} | "
                f"${product['price']} | "
                f"Stock: {product['stock']}"
            )

        return sorted_products


product_hunter_agent = ProductHunterAgent()

ai_agent_manager.register_agent(
    "product_hunter_agent",
    product_hunter_agent
)