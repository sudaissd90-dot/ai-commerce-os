from flask import Flask, jsonify, redirect, request
import requests
import config

app = Flask(__name__)


@app.route("/")
def home():
    return "AI Store Manager V1.0 Running"


@app.route("/shopify/install")
def shopify_install():

    shop = config.config.SHOPIFY_STORE_URL

    scopes = "write_products,read_products,write_inventory,read_inventory"

    url = (
        f"https://{shop}/admin/oauth/authorize"
        f"?client_id={config.config.SHOPIFY_CLIENT_ID}"
        f"&scope={scopes}"
        f"&redirect_uri={config.config.SHOPIFY_REDIRECT_URI}"
    )

    return redirect(url)


@app.route("/shopify/callback")
def shopify_callback():

    code = request.args.get("code")
    shop = request.args.get("shop")

    return jsonify({
        "message": "Shopify OAuth Callback Received",
        "shop": shop,
        "code_received": bool(code)
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
