VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]


def validate_symbol(symbol: str) -> str:
    """
    Validate trading symbol.
    """

    symbol = symbol.upper().strip()

    if len(symbol) < 6:
        raise ValueError("Invalid trading symbol.")

    return symbol


def validate_side(side: str) -> str:
    """
    Validate BUY or SELL.
    """

    side = side.upper().strip()

    if side not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL.")

    return side


def validate_order_type(order_type: str) -> str:
    """
    Validate MARKET or LIMIT.
    """

    order_type = order_type.upper().strip()

    if order_type not in VALID_ORDER_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT.")

    return order_type


def validate_quantity(quantity: float) -> float:
    """
    Validate quantity.
    """

    try:
        quantity = float(quantity)
    except ValueError:
        raise ValueError("Quantity must be a number.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    return quantity


def validate_price(price):
    """
    Validate price for LIMIT orders.
    """

    try:
        price = float(price)
    except ValueError:
        raise ValueError("Price must be a number.")

    if price <= 0:
        raise ValueError("Price must be greater than zero.")

    return price