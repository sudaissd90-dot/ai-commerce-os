from ai_agent_manager import ai_agent_manager


class ListingAgent:

    def run(self, product):

        name = product["name"]
        price = product["price"]


        listing = {

            "title": f"{name} | Premium Quality | Best Value",


            "description": (
                f"Discover {name}, a high-quality product "
                f"designed to make your daily life easier. "
                f"Reliable performance, modern design and great value "
                f"for customers."
            ),


            "features": [
                f"Premium {name}",
                "Easy to use",
                "Durable design",
                "Customer friendly",
                "Excellent value"
            ],


            "benefits": [
                "Saves time",
                "Improves daily experience",
                "Useful for everyday needs"
            ],


            "keywords": [
                name,
                "trending product",
                "best online deal",
                "premium gadget"
            ],


            "price": price
        }


        return listing



listing_agent = ListingAgent()



ai_agent_manager.register_agent(
    "listing_agent",
    listing_agent
)