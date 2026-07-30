class ListingAgent:

    def __init__(self):
        self.name = "AI Listing Agent V3"

    def run(self, product):

        # Sirf AUTO_LIST products ko list karo
        if product.get("decision") != "AUTO_LIST ✅":
            return {
                "status": "SKIPPED",
                "reason": "Product not approved for auto listing."
            }

        # Product Data
        name = product["product"]
        price = product.get("price", 0)

        # SEO Title
        title = f"{name} | Premium Quality | Best Seller"

        # Product Description
        description = f"""
{name}

⭐ Key Features:
• Premium Quality
• Easy To Use
• High Customer Demand
• Excellent Value

🚀 Why Buy This Product?

This product has been selected by the AI Product Analysis System based on demand, profit potential, supplier quality and market opportunity.

💰 Price: ${price}

✅ AI Approved Product
"""

        # SEO Keywords
        keywords = [
            name,
            "premium",
            "best seller",
            "high demand",
            "online shopping",
            "AI recommended"
        ]

        return {
            "status": "READY_TO_LIST",
            "title": title,
            "description": description,
            "keywords": keywords,
            "price": price
        }


listing_agent = ListingAgent()