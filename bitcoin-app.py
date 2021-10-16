from flask import Flask
import requests
# Description: get the cuurent Bitcoin currency and the avrage for the last 10 min
# desplay data as a web app


app = Flask(__name__)
#add argument latest price to app inorder to update price if changed
app.config['latest_price'] = '-1' 

@app.route("/") # att root display 
def main():
    while True:
        # keep cheking if bitcoin price changed
        if app.config['latest_price'] != get_latest_bitcoin_price(): # update argumanet if changed
            app.config['latest_price'] = get_latest_bitcoin_price()
        return "The current Price of bitcoin is: " + app.config['latest_price'] + " US $ \n"

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