from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)

print("=" * 50)
print("SUCCESS TESTS")
print("=" * 50)

try:
    print("Symbol      :", validate_symbol("btcusdt"))
    print("Side        :", validate_side("buy"))
    print("Order Type  :", validate_order_type("market"))
    print("Quantity    :", validate_quantity(0.01))
    print("Price       :", validate_price(108000))
except ValueError as e:
    print("Error:", e)

print("\n" + "=" * 50)
print("ERROR TESTS")
print("=" * 50)

# Invalid Side
try:
    validate_side("ABC")
except ValueError as e:
    print("Invalid Side Test      :", e)

# Invalid Quantity
try:
    validate_quantity(-5)
except ValueError as e:
    print("Invalid Quantity Test  :", e)

# Invalid Price
try:
    validate_price(-100)
except ValueError as e:
    print("Invalid Price Test     :", e)

# Invalid Symbol
try:
    validate_symbol("BTC")
except ValueError as e:
    print("Invalid Symbol Test    :", e)