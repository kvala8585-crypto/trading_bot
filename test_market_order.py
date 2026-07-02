from bot.orders import OrderManager

order = OrderManager()

response = order.place_market_order(
    symbol="BTCUSDT",
    side="BUY",
    quantity=0.001
)

order.print_order_summary(response)