from flask import Flask, jsonify, redirect, request
import requests
import os
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

    if not code or not shop:
        return jsonify({
            "success": False,
            "message": "Missing Shopify OAuth code or shop"
        }), 400

    client_id = os.getenv(
        "SHOPIFY_CLIENT_ID",
        config.config.SHOPIFY_CLIENT_ID
    )

    client_secret = os.getenv(
        "SHOPIFY_CLIENT_SECRET",
        config.config.SHOPIFY_CLIENT_SECRET
    )

    if not client_id or not client_secret:
        return jsonify({
            "success": False,
            "message": "Shopify Client ID/Secret missing"
        }), 500

    token_url = f"https://{shop}/admin/oauth/access_token"

    response = requests.post(
        token_url,
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code
        },
        timeout=30
    )

    if response.status_code != 200:
        return jsonify({
            "success": False,
            "message": "Shopify token exchange failed",
            "status": response.status_code, "shopify_error": response.text
        }), 500

    token_data = response.json()

    return jsonify({
        "success": True,
        "message": "Shopify OAuth completed successfully",
        "shop": shop,
        "token_received": bool(token_data.get("access_token")),
        "scope": token_data.get("scope", "")
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
