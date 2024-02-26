import yfinance as yf
from datetime import datetime

userInput = input('enter tickers & separate with a comma: ')
timePeriod = input('enter the time period: ')

now = datetime.now()

tickerList = userInput.split(',')

def specialSauce(stockInput, pd):
    hist = stockInput.history(period=pd)
    print(type(hist))


for ticker in tickerList:
    stock = yf.Ticker(ticker.strip())
    specialSauce(stock, timePeriod)

print(tickerList)
