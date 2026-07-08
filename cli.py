from bot.orders import OrderManager


def place_order():

    order_manager = OrderManager()

    try:

        symbol = input("\nEnter Symbol (Ex: BTCUSDT): ").strip().upper()

        if not symbol:
            print("\nSymbol cannot be empty.")
            return

        side = input("Enter Side (BUY / SELL): ").strip().upper()

        if side not in ["BUY", "SELL"]:
            print("\nInvalid Side. Please enter BUY or SELL.")
            return

        order_type = input("Enter Order Type (MARKET / LIMIT): ").strip().upper()

        if order_type not in ["MARKET", "LIMIT"]:
            print("\nInvalid Order Type. Please enter MARKET or LIMIT.")
            return

        quantity = float(input("Enter Quantity: "))

        if quantity <= 0:
            print("\nQuantity must be greater than zero.")
            return

        if order_type == "MARKET":

            response = order_manager.place_market_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
            )

        else:

            price = float(input("Enter Price: "))

            if price <= 0:
                print("\nPrice must be greater than zero.")
                return

            response = order_manager.place_limit_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
                price=price,
            )

        order_manager.print_order_summary(response)

        if response["success"]:
            print("\nOrder placed successfully.")

    except ValueError:
        print("\nPlease enter valid numeric values.")

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")

    except Exception as e:
        print(f"\nUnexpected Error : {e}")


def main():

    while True:

        print("\n" + "=" * 60)
        print("      Binance Futures Testnet Trading Bot")
        print("=" * 60)

        print("1. Place New Order")
        print("2. Exit")

        choice = input("\nChoose Option: ").strip()

        if choice == "1":

            place_order()

            again = input(
                "\nDo you want to place another order? (Y/N): "
            ).strip().upper()

            if again != "Y":

                print("\nThank you for using Binance Futures Testnet Trading Bot.")
                break

        elif choice == "2":

            print("\nThank you for using Binance Futures Testnet Trading Bot.")
            break

        else:

            print("\nInvalid Option. Please choose 1 or 2.")


if __name__ == "__main__":
    main()