---
date: "2024-01-04" # 2021-07-14
title: "finnhub-recommendations"
image: "images/plots/finnhub-recommendations.png"
author: "justin-guese"
draft: false
pctgain: -52
---

## Introduction to our strategy

created in basebot

## Quick Summary

<img src="/images/plots/finnhub-recommendations.png" alt = "returns chart for finnhub-recommendations" width="100%">

| Metric | Value |
| --- | --- |
| Return % p.a. | -52 |
| Days active | 54 |
| Starting capital | 10000 |
| Current capital | 9832.67€ |

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
      <td>371.83</td>
      <td>1320.44</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/NVDA'>NVDA</a></td>
      <td>2.659663e+00</td>
      <td>480.04</td>
      <td>1276.74</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/AMZN'>AMZN</a></td>
      <td>8.522266e+00</td>
      <td>146.38</td>
      <td>1247.49</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/GOOG'>GOOG</a></td>
      <td>7.564901e+00</td>
      <td>139.96</td>
      <td>1058.78</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/AMD'>AMD</a></td>
      <td>6.381049e+00</td>
      <td>136.50</td>
      <td>871.01</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/AAPL'>AAPL</a></td>
      <td>4.170912e+00</td>
      <td>181.29</td>
      <td>756.14</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/UNH'>UNH</a></td>
      <td>1.175077e+00</td>
      <td>545.63</td>
      <td>641.16</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/LLY'>LLY</a></td>
      <td>1.004302e+00</td>
      <td>628.37</td>
      <td>631.07</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/WM'>WM</a></td>
      <td>2.586596e+00</td>
      <td>180.17</td>
      <td>466.03</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/DG'>DG</a></td>
      <td>3.420158e+00</td>
      <td>134.82</td>
      <td>461.11</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/KDP'>KDP</a></td>
      <td>9.239107e+00</td>
      <td>32.49</td>
      <td>300.18</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/NOC'>NOC</a></td>
      <td>6.233268e-01</td>
      <td>481.37</td>
      <td>300.05</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/TSLA'>TSLA</a></td>
      <td>1.104134e+00</td>
      <td>241.78</td>
      <td>266.96</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/PGR'>PGR</a></td>
      <td>1.617249e+00</td>
      <td>164.55</td>
      <td>266.12</td>
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
      <td>2024-01-03</td>
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
      <td>-0.08</td>
    </tr>
    <tr>
      <th>CAGR﹪</th>
      <td>-0.33</td>
    </tr>
    <tr>
      <th>Sharpe</th>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>Prob. Sharpe Ratio</th>
      <td>0.15</td>
    </tr>
    <tr>
      <th>Sortino</th>
      <td>-2.14</td>
    </tr>
    <tr>
      <th>Sortino/√2</th>
      <td>-1.52</td>
    </tr>
    <tr>
      <th>Omega</th>
      <td>0.58</td>
    </tr>
    <tr>
      <th>Max Drawdown</th>
      <td>-0.09</td>
    </tr>
    <tr>
      <th>Longest DD Days</th>
      <td>44</td>
    </tr>
    <tr>
      <th>Gain/Pain Ratio</th>
      <td>-0.42</td>
    </tr>
    <tr>
      <th>Gain/Pain (1M)</th>
      <td>-0.83</td>
    </tr>
    <tr>
      <th>Payoff Ratio</th>
      <td>0.5</td>
    </tr>
    <tr>
      <th>Profit Factor</th>
      <td>0.58</td>
    </tr>
    <tr>
      <th>Common Sense Ratio</th>
      <td>0.49</td>
    </tr>
    <tr>
      <th>CPC Index</th>
      <td>0.16</td>
    </tr>
    <tr>
      <th>Tail Ratio</th>
      <td>0.85</td>
    </tr>
    <tr>
      <th>Outlier Win Ratio</th>
      <td>4.49</td>
    </tr>
    <tr>
      <th>Outlier Loss Ratio</th>
      <td>4.37</td>
    </tr>
    <tr>
      <th>MTD</th>
      <td>-0.02</td>
    </tr>
    <tr>
      <th>3M</th>
      <td>-0.08</td>
    </tr>
    <tr>
      <th>6M</th>
      <td>-0.08</td>
    </tr>
    <tr>
      <th>YTD</th>
      <td>-0.02</td>
    </tr>
    <tr>
      <th>1Y</th>
      <td>-0.08</td>
    </tr>
    <tr>
      <th>3Y (ann.)</th>
      <td>-0.33</td>
    </tr>
    <tr>
      <th>5Y (ann.)</th>
      <td>-0.33</td>
    </tr>
    <tr>
      <th>10Y (ann.)</th>
      <td>-0.33</td>
    </tr>
    <tr>
      <th>All-time (ann.)</th>
      <td>-0.33</td>
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
      <td>0.81</td>
    </tr>
    <tr>
      <th>Ulcer Index</th>
      <td>0.07</td>
    </tr>
    <tr>
      <th>Serenity Index</th>
      <td>-0.15</td>
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
      <td>2024-01-03</td>
      <td>9832.67€</td>
    </tr>
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