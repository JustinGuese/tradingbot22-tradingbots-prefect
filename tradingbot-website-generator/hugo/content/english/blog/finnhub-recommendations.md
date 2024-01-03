---
date: "2024-01-03" # 2021-07-14
title: "finnhub-recommendations"
image: "images/plots/finnhub-recommendations.png"
author: "justin-guese"
draft: false
pctgain: -49
---

## Introduction to our strategy

created in basebot

## Quick Summary

<img src="/images/plots/finnhub-recommendations.png" alt = "returns chart for finnhub-recommendations" width="100%">

| Metric | Value |
| --- | --- |
| Return % p.a. | -49 |
| Days active | 53 |
| Starting capital | 10000 |
| Current capital | 9900.61€ |

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
      <td><a target='_blank' href='https://finance.yahoo.com/quote/MSFT'>MSFT</a></td>
      <td>3.551194e+00</td>
      <td>371.70</td>
      <td>1319.98</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/AMZN'>AMZN</a></td>
      <td>8.522266e+00</td>
      <td>150.07</td>
      <td>1278.94</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/NVDA'>NVDA</a></td>
      <td>2.659663e+00</td>
      <td>478.99</td>
      <td>1273.95</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/GOOG'>GOOG</a></td>
      <td>7.564901e+00</td>
      <td>139.55</td>
      <td>1055.68</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/AMD'>AMD</a></td>
      <td>6.381049e+00</td>
      <td>136.05</td>
      <td>868.14</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/AAPL'>AAPL</a></td>
      <td>4.170912e+00</td>
      <td>185.12</td>
      <td>772.12</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/UNH'>UNH</a></td>
      <td>1.175077e+00</td>
      <td>546.00</td>
      <td>641.59</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/LLY'>LLY</a></td>
      <td>1.004302e+00</td>
      <td>606.41</td>
      <td>609.02</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/DG'>DG</a></td>
      <td>3.420158e+00</td>
      <td>138.81</td>
      <td>474.75</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/WM'>WM</a></td>
      <td>2.586596e+00</td>
      <td>180.60</td>
      <td>467.14</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/KDP'>KDP</a></td>
      <td>9.239107e+00</td>
      <td>32.47</td>
      <td>299.99</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/NOC'>NOC</a></td>
      <td>6.233268e-01</td>
      <td>473.68</td>
      <td>295.26</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/TSLA'>TSLA</a></td>
      <td>1.104134e+00</td>
      <td>241.99</td>
      <td>267.19</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/PGR'>PGR</a></td>
      <td>1.617249e+00</td>
      <td>163.04</td>
      <td>263.68</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/USD'>USD</a></td>
      <td>4.831691e-13</td>
      <td>1.00</td>
      <td>0.00</td>
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
      <td>0.7</td>
    </tr>
    <tr>
      <th>Cumulative Return</th>
      <td>-0.07</td>
    </tr>
    <tr>
      <th>CAGR﹪</th>
      <td>-0.31</td>
    </tr>
    <tr>
      <th>Sharpe</th>
      <td>-1.85</td>
    </tr>
    <tr>
      <th>Prob. Sharpe Ratio</th>
      <td>0.18</td>
    </tr>
    <tr>
      <th>Sortino</th>
      <td>-1.98</td>
    </tr>
    <tr>
      <th>Sortino/√2</th>
      <td>-1.4</td>
    </tr>
    <tr>
      <th>Omega</th>
      <td>0.6</td>
    </tr>
    <tr>
      <th>Max Drawdown</th>
      <td>-0.09</td>
    </tr>
    <tr>
      <th>Longest DD Days</th>
      <td>43</td>
    </tr>
    <tr>
      <th>Gain/Pain Ratio</th>
      <td>-0.4</td>
    </tr>
    <tr>
      <th>Gain/Pain (1M)</th>
      <td>-0.81</td>
    </tr>
    <tr>
      <th>Payoff Ratio</th>
      <td>0.48</td>
    </tr>
    <tr>
      <th>Profit Factor</th>
      <td>0.6</td>
    </tr>
    <tr>
      <th>Common Sense Ratio</th>
      <td>0.48</td>
    </tr>
    <tr>
      <th>CPC Index</th>
      <td>0.16</td>
    </tr>
    <tr>
      <th>Tail Ratio</th>
      <td>0.8</td>
    </tr>
    <tr>
      <th>Outlier Win Ratio</th>
      <td>4.51</td>
    </tr>
    <tr>
      <th>Outlier Loss Ratio</th>
      <td>4.22</td>
    </tr>
    <tr>
      <th>MTD</th>
      <td>-0.01</td>
    </tr>
    <tr>
      <th>3M</th>
      <td>-0.07</td>
    </tr>
    <tr>
      <th>6M</th>
      <td>-0.07</td>
    </tr>
    <tr>
      <th>YTD</th>
      <td>-0.01</td>
    </tr>
    <tr>
      <th>1Y</th>
      <td>-0.07</td>
    </tr>
    <tr>
      <th>3Y (ann.)</th>
      <td>-0.31</td>
    </tr>
    <tr>
      <th>5Y (ann.)</th>
      <td>-0.31</td>
    </tr>
    <tr>
      <th>10Y (ann.)</th>
      <td>-0.31</td>
    </tr>
    <tr>
      <th>All-time (ann.)</th>
      <td>-0.31</td>
    </tr>
    <tr>
      <th>Avg. Drawdown</th>
      <td>-0.03</td>
    </tr>
    <tr>
      <th>Avg. Drawdown Days</th>
      <td>12</td>
    </tr>
    <tr>
      <th>Recovery Factor</th>
      <td>0.73</td>
    </tr>
    <tr>
      <th>Ulcer Index</th>
      <td>0.07</td>
    </tr>
    <tr>
      <th>Serenity Index</th>
      <td>-0.14</td>
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
      <td>2023-12-27 16:00:22.377582</td>
      <td>Buy</td>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/PGR'>PGR</a></td>
      <td>157.770004</td>
      <td>255.536627</td>
      <td>40316.01</td>
    </tr>
    <tr>
      <td>2023-12-27 16:00:22.124613</td>
      <td>Buy</td>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/NOC'>NOC</a></td>
      <td>463.920013</td>
      <td>289.608177</td>
      <td>134355.03</td>
    </tr>
    <tr>
      <td>2023-12-27 16:00:17.851795</td>
      <td>Buy</td>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/TSLA'>TSLA</a></td>
      <td>261.901001</td>
      <td>289.608177</td>
      <td>75848.67</td>
    </tr>
    <tr>
      <td>2023-12-27 16:00:17.594556</td>
      <td>Buy</td>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/KDP'>KDP</a></td>
      <td>33.139999</td>
      <td>306.643952</td>
      <td>10162.18</td>
    </tr>
    <tr>
      <td>2023-12-27 16:00:17.341703</td>
      <td>Buy</td>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/WM'>WM</a></td>
      <td>177.559998</td>
      <td>459.965928</td>
      <td>81671.55</td>
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
      <td>9900.61€</td>
    </tr>
    <tr>
      <td>2024-01-01</td>
      <td>10021.06€</td>
    </tr>
    <tr>
      <td>2023-12-31</td>
      <td>10021.06€</td>
    </tr>
    <tr>
      <td>2023-12-30</td>
      <td>10021.06€</td>
    </tr>
    <tr>
      <td>2023-12-29</td>
      <td>10021.06€</td>
    </tr>
    <tr>
      <td>2023-12-28</td>
      <td>10040.91€</td>
    </tr>
    <tr>
      <td>2023-12-28</td>
      <td>10014.01€</td>
    </tr>
    <tr>
      <td>2023-12-27</td>
      <td>10014.01€</td>
    </tr>
    <tr>
      <td>2023-12-26</td>
      <td>9989.45€</td>
    </tr>
    <tr>
      <td>2023-12-25</td>
      <td>9942.34€</td>
    </tr>
    <tr>
      <td>2023-12-24</td>
      <td>9942.34€</td>
    </tr>
    <tr>
      <td>2023-12-23</td>
      <td>9942.34€</td>
    </tr>
    <tr>
      <td>2023-12-22</td>
      <td>9942.34€</td>
    </tr>
    <tr>
      <td>2023-12-21</td>
      <td>9933.9€</td>
    </tr>
    <tr>
      <td>2023-12-20</td>
      <td>9814.32€</td>
    </tr>
    <tr>
      <td>2023-12-19</td>
      <td>10112.93€</td>
    </tr>
    <tr>
      <td>2023-12-18</td>
      <td>10087.18€</td>
    </tr>
    <tr>
      <td>2023-12-17</td>
      <td>9988.56€</td>
    </tr>
    <tr>
      <td>2023-12-16</td>
      <td>9988.56€</td>
    </tr>
    <tr>
      <td>2023-12-15</td>
      <td>9988.56€</td>
    </tr>
    <tr>
      <td>2023-12-14</td>
      <td>9939.07€</td>
    </tr>
    <tr>
      <td>2023-12-13</td>
      <td>10043.52€</td>
    </tr>
    <tr>
      <td>2023-12-12</td>
      <td>10173.34€</td>
    </tr>
    <tr>
      <td>2023-12-11</td>
      <td>10092.66€</td>
    </tr>
    <tr>
      <td>2023-12-10</td>
      <td>10142.77€</td>
    </tr>
    <tr>
      <td>2023-12-09</td>
      <td>10142.77€</td>
    </tr>
    <tr>
      <td>2023-12-08</td>
      <td>10142.77€</td>
    </tr>
    <tr>
      <td>2023-12-07</td>
      <td>10114.73€</td>
    </tr>
    <tr>
      <td>2023-12-06</td>
      <td>9908.67€</td>
    </tr>
    <tr>
      <td>2023-12-06</td>
      <td>9957.46€</td>
    </tr>
    <tr>
      <td>2023-11-22</td>
      <td>10835.1€</td>
    </tr>
    <tr>
      <td>2023-11-21</td>
      <td>10777.01€</td>
    </tr>
    <tr>
      <td>2023-11-20</td>
      <td>10843.31€</td>
    </tr>
    <tr>
      <td>2023-11-19</td>
      <td>10751.47€</td>
    </tr>
    <tr>
      <td>2023-11-16</td>
      <td>10771.0€</td>
    </tr>
    <tr>
      <td>2023-11-15</td>
      <td>10690.84€</td>
    </tr>
    <tr>
      <td>2023-11-14</td>
      <td>10756.5€</td>
    </tr>
    <tr>
      <td>2023-11-13</td>
      <td>10634.16€</td>
    </tr>
    <tr>
      <td>2023-11-12</td>
      <td>10666.04€</td>
    </tr>
    <tr>
      <td>2023-11-10</td>
      <td>10666.04€</td>
    </tr>
  </tbody>
</table>