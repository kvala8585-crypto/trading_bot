                                         ## Binance Futures Testnet Trading Bot##

A simple command-line trading bot built in Python using the Binance Futures Testnet API.

This project allows users to place Market and Limit orders from the terminal while performing input validation, logging every activity, handling errors gracefully, and displaying an order summary after each successful order.

---

# Features

- Binance Futures Testnet Integration
- Place Market Orders
- Place Limit Orders
- BUY and SELL Order Support
- Command Line Interface (CLI)
- Input Validation
- Error Handling
- Logging System
- Environment Variable Configuration
- Modular Python Project Structure

---

# Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── logs/
│   └── trading_bot.log
│
├── .env
├── .gitignore
├── cli.py
├── README.md
├── requirements.txt
│
├── test_client.py
├── test_logging.py
├── test_validation.py
├── test_market_order.py
└── test_limit_order.py
```

---

# Installation

### Clone Repository

```bash
git clone <repository-url>
```

### Go to Project Folder

```bash
cd trading_bot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate

```bash
source venv/bin/activate
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file inside the project folder.

Example:

```env
API_KEY=YOUR_BINANCE_API_KEY
API_SECRET=YOUR_BINANCE_SECRET_KEY
```

---

# Running the Project

Run the application using:

```bash
python cli.py
```

When the program starts, the following menu appears:

```
============================================================
      Binance Futures Testnet Trading Bot
============================================================

1. Place New Order
2. Exit
```

---

# Order Flow

### Step 1

Select **Place New Order**

### Step 2

Enter Trading Symbol

Example

```
BTCUSDT
```

### Step 3

Choose Order Side

```
BUY
```

or

```
SELL
```

### Step 4

Choose Order Type

```
MARKET
```

or

```
LIMIT
```

### Step 5

Enter Quantity

Example

```
0.001
```

### Step 6 (Only for LIMIT Order)

Enter Price

Example

```
107000
```

### Step 7

Bot sends the order to Binance Futures Testnet.

### Step 8

Order Summary is displayed.

Example

```
ORDER SUMMARY

Order ID    : 19828348044
Symbol      : BTCUSDT
Side        : SELL
Order Type  : LIMIT
Quantity    : 0.001
Price       : 107000.00
Status      : NEW
```

### Step 9

The bot asks:

```
Do you want to place another order? (Y/N)
```

---

# Input Validation

The application validates user input before sending the request.

Validation includes:

- Symbol cannot be empty
- BUY or SELL only
- MARKET or LIMIT only
- Quantity must be greater than zero
- Price must be greater than zero (Limit Order)
- Numeric value validation

---

# Logging

Every important action is stored inside:

```
logs/trading_bot.log
```

The log file contains:

- Server Time Synchronization
- Order Requests
- Successful Orders
- Errors
- Exceptions

---

# Error Handling

The project handles common runtime errors such as:

- Invalid user input
- Invalid numeric values
- Keyboard Interrupt (Ctrl + C)
- Binance API Errors
- Unexpected Exceptions

---

# Technologies Used

- Python
- python-binance
- python-dotenv
- Binance Futures Testnet API

---

# Future Improvements

Some features that can be added later:

- Cancel Order
- Order History
- Open Position Tracking
- Take Profit / Stop Loss
- Account Balance
- Multiple Trading Symbols
- Order Book Information

# Author

**Kavi Vala**

Python Developer | AI Automation Enthusiast