import requests
import base64
from config import config


class OAuthManager:

    def __init__(self):
        self.client_id = config.EBAY_APP_ID
        self.client_secret = config.EBAY_CLIENT_SECRET
        self.runame = "Usman_Aslam-UsmanAsl-AiStor-gyditjfym"
        self.token_url = config.EBAY_OAUTH_URL
        self.refresh_token = config.EBAY_REFRESH_TOKEN

    def get_access_token(self):

        credentials = f"{self.client_id}:{self.client_secret}"
        encoded_credentials = base64.b64encode(
            credentials.encode()
        ).decode()

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {encoded_credentials}"
        }

        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            "scope": "https://api.ebay.com/oauth/api_scope"
        }

        response = requests.post(
            self.token_url,
            headers=headers,
            data=data
        )

        return response.json()


oauth = OAuthManager()