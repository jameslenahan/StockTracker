import requests
import pandas as pd

def getdata(stock):
    company_quote = requests.get(f"https://financialmodelingprep.com/api/v3/quote/{stock}")
    company_quote = company_quote.json()
    share_price = float("{0:.2f}".format(company_quote[0]['price']))

print(getdata("aapl"))