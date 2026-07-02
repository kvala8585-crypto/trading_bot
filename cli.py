from bot.orders import OrderManager


def main():

    print("=" * 60)
    print("      Binance Futures Testnet Trading Bot")
    print("=" * 60)

    order_manager = OrderManager()

    symbol = input("Enter Symbol (Ex: BTCUSDT): ").strip()

    side = input("Enter Side (BUY / SELL): ").strip().upper()

    order_type = input("Enter Order Type (MARKET / LIMIT): ").strip().upper()

    quantity = input("Enter Quantity: ").strip()

    if order_type == "MARKET":

        response = order_manager.place_market_order(
            symbol=symbol,
            side=side,
            quantity=quantity,
        )

    elif order_type == "LIMIT":

        price = input("Enter Price: ").strip()

        response = order_manager.place_limit_order(
            symbol=symbol,
            side=side,
            quantity=quantity,
            price=price,
        )

    else:

        print("\nInvalid Order Type.")
        return

    order_manager.print_order_summary(response)


if __name__ == "__main__":
    main()