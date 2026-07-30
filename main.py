print("MAIN FILE RUNNING")
print("MAIN FILE RUNNING")

print("=" * 60)
print("🚀 AI STORE MANAGER V1.0")
print("=" * 60)


# ==============================
# LOAD MODULES
# ==============================

import config
import workflow_setup
import pricing_setup
import agent_setup
import product_hunter_agent
import agent_analysis_setup
import supplier_setup

from autopilot_workflow import autopilot_workflow
from ebay_manager import ebay
from database import db


print("✅ AUTOPILOT IMPORT SUCCESS")


# ==============================
# CONFIG DEBUG
# ==============================

print("\n========== CONFIG CHECK ==========")

print("Config File :", config.__file__)

print(
    "Environment :",
    config.config.EBAY_ENVIRONMENT
)

print(
    "App ID :",
    config.config.EBAY_APP_ID
)


if config.config.EBAY_USER_TOKEN:
    print("User Token : FOUND")
else:
    print("User Token : EMPTY")


print("==================================")


# ==============================
# EBAY MANAGER CHECK
# ==============================

print("\n========== EBAY MANAGER CHECK ==========")

print(
    "create_offer:",
    hasattr(ebay, "create_offer")
)

print(
    "create_inventory_location:",
    hasattr(ebay, "create_inventory_location")
)

print("========================================")


# ==============================
# INITIALIZATION
# ==============================

print("\n🚀 Initializing AI Store Manager...\n")


print("✅ Database Module Loaded")


# ==============================
# EBAY CONNECTION TEST
# ==============================

print("\n🧪 Testing eBay Connection...\n")


ebay.test_connection()


# ==============================
# RUN AUTOPILOT WORKFLOW
# ==============================

try:

    print("\n🔥 Starting Autopilot Workflow...\n")


    result = autopilot_workflow.run()


    print("\n✅ Workflow Completed")


    print("\n📦 Approved Products:")


    if not result:

        print("No Approved Products")


    else:

        for item in result:

            print(item)


except Exception as e:

    print(
        "❌ Workflow Error:",
        e
    )


# ==============================
# SYSTEM READY
# ==============================

print("\n" + "=" * 60)

print("🤖 AI STORE MANAGER V1.0 READY")

print("=" * 60)