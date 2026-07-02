from binance.enums import *
from binance.exceptions import (
    BinanceAPIException,
    BinanceRequestException,
)

from bot.client import BinanceClient
from bot.logging_config import setup_logger
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_quantity,
    validate_price,
)

logger = setup_logger()


class OrderManager:

    def __init__(self):
        self.client = BinanceClient().client

    def place_market_order(
        self,
        symbol,
        side,
        quantity,
    ):
        """
        Place Futures Market Order
        """

        try:

            symbol = validate_symbol(symbol)
            side = validate_side(side)
            quantity = validate_quantity(quantity)

            logger.info(
                f"MARKET ORDER -> "
                f"Symbol={symbol}, "
                f"Side={side}, "
                f"Qty={quantity}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=FUTURE_ORDER_TYPE_MARKET,
                quantity=quantity,
            )

            logger.info(
                f"Market Order Success | Order ID: {response['orderId']}"
            )

            return {
                "success": True,
                "message": "Market order placed successfully.",
                "data": response,
            }

        except BinanceAPIException as e:

            logger.error(f"Binance API Error: {e}")

            return {
                "success": False,
                "message": str(e),
            }

        except BinanceRequestException as e:

            logger.error(f"Network Error: {e}")

            return {
                "success": False,
                "message": str(e),
            }

        except Exception as e:

            logger.error(f"Unexpected Error: {e}")

            return {
                "success": False,
                "message": str(e),
            }

    def place_limit_order(
        self,
        symbol,
        side,
        quantity,
        price,
    ):
        """
        Place Futures Limit Order
        """

        try:

            symbol = validate_symbol(symbol)
            side = validate_side(side)
            quantity = validate_quantity(quantity)
            price = validate_price(price)

            logger.info(
                f"LIMIT ORDER -> "
                f"Symbol={symbol}, "
                f"Side={side}, "
                f"Qty={quantity}, "
                f"Price={price}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=FUTURE_ORDER_TYPE_LIMIT,
                quantity=quantity,
                price=price,
                timeInForce=TIME_IN_FORCE_GTC,
            )

            logger.info(
                f"Limit Order Success | Order ID: {response['orderId']}"
            )

            return {
                "success": True,
                "message": "Limit order placed successfully.",
                "data": response,
            }

        except BinanceAPIException as e:

            logger.error(f"Binance API Error: {e}")

            return {
                "success": False,
                "message": str(e),
            }

        except BinanceRequestException as e:

            logger.error(f"Network Error: {e}")

            return {
                "success": False,
                "message": str(e),
            }

        except Exception as e:

            logger.error(f"Unexpected Error: {e}")

            return {
                "success": False,
                "message": str(e),
            }

    def print_order_summary(self, response):
        """
        Print formatted order summary.
        """

        if not response["success"]:
            print("\nOrder Failed")
            print(f"Reason : {response['message']}")
            return

        order = response["data"]

        print("\n" + "=" * 50)
        print("ORDER SUMMARY")
        print("=" * 50)

        print(f"Order ID     : {order.get('orderId')}")
        print(f"Symbol       : {order.get('symbol')}")
        print(f"Side         : {order.get('side')}")
        print(f"Order Type   : {order.get('type')}")
        print(f"Quantity     : {order.get('origQty')}")
        print(f"Price        : {order.get('price')}")
        print(f"Status       : {order.get('status')}")

        print("=" * 50)