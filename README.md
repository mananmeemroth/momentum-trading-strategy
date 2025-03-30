# **Momentum Trading Strategy**

This repository contains a Python-based **Momentum Trading Strategy** implemented and tested using daily stock data for five major companies: **Apple Inc.**, **Facebook**, **Tesla**, **JP Morgan**, and **Amazon**. The strategy is based on momentum indicators like the **Relative Strength Index (RSI)** and other technical analysis tools.

The project uses **backtesting** to evaluate the strategy's performance, including **trade-level** and **performance-level** analytics. This project is built using **Jupyter Notebook** and can be easily extended or modified for further experimentation with different trading strategies and data sources.

---

## **Table of Contents**
1. [Installation](#installation)
2. [Usage](#usage)
3. [Data](#data)
4. [Strategy Overview](#strategy-overview)
5. [Backtesting and Analytics](#backtesting-and-analytics)
6. [Results](#results)
7. [Contribution](#contribution)
8. [License](#license)

---

## **Installation**

To run the project locally, follow the steps below to install the necessary dependencies.

The datasets for each company are stored in the `data/` directory:

- `apple.csv`
- `facebook.csv`
- `tesla.csv`
- `jpmorgan.csv`
- `amazon.csv`

These CSV files contain the historical stock price data that is used in the backtesting and performance evaluation.

---

## **Strategy Overview**

The **Momentum Trading Strategy** uses **Relative Strength Index (RSI)** to generate buy and sell signals:

- **Buy** when the RSI falls below **30** (indicating oversold conditions).
- **Sell** when the RSI rises above **70** (indicating overbought conditions).

Additionally, you can modify the strategy to incorporate other indicators such as **Simple Moving Average (SMA)**, **Exponential Moving Average (EMA)**, or any other trading indicators of your choice.

### **RSI Calculation**
The **RSI** is calculated using the following steps:

1. Calculate the daily price changes (`delta`).
2. Separate the positive and negative changes.
3. Calculate the average gain and average loss over a defined period (e.g., 14 days).
4. Compute the Relative Strength (RS) as the ratio of average gain to average loss.
5. Calculate the RSI as:  
   
   \[
   RSI = 100 - \frac{100}{1 + RS}
   \]

---

## **Backtesting and Analytics**

### **Backtesting Process**

The strategy is tested using the following steps:

1. **Indicator Calculation**: The RSI and other technical indicators (e.g., SMA, EMA) are calculated for each stock.
2. **Signal Generation**: Buy and sell signals are generated based on the calculated RSI values.
3. **Backtesting**: The strategy is backtested using historical data. This simulates the buy/sell actions of a trader according to the generated signals.
4. **Execution**: Trades are executed based on the buy and sell signals, and the portfolio value is updated accordingly.

### **Analytics**

- **Trade-level analytics**: Tracks individual trades including entry/exit points and returns for each trade.
- **Performance-level analytics**: Calculates overall strategy performance using metrics such as:
  - **Cumulative Returns**: The overall return from the strategy.
  - **Sharpe Ratio**: A measure of the risk-adjusted return.
  - **Maximum Drawdown**: The maximum observed loss from a peak to a trough.

---

## **Results**

After running the Jupyter notebook, you will see the following results:

- **Cumulative Returns**: A plot showing the growth of $1 invested in the strategy over time compared to a buy-and-hold strategy.
- **Performance Metrics**: Key performance indicators such as the **Sharpe ratio**, **maximum drawdown**, and **total returns**.
- **Visualizations**: Charts to visualize the price action, buy/sell signals, and cumulative returns.

### **Examples of Results**

- A line chart comparing the **buy-and-hold** strategy against the momentum strategy with buy/sell signals overlaid.
- A performance summary showing the **Sharpe ratio** and **maximum drawdown** for the backtest period.

---

## **Contribution**

Feel free to fork this project, create issues, or submit pull requests. Contributions are welcome!

To contribute:

1. Fork the repository to your own GitHub account.
2. Create a new branch for your feature or fix.
3. Make the necessary changes and commit them.
4. Push your changes to your repository.
5. Open a pull request to the original repository.

---

## **License**

This project is licensed under the **MIT License** 
