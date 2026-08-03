class Config:

    # ==========================================
    # DATABASE
    # ==========================================

    DATABASE_PATH = "database/ai_enterprise.db"

    # ==========================================
    # SHOPIFY
    # ==========================================

    SHOPIFY_STORE_URL = "ai-store-manager-cnd98t8u.myshopify.com"
    SHOPIFY_ACCESS_TOKEN = ""

    # ==========================================
    # EBAY SANDBOX
    # ==========================================

    EBAY_ENVIRONMENT = "sandbox"

    # eBay Developer Credentials
    EBAY_APP_ID = ""
    EBAY_CLIENT_SECRET = ""
    EBAY_DEV_ID = ""

    # eBay OAuth
    EBAY_USER_TOKEN = ""
    # eBay API URLs
    EBAY_API_BASE = "https://api.sandbox.ebay.com"
    EBAY_OAUTH_URL = "https://api.sandbox.ebay.com/identity/v1/oauth2/token"
    EBAY_REFRESH_TOKEN = ""
    EBAY_ACCESS_TOKEN = ""

    # ==========================================
    # SUPPLIERS
    # ==========================================

    ALIEXPRESS_API_KEY = ""
    CJ_API_KEY = ""
    ZENDROP_API_KEY = ""

    # ==========================================
    # SHIPPING
    # ==========================================

    DHL_API_KEY = ""
    FEDEX_API_KEY = ""
    UPS_API_KEY = ""

    # ==========================================
    # PAYMENTS
    # ==========================================

    STRIPE_API_KEY = ""
    PAYPAL_API_KEY = ""

    # ==========================================
    # AI SETTINGS
    # ==========================================

    AI_ENABLED = True
    AUTO_PRODUCT_LISTING = True
    AUTO_PRICE_UPDATE = True
    AUTO_STOCK_UPDATE = True
    AUTO_ORDER_PROCESSING = True
    AUTO_MARKETING = True
    AUTO_SUPPLIER_SELECTION = True

    # ==========================================
    # SYSTEM
    # ==========================================

    DEFAULT_CURRENCY = "USD"
    DEFAULT_COUNTRY = "US"

    # ==========================================
    # LOGGING
    # ==========================================

    DEBUG_MODE = True
    LOG_LEVEL = "INFO"


    # ==========================================
    # SHOPIFY OAUTH
    # ==========================================

    SHOPIFY_CLIENT_ID = "8f4fac2a7b2e685dbc654fc421bd4776"
    SHOPIFY_CLIENT_SECRET = ""
    SHOPIFY_REDIRECT_URI = "https://site--ai-commerce-os--sm2wxhqvtd97.code.run/shopify/callback"


config = Config()
print("Refresh Token Exists:", hasattr(config, "EBAY_REFRESH_TOKEN"))