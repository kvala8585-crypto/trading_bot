import os
import time
from pathlib import Path

from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import (
    BinanceAPIException,
    BinanceRequestException,
)

from bot.logging_config import setup_logger

# Load .env file
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

logger = setup_logger()


class BinanceClient:
    """
    Binance Futures Testnet Client
    """

    def __init__(self):

        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        if not self.api_key or not self.api_secret:
            raise ValueError("API Key or Secret not found in .env file.")

        self.client = Client(
            api_key=self.api_key,
            api_secret=self.api_secret,
            testnet=True,
        )

        # Binance Futures Testnet URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        # Sync local time with Binance server
        self.sync_time()

    def sync_time(self):
        """
        Synchronize local timestamp with Binance server.
        """

        try:

            logger.info("Synchronizing server time...")

            server_time = self.client.get_server_time()["serverTime"]
            local_time = int(time.time() * 1000)

            self.client.timestamp_offset = server_time - local_time

            logger.info(
                f"Timestamp synchronized. Offset = {self.client.timestamp_offset} ms"
            )

        except Exception as e:

            logger.error(f"Time Synchronization Failed: {e}")

    def ping(self):
        """
        Check Binance connection.
        """

        try:

            logger.info("Checking Binance Futures Testnet connection...")

            self.client.ping()

            logger.info("Connected successfully.")

            return True

        except BinanceAPIException as e:

            logger.error(f"Binance API Error: {e}")

            return False

        except BinanceRequestException as e:

            logger.error(f"Network Error: {e}")

            return False

        except Exception as e:

            logger.error(f"Unexpected Error: {e}")

            return False

    def get_server_time(self):
        """
        Fetch Binance server time.
        """

        try:

            logger.info("Fetching Binance server time...")

            data = self.client.get_server_time()

            logger.info("Server time fetched successfully.")

            return data

        except Exception as e:

            logger.error(f"Failed to fetch server time: {e}")

            return None