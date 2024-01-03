---
date: "2024-01-03" # 2021-07-14
title: "c-nsdq-adapted"
image: "images/plots/c-nsdq-adapted.png"
author: "justin-guese"
draft: false
pctgain: 38
---

## Introduction to our strategy

Another trading bot strategy that you can find on our website is the c-nsdq strategy. This strategy is based on the idea that the NASDAQ index, which tracks the performance of the largest and most innovative technology companies in the US, can exhibit strong and persistent trends in either direction. It either enters a leveraged long or a shorted NASDAQ ETF position depending on if a calculated threshold of the cumulative return is reached.

The c-nsdq strategy is a dynamic and aggressive way to profit from the volatility and momentum of the technology sector, which is often influenced by factors such as news, earnings, regulations, and innovations. It uses a leveraged ETF, which is an exchange-traded fund that amplifies the returns of the underlying index by using financial derivatives and debt, to magnify the gains or losses of the NASDAQ index. It also uses a shorted ETF, which is an exchange-traded fund that inversely tracks the performance of the underlying index, to profit from the downward movements of the NASDAQ index.

The c-nsdq strategy is suitable for traders who are looking for a short-term and active approach to investing in the technology sector. It requires frequent monitoring and adjustments, as it constantly evaluates the cumulative return, which is the total percentage change in the value of the portfolio over a given period of time, of the NASDAQ index. The strategy also has a high turnover rate, which means higher transaction costs and taxes.

## Quick Summary

<img src="/images/plots/c-nsdq-adapted.png" alt = "returns chart for c-nsdq-adapted" width="100%">

| Metric | Value |
| --- | --- |
| Return % p.a. | 38 |
| Days active | 53 |
| Starting capital | 8834.7 |
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
      <td>0.83</td>
    </tr>
    <tr>
      <th>Cumulative Return</th>
      <td>0.06</td>
    </tr>
    <tr>
      <th>CAGR﹪</th>
      <td>0.31</td>
    </tr>
    <tr>
      <th>Sharpe</th>
      <td>0.86</td>
    </tr>
    <tr>
      <th>Prob. Sharpe Ratio</th>
      <td>0.63</td>
    </tr>
    <tr>
      <th>Sortino</th>
      <td>1.49</td>
    </tr>
    <tr>
      <th>Sortino/√2</th>
      <td>1.05</td>
    </tr>
    <tr>
      <th>Omega</th>
      <td>1.18</td>
    </tr>
    <tr>
      <th>Max Drawdown</th>
      <td>-0.12</td>
    </tr>
    <tr>
      <th>Longest DD Days</th>
      <td>49</td>
    </tr>
    <tr>
      <th>Gain/Pain Ratio</th>
      <td>0.19</td>
    </tr>
    <tr>
      <th>Gain/Pain (1M)</th>
      <td>1.21</td>
    </tr>
    <tr>
      <th>Payoff Ratio</th>
      <td>1.73</td>
    </tr>
    <tr>
      <th>Profit Factor</th>
      <td>1.18</td>
    </tr>
    <tr>
      <th>Common Sense Ratio</th>
      <td>1.54</td>
    </tr>
    <tr>
      <th>CPC Index</th>
      <td>0.83</td>
    </tr>
    <tr>
      <th>Tail Ratio</th>
      <td>1.3</td>
    </tr>
    <tr>
      <th>Outlier Win Ratio</th>
      <td>4.33</td>
    </tr>
    <tr>
      <th>Outlier Loss Ratio</th>
      <td>2.63</td>
    </tr>
    <tr>
      <th>MTD</th>
      <td>-0.05</td>
    </tr>
    <tr>
      <th>3M</th>
      <td>0.06</td>
    </tr>
    <tr>
      <th>6M</th>
      <td>0.06</td>
    </tr>
    <tr>
      <th>YTD</th>
      <td>-0.05</td>
    </tr>
    <tr>
      <th>1Y</th>
      <td>0.06</td>
    </tr>
    <tr>
      <th>3Y (ann.)</th>
      <td>0.31</td>
    </tr>
    <tr>
      <th>5Y (ann.)</th>
      <td>0.31</td>
    </tr>
    <tr>
      <th>10Y (ann.)</th>
      <td>0.31</td>
    </tr>
    <tr>
      <th>All-time (ann.)</th>
      <td>0.31</td>
    </tr>
    <tr>
      <th>Avg. Drawdown</th>
      <td>-0.07</td>
    </tr>
    <tr>
      <th>Avg. Drawdown Days</th>
      <td>25</td>
    </tr>
    <tr>
      <th>Recovery Factor</th>
      <td>0.67</td>
    </tr>
    <tr>
      <th>Ulcer Index</th>
      <td>0.06</td>
    </tr>
    <tr>
      <th>Serenity Index</th>
      <td>0.52</td>
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
      <td>2023-12-28 01:35:03.218088</td>
      <td>Buy</td>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/TQQQ'>TQQQ</a></td>
      <td>51.540001</td>
      <td>10000.0</td>
      <td>515400.01</td>
    </tr>
    <tr>
      <td>2023-12-27 01:35:03.206656</td>
      <td>Buy</td>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/TQQQ'>TQQQ</a></td>
      <td>51.270000</td>
      <td>10000.0</td>
      <td>512700.00</td>
    </tr>
    <tr>
      <td>2023-12-26 01:35:03.623343</td>
      <td>Buy</td>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/TQQQ'>TQQQ</a></td>
      <td>50.349998</td>
      <td>10000.0</td>
      <td>503499.98</td>
    </tr>
    <tr>
      <td>2023-12-25 01:35:03.826083</td>
      <td>Buy</td>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/TQQQ'>TQQQ</a></td>
      <td>50.349998</td>
      <td>10000.0</td>
      <td>503499.98</td>
    </tr>
    <tr>
      <td>2023-12-24 01:35:19.929802</td>
      <td>Buy</td>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/TQQQ'>TQQQ</a></td>
      <td>50.349998</td>
      <td>10000.0</td>
      <td>503499.98</td>
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
      <td>9985.0€</td>
    </tr>
    <tr>
      <td>2023-12-27</td>
      <td>10037.58€</td>
    </tr>
    <tr>
      <td>2023-12-26</td>
      <td>10167.45€</td>
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
      <td>10025.82€</td>
    </tr>
    <tr>
      <td>2023-12-21</td>
      <td>10315.16€</td>
    </tr>
    <tr>
      <td>2023-12-20</td>
      <td>9499.65€</td>
    </tr>
    <tr>
      <td>2023-12-19</td>
      <td>10133.97€</td>
    </tr>
    <tr>
      <td>2023-12-18</td>
      <td>10193.87€</td>
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
      <td>10104.02€</td>
    </tr>
    <tr>
      <td>2023-12-14</td>
      <td>9968.61€</td>
    </tr>
    <tr>
      <td>2023-12-13</td>
      <td>10337.06€</td>
    </tr>
    <tr>
      <td>2023-12-12</td>
      <td>10226.1€</td>
    </tr>
    <tr>
      <td>2023-12-11</td>
      <td>9729.96€</td>
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
      <td>9865.31€</td>
    </tr>
    <tr>
      <td>2023-12-07</td>
      <td>9580.04€</td>
    </tr>
    <tr>
      <td>2023-12-06</td>
      <td>10185.38€</td>
    </tr>
    <tr>
      <td>2023-12-06</td>
      <td>10055.97€</td>
    </tr>
    <tr>
      <td>2023-11-22</td>
      <td>10101.03€</td>
    </tr>
    <tr>
      <td>2023-11-21</td>
      <td>9804.06€</td>
    </tr>
    <tr>
      <td>2023-11-20</td>
      <td>10341.28€</td>
    </tr>
    <tr>
      <td>2023-11-19</td>
      <td>9985.0€</td>
    </tr>
    <tr>
      <td>2023-11-16</td>
      <td>10001.23€</td>
    </tr>
    <tr>
      <td>2023-11-15</td>
      <td>10012.9€</td>
    </tr>
    <tr>
      <td>2023-11-14</td>
      <td>10612.77€</td>
    </tr>
    <tr>
      <td>2023-11-13</td>
      <td>9894.38€</td>
    </tr>
    <tr>
      <td>2023-11-12</td>
      <td>9985.0€</td>
    </tr>
    <tr>
      <td>2023-11-10</td>
      <td>8834.7€</td>
    </tr>
  </tbody>
</table>