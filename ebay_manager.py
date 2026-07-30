import requests
from config import config


class EbayManager:

    def __init__(self):

        self.environment = config.EBAY_ENVIRONMENT
        self.oauth_token = config.EBAY_USER_TOKEN

        if self.environment.lower() == "sandbox":
            self.base_url = "https://api.sandbox.ebay.com"
        else:
            self.base_url = "https://api.ebay.com"

    # =====================================

    def headers(self):

        return {
            "Authorization": f"Bearer {self.oauth_token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    # =====================================

    def is_connected(self):

        return (
            self.oauth_token is not None
            and self.oauth_token.strip() != ""
        )

    # =====================================

    def connect(self):

        if not self.is_connected():

            print("eBay User Token Missing")
            return False

        print("eBay Connected")
        print("Environment :", self.environment)

        return True

    # =====================================

    def test_connection(self):

        if not self.connect():
            return False

        print("Testing eBay Connection...")

        url = f"{self.base_url}/sell/inventory/v1/location"

        print("URL :", url)

        try:

            response = requests.get(
                url,
                headers=self.headers(),
                timeout=20
            )

            print("Response Received")
            print("Status Code :", response.status_code)
            print("Response :")
            print(response.text)

            if response.status_code == 200:

                print("eBay API Connected Successfully")
                return True

            elif response.status_code == 401:

                print("Invalid or Expired User Token")
                return False

            elif response.status_code == 403:

                print("Permission Denied")
                return False

            else:

                print("API Error")
                return False

        except Exception as e:

            print("Connection Error :", e)
            return False

    # =====================================

    def create_listing(self, listing):

        if not self.is_connected():
            print("eBay Not Connected")
            return False

        print("Uploading Product To eBay...")
        print("Title :", listing["title"])
        print("Price :", listing["price"])

        sku = listing["title"].replace(" ", "_").replace("|", "")[:50]

        url = f"{self.base_url}/sell/inventory/v1/inventory_item/{sku}"

        headers = self.headers()
        headers["Content-Language"] = "en-US"

        payload = {
            "availability": {
                "shipToLocationAvailability": {
                    "quantity": 10
                }
            },
            "condition": "NEW",
            "product": {
                "title": listing["title"],
                "description": listing["description"]
            }
        }

        response = requests.put(
            url,
            headers=headers,
            json=payload,
            timeout=30
        )

        print("Inventory Status :", response.status_code)
        print(response.text)

        if response.status_code not in [200, 201, 204]:
            return False

        self.create_inventory_location()

        existing_offer = self.get_offer(sku)

        if existing_offer:

            print("Existing Offer Found")

            self.publish_offer(existing_offer["offerId"])

        else:

            offer = self.create_offer(
                sku,
                listing["price"]
            )

            if offer:

                self.publish_offer(
                    offer["offerId"]
                )

        return True
            # =====================================

    def create_offer(self, sku, price):

        print("Creating eBay Offer...")
        print("SKU :", sku)
        print("Price :", price)

        url = f"{self.base_url}/sell/inventory/v1/offer"

        payload = {
            "sku": sku,
            "marketplaceId": "EBAY_US",
            "format": "FIXED_PRICE",
            "availableQuantity": 10,
            "categoryId": "179697",
            "listingDescription": "AI Store Manager Product Listing",
            "merchantLocationKey": "AI_STORE",

            "pricingSummary": {
                "price": {
                    "value": str(price),
                    "currency": "USD"
                }
            },

            "listingPolicies": {
                "fulfillmentPolicyId": "YOUR_FULFILLMENT_POLICY_ID",
                "paymentPolicyId": "YOUR_PAYMENT_POLICY_ID",
                "returnPolicyId": "YOUR_RETURN_POLICY_ID"
            },

            "includeCatalogProductDetails": True
        }

        headers = self.headers()
        headers["Content-Language"] = "en-US"

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=30
        )

        print("Offer Status :", response.status_code)
        print(response.text)

        if response.status_code in [200, 201]:

            data = response.json()

            print("✅ Offer Created")
            print("Offer ID :", data.get("offerId"))

            return data

        print("❌ Offer Creation Failed")
        return False

    # =====================================

    def get_offer(self, sku):

        print("Checking Existing Offer...")

        url = f"{self.base_url}/sell/inventory/v1/offer?sku={sku}"

        response = requests.get(
            url,
            headers=self.headers(),
            timeout=30
        )

        print("Offer Check Status :", response.status_code)
        print(response.text)

        if response.status_code == 200:

            data = response.json()

            if data.get("offers"):
                return data["offers"][0]

        return None

    # =====================================

    def publish_offer(self, offer_id):

        print("Publishing Offer...")
        print("Offer ID :", offer_id)

        url = f"{self.base_url}/sell/inventory/v1/offer/{offer_id}/publish"

        headers = self.headers()
        headers["Content-Language"] = "en-US"

        response = requests.post(
            url,
            headers=headers,
            timeout=30
        )

        print("Publish Status :", response.status_code)
        print(response.text)

        return response.status_code in [200, 201]

    # =====================================

    def create_inventory_location(self):

        print("Creating Inventory Location...")

        location_key = "AI_STORE"

        url = f"{self.base_url}/sell/inventory/v1/location/{location_key}"

        headers = self.headers()
        headers["Content-Language"] = "en-US"

        payload = {
    "name": "AI Store Manager",
    "merchantLocationStatus": "ENABLED",
    "locationTypes": [
        "WAREHOUSE"
    ],
    "location": {
        "address": {
            "addressLine1": "123 Main Street",
            "city": "San Jose",
            "stateOrProvince": "CA",
            "postalCode": "95125",
            "country": "US"
        }
    }
}

        response = requests.put(
            url,
            headers=headers,
            json=payload,
            timeout=30
        )

        if response.status_code == 409:
            print("Inventory Location Already Exists")
            return True

        print("Location Status :", response.status_code)
        print(response.text)

        return response.status_code in [200, 201, 204]
            # =====================================

    def update_price(self, listing_id, new_price):

        print("Updating Price")
        print("Listing :", listing_id)
        print("New Price :", new_price)

        return True

    # =====================================

    def update_inventory(self, listing_id, stock):

        print("Updating Inventory")
        print("Listing :", listing_id)
        print("Stock :", stock)

        return True

    # =====================================

    def end_listing(self, listing_id):

        print("Ending Listing :", listing_id)

        return True

    # =====================================

    def account_status(self):

        if self.is_connected():
            return "Connected"

        return "Not Connected"


# =====================================

print("Methods in EbayManager:")
print("create_offer:", hasattr(EbayManager, "create_offer"))
print("create_inventory_location:", hasattr(EbayManager, "create_inventory_location"))

ebay = EbayManager()