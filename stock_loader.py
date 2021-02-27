import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_stock_data(keyword, length="5mo", pct_change_periods=4):
    # penny_tickers = yf.Tickers('ENZC TSNP CBBT VPER OZSC')
    penny_ticker = yf.Ticker(keyword)
    # gamble_tickers = yf.Tickers('HCMC VITX')
    history = length
    stock_price_history = penny_ticker.history(history)
    pct_change = stock_price_history["Close"].pct_change(periods=pct_change_periods)
    return {"volatility" : pct_change, "price" : stock_price_history}

def chart_stock_price_data(stock_data, keyword, plt_ax, show_plot=False, save_fig = False, y_lim=0.5, start_time='2020-08-15', end_time='2021-02-09', fig_size=(12,6)):
    stock_data["price"].plot(y="Close", figsize=fig_size, ax=plt_ax)

    plt_ax.set_xlim(pd.Timestamp(start_time), pd.Timestamp(end_time))
    if y_lim != 0.5:
        plt_ax.set_ylim(0, y_lim)

    plt_ax.set_title("Fast Risers (OTC) " + keyword + " Stock Price Close")
    if save_fig:
        plt.savefig("figures/" + keyword + "_price_close.png")
    if show_plot:
        plt.show()
    return plt_ax

def chart_stock_volatility_data(stock_data, keyword, plt_ax, show_plot=False, save_fig=False, y_lim=0.5, start_time='2020-08-15', end_time='2021-02-09', fig_size=(12,6)):
    stock_data["volatility"].plot(y="Close", figsize=fig_size, ax=plt_ax)

    plt_ax.set_xlim(pd.Timestamp(start_time), pd.Timestamp(end_time))
    if y_lim != 0.5:
        plt_ax.set_ylim(0, y_lim)

    plt_ax.set_title("Fast Risers (OTC) " + keyword + " Stock Price Close")
    if save_fig:
        plt.savefig("figures/" + keyword + "_price_close.png")
    if show_plot:
        plt.show()
    return plt_ax