import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc

# Created the dictionary

dict_={'a':[11,21,31],'b':[12,22,32]}

# Casted Dictionary in Pandas whereas pandas is also an API and it has interfaces

df=pd.DataFrame(dict_)

# DataFrame Type
print(type(df))

#Data Frame Head
print(df.head())

# Mean Position
print(df.mean())

# Working on Coins of Crypto currencies

cg = CoinGeckoAPI()

bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

bitcoin_price_data = bitcoin_data['prices']

# printing first 5 prices of bitcoin
print(bitcoin_price_data[0:5])

# Finally turns this to data to Pandas Data Frame

data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp', 'Price'])

# Now that we have the DataFrame we will convert the timestamp to datetime and save it as a column called Date. We will map our unix_to_datetime to each timestamp and convert it to a readable datetime.

data['date'] = data['TimeStamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))

# print(data['date'])

# Using this modified dataset we can now group by the Date and find the min, max, open, and close for the candlesticks.

candlestick_data = data.groupby(data.date, as_index=False).agg({"Price": ['min', 'max', 'first', 'last']})
print(candlestick_data)

# Finally we are now ready to use plotly to create our Candlestick Chart.
fig = go.Figure(data=[go.Candlestick(x=candlestick_data['date'],
                open=candlestick_data['Price']['first'],
                high=candlestick_data['Price']['max'],
                low=candlestick_data['Price']['min'],
                close=candlestick_data['Price']['last'])
                ])

fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()





