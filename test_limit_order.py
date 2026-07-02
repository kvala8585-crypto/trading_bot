from bot.orders import OrderManager

order = OrderManager()

response = order.place_limit_order(
    symbol="BTCUSDT",
    side="BUY",
    quantity=0.001,
    price=10000
)

order.print_order_summary(response)