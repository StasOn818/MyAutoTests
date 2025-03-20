# pages/base_api.py
import requests
from src.api.config.settings import API_KEY, ACCESS_TOKEN, BASE_URL, DEFAULT_LANGUAGE, TIMEOUT
from src.logger import setup_logger

class BaseAPI:
    def __init__(self, api_key=API_KEY, access_token=ACCESS_TOKEN, base_url=BASE_URL):
        self.api_key = api_key
        self.access_token = access_token
        self.base_url = base_url
        self.logger = setup_logger("TMDb_API")  # Initialize logger

    def _make_request(self, endpoint, method="GET", params=None, json_data=None):
        """Generic method to send requests to the API."""
        default_params = {"api_key": self.api_key, "language": DEFAULT_LANGUAGE}
        if params:
            default_params.update(params)

        headers = {}
        if method in ["POST", "DELETE"] and self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"
            headers["Content-Type"] = "application/json;charset=utf-8"

        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"Sending {method} request to {url} with params {default_params} and data {json_data}")

        try:
            response = requests.request(
                method, url, params=default_params, json=json_data, headers=headers, timeout=TIMEOUT
            )
            response.raise_for_status()
            response_data = response.json()
            self.logger.info(f"Received response: {response_data}")
            return response_data
        except requests.exceptions.HTTPError as e:
            self.logger.error(f"HTTP error occurred: {e} - Response: {response.text}")
            raise
        except Exception as e:
            self.logger.error(f"Error occurred: {e}")
            raise