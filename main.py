from src.data_loader import load_data
from src.backtester import backtest
from src.metrics import total_return, sharpe_ratio, max_drawdown

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]

data = load_data(tickers)

# 🔹 Estratégia
portfolio_returns = backtest(data)

# 🔹 Benchmark
benchmark = yf.download("^GSPC", start="2015-01-01")["Close"].pct_change().dropna()

# 🔹 Alinha datas
common_index = portfolio_returns.index.intersection(benchmark.index)
portfolio_returns = portfolio_returns.loc[common_index]
benchmark = benchmark.loc[common_index]

# 🔹 Curva de capital
portfolio_curve = (1 + portfolio_returns).cumprod()
benchmark_curve = (1 + benchmark).cumprod()

# 🔹 Métricas
print("\n=== STRATEGY ===")
print("Return:", total_return(portfolio_returns))
print("Sharpe:", sharpe_ratio(portfolio_returns))
print("Max Drawdown:", max_drawdown(portfolio_returns))

print("\n=== BENCHMARK ===")
print("Return:", total_return(benchmark))
print("Sharpe:", sharpe_ratio(benchmark))
print("Max Drawdown:", max_drawdown(benchmark))

# 🔹 GRÁFICO
plt.figure()
plt.plot(portfolio_curve, label="Strategy")
plt.plot(benchmark_curve, label="S&P 500")
plt.title("Equity Curve: Strategy vs Benchmark")
plt.xlabel("Date")
plt.ylabel("Growth of $1")
plt.legend()
plt.grid()

plt.show()