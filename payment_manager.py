import requests


class PaymentManager:

    def __init__(self):

        self.gateways = {}

    def add_gateway(self, name, api_url, api_key):

        self.gateways[name] = {
            "api_url": api_url,
            "api_key": api_key
        }

        print(f"✅ Payment Gateway Added: {name}")

    def get_gateway(self, name):

        return self.gateways.get(name)

    def list_gateways(self):

        return list(self.gateways.keys())

    def remove_gateway(self, name):

        if name in self.gateways:
            del self.gateways[name]
            print(f"✅ Payment Gateway Removed: {name}")
        else:
            print("❌ Payment Gateway Not Found")

    def is_connected(self, name):

        return name in self.gateways


payment_manager = PaymentManager()