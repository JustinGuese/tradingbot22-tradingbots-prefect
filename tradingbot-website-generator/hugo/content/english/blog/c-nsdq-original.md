---
date: "2024-01-03" # 2021-07-14
title: "c-nsdq-original"
image: "images/plots/c-nsdq-original.png"
author: "justin-guese"
draft: false
pctgain: -1
---

## Introduction to our strategy

Another trading bot strategy that you can find on our website is the c-nsdq strategy. This strategy is based on the idea that the NASDAQ index, which tracks the performance of the largest and most innovative technology companies in the US, can exhibit strong and persistent trends in either direction. It either enters a leveraged long or a shorted NASDAQ ETF position depending on if a calculated threshold of the cumulative return is reached.

The c-nsdq strategy is a dynamic and aggressive way to profit from the volatility and momentum of the technology sector, which is often influenced by factors such as news, earnings, regulations, and innovations. It uses a leveraged ETF, which is an exchange-traded fund that amplifies the returns of the underlying index by using financial derivatives and debt, to magnify the gains or losses of the NASDAQ index. It also uses a shorted ETF, which is an exchange-traded fund that inversely tracks the performance of the underlying index, to profit from the downward movements of the NASDAQ index.

The c-nsdq strategy is suitable for traders who are looking for a short-term and active approach to investing in the technology sector. It requires frequent monitoring and adjustments, as it constantly evaluates the cumulative return, which is the total percentage change in the value of the portfolio over a given period of time, of the NASDAQ index. The strategy also has a high turnover rate, which means higher transaction costs and taxes.

## Quick Summary

<img src="/images/plots/c-nsdq-original.png" alt = "returns chart for c-nsdq-original" width="100%">

| Metric | Value |
| --- | --- |
| Return % p.a. | -1 |
| Days active | 53 |
| Starting capital | 9986.99 |
| Current capital | 9960.37€ |

## Current portfolio
    
<table border="1" class="dataframe" id="portfolio">
  <thead>
    <tr style="text-align: right;">
      <th>Ticker</th>
      <th>Qty</th>
      <th>Crnt Price</th>
      <th>Worth (USD)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/BSV'>BSV</a></td>
      <td>129.624824</td>
      <td>76.78</td>
      <td>9952.59</td>
    </tr>
  </tbody>
</table>

## Detailed statistics

<table border="1" class="dataframe" id="qsmetrics">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Strategy</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Start Period</th>
      <td>2023-11-12</td>
    </tr>
    <tr>
      <th>End Period</th>
      <td>2024-01-02</td>
    </tr>
    <tr>
      <th>Risk-Free Rate</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Time in Market</th>
      <td>0.8</td>
    </tr>
    <tr>
      <th>Cumulative Return</th>
      <td>0</td>
    </tr>
    <tr>
      <th>CAGR﹪</th>
      <td>-0.01</td>
    </tr>
    <tr>
      <th>Sharpe</th>
      <td>-0.4</td>
    </tr>
    <tr>
      <th>Prob. Sharpe Ratio</th>
      <td>0.44</td>
    </tr>
    <tr>
      <th>Sortino</th>
      <td>-0.55</td>
    </tr>
    <tr>
      <th>Sortino/√2</th>
      <td>-0.39</td>
    </tr>
    <tr>
      <th>Omega</th>
      <td>0.93</td>
    </tr>
    <tr>
      <th>Max Drawdown</th>
      <td>-0.01</td>
    </tr>
    <tr>
      <th>Longest DD Days</th>
      <td>28</td>
    </tr>
    <tr>
      <th>Gain/Pain Ratio</th>
      <td>-0.07</td>
    </tr>
    <tr>
      <th>Gain/Pain (1M)</th>
      <td>-1.0</td>
    </tr>
    <tr>
      <th>Payoff Ratio</th>
      <td>0.99</td>
    </tr>
    <tr>
      <th>Profit Factor</th>
      <td>0.93</td>
    </tr>
    <tr>
      <th>Common Sense Ratio</th>
      <td>1.07</td>
    </tr>
    <tr>
      <th>CPC Index</th>
      <td>0.44</td>
    </tr>
    <tr>
      <th>Tail Ratio</th>
      <td>1.16</td>
    </tr>
    <tr>
      <th>Outlier Win Ratio</th>
      <td>3.98</td>
    </tr>
    <tr>
      <th>Outlier Loss Ratio</th>
      <td>3.02</td>
    </tr>
    <tr>
      <th>MTD</th>
      <td>0</td>
    </tr>
    <tr>
      <th>3M</th>
      <td>0</td>
    </tr>
    <tr>
      <th>6M</th>
      <td>0</td>
    </tr>
    <tr>
      <th>YTD</th>
      <td>0</td>
    </tr>
    <tr>
      <th>1Y</th>
      <td>0</td>
    </tr>
    <tr>
      <th>3Y (ann.)</th>
      <td>-0.01</td>
    </tr>
    <tr>
      <th>5Y (ann.)</th>
      <td>-0.01</td>
    </tr>
    <tr>
      <th>10Y (ann.)</th>
      <td>-0.01</td>
    </tr>
    <tr>
      <th>All-time (ann.)</th>
      <td>-0.01</td>
    </tr>
    <tr>
      <th>Avg. Drawdown</th>
      <td>-0.01</td>
    </tr>
    <tr>
      <th>Avg. Drawdown Days</th>
      <td>24</td>
    </tr>
    <tr>
      <th>Recovery Factor</th>
      <td>0.28</td>
    </tr>
    <tr>
      <th>Ulcer Index</th>
      <td>0.01</td>
    </tr>
    <tr>
      <th>Serenity Index</th>
      <td>-0.11</td>
    </tr>
  </tbody>
</table>

## Last trades

<table border="1" class="dataframe" id="trades">
  <thead>
    <tr style="text-align: right;">
      <th>Date</th>
      <th>Buy/Sell</th>
      <th>Ticker</th>
      <th>Price</th>
      <th>Qty</th>
      <th>Volume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2023-12-28 01:40:03.516032</td>
      <td>Buy</td>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/BSV'>BSV</a></td>
      <td>77.029999</td>
      <td>10000.0</td>
      <td>770299.99</td>
    </tr>
    <tr>
      <td>2023-12-27 01:40:04.104624</td>
      <td>Buy</td>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/BSV'>BSV</a></td>
      <td>76.830002</td>
      <td>10000.0</td>
      <td>768300.02</td>
    </tr>
    <tr>
      <td>2023-12-26 01:40:03.697821</td>
      <td>Buy</td>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/BSV'>BSV</a></td>
      <td>76.879997</td>
      <td>10000.0</td>
      <td>768799.97</td>
    </tr>
    <tr>
      <td>2023-12-25 01:40:21.612259</td>
      <td>Buy</td>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/BSV'>BSV</a></td>
      <td>76.879997</td>
      <td>10000.0</td>
      <td>768799.97</td>
    </tr>
    <tr>
      <td>2023-12-24 01:40:03.723060</td>
      <td>Buy</td>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/BSV'>BSV</a></td>
      <td>76.879997</td>
      <td>10000.0</td>
      <td>768799.97</td>
    </tr>
  </tbody>
</table>

## Portfolio worth over time 

<table border="1" class="dataframe" id="portfolioworth">
  <thead>
    <tr style="text-align: right;">
      <th>Date</th>
      <th>Portfolio Worth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2024-01-02</td>
      <td>9960.37€</td>
    </tr>
    <tr>
      <td>2024-01-01</td>
      <td>9983.7€</td>
    </tr>
    <tr>
      <td>2023-12-31</td>
      <td>9983.7€</td>
    </tr>
    <tr>
      <td>2023-12-30</td>
      <td>9983.7€</td>
    </tr>
    <tr>
      <td>2023-12-29</td>
      <td>9983.7€</td>
    </tr>
    <tr>
      <td>2023-12-28</td>
      <td>9977.22€</td>
    </tr>
    <tr>
      <td>2023-12-28</td>
      <td>9985.0€</td>
    </tr>
    <tr>
      <td>2023-12-27</td>
      <td>10010.99€</td>
    </tr>
    <tr>
      <td>2023-12-26</td>
      <td>9978.51€</td>
    </tr>
    <tr>
      <td>2023-12-25</td>
      <td>9985.0€</td>
    </tr>
    <tr>
      <td>2023-12-24</td>
      <td>9985.0€</td>
    </tr>
    <tr>
      <td>2023-12-23</td>
      <td>9985.0€</td>
    </tr>
    <tr>
      <td>2023-12-22</td>
      <td>9966.85€</td>
    </tr>
    <tr>
      <td>2023-12-21</td>
      <td>9991.49€</td>
    </tr>
    <tr>
      <td>2023-12-20</td>
      <td>10005.8€</td>
    </tr>
    <tr>
      <td>2023-12-19</td>
      <td>9987.6€</td>
    </tr>
    <tr>
      <td>2023-12-18</td>
      <td>9982.4€</td>
    </tr>
    <tr>
      <td>2023-12-17</td>
      <td>9985.0€</td>
    </tr>
    <tr>
      <td>2023-12-16</td>
      <td>9985.0€</td>
    </tr>
    <tr>
      <td>2023-12-15</td>
      <td>9973.31€</td>
    </tr>
    <tr>
      <td>2023-12-14</td>
      <td>10011.04€</td>
    </tr>
    <tr>
      <td>2023-12-13</td>
      <td>10051.84€</td>
    </tr>
    <tr>
      <td>2023-12-12</td>
      <td>9994.18€</td>
    </tr>
    <tr>
      <td>2023-12-11</td>
      <td>9985.0€</td>
    </tr>
    <tr>
      <td>2023-12-10</td>
      <td>9985.0€</td>
    </tr>
    <tr>
      <td>2023-12-09</td>
      <td>9985.0€</td>
    </tr>
    <tr>
      <td>2023-12-08</td>
      <td>9954.92€</td>
    </tr>
    <tr>
      <td>2023-12-07</td>
      <td>9995.47€</td>
    </tr>
    <tr>
      <td>2023-12-06</td>
      <td>9978.45€</td>
    </tr>
    <tr>
      <td>2023-12-06</td>
      <td>9979.1€</td>
    </tr>
    <tr>
      <td>2023-11-22</td>
      <td>9985.0€</td>
    </tr>
    <tr>
      <td>2023-11-21</td>
      <td>9994.23€</td>
    </tr>
    <tr>
      <td>2023-11-20</td>
      <td>9987.64€</td>
    </tr>
    <tr>
      <td>2023-11-19</td>
      <td>9985.0€</td>
    </tr>
    <tr>
      <td>2023-11-16</td>
      <td>10008.8€</td>
    </tr>
    <tr>
      <td>2023-11-15</td>
      <td>9962.58€</td>
    </tr>
    <tr>
      <td>2023-11-14</td>
      <td>10043.38€</td>
    </tr>
    <tr>
      <td>2023-11-13</td>
      <td>9991.64€</td>
    </tr>
    <tr>
      <td>2023-11-12</td>
      <td>9985.0€</td>
    </tr>
    <tr>
      <td>2023-11-10</td>
      <td>9986.99€</td>
    </tr>
  </tbody>
</table>