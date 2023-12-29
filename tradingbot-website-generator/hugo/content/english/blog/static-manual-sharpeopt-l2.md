---
date: "2023-12-29" # 2021-07-14
title: "static-manual-sharpeopt-l2"
image: "images/plots/static-manual-sharpeopt-l2.png"
author: "justin-guese"
draft: false
pctgain: 65
---

## Introduction to our strategy

created in basebot

## Quick Summary

<img src="/images/plots/static-manual-sharpeopt-l2.png" alt = "returns chart for static-manual-sharpeopt-l2" width="100%">

| Metric | Value |
| --- | --- |
| Return % p.a. | 65 |
| Days active | 12 |
| Starting capital | 10000 |
| Current capital | 16166.02€ |

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
      <td>USD</td>
      <td>368.602408</td>
      <td>1</td>
      <td>368.6</td>
    </tr>
    <tr>
      <td>URA</td>
      <td>18.814410</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>BTC-USD</td>
      <td>0.008946</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>WM</td>
      <td>1.024449</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>VDE</td>
      <td>1.503508</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>DBE</td>
      <td>12.331581</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>AAPL</td>
      <td>2.413577</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>NOC</td>
      <td>0.559623</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>DG</td>
      <td>1.531187</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>ETH-USD</td>
      <td>1.954529</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>W1TA.DE</td>
      <td>11.612243</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>UNH</td>
      <td>1.057598</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>NVDA</td>
      <td>4.475467</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>PGR</td>
      <td>4.996344</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>LLY</td>
      <td>3.699339</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>TSLA</td>
      <td>13.112828</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>DBO</td>
      <td>7.884130</td>
      <td>0</td>
      <td>0.0</td>
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
      <td>2023-11-22</td>
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
      <td>0.02</td>
    </tr>
    <tr>
      <th>CAGR﹪</th>
      <td>0.71</td>
    </tr>
    <tr>
      <th>Sharpe</th>
      <td>3.95</td>
    </tr>
    <tr>
      <th>Prob. Sharpe Ratio</th>
      <td>0.74</td>
    </tr>
    <tr>
      <th>Sortino</th>
      <td>6.3</td>
    </tr>
    <tr>
      <th>Sortino/√2</th>
      <td>4.45</td>
    </tr>
    <tr>
      <th>Omega</th>
      <td>1.87</td>
    </tr>
    <tr>
      <th>Max Drawdown</th>
      <td>-0.02</td>
    </tr>
    <tr>
      <th>Longest DD Days</th>
      <td>4</td>
    </tr>
    <tr>
      <th>Gain/Pain Ratio</th>
      <td>0.87</td>
    </tr>
    <tr>
      <th>Gain/Pain (1M)</th>
      <td>-</td>
    </tr>
    <tr>
      <th>Payoff Ratio</th>
      <td>0.94</td>
    </tr>
    <tr>
      <th>Profit Factor</th>
      <td>1.87</td>
    </tr>
    <tr>
      <th>Common Sense Ratio</th>
      <td>2.12</td>
    </tr>
    <tr>
      <th>CPC Index</th>
      <td>1.17</td>
    </tr>
    <tr>
      <th>Tail Ratio</th>
      <td>1.13</td>
    </tr>
    <tr>
      <th>Outlier Win Ratio</th>
      <td>1.8</td>
    </tr>
    <tr>
      <th>Outlier Loss Ratio</th>
      <td>1.98</td>
    </tr>
    <tr>
      <th>MTD</th>
      <td>0.02</td>
    </tr>
    <tr>
      <th>3M</th>
      <td>0.02</td>
    </tr>
    <tr>
      <th>6M</th>
      <td>0.02</td>
    </tr>
    <tr>
      <th>YTD</th>
      <td>0.02</td>
    </tr>
    <tr>
      <th>1Y</th>
      <td>0.02</td>
    </tr>
    <tr>
      <th>3Y (ann.)</th>
      <td>0.71</td>
    </tr>
    <tr>
      <th>5Y (ann.)</th>
      <td>0.71</td>
    </tr>
    <tr>
      <th>10Y (ann.)</th>
      <td>0.71</td>
    </tr>
    <tr>
      <th>All-time (ann.)</th>
      <td>0.71</td>
    </tr>
    <tr>
      <th>Avg. Drawdown</th>
      <td>-0.01</td>
    </tr>
    <tr>
      <th>Avg. Drawdown Days</th>
      <td>2</td>
    </tr>
    <tr>
      <th>Recovery Factor</th>
      <td>1.24</td>
    </tr>
    <tr>
      <th>Ulcer Index</th>
      <td>0.01</td>
    </tr>
    <tr>
      <th>Serenity Index</th>
      <td>1.89</td>
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
      <td>22.11.2023</td>
      <td>16166.02€</td>
    </tr>
    <tr>
      <td>21.11.2023</td>
      <td>16091.27€</td>
    </tr>
    <tr>
      <td>20.11.2023</td>
      <td>16139.56€</td>
    </tr>
    <tr>
      <td>19.11.2023</td>
      <td>15922.96€</td>
    </tr>
    <tr>
      <td>16.11.2023</td>
      <td>15843.16€</td>
    </tr>
    <tr>
      <td>15.11.2023</td>
      <td>16125.06€</td>
    </tr>
    <tr>
      <td>14.11.2023</td>
      <td>16049.33€</td>
    </tr>
    <tr>
      <td>13.11.2023</td>
      <td>15975.46€</td>
    </tr>
    <tr>
      <td>12.11.2023</td>
      <td>15754.35€</td>
    </tr>
    <tr>
      <td>10.11.2023</td>
      <td>15824.46€</td>
    </tr>
  </tbody>
</table>