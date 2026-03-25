from pypfopt import EfficientFrontier, risk_models, expected_returns

def compute_weights(data_window):
    """
    Calcula pesos ótimos com restrição de concentração
    """

    mu = expected_returns.mean_historical_return(data_window)
    S = risk_models.sample_cov(data_window)

    # 🔹 Limite de 40% por ativo (mais realista)
    ef = EfficientFrontier(mu, S, weight_bounds=(0, 0.4))

    try:
        ef.max_sharpe()
    except:
        ef.min_volatility()

    weights = ef.clean_weights()

    return weights