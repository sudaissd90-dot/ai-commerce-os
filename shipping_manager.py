import requests


class ShippingManager:

    def __init__(self):

        self.providers = {}

    def add_provider(self, name, api_url, api_key):

        self.providers[name] = {
            "api_url": api_url,
            "api_key": api_key
        }

        print(f"✅ Shipping Provider Added: {name}")

    def get_provider(self, name):

        return self.providers.get(name)

    def list_providers(self):

        return list(self.providers.keys())

    def remove_provider(self, name):

        if name in self.providers:
            del self.providers[name]
            print(f"✅ Shipping Provider Removed: {name}")
        else:
            print("❌ Shipping Provider Not Found")

    def is_connected(self, name):

        return name in self.providers


shipping_manager = ShippingManager()