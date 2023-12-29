---
date: "2023-12-29" # 2021-07-14
title: "static-sharpe-manual-0922"
image: "images/plots/static-sharpe-manual-0922.png"
author: "justin-guese"
draft: false
pctgain: 25
---

## Introduction to our strategy

created in basebot

## Quick Summary

<img src="/images/plots/static-sharpe-manual-0922.png" alt = "returns chart for static-sharpe-manual-0922" width="100%">

| Metric | Value |
| --- | --- |
| Return % p.a. | 25 |
| Days active | 48 |
| Starting capital | 10000 |
| Current capital | 16138.37€ |

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
      <td>NVDA</td>
      <td>9.715289</td>
      <td>496.41</td>
      <td>4822.77</td>
    </tr>
    <tr>
      <td>PGR</td>
      <td>22.859741</td>
      <td>159.04</td>
      <td>3635.61</td>
    </tr>
    <tr>
      <td>LLY</td>
      <td>4.513932</td>
      <td>581.45</td>
      <td>2624.63</td>
    </tr>
    <tr>
      <td>KDP</td>
      <td>39.845779</td>
      <td>33.33</td>
      <td>1328.06</td>
    </tr>
    <tr>
      <td>WM</td>
      <td>5.710737</td>
      <td>178.93</td>
      <td>1021.82</td>
    </tr>
    <tr>
      <td>AMD</td>
      <td>5.243304</td>
      <td>148.43</td>
      <td>778.26</td>
    </tr>
    <tr>
      <td>TSLA</td>
      <td>2.408310</td>
      <td>250.63</td>
      <td>603.59</td>
    </tr>
    <tr>
      <td>TEAM</td>
      <td>2.098381</td>
      <td>239.13</td>
      <td>501.79</td>
    </tr>
    <tr>
      <td>UNH</td>
      <td>0.697072</td>
      <td>525.44</td>
      <td>366.27</td>
    </tr>
    <tr>
      <td>AMZN</td>
      <td>2.152063</td>
      <td>152.37</td>
      <td>327.91</td>
    </tr>
    <tr>
      <td>DG</td>
      <td>0.591310</td>
      <td>136.49</td>
      <td>80.71</td>
    </tr>
    <tr>
      <td>NOC</td>
      <td>0.142868</td>
      <td>467.23</td>
      <td>66.75</td>
    </tr>
    <tr>
      <td>USD</td>
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
      <td>0.03</td>
    </tr>
    <tr>
      <th>CAGR﹪</th>
      <td>0.2</td>
    </tr>
    <tr>
      <th>Sharpe</th>
      <td>1.91</td>
    </tr>
    <tr>
      <th>Prob. Sharpe Ratio</th>
      <td>0.75</td>
    </tr>
    <tr>
      <th>Sortino</th>
      <td>2.69</td>
    </tr>
    <tr>
      <th>Sortino/√2</th>
      <td>1.9</td>
    </tr>
    <tr>
      <th>Omega</th>
      <td>1.42</td>
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
      <td>0.42</td>
    </tr>
    <tr>
      <th>Gain/Pain (1M)</th>
      <td>-</td>
    </tr>
    <tr>
      <th>Payoff Ratio</th>
      <td>0.8</td>
    </tr>
    <tr>
      <th>Profit Factor</th>
      <td>1.42</td>
    </tr>
    <tr>
      <th>Common Sense Ratio</th>
      <td>1.0</td>
    </tr>
    <tr>
      <th>CPC Index</th>
      <td>0.72</td>
    </tr>
    <tr>
      <th>Tail Ratio</th>
      <td>0.71</td>
    </tr>
    <tr>
      <th>Outlier Win Ratio</th>
      <td>3.03</td>
    </tr>
    <tr>
      <th>Outlier Loss Ratio</th>
      <td>2.01</td>
    </tr>
    <tr>
      <th>MTD</th>
      <td>0.02</td>
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
      <td>0.03</td>
    </tr>
    <tr>
      <th>1Y</th>
      <td>0.03</td>
    </tr>
    <tr>
      <th>3Y (ann.)</th>
      <td>0.2</td>
    </tr>
    <tr>
      <th>5Y (ann.)</th>
      <td>0.2</td>
    </tr>
    <tr>
      <th>10Y (ann.)</th>
      <td>0.2</td>
    </tr>
    <tr>
      <th>All-time (ann.)</th>
      <td>0.2</td>
    </tr>
    <tr>
      <th>Avg. Drawdown</th>
      <td>-0.02</td>
    </tr>
    <tr>
      <th>Avg. Drawdown Days</th>
      <td>9</td>
    </tr>
    <tr>
      <th>Recovery Factor</th>
      <td>1.29</td>
    </tr>
    <tr>
      <th>Ulcer Index</th>
      <td>0.01</td>
    </tr>
    <tr>
      <th>Serenity Index</th>
      <td>1.43</td>
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
      <td>28.12.2023</td>
      <td>16138.37€</td>
    </tr>
    <tr>
      <td>28.12.2023</td>
      <td>16111.04€</td>
    </tr>
    <tr>
      <td>27.12.2023</td>
      <td>16111.04€</td>
    </tr>
    <tr>
      <td>26.12.2023</td>
      <td>16014.64€</td>
    </tr>
    <tr>
      <td>25.12.2023</td>
      <td>15927.24€</td>
    </tr>
    <tr>
      <td>24.12.2023</td>
      <td>15927.24€</td>
    </tr>
    <tr>
      <td>23.12.2023</td>
      <td>15927.24€</td>
    </tr>
    <tr>
      <td>22.12.2023</td>
      <td>15927.24€</td>
    </tr>
    <tr>
      <td>21.12.2023</td>
      <td>15921.66€</td>
    </tr>
    <tr>
      <td>20.12.2023</td>
      <td>15727.55€</td>
    </tr>
    <tr>
      <td>19.12.2023</td>
      <td>16030.79€</td>
    </tr>
    <tr>
      <td>18.12.2023</td>
      <td>16009.19€</td>
    </tr>
    <tr>
      <td>17.12.2023</td>
      <td>15767.97€</td>
    </tr>
    <tr>
      <td>16.12.2023</td>
      <td>15767.97€</td>
    </tr>
    <tr>
      <td>15.12.2023</td>
      <td>15767.97€</td>
    </tr>
    <tr>
      <td>14.12.2023</td>
      <td>15717.45€</td>
    </tr>
    <tr>
      <td>13.12.2023</td>
      <td>15988.72€</td>
    </tr>
    <tr>
      <td>12.12.2023</td>
      <td>15911.34€</td>
    </tr>
    <tr>
      <td>11.12.2023</td>
      <td>15732.96€</td>
    </tr>
    <tr>
      <td>10.12.2023</td>
      <td>15775.27€</td>
    </tr>
    <tr>
      <td>09.12.2023</td>
      <td>15775.27€</td>
    </tr>
    <tr>
      <td>08.12.2023</td>
      <td>15775.27€</td>
    </tr>
    <tr>
      <td>07.12.2023</td>
      <td>15652.7€</td>
    </tr>
    <tr>
      <td>06.12.2023</td>
      <td>15476.02€</td>
    </tr>
    <tr>
      <td>06.12.2023</td>
      <td>15544.7€</td>
    </tr>
    <tr>
      <td>22.11.2023</td>
      <td>15830.85€</td>
    </tr>
    <tr>
      <td>21.11.2023</td>
      <td>15899.0€</td>
    </tr>
    <tr>
      <td>20.11.2023</td>
      <td>15903.54€</td>
    </tr>
    <tr>
      <td>19.11.2023</td>
      <td>15710.66€</td>
    </tr>
    <tr>
      <td>16.11.2023</td>
      <td>15768.96€</td>
    </tr>
    <tr>
      <td>15.11.2023</td>
      <td>15678.88€</td>
    </tr>
    <tr>
      <td>14.11.2023</td>
      <td>15902.46€</td>
    </tr>
    <tr>
      <td>13.11.2023</td>
      <td>15757.77€</td>
    </tr>
    <tr>
      <td>12.11.2023</td>
      <td>15607.05€</td>
    </tr>
    <tr>
      <td>10.11.2023</td>
      <td>15607.05€</td>
    </tr>
  </tbody>
</table>