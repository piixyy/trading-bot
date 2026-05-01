from binance.client import Client
import os
import time
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

def get_client():
    client = Client(API_KEY, API_SECRET)

    # Set testnet URL
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    # 🔥 REAL FIX: calculate time offset
    server_time = client.futures_time()['serverTime']
    local_time = int(time.time() * 1000)
    client.TIME_OFFSET = server_time - local_time

    return client