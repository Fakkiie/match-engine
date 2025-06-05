import random
import time
import os
import json

#file paths
folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
os.makedirs(folder_path, exist_ok=True)  # Create the 'data/' folder if it doesn't exist

file_path = os.path.join(folder_path, "orders.txt")

#tickers
Tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]

#generaete random orders as a dict 
def generate_order():
    ticker = random.choice(Tickers)
    price = random.randint(65, 127)
    quantity = random.randint(1, 100)
    side = random.choice(["BUY", "SELL"])
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return {
        "ticker": ticker,
        "price": price,
        "quantity": quantity,
        "side": side,
        "timestamp": timestamp
    }

#write all orders to a file
with open(file_path, "w") as f:
    for _ in range(5):
        order = generate_order()
        f.write(json.dumps(order) + "\n")
