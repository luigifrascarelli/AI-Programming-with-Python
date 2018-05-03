import matplotlib.pyplot as plt
import pandas as pd
google_stock = pd.read_csv('Documents/NumPy/GOOG.csv', index_col = ['Date'], parse_dates = True, usecols = ['Date','Adj Close'])
apple_stock = pd.read_csv('Documents/NumPy/AAPL.csv', index_col = ['Date'], parse_dates = True, usecols = ['Date','Adj Close'])
amazon_stock = pd.read_csv('Documents/NumPy/AMZN.csv', index_col = ['Date'], parse_dates = True, usecols = ['Date','Adj Close'])
google_stock = google_stock.rename(columns ={'Adj Close':'Google'})
apple_stock = apple_stock.rename(columns ={'Adj Close' : 'Apple'})
amazon_stock = amazon_stock.rename(columns ={'Adj Close' : 'Amazon'})
dates = pd.date_range('2000-01-01', '2016-12-31')
all_stocks = pd.DataFrame(index = dates)
all_stocks = all_stocks.join(google_stock)
all_stocks = all_stocks.join(apple_stock)
all_stocks = all_stocks.join(amazon_stock)
nan_values = all_stocks.isnull().sum().sum()
all_stocks.dropna(axis=0)
print('Average stock price:\n', all_stocks.mean())
print('\nMedian stock price:\n', all_stocks.median())
print('\nStandard deviation:\n', all_stocks.std())
print('\nCorrelation:\n', all_stocks.corr())
rollingMean = google_stock.rolling(150).mean()
plt.plot(all_stocks['Google'])
plt.plot(rollingMean)
plt.legend(['Google Stock Price', 'Rolling Mean'])
plt.show()