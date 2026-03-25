# DecisionAlpha — AI Portfolio Optimization & Backtesting Engine

## Overview

DecisionAlpha is a quantitative investment framework designed to simulate real-world portfolio decision-making using optimization and backtesting.

It combines financial modeling, data analysis, and algorithmic decision-making to evaluate investment strategies under uncertainty.

---

## Problem

Investors struggle to balance risk and return in dynamic markets.

Static strategies fail to adapt, leading to inefficient capital allocation.

---

## Solution

This project builds a dynamic portfolio allocation engine that:

- Uses rolling-window optimization (no lookahead bias)
- Rebalances periodically based on market data
- Applies realistic constraints (position limits, transaction costs)
- Benchmarks performance against the S&P 500

---

## Methodology

1. Data ingestion via Yahoo Finance  
2. Data cleaning and preprocessing  
3. Rolling window optimization (Modern Portfolio Theory)  
4. Backtesting with transaction costs  
5. Performance evaluation vs benchmark  

---

## Results

- Outperformed the S&P 500 in total return  
- Similar Sharpe ratio (risk-adjusted performance)  
- Higher drawdowns indicate opportunity for improvement  

---

## Performance Comparison

| Metric        | Strategy | S&P 500 |
|--------------|--------|--------|
| Return       | ~515%   | ~233%   |
| Sharpe       | ~0.76   | ~0.75   |
| Max Drawdown | ~-37%   | ~-33%   |

---

## Key Insights

- The strategy captures return opportunities through dynamic allocation  
- Performance is strong but sensitive to volatility  
- Risk management is the next major improvement area  

---

## Tech Stack

- Python  
- Pandas / NumPy  
- PyPortfolioOpt  
- Matplotlib  
- Yahoo Finance  

---

## Author

Geovane — Decision Analyst focused on Optimization, AI, and Financial Systems