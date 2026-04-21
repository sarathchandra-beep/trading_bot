from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

class BinanceFuturesClient:
    def __init__(self):
        self.client = Client(
            os.getenv("API_KEY"),
            os.getenv("API_SECRET")
        )

        
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

    def place_order(self, **kwargs):
        return self.client.futures_create_order(**kwargs)