\# Binance Futures Testnet Trading Bot



\## Overview



This project is a command-line trading bot developed using Python and the Binance Futures Testnet API.



The application allows users to place Market and Limit orders securely through the Binance Futures Testnet while following clean code practices, logging, input validation, and error handling.



\---



\## Features



\- Binance Futures Testnet Integration

\- Market Orders

\- Limit Orders

\- BUY / SELL Support

\- Input Validation

\- Logging

\- Exception Handling

\- Environment Variable Support

\- Modular Project Structure

\- Command Line Interface (CLI)



\---



\## Project Structure



```

trading\_bot/

│

├── bot/

│   ├── \_\_init\_\_.py

│   ├── client.py

│   ├── logging\_config.py

│   ├── orders.py

│   └── validators.py

│

├── logs/

│

├── .env

├── cli.py

├── requirements.txt

├── README.md

├── test\_client.py

├── test\_market\_order.py

└── test\_limit\_order.py

```



\---



\## Installation



Clone the repository



```bash

git clone <repository-url>

```



Create virtual environment



```bash

python -m venv venv

```



Activate virtual environment



Windows



```bash

venv\\Scripts\\activate

```



Install dependencies



```bash

pip install -r requirements.txt

```



\---



\## Environment Variables

\---



\## Run



```bash

python cli.py

```



\---



\## Market Order Example



```

Symbol      : BTCUSDT

Side        : BUY

Order Type  : MARKET

Quantity    : 0.001

```



\---



\## Limit Order Example



```

Symbol      : BTCUSDT

Side        : BUY

Order Type  : LIMIT

Quantity    : 0.001

Price       : 10000

```



\---



\## Logging



All API requests, responses, and errors are automatically stored inside



```

logs/trading\_bot.log

```



\---



\## Technologies Used



\- Python

\- python-binance

\- python-dotenv

\- Binance Futures Testnet API



&#x20;- Project Structure

\- Binance Futures Testnet Integration

\- Environment Variables

\- Logging

\- Error Handling

\- Input Validation

\- Market Orders

\- Limit Orders

\- CLI





\---



\## Author



Kavi Vala

