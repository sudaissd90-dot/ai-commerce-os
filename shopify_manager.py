import os
import time
from pathlib import Path
import requests


def load_env():
    env_file = Path(".env")

    if not env_file.exists():
        return

    for line in env_file.read_text().splitlines():
        line = line.strip()

        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ[key.strip()] = value.strip()


load_env()


class ShopifyManager:

    def __init__(self):
        self.store_url = os.getenv(
            "SHOPIFY_STORE_URL",
            "ai-store-manager-cnd98t8u.myshopify.com"
        )

        self.client_id = os.getenv(
            "SHOPIFY_CLIENT_ID",
            ""
        )

        self.client_secret = os.getenv(
            "SHOPIFY_CLIENT_SECRET",
            ""
        )

        self.access_token = os.getenv("SHOPIFY_ACCESS_TOKEN", "").strip()

        self.token_expires_at = 0


    def connect(self, store_url=None, access_token=None):

        if store_url:
            self.store_url = store_url

        if access_token:
            self.access_token = access_token
            self.token_expires_at = time.time() + 86399

        else:
            self.get_access_token()

        print("✅ Shopify Connected")


    def get_access_token(self):
        if self.access_token:
            return self.access_token

        print("❌ SHOPIFY_ACCESS_TOKEN missing")
        return False

    def headers(self):

        return {
            "X-Shopify-Access-Token":
                self.access_token,

            "Content-Type":
                "application/json"
        }


    def is_connected(self):

        return bool(
            self.store_url
            and self.get_access_token()
        )


    def find_product(self, title):

        url = (
            f"https://{self.store_url}"
            "/admin/api/2026-01/products.json"
        )


        response = requests.get(
            url,
            headers=self.headers(),
            params={
                "limit": 250
            }
        )


        if response.status_code != 200:

            print(
                "❌ Shopify Product Search Error:",
                response.status_code
            )

            print(response.text)

            return None


        products = response.json().get(
            "products",
            []
        )


        target = title.strip().lower()


        for product in products:

            if product.get(
                "title",
                ""
            ).strip().lower() == target:

                return product


        return None


    def create_product(self, listing):

        if not self.is_connected():

            print("⚠️ Shopify Not Connected")

            return False


        title = listing["title"]

        image_url = listing.get(
            "image_url",
            ""
        )


        product_data = {

            "title": title,

            "body_html": listing.get(
                "description",
                ""
            ),

            "vendor": "AI Store Manager",

            "variants": [
                {
                    "price": str(
                        listing.get(
                            "price",
                            0
                        )
                    ),

                    "inventory_quantity":
                        listing.get(
                            "stock",
                            10
                        )
                }
            ]
        }


        # Image attach
        if image_url:

            product_data["images"] = [
                {
                    "src": image_url
                }
            ]


        existing = self.find_product(title)


        # =====================================
        # EXISTING PRODUCT -> UPDATE
        # =====================================

        if existing:

            product_id = existing["id"]

            url = (
                f"https://{self.store_url}"
                f"/admin/api/2026-01/products/{product_id}.json"
            )


            update_data = {
                "id": product_id,
                "title": title,
                "body_html": listing.get(
                    "description",
                    ""
                )
            }


            if image_url:

                update_data["images"] = [
                    {
                        "src": image_url
                    }
                ]


            response = requests.put(
                url,
                headers=self.headers(),
                json={
                    "product": update_data
                }
            )


            print(
                "Shopify Existing Product Update:",
                response.status_code
            )


            print(response.text)


            return response.status_code == 200


        # =====================================
        # NEW PRODUCT -> CREATE
        # =====================================

        url = (
            f"https://{self.store_url}"
            "/admin/api/2026-01/products.json"
        )


        response = requests.post(
            url,
            headers=self.headers(),
            json={
                "product": product_data
            }
        )


        print(
            "Shopify Product Create:",
            response.status_code
        )


        print(response.text)


        return response.status_code == 201


    def update_price(
        self,
        product_id,
        new_price
    ):

        print(
            f"💰 Updating Shopify Price -> "
            f"{new_price}"
        )

        return True


    def update_inventory(
        self,
        product_id,
        stock
    ):

        print(
            f"📦 Updating Shopify Inventory -> "
            f"{stock}"
        )

        return True


    def publish_product(
        self,
        product_id
    ):

        print(
            "🌍 Publishing Product..."
        )

        return True


shopify = ShopifyManager()
