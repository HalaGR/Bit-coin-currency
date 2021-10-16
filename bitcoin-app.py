from flask import Flask
import requests
import time
from collections import deque
# Description: get the cuurent Bitcoin currency and the avrage for the last 10 min
# desplay data as a web app


app = Flask(__name__)
#add argument latest price to app inorder to update price if changed
app.config['latest_price'] = '-1' 
app.config['counter'] = 0

@app.route("/") # att root display 
def main():
    mesurmentsQueue = deque([]) # que to save last 10 bitcoin price value
    while True:
        # keep cheking if bitcoin price changed
        if app.config['latest_price'] != get_latest_bitcoin_price(): # update argumanet if changed
            app.config['latest_price'] = get_latest_bitcoin_price()
        output = "The current Price of Bitcoin is: " + app.config['latest_price'] + " US $ <br/><br/>"
        # if first time cheking return avg as cuurent price
        if app.config['counter'] == 0 : 
            output += "BitCoin Average price for the last 10 minutes: " + app.config['latest_price'] + " US $"
            return output
        # if not 1'st time calculate avg and wait 1 min before returning output
        else :
            if(len(mesurmentsQueue)==10): # if 10 minutes passed pop fierst in value
                mesurmentsQueue.popleft()
            mesurmentsQueue.append(float(app.config['latest_price']))
            # update counter
            app.config['counter'] += 1
            if(app.config['counter'] == 10):
                output += "BitCoin Average price for the last 10 minutes: ",(sum(mesurmentsQueue)/len(mesurmentsQueue))
                counter=0
        time.sleep(60)
        return output

# get the latest bitcoin price from URL 
def get_latest_bitcoin_price():
     # the URL to get the .json file of the crypto currency
    TICKER_API_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(TICKER_API_URL)
    # get json file
    response_json = response.json() 
    # return the current price in USD
    return response_json["bpi"]["USD"]["rate"]



if __name__ == "__main__":
    # run app
    app.run()