from ai_agent_manager import ai_agent_manager


class PricingAgent:

    def run(self, product):

        cost = product.get("price", 0)


        # Dynamic Profit Margin

        if cost <= 20:
            profit_margin = 100

        elif cost <= 40:
            profit_margin = 80

        else:
            profit_margin = 60



        selling_price = round(
            cost * (1 + profit_margin / 100),
            2
        )


        profit = round(
            selling_price - cost,
            2
        )



        return {

            "product": product["name"],

            "supplier_cost": cost,

            "profit_margin": profit_margin,

            "selling_price": selling_price,

            "expected_profit": profit

        }



pricing_agent = PricingAgent()



ai_agent_manager.register_agent(
    "pricing_agent",
    pricing_agent
)


print("🔥 PRICING AGENT V2 LOADED")