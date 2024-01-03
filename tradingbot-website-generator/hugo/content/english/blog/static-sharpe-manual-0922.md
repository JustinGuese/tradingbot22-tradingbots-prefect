---
date: "2024-01-03" # 2021-07-14
title: "static-sharpe-manual-0922"
image: "images/plots/static-sharpe-manual-0922.png"
author: "justin-guese"
draft: false
pctgain: 19
---

## Introduction to our strategy

created in basebot

## Quick Summary

<img src="/images/plots/static-sharpe-manual-0922.png" alt = "returns chart for static-sharpe-manual-0922" width="100%">

| Metric | Value |
| --- | --- |
| Return % p.a. | 19 |
| Days active | 53 |
| Starting capital | 10000 |
| Current capital | 16053.24€ |

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
      <td><a target='_blank' href='https://finance.yahoo.com/quote/NVDA'>NVDA</a></td>
      <td>9.715289</td>
      <td>478.99</td>
      <td>4653.53</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/PGR'>PGR</a></td>
      <td>22.859741</td>
      <td>163.04</td>
      <td>3727.05</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/LLY'>LLY</a></td>
      <td>4.513932</td>
      <td>606.41</td>
      <td>2737.29</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/KDP'>KDP</a></td>
      <td>39.845779</td>
      <td>32.47</td>
      <td>1293.79</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/WM'>WM</a></td>
      <td>5.710737</td>
      <td>180.60</td>
      <td>1031.36</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/AMD'>AMD</a></td>
      <td>5.243304</td>
      <td>136.05</td>
      <td>713.35</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/TSLA'>TSLA</a></td>
      <td>2.408310</td>
      <td>241.99</td>
      <td>582.79</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/TEAM'>TEAM</a></td>
      <td>2.098381</td>
      <td>221.89</td>
      <td>465.61</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/UNH'>UNH</a></td>
      <td>0.697072</td>
      <td>546.00</td>
      <td>380.60</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/AMZN'>AMZN</a></td>
      <td>2.152063</td>
      <td>150.07</td>
      <td>322.96</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/DG'>DG</a></td>
      <td>0.591310</td>
      <td>138.81</td>
      <td>82.08</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/NOC'>NOC</a></td>
      <td>0.142868</td>
      <td>473.68</td>
      <td>67.67</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/USD'>USD</a></td>
      <td>0.905557</td>
      <td>1.00</td>
      <td>0.91</td>
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
      <td>0.03</td>
    </tr>
    <tr>
      <th>CAGR﹪</th>
      <td>0.15</td>
    </tr>
    <tr>
      <th>Sharpe</th>
      <td>1.5</td>
    </tr>
    <tr>
      <th>Prob. Sharpe Ratio</th>
      <td>0.71</td>
    </tr>
    <tr>
      <th>Sortino</th>
      <td>2.1</td>
    </tr>
    <tr>
      <th>Sortino/√2</th>
      <td>1.49</td>
    </tr>
    <tr>
      <th>Omega</th>
      <td>1.33</td>
    </tr>
    <tr>
      <th>Max Drawdown</th>
      <td>-0.03</td>
    </tr>
    <tr>
      <th>Longest DD Days</th>
      <td>21</td>
    </tr>
    <tr>
      <th>Gain/Pain Ratio</th>
      <td>0.33</td>
    </tr>
    <tr>
      <th>Gain/Pain (1M)</th>
      <td>5.09</td>
    </tr>
    <tr>
      <th>Payoff Ratio</th>
      <td>0.78</td>
    </tr>
    <tr>
      <th>Profit Factor</th>
      <td>1.33</td>
    </tr>
    <tr>
      <th>Common Sense Ratio</th>
      <td>0.96</td>
    </tr>
    <tr>
      <th>CPC Index</th>
      <td>0.65</td>
    </tr>
    <tr>
      <th>Tail Ratio</th>
      <td>0.72</td>
    </tr>
    <tr>
      <th>Outlier Win Ratio</th>
      <td>3.47</td>
    </tr>
    <tr>
      <th>Outlier Loss Ratio</th>
      <td>2.09</td>
    </tr>
    <tr>
      <th>MTD</th>
      <td>-0.01</td>
    </tr>
    <tr>
      <th>3M</th>
      <td>0.03</td>
    </tr>
    <tr>
      <th>6M</th>
      <td>0.03</td>
    </tr>
    <tr>
      <th>YTD</th>
      <td>-0.01</td>
    </tr>
    <tr>
      <th>1Y</th>
      <td>0.03</td>
    </tr>
    <tr>
      <th>3Y (ann.)</th>
      <td>0.15</td>
    </tr>
    <tr>
      <th>5Y (ann.)</th>
      <td>0.15</td>
    </tr>
    <tr>
      <th>10Y (ann.)</th>
      <td>0.15</td>
    </tr>
    <tr>
      <th>All-time (ann.)</th>
      <td>0.15</td>
    </tr>
    <tr>
      <th>Avg. Drawdown</th>
      <td>-0.02</td>
    </tr>
    <tr>
      <th>Avg. Drawdown Days</th>
      <td>8</td>
    </tr>
    <tr>
      <th>Recovery Factor</th>
      <td>1.09</td>
    </tr>
    <tr>
      <th>Ulcer Index</th>
      <td>0.01</td>
    </tr>
    <tr>
      <th>Serenity Index</th>
      <td>1.28</td>
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
      <td>16053.24€</td>
    </tr>
    <tr>
      <td>2024-01-01</td>
      <td>16146.62€</td>
    </tr>
    <tr>
      <td>2023-12-31</td>
      <td>16146.62€</td>
    </tr>
    <tr>
      <td>2023-12-30</td>
      <td>16146.62€</td>
    </tr>
    <tr>
      <td>2023-12-29</td>
      <td>16146.62€</td>
    </tr>
    <tr>
      <td>2023-12-28</td>
      <td>16138.37€</td>
    </tr>
    <tr>
      <td>2023-12-28</td>
      <td>16111.04€</td>
    </tr>
    <tr>
      <td>2023-12-27</td>
      <td>16111.04€</td>
    </tr>
    <tr>
      <td>2023-12-26</td>
      <td>16014.64€</td>
    </tr>
    <tr>
      <td>2023-12-25</td>
      <td>15927.24€</td>
    </tr>
    <tr>
      <td>2023-12-24</td>
      <td>15927.24€</td>
    </tr>
    <tr>
      <td>2023-12-23</td>
      <td>15927.24€</td>
    </tr>
    <tr>
      <td>2023-12-22</td>
      <td>15927.24€</td>
    </tr>
    <tr>
      <td>2023-12-21</td>
      <td>15921.66€</td>
    </tr>
    <tr>
      <td>2023-12-20</td>
      <td>15727.55€</td>
    </tr>
    <tr>
      <td>2023-12-19</td>
      <td>16030.79€</td>
    </tr>
    <tr>
      <td>2023-12-18</td>
      <td>16009.19€</td>
    </tr>
    <tr>
      <td>2023-12-17</td>
      <td>15767.97€</td>
    </tr>
    <tr>
      <td>2023-12-16</td>
      <td>15767.97€</td>
    </tr>
    <tr>
      <td>2023-12-15</td>
      <td>15767.97€</td>
    </tr>
    <tr>
      <td>2023-12-14</td>
      <td>15717.45€</td>
    </tr>
    <tr>
      <td>2023-12-13</td>
      <td>15988.72€</td>
    </tr>
    <tr>
      <td>2023-12-12</td>
      <td>15911.34€</td>
    </tr>
    <tr>
      <td>2023-12-11</td>
      <td>15732.96€</td>
    </tr>
    <tr>
      <td>2023-12-10</td>
      <td>15775.27€</td>
    </tr>
    <tr>
      <td>2023-12-09</td>
      <td>15775.27€</td>
    </tr>
    <tr>
      <td>2023-12-08</td>
      <td>15775.27€</td>
    </tr>
    <tr>
      <td>2023-12-07</td>
      <td>15652.7€</td>
    </tr>
    <tr>
      <td>2023-12-06</td>
      <td>15476.02€</td>
    </tr>
    <tr>
      <td>2023-12-06</td>
      <td>15544.7€</td>
    </tr>
    <tr>
      <td>2023-11-22</td>
      <td>15830.85€</td>
    </tr>
    <tr>
      <td>2023-11-21</td>
      <td>15899.0€</td>
    </tr>
    <tr>
      <td>2023-11-20</td>
      <td>15903.54€</td>
    </tr>
    <tr>
      <td>2023-11-19</td>
      <td>15710.66€</td>
    </tr>
    <tr>
      <td>2023-11-16</td>
      <td>15768.96€</td>
    </tr>
    <tr>
      <td>2023-11-15</td>
      <td>15678.88€</td>
    </tr>
    <tr>
      <td>2023-11-14</td>
      <td>15902.46€</td>
    </tr>
    <tr>
      <td>2023-11-13</td>
      <td>15757.77€</td>
    </tr>
    <tr>
      <td>2023-11-12</td>
      <td>15607.05€</td>
    </tr>
    <tr>
      <td>2023-11-10</td>
      <td>15607.05€</td>
    </tr>
  </tbody>
</table>