import yfinance as yf
import pandas as pd

def load_data(tickers, start="2015-01-01"):
    # 🔹 Download
    data = yf.download(tickers, start=start)

    # 🔹 Trata MultiIndex ou colunas simples
    if isinstance(data.columns, pd.MultiIndex):
        if "Adj Close" in data.columns.levels[0]:
            data = data["Adj Close"]
        else:
            data = data["Close"]
    else:
        if "Adj Close" in data.columns:
            data = data["Adj Close"]
        else:
            data = data["Close"]

    # 🔹 Garante ordem temporal
    data = data.sort_index()

    # 🔹 Remove duplicatas (raro, mas profissional tratar)
    data = data[~data.index.duplicated(keep="first")]

    # 🔹 Remove ativos com muitos dados faltantes
    data = data.dropna(axis=1, thresh=int(len(data) * 0.9))

    # 🔹 Preenche pequenos gaps
    data = data.ffill()

    # 🔹 Remove qualquer resíduo de NaN
    data = data.dropna()

    return data