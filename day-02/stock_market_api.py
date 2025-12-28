
import requests

API_KEY = "SZISX3Y0ZUAZV2WA"

api_url = "https://www.alphavantage.co/"

symbol = "IBM"
# interval = "5min"

def get_stock_data(symbol, is_timeseries=True):
    query = f"query?function=TIME_SERIES_INTRADAY&symbol={symbol}&apikey={API_KEY}"
    url = api_url + query
    print(url)

    response = requests.get(url=url)
    data = response.json()
    for key, value in data.items():
        if is_timeseries:
            if key == 'Time Series (Daily)':
                continue
            else:
                print(key, value)
        else:
            print(key, value)
    print(data)

symbol = input("Enter the stock symbol (e.g., IBM, AMZN, GOOG): ")
is_timeseries = True # Set to True to fetch time series data
get_stock_data(symbol, is_timeseries)