---
date: "2024-01-03" # 2021-07-14
title: "static-manual-sharpeopt-l2"
image: "images/plots/static-manual-sharpeopt-l2.png"
author: "justin-guese"
draft: false
pctgain: 46
---

## Introduction to our strategy

created in basebot

## Quick Summary

<img src="/images/plots/static-manual-sharpeopt-l2.png" alt = "returns chart for static-manual-sharpeopt-l2" width="100%">

| Metric | Value |
| --- | --- |
| Return % p.a. | 46 |
| Days active | 53 |
| Starting capital | 10000 |
| Current capital | 16885.75€ |

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
      <td><a target='_blank' href='https://finance.yahoo.com/quote/ETH-USD'>ETH-USD</a></td>
      <td>1.954529</td>
      <td>2199.01</td>
      <td>4298.03</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/TSLA'>TSLA</a></td>
      <td>13.112828</td>
      <td>241.99</td>
      <td>3173.17</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/LLY'>LLY</a></td>
      <td>3.699339</td>
      <td>606.41</td>
      <td>2243.32</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/NVDA'>NVDA</a></td>
      <td>4.475467</td>
      <td>478.99</td>
      <td>2143.70</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/PGR'>PGR</a></td>
      <td>4.996344</td>
      <td>163.04</td>
      <td>814.60</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/UNH'>UNH</a></td>
      <td>1.057598</td>
      <td>546.00</td>
      <td>577.45</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/URA'>URA</a></td>
      <td>18.814410</td>
      <td>26.86</td>
      <td>505.36</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/AAPL'>AAPL</a></td>
      <td>2.413577</td>
      <td>185.12</td>
      <td>446.80</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/BTC-USD'>BTC-USD</a></td>
      <td>0.008946</td>
      <td>42138.48</td>
      <td>376.97</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/USD'>USD</a></td>
      <td>368.602408</td>
      <td>1.00</td>
      <td>368.60</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/W1TA.DE'>W1TA.DE</a></td>
      <td>11.612243</td>
      <td>30.17</td>
      <td>350.34</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/NOC'>NOC</a></td>
      <td>0.559623</td>
      <td>473.68</td>
      <td>265.08</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/DBE'>DBE</a></td>
      <td>12.331581</td>
      <td>19.09</td>
      <td>235.41</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/DG'>DG</a></td>
      <td>1.531187</td>
      <td>138.81</td>
      <td>212.54</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/WM'>WM</a></td>
      <td>1.024449</td>
      <td>180.60</td>
      <td>185.02</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/VDE'>VDE</a></td>
      <td>1.503508</td>
      <td>118.06</td>
      <td>177.50</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/DBO'>DBO</a></td>
      <td>7.884130</td>
      <td>14.00</td>
      <td>110.38</td>
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
      <td>1.0</td>
    </tr>
    <tr>
      <th>Cumulative Return</th>
      <td>0.07</td>
    </tr>
    <tr>
      <th>CAGR﹪</th>
      <td>0.38</td>
    </tr>
    <tr>
      <th>Sharpe</th>
      <td>2.53</td>
    </tr>
    <tr>
      <th>Prob. Sharpe Ratio</th>
      <td>0.84</td>
    </tr>
    <tr>
      <th>Sortino</th>
      <td>4.1</td>
    </tr>
    <tr>
      <th>Sortino/√2</th>
      <td>2.9</td>
    </tr>
    <tr>
      <th>Omega</th>
      <td>1.56</td>
    </tr>
    <tr>
      <th>Max Drawdown</th>
      <td>-0.03</td>
    </tr>
    <tr>
      <th>Longest DD Days</th>
      <td>18</td>
    </tr>
    <tr>
      <th>Gain/Pain Ratio</th>
      <td>0.61</td>
    </tr>
    <tr>
      <th>Gain/Pain (1M)</th>
      <td>-</td>
    </tr>
    <tr>
      <th>Payoff Ratio</th>
      <td>1.33</td>
    </tr>
    <tr>
      <th>Profit Factor</th>
      <td>1.56</td>
    </tr>
    <tr>
      <th>Common Sense Ratio</th>
      <td>1.95</td>
    </tr>
    <tr>
      <th>CPC Index</th>
      <td>1.12</td>
    </tr>
    <tr>
      <th>Tail Ratio</th>
      <td>1.25</td>
    </tr>
    <tr>
      <th>Outlier Win Ratio</th>
      <td>2.62</td>
    </tr>
    <tr>
      <th>Outlier Loss Ratio</th>
      <td>3.52</td>
    </tr>
    <tr>
      <th>MTD</th>
      <td>0.01</td>
    </tr>
    <tr>
      <th>3M</th>
      <td>0.07</td>
    </tr>
    <tr>
      <th>6M</th>
      <td>0.07</td>
    </tr>
    <tr>
      <th>YTD</th>
      <td>0.01</td>
    </tr>
    <tr>
      <th>1Y</th>
      <td>0.07</td>
    </tr>
    <tr>
      <th>3Y (ann.)</th>
      <td>0.38</td>
    </tr>
    <tr>
      <th>5Y (ann.)</th>
      <td>0.38</td>
    </tr>
    <tr>
      <th>10Y (ann.)</th>
      <td>0.38</td>
    </tr>
    <tr>
      <th>All-time (ann.)</th>
      <td>0.38</td>
    </tr>
    <tr>
      <th>Avg. Drawdown</th>
      <td>-0.02</td>
    </tr>
    <tr>
      <th>Avg. Drawdown Days</th>
      <td>6</td>
    </tr>
    <tr>
      <th>Recovery Factor</th>
      <td>2.09</td>
    </tr>
    <tr>
      <th>Ulcer Index</th>
      <td>0.01</td>
    </tr>
    <tr>
      <th>Serenity Index</th>
      <td>2.1</td>
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
      <td>16885.75€</td>
    </tr>
    <tr>
      <td>2024-01-01</td>
      <td>16828.09€</td>
    </tr>
    <tr>
      <td>2023-12-31</td>
      <td>16719.9€</td>
    </tr>
    <tr>
      <td>2023-12-30</td>
      <td>16747.76€</td>
    </tr>
    <tr>
      <td>2023-12-29</td>
      <td>16712.54€</td>
    </tr>
    <tr>
      <td>2023-12-28</td>
      <td>16884.35€</td>
    </tr>
    <tr>
      <td>2023-12-28</td>
      <td>17116.82€</td>
    </tr>
    <tr>
      <td>2023-12-27</td>
      <td>17064.57€</td>
    </tr>
    <tr>
      <td>2023-12-26</td>
      <td>16679.49€</td>
    </tr>
    <tr>
      <td>2023-12-25</td>
      <td>16703.58€</td>
    </tr>
    <tr>
      <td>2023-12-24</td>
      <td>16710.16€</td>
    </tr>
    <tr>
      <td>2023-12-23</td>
      <td>16738.71€</td>
    </tr>
    <tr>
      <td>2023-12-22</td>
      <td>16775.75€</td>
    </tr>
    <tr>
      <td>2023-12-21</td>
      <td>16671.76€</td>
    </tr>
    <tr>
      <td>2023-12-20</td>
      <td>16373.88€</td>
    </tr>
    <tr>
      <td>2023-12-19</td>
      <td>16633.52€</td>
    </tr>
    <tr>
      <td>2023-12-18</td>
      <td>16663.84€</td>
    </tr>
    <tr>
      <td>2023-12-17</td>
      <td>16624.01€</td>
    </tr>
    <tr>
      <td>2023-12-16</td>
      <td>16618.7€</td>
    </tr>
    <tr>
      <td>2023-12-15</td>
      <td>16648.57€</td>
    </tr>
    <tr>
      <td>2023-12-14</td>
      <td>16740.48€</td>
    </tr>
    <tr>
      <td>2023-12-13</td>
      <td>16619.69€</td>
    </tr>
    <tr>
      <td>2023-12-12</td>
      <td>16323.56€</td>
    </tr>
    <tr>
      <td>2023-12-11</td>
      <td>16380.13€</td>
    </tr>
    <tr>
      <td>2023-12-10</td>
      <td>16841.45€</td>
    </tr>
    <tr>
      <td>2023-12-09</td>
      <td>16827.56€</td>
    </tr>
    <tr>
      <td>2023-12-08</td>
      <td>16864.91€</td>
    </tr>
    <tr>
      <td>2023-12-07</td>
      <td>16752.13€</td>
    </tr>
    <tr>
      <td>2023-12-06</td>
      <td>16433.3€</td>
    </tr>
    <tr>
      <td>2023-12-06</td>
      <td>16549.83€</td>
    </tr>
    <tr>
      <td>2023-11-22</td>
      <td>16166.02€</td>
    </tr>
    <tr>
      <td>2023-11-21</td>
      <td>16091.27€</td>
    </tr>
    <tr>
      <td>2023-11-20</td>
      <td>16139.56€</td>
    </tr>
    <tr>
      <td>2023-11-19</td>
      <td>15922.96€</td>
    </tr>
    <tr>
      <td>2023-11-16</td>
      <td>15843.16€</td>
    </tr>
    <tr>
      <td>2023-11-15</td>
      <td>16125.06€</td>
    </tr>
    <tr>
      <td>2023-11-14</td>
      <td>16049.33€</td>
    </tr>
    <tr>
      <td>2023-11-13</td>
      <td>15975.46€</td>
    </tr>
    <tr>
      <td>2023-11-12</td>
      <td>15754.35€</td>
    </tr>
    <tr>
      <td>2023-11-10</td>
      <td>15824.46€</td>
    </tr>
  </tbody>
</table>