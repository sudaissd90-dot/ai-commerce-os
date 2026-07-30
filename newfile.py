from logger import logger
from config import config

from product_manager import product_manager
from order_manager import order_manager
from inventory_manager import inventory_manager

from shopify_manager import shopify
from ebay_manager import ebay

from supplier_manager import supplier_manager
from shipping_manager import shipping_manager
from payment_manager import payment_manager

from ai_agent_manager import ai_agent_manager
from workflow_manager import workflow_manager
from event_manager import event_manager


class AIStoreManager:

    def __init__(self):

        logger.info("🚀 AI Store Manager Initializing...")

        self.product_manager = product_manager
        self.order_manager = order_manager
        self.inventory_manager = inventory_manager

        self.shopify = shopify
        self.ebay = ebay

        self.suppliers = supplier_manager
        self.shipping = shipping_manager
        self.payment = payment_manager

        self.ai_agents = ai_agent_manager
        self.workflows = workflow_manager
        self.events = event_manager

        logger.info("✅ All Modules Loaded Successfully")

    def start(self):

        logger.info("=" * 60)
        logger.info("🤖 AI STORE MANAGER ENTERPRISE")
        logger.info("=" * 60)

        logger.info("System Ready")


if __name__ == "__main__":

    app = AIStoreManager()
    app.start()