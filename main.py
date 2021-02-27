from reddit_loader import import_reddit_data, chart_reddit_data
from stock_loader import load_stock_data, chart_stock_price_data, chart_stock_volatility_data
import matplotlib.pyplot as plt

# STOCKS_RISING = ['ENZC', 'TSNP', 'CBBT', 'VPER', 'OZSC', 'OPTI', 'GTLL']
# TO_WATCH = ['HCMC', 'VITX']
# could_rise = ["HBRM"]
STOCK_NAME = "ENZC"

reddit_data = import_reddit_data(STOCK_NAME)
stock_data = load_stock_data(STOCK_NAME)

fig, axs = plt.subplots(3)

reddit_ax = chart_reddit_data(reddit_data, STOCK_NAME, axs[0])
price_ax = chart_stock_price_data(stock_data, STOCK_NAME, axs[1])
vol_ax = chart_stock_volatility_data(stock_data, STOCK_NAME, axs[2])

plt.show()

