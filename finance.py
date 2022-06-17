import yfinance

amzn = yfinance.Ticker('AMZN')

info = amzn.info
print(info)
