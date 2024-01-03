---
date: "2024-01-03" # 2021-07-14
title: "c-bonds-and-nsdq"
image: "images/plots/c-bonds-and-nsdq.png"
author: "justin-guese"
draft: false
pctgain: -42
---

## Introduction to our strategy

If you are an investor who wants to diversify your portfolio and profit from the market volatility, you might be interested in our trading bot that switches between bonds and a leveraged Nasdaq index based on the cumulative return of different other indexes.

Our trading bot is based on a sophisticated algorithm that calculates the cumulative return of six stocks: BIL, QQQ, BND, SVXY, TMF, and GLD. These stocks represent different asset classes that have different risk-return profiles and correlations. By choosing these stocks, we aim to capture the market trends and hedge against various risks.

- BIL is an ETF that invests in short-term U.S. Treasury bills, which are considered to be risk-free and offer a stable income.
- QQQ is an ETF that tracks the performance of the Nasdaq-100 Index, which consists of the 100 largest and most innovative companies in the technology sector.
- BND is an ETF that invests in a broad range of U.S. investment-grade bonds, which provide diversification and lower volatility than stocks.
- SVXY is an ETF that seeks to provide inverse exposure to the short-term volatility of the S&P 500 Index, which means it gains value when the market is calm and loses value when the market is turbulent.
- TMF is an ETF that provides leveraged exposure to long-term U.S. Treasury bonds, which tend to appreciate when the market is bearish and interest rates are falling.
- GLD is an ETF that invests in physical gold, which is a traditional safe-haven asset that can hedge against inflation and currency fluctuations.

By comparing the cumulative return of these stocks, our trading bot can determine the optimal allocation between bonds and a leveraged Nasdaq index, which is QQQ x 2. Our trading bot aims to maximize your returns while minimizing your risk.

## Quick Summary

<img src="/images/plots/c-bonds-and-nsdq.png" alt = "returns chart for c-bonds-and-nsdq" width="100%">

| Metric | Value |
| --- | --- |
| Return % p.a. | -42 |
| Days active | 53 |
| Starting capital | 9939.86 |
| Current capital | 9324.37€ |

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
      <td><a target='_blank' href='https://finance.yahoo.com/quote/TQQQ'>TQQQ</a></td>
      <td>193.733019</td>
      <td>47.26</td>
      <td>9155.82</td>
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
      <td>0.34</td>
    </tr>
    <tr>
      <th>Cumulative Return</th>
      <td>-0.06</td>
    </tr>
    <tr>
      <th>CAGR﹪</th>
      <td>-0.27</td>
    </tr>
    <tr>
      <th>Sharpe</th>
      <td>-2.88</td>
    </tr>
    <tr>
      <th>Prob. Sharpe Ratio</th>
      <td>0.03</td>
    </tr>
    <tr>
      <th>Sortino</th>
      <td>-2.94</td>
    </tr>
    <tr>
      <th>Sortino/√2</th>
      <td>-2.08</td>
    </tr>
    <tr>
      <th>Omega</th>
      <td>0.29</td>
    </tr>
    <tr>
      <th>Max Drawdown</th>
      <td>-0.08</td>
    </tr>
    <tr>
      <th>Longest DD Days</th>
      <td>49</td>
    </tr>
    <tr>
      <th>Gain/Pain Ratio</th>
      <td>-0.71</td>
    </tr>
    <tr>
      <th>Gain/Pain (1M)</th>
      <td>-0.95</td>
    </tr>
    <tr>
      <th>Payoff Ratio</th>
      <td>0.34</td>
    </tr>
    <tr>
      <th>Profit Factor</th>
      <td>0.29</td>
    </tr>
    <tr>
      <th>Common Sense Ratio</th>
      <td>0.16</td>
    </tr>
    <tr>
      <th>CPC Index</th>
      <td>0.04</td>
    </tr>
    <tr>
      <th>Tail Ratio</th>
      <td>0.56</td>
    </tr>
    <tr>
      <th>Outlier Win Ratio</th>
      <td>9.24</td>
    </tr>
    <tr>
      <th>Outlier Loss Ratio</th>
      <td>2.93</td>
    </tr>
    <tr>
      <th>MTD</th>
      <td>-0.05</td>
    </tr>
    <tr>
      <th>3M</th>
      <td>-0.06</td>
    </tr>
    <tr>
      <th>6M</th>
      <td>-0.06</td>
    </tr>
    <tr>
      <th>YTD</th>
      <td>-0.05</td>
    </tr>
    <tr>
      <th>1Y</th>
      <td>-0.06</td>
    </tr>
    <tr>
      <th>3Y (ann.)</th>
      <td>-0.27</td>
    </tr>
    <tr>
      <th>5Y (ann.)</th>
      <td>-0.27</td>
    </tr>
    <tr>
      <th>10Y (ann.)</th>
      <td>-0.27</td>
    </tr>
    <tr>
      <th>All-time (ann.)</th>
      <td>-0.27</td>
    </tr>
    <tr>
      <th>Avg. Drawdown</th>
      <td>-0.08</td>
    </tr>
    <tr>
      <th>Avg. Drawdown Days</th>
      <td>49</td>
    </tr>
    <tr>
      <th>Recovery Factor</th>
      <td>0.82</td>
    </tr>
    <tr>
      <th>Ulcer Index</th>
      <td>0.02</td>
    </tr>
    <tr>
      <th>Serenity Index</th>
      <td>-1.0</td>
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
      <td>2023-12-28 10:03:57.930041</td>
      <td>Buy</td>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/TQQQ'>TQQQ</a></td>
      <td>51.540001</td>
      <td>10000.0</td>
      <td>515400.01</td>
    </tr>
    <tr>
      <td>2023-11-22 22:15:02.065514</td>
      <td>Buy</td>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/BND'>BND</a></td>
      <td>70.900002</td>
      <td>5000.0</td>
      <td>354500.01</td>
    </tr>
    <tr>
      <td>2023-11-22 22:15:02.018070</td>
      <td>Buy</td>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/QQQ'>QQQ</a></td>
      <td>390.059998</td>
      <td>5000.0</td>
      <td>1950299.99</td>
    </tr>
    <tr>
      <td>2023-11-21 22:15:02.808992</td>
      <td>Buy</td>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/GLD'>GLD</a></td>
      <td>185.350006</td>
      <td>5000.0</td>
      <td>926750.03</td>
    </tr>
    <tr>
      <td>2023-11-21 22:15:02.773493</td>
      <td>Buy</td>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/BND'>BND</a></td>
      <td>70.839996</td>
      <td>5000.0</td>
      <td>354199.98</td>
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
      <td>9324.37€</td>
    </tr>
    <tr>
      <td>2024-01-01</td>
      <td>9822.26€</td>
    </tr>
    <tr>
      <td>2023-12-31</td>
      <td>9822.26€</td>
    </tr>
    <tr>
      <td>2023-12-30</td>
      <td>9822.26€</td>
    </tr>
    <tr>
      <td>2023-12-29</td>
      <td>9822.26€</td>
    </tr>
    <tr>
      <td>2023-12-28</td>
      <td>9959.81€</td>
    </tr>
    <tr>
      <td>2023-12-28</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-27</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-26</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-25</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-24</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-23</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-22</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-21</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-20</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-19</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-18</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-17</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-16</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-15</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-14</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-13</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-12</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-11</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-10</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-09</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-08</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-07</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-06</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-06</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-11-22</td>
      <td>9967.95€</td>
    </tr>
    <tr>
      <td>2023-11-21</td>
      <td>10045.97€</td>
    </tr>
    <tr>
      <td>2023-11-20</td>
      <td>9983.91€</td>
    </tr>
    <tr>
      <td>2023-11-19</td>
      <td>9993.24€</td>
    </tr>
    <tr>
      <td>2023-11-16</td>
      <td>10019.18€</td>
    </tr>
    <tr>
      <td>2023-11-15</td>
      <td>10012.9€</td>
    </tr>
    <tr>
      <td>2023-11-14</td>
      <td>10090.45€</td>
    </tr>
    <tr>
      <td>2023-11-13</td>
      <td>10011.38€</td>
    </tr>
    <tr>
      <td>2023-11-12</td>
      <td>9985.0€</td>
    </tr>
    <tr>
      <td>2023-11-10</td>
      <td>9939.86€</td>
    </tr>
  </tbody>
</table>