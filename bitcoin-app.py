from typing import Counter
from flask import Flask
import requests
import time
from collections import deque
# Description: get the cuurent Bitcoin currency and the avrage for the last 10 min
# desplay data as a web app

# global arguments
start_time = time.time()
total = 0
counter = 0


# get the latest bitcoin price from URL 
def get_latest_bitcoin_price():
     # the URL to get the .json file of the crypto currency
    TICKER_API_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(TICKER_API_URL)
    # get json file
    response_json = response.json() 
    # return the current price in USD
    return response_json["bpi"]["USD"]["rate"]

def get_price_avg():
    global total, counter
    while time.time() < start_time + 600:
        counter += 1
        total += float(latest_price.replace(",", ""))
        avg = total / counter
        return avg

def my_value(number):
    return ("{:,}".format(number))

latest_price = get_latest_bitcoin_price()
#mesurmentsQueue = deque([]) # que to save last 10 bitcoin price value

app = Flask(__name__)

@app.route("/") # att root display 
def main():
    global total, counter, latest_price, mesurmentsQueue
    #mesurmentsQueue = deque([]) # que to save last 10 bitcoin price value
    # keep cheking if bitcoin price changed
    if latest_price != get_latest_bitcoin_price(): # update argumanet if changed
        latest_price = get_latest_bitcoin_price()
    output = "The current Price of BitCoin is: " + latest_price + " US $ <br/><br/>"
    output += "BitCoin Average price for the last 10 minutes: " + my_value(get_price_avg()) + " US $"
    return output



if __name__ == "__main__":
    # run app
    app.run(host ='0.0.0.0', port = 5000, debug = True)
