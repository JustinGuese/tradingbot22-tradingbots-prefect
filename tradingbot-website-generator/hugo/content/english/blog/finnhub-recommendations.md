---
date: "2023-12-29" # 2021-07-14
title: "finnhub-recommendations"
image: "images/plots/finnhub-recommendations.png"
author: "justin-guese"
draft: false
pctgain: -44
---

## Introduction to our strategy

created in basebot

## Quick Summary

<img src="/images/plots/finnhub-recommendations.png" alt = "returns chart for finnhub-recommendations" width="100%">

| Metric | Value |
| --- | --- |
| Return % p.a. | -44 |
| Days active | 48 |
| Starting capital | 10000 |
| Current capital | 10040.91€ |

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
      <td>MSFT</td>
      <td>3.551194e+00</td>
      <td>375.85</td>
      <td>1334.72</td>
    </tr>
    <tr>
      <td>NVDA</td>
      <td>2.659663e+00</td>
      <td>496.41</td>
      <td>1320.28</td>
    </tr>
    <tr>
      <td>AMZN</td>
      <td>8.522266e+00</td>
      <td>152.37</td>
      <td>1298.54</td>
    </tr>
    <tr>
      <td>GOOG</td>
      <td>7.564901e+00</td>
      <td>140.74</td>
      <td>1064.68</td>
    </tr>
    <tr>
      <td>AMD</td>
      <td>6.381049e+00</td>
      <td>148.43</td>
      <td>947.14</td>
    </tr>
    <tr>
      <td>AAPL</td>
      <td>4.170912e+00</td>
      <td>192.26</td>
      <td>801.90</td>
    </tr>
    <tr>
      <td>UNH</td>
      <td>1.175077e+00</td>
      <td>525.44</td>
      <td>617.43</td>
    </tr>
    <tr>
      <td>LLY</td>
      <td>1.004302e+00</td>
      <td>581.45</td>
      <td>583.95</td>
    </tr>
    <tr>
      <td>DG</td>
      <td>3.420158e+00</td>
      <td>136.49</td>
      <td>466.82</td>
    </tr>
    <tr>
      <td>WM</td>
      <td>2.586596e+00</td>
      <td>178.93</td>
      <td>462.82</td>
    </tr>
    <tr>
      <td>KDP</td>
      <td>9.239107e+00</td>
      <td>33.33</td>
      <td>307.94</td>
    </tr>
    <tr>
      <td>NOC</td>
      <td>6.233268e-01</td>
      <td>467.23</td>
      <td>291.24</td>
    </tr>
    <tr>
      <td>TSLA</td>
      <td>1.104134e+00</td>
      <td>250.63</td>
      <td>276.73</td>
    </tr>
    <tr>
      <td>PGR</td>
      <td>1.617249e+00</td>
      <td>159.04</td>
      <td>257.21</td>
    </tr>
    <tr>
      <td>USD</td>
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
      <td>2023-12-28</td>
    </tr>
    <tr>
      <th>Risk-Free Rate</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Time in Market</th>
      <td>0.74</td>
    </tr>
    <tr>
      <th>Cumulative Return</th>
      <td>-0.06</td>
    </tr>
    <tr>
      <th>CAGR﹪</th>
      <td>-0.28</td>
    </tr>
    <tr>
      <th>Sharpe</th>
      <td>-1.59</td>
    </tr>
    <tr>
      <th>Prob. Sharpe Ratio</th>
      <td>0.24</td>
    </tr>
    <tr>
      <th>Sortino</th>
      <td>-1.71</td>
    </tr>
    <tr>
      <th>Sortino/√2</th>
      <td>-1.21</td>
    </tr>
    <tr>
      <th>Omega</th>
      <td>0.65</td>
    </tr>
    <tr>
      <th>Max Drawdown</th>
      <td>-0.09</td>
    </tr>
    <tr>
      <th>Longest DD Days</th>
      <td>38</td>
    </tr>
    <tr>
      <th>Gain/Pain Ratio</th>
      <td>-0.35</td>
    </tr>
    <tr>
      <th>Gain/Pain (1M)</th>
      <td>-0.78</td>
    </tr>
    <tr>
      <th>Payoff Ratio</th>
      <td>0.44</td>
    </tr>
    <tr>
      <th>Profit Factor</th>
      <td>0.65</td>
    </tr>
    <tr>
      <th>Common Sense Ratio</th>
      <td>0.41</td>
    </tr>
    <tr>
      <th>CPC Index</th>
      <td>0.17</td>
    </tr>
    <tr>
      <th>Tail Ratio</th>
      <td>0.63</td>
    </tr>
    <tr>
      <th>Outlier Win Ratio</th>
      <td>4.11</td>
    </tr>
    <tr>
      <th>Outlier Loss Ratio</th>
      <td>3.99</td>
    </tr>
    <tr>
      <th>MTD</th>
      <td>-0.07</td>
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
      <td>-0.06</td>
    </tr>
    <tr>
      <th>1Y</th>
      <td>-0.06</td>
    </tr>
    <tr>
      <th>3Y (ann.)</th>
      <td>-0.28</td>
    </tr>
    <tr>
      <th>5Y (ann.)</th>
      <td>-0.28</td>
    </tr>
    <tr>
      <th>10Y (ann.)</th>
      <td>-0.28</td>
    </tr>
    <tr>
      <th>All-time (ann.)</th>
      <td>-0.28</td>
    </tr>
    <tr>
      <th>Avg. Drawdown</th>
      <td>-0.03</td>
    </tr>
    <tr>
      <th>Avg. Drawdown Days</th>
      <td>10</td>
    </tr>
    <tr>
      <th>Recovery Factor</th>
      <td>0.59</td>
    </tr>
    <tr>
      <th>Ulcer Index</th>
      <td>0.07</td>
    </tr>
    <tr>
      <th>Serenity Index</th>
      <td>-0.12</td>
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
      <td>PGR</td>
      <td>157.770004</td>
      <td>255.536627</td>
      <td>40316.01</td>
    </tr>
    <tr>
      <td>2023-12-27 16:00:22.124613</td>
      <td>Buy</td>
      <td>NOC</td>
      <td>463.920013</td>
      <td>289.608177</td>
      <td>134355.03</td>
    </tr>
    <tr>
      <td>2023-12-27 16:00:17.851795</td>
      <td>Buy</td>
      <td>TSLA</td>
      <td>261.901001</td>
      <td>289.608177</td>
      <td>75848.67</td>
    </tr>
    <tr>
      <td>2023-12-27 16:00:17.594556</td>
      <td>Buy</td>
      <td>KDP</td>
      <td>33.139999</td>
      <td>306.643952</td>
      <td>10162.18</td>
    </tr>
    <tr>
      <td>2023-12-27 16:00:17.341703</td>
      <td>Buy</td>
      <td>WM</td>
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
      <td>28.12.2023</td>
      <td>10040.91€</td>
    </tr>
    <tr>
      <td>28.12.2023</td>
      <td>10014.01€</td>
    </tr>
    <tr>
      <td>27.12.2023</td>
      <td>10014.01€</td>
    </tr>
    <tr>
      <td>26.12.2023</td>
      <td>9989.45€</td>
    </tr>
    <tr>
      <td>25.12.2023</td>
      <td>9942.34€</td>
    </tr>
    <tr>
      <td>24.12.2023</td>
      <td>9942.34€</td>
    </tr>
    <tr>
      <td>23.12.2023</td>
      <td>9942.34€</td>
    </tr>
    <tr>
      <td>22.12.2023</td>
      <td>9942.34€</td>
    </tr>
    <tr>
      <td>21.12.2023</td>
      <td>9933.9€</td>
    </tr>
    <tr>
      <td>20.12.2023</td>
      <td>9814.32€</td>
    </tr>
    <tr>
      <td>19.12.2023</td>
      <td>10112.93€</td>
    </tr>
    <tr>
      <td>18.12.2023</td>
      <td>10087.18€</td>
    </tr>
    <tr>
      <td>17.12.2023</td>
      <td>9988.56€</td>
    </tr>
    <tr>
      <td>16.12.2023</td>
      <td>9988.56€</td>
    </tr>
    <tr>
      <td>15.12.2023</td>
      <td>9988.56€</td>
    </tr>
    <tr>
      <td>14.12.2023</td>
      <td>9939.07€</td>
    </tr>
    <tr>
      <td>13.12.2023</td>
      <td>10043.52€</td>
    </tr>
    <tr>
      <td>12.12.2023</td>
      <td>10173.34€</td>
    </tr>
    <tr>
      <td>11.12.2023</td>
      <td>10092.66€</td>
    </tr>
    <tr>
      <td>10.12.2023</td>
      <td>10142.77€</td>
    </tr>
    <tr>
      <td>09.12.2023</td>
      <td>10142.77€</td>
    </tr>
    <tr>
      <td>08.12.2023</td>
      <td>10142.77€</td>
    </tr>
    <tr>
      <td>07.12.2023</td>
      <td>10114.73€</td>
    </tr>
    <tr>
      <td>06.12.2023</td>
      <td>9908.67€</td>
    </tr>
    <tr>
      <td>06.12.2023</td>
      <td>9957.46€</td>
    </tr>
    <tr>
      <td>22.11.2023</td>
      <td>10835.1€</td>
    </tr>
    <tr>
      <td>21.11.2023</td>
      <td>10777.01€</td>
    </tr>
    <tr>
      <td>20.11.2023</td>
      <td>10843.31€</td>
    </tr>
    <tr>
      <td>19.11.2023</td>
      <td>10751.47€</td>
    </tr>
    <tr>
      <td>16.11.2023</td>
      <td>10771.0€</td>
    </tr>
    <tr>
      <td>15.11.2023</td>
      <td>10690.84€</td>
    </tr>
    <tr>
      <td>14.11.2023</td>
      <td>10756.5€</td>
    </tr>
    <tr>
      <td>13.11.2023</td>
      <td>10634.16€</td>
    </tr>
    <tr>
      <td>12.11.2023</td>
      <td>10666.04€</td>
    </tr>
    <tr>
      <td>10.11.2023</td>
      <td>10666.04€</td>
    </tr>
  </tbody>
</table>