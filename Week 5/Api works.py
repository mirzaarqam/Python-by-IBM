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

# Casted Dictionary in Pandas

df=pd.DataFrame(dict_)

# DataFrame Type
print(type(df))

# Getting Crypto Data
cg = CoinGeckoAPI()

bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

# Bit Coin price data fetch
bitcoin_price_data = bitcoin_data['prices']

print(bitcoin_price_data[0:5])

#Data Frame Head
print(df.head())

# Mean Position
print(df.mean())

