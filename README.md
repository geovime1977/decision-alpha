# DecisionAlpha — AI Portfolio Optimization & Decision System

## Overview

DecisionAlpha is a decision system that applies optimization and data-driven logic to outperform traditional market strategies under uncertainty.

It combines financial modeling, operations research, and systematic decision-making to simulate real-world portfolio allocation.

---

## Problem

Investors and organizations struggle to balance risk and return in dynamic and uncertain environments.

Traditional allocation approaches are static and fail to adapt to changing market conditions.

---

## Solution

This project implements a **dynamic decision system** that:

- Uses rolling-window optimization (no lookahead bias)
- Dynamically reallocates capital based on market conditions
- Applies realistic constraints (position limits, transaction costs)
- Benchmarks performance against the S&P 500

---

## Methodology

1. Data ingestion via Yahoo Finance  
2. Data cleaning and validation  
3. Rolling window portfolio optimization (Modern Portfolio Theory)  
4. Backtesting with transaction costs  
5. Performance evaluation vs benchmark  

---

## Results

The strategy achieved:

- **~515% total return vs ~233% (S&P 500)**
- **Sharpe ratio: 0.76 vs 0.75**
- **Max drawdown: -37% vs -33%**

👉 The model outperforms in total return while maintaining similar risk-adjusted performance, with higher downside volatility.

---

## Equity Curve

![Equity Curve](equity_curve.png)

---

## Key Insights

- The model captures return opportunities through dynamic allocation  
- Performance is strong but sensitive to volatility  
- Drawdown control is the main improvement opportunity  

---

## Business Impact

This framework can support:

- Better capital allocation decisions  
- Improved risk management  
- More adaptive investment strategies in uncertain environments  

---

## So What?

The results suggest that systematic decision models can outperform traditional approaches.

However, without proper downside protection, higher returns come with increased risk exposure — highlighting the importance of risk control mechanisms.

---

## Why This Matters

This is not just a financial model — it is a **decision system**.

It demonstrates how optimization, constraints, and data can be combined to support real-world decision making under uncertainty.

---

## Perspective

With a background in **Mathematics and Geopolitics**, this project reflects a broader approach to decision-making:

- Modeling uncertainty  
- Understanding complex systems  
- Adapting to dynamic environments  

---

## Next Steps

- Volatility targeting  
- Drawdown control mechanisms  
- Integration of macroeconomic and geopolitical signals  

---

## Tech Stack

- Python  
- Pandas / NumPy  
- PyPortfolioOpt  
- Matplotlib  
- Yahoo Finance  

---

## Author

Geovane — Decision Analyst focused on Optimization, AI, and Decision Systems