import pandas as pd
import numpy as np
from src.strategy import compute_weights

def backtest(
    data,
    window=252,
    rebalance_freq=21,
    transaction_cost=0.001  # 0.1%
):
    """
    Backtest com rebalanceamento periódico e custo de transação
    """

    returns = data.pct_change().dropna()

    portfolio_returns = []
    dates = []

    prev_weights = None

    for i in range(window, len(data), rebalance_freq):

        # 🔹 Janela de treino (sem lookahead)
        train = data.iloc[i - window:i]

        # 🔹 Calcula novos pesos
        try:
            weights = compute_weights(train)
        except:
            continue

        # 🔹 Período de teste
        test = returns.iloc[i:i + rebalance_freq]

        for date, row in test.iterrows():

            # 🔹 Retorno do portfólio
            daily_return = 0

            for asset in weights:
                if asset in row:
                    daily_return += weights[asset] * row[asset]

            # 🔹 Custo de transação (no rebalanceamento)
            if prev_weights is not None:
                turnover = sum(abs(weights.get(a, 0) - prev_weights.get(a, 0)) for a in weights)
                cost = turnover * transaction_cost
                daily_return -= cost

            portfolio_returns.append(daily_return)
            dates.append(date)

        prev_weights = weights

    portfolio_series = pd.Series(portfolio_returns, index=dates)

    return portfolio_series