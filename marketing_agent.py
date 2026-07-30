class MarketingAgent:


    def generate_campaign(self, product):

        name = product["name"]
        price = product["price"]


        campaign = {

            "product": name,

            "target_customer":
                "Online shoppers looking for problem solving products",

            "ad_title":
                f"🔥 {name} - Make Your Life Easier!",


            "ad_copy":
                f"""
🚀 Introducing {name}

⭐ Premium Quality
⭐ Easy To Use
⭐ Great Value

Perfect solution for your daily needs.

💰 Price: ${price}

Order now and experience the difference!
""",


            "social_caption":
                f"""
🚀 Upgrade your lifestyle with {name}!

Quality + Convenience in one product.

🛒 Shop now!
#SmartShopping #OnlineDeals
""",


            "strategy":
                "Facebook Ads + TikTok Content + Organic Social Media"
        }


        return campaign



marketing_agent = MarketingAgent()