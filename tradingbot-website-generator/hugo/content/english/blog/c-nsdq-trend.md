---
date: "2024-01-03" # 2021-07-14
title: "c-nsdq-trend"
image: "images/plots/c-nsdq-trend.png"
author: "justin-guese"
draft: false
pctgain: 0
---

## Introduction to our strategy

Another trading bot strategy that you can find on our website is the c-nsdq strategy. This strategy is based on the idea that the NASDAQ index, which tracks the performance of the largest and most innovative technology companies in the US, can exhibit strong and persistent trends in either direction. It either enters a leveraged long or a shorted NASDAQ ETF position depending on if a calculated threshold of the cumulative return is reached.

The c-nsdq strategy is a dynamic and aggressive way to profit from the volatility and momentum of the technology sector, which is often influenced by factors such as news, earnings, regulations, and innovations. It uses a leveraged ETF, which is an exchange-traded fund that amplifies the returns of the underlying index by using financial derivatives and debt, to magnify the gains or losses of the NASDAQ index. It also uses a shorted ETF, which is an exchange-traded fund that inversely tracks the performance of the underlying index, to profit from the downward movements of the NASDAQ index.

The c-nsdq strategy is suitable for traders who are looking for a short-term and active approach to investing in the technology sector. It requires frequent monitoring and adjustments, as it constantly evaluates the cumulative return, which is the total percentage change in the value of the portfolio over a given period of time, of the NASDAQ index. The strategy also has a high turnover rate, which means higher transaction costs and taxes.

## Quick Summary

<img src="/images/plots/c-nsdq-trend.png" alt = "returns chart for c-nsdq-trend" width="100%">

| Metric | Value |
| --- | --- |
| Return % p.a. | 0 |
| Days active | 51 |
| Starting capital | 10000.0 |
| Current capital | 10000.0€ |

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
      <td><a target='_blank' href='https://finance.yahoo.com/quote/USD'>USD</a></td>
      <td>10000</td>
      <td>1</td>
      <td>10000</td>
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
      <td>2023-11-13</td>
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
      <td>0</td>
    </tr>
    <tr>
      <th>Cumulative Return</th>
      <td>0</td>
    </tr>
    <tr>
      <th>CAGR﹪</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Sharpe</th>
      <td>-</td>
    </tr>
    <tr>
      <th>Prob. Sharpe Ratio</th>
      <td>-</td>
    </tr>
    <tr>
      <th>Sortino</th>
      <td>-</td>
    </tr>
    <tr>
      <th>Sortino/√2</th>
      <td>-</td>
    </tr>
    <tr>
      <th>Omega</th>
      <td>-</td>
    </tr>
    <tr>
      <th>Max Drawdown</th>
      <td></td>
    </tr>
    <tr>
      <th>Longest DD Days</th>
      <td>-</td>
    </tr>
    <tr>
      <th>Gain/Pain Ratio</th>
      <td>-</td>
    </tr>
    <tr>
      <th>Gain/Pain (1M)</th>
      <td>-</td>
    </tr>
    <tr>
      <th>Payoff Ratio</th>
      <td>-</td>
    </tr>
    <tr>
      <th>Profit Factor</th>
      <td>-</td>
    </tr>
    <tr>
      <th>Common Sense Ratio</th>
      <td>-</td>
    </tr>
    <tr>
      <th>CPC Index</th>
      <td>-</td>
    </tr>
    <tr>
      <th>Tail Ratio</th>
      <td>-</td>
    </tr>
    <tr>
      <th>Outlier Win Ratio</th>
      <td>-</td>
    </tr>
    <tr>
      <th>Outlier Loss Ratio</th>
      <td>-</td>
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
      <td>0</td>
    </tr>
    <tr>
      <th>5Y (ann.)</th>
      <td>0</td>
    </tr>
    <tr>
      <th>10Y (ann.)</th>
      <td>0</td>
    </tr>
    <tr>
      <th>All-time (ann.)</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Recovery Factor</th>
      <td>-</td>
    </tr>
    <tr>
      <th>Ulcer Index</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Serenity Index</th>
      <td>-</td>
    </tr>
    <tr>
      <th>Avg. Drawdown Days</th>
      <td>-</td>
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
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2024-01-01</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-31</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-30</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-29</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-12-28</td>
      <td>10000.0€</td>
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
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-11-21</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-11-20</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-11-19</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-11-16</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-11-15</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-11-14</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-11-13</td>
      <td>10000.0€</td>
    </tr>
    <tr>
      <td>2023-11-12</td>
      <td>10000.0€</td>
    </tr>
  </tbody>
</table>