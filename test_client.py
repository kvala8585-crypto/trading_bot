from bot.client import BinanceClient

client = BinanceClient()

if client.ping():

    print("Connected Successfully")

    print(client.get_server_time())

else:

    print("Connection Failed")