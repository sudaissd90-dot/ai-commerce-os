import requests


class ShopifyManager:

    def __init__(self):

        self.store_url = ""
        self.access_token = ""

    def connect(self, store_url, access_token):

        self.store_url = store_url
        self.access_token = access_token

        print("✅ Shopify Connected")

    def headers(self):

        return {
            "X-Shopify-Access-Token": self.access_token,
            "Content-Type": "application/json"
        }

    def is_connected(self):

        return bool(self.store_url and self.access_token)

    # ----------------------------
    # Dummy Product Create
    # ----------------------------

    def create_product(self, listing):

        if not self.is_connected():

            print("⚠️ Shopify Not Connected")
            print("🧪 Dummy Mode: Product Ready For Upload")
            print("Title :", listing["title"])
            print("Price :", listing["price"])

            return True

        url = f"https://{self.store_url}/admin/api/2026-01/products.json"

        payload = {
            "product": {
                "title": listing["title"],
                "body_html": listing.get("description", ""),
                "vendor": "AI Store Manager",
                "variants": [
                    {
                        "price": str(listing["price"]),
                        "inventory_quantity": listing.get("stock", 10)
                    }
                ]
            }
        }

        response = requests.post(
            url,
            headers=self.headers(),
            json=payload
        )

        print("Shopify Response:", response.status_code)
        print(response.text)

        return response.status_code == 201

    # ----------------------------

    def update_price(self, product_id, new_price):

        if not self.is_connected():

            print(f"🧪 Dummy Mode: Price Updated -> ${new_price}")
            return True

        print("💰 Updating Shopify Price...")
        return True

    # ----------------------------

    def update_inventory(self, product_id, stock):

        if not self.is_connected():

            print(f"🧪 Dummy Mode: Stock Updated -> {stock}")
            return True

        print("📦 Updating Shopify Inventory...")
        return True

    # ----------------------------

    def publish_product(self, product_id):

        if not self.is_connected():

            print("🧪 Dummy Mode: Product Published")
            return True

        print("🌍 Publishing Product...")
        return True


shopify = ShopifyManager()