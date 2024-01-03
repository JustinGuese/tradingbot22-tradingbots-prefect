---
date: "2024-01-03" # 2021-07-14
title: "c-volume-hedged"
image: "images/plots/c-volume-hedged.png"
author: "justin-guese"
draft: false
pctgain: -23
---

## Introduction to our strategy

created in basebot

## Quick Summary

<img src="/images/plots/c-volume-hedged.png" alt = "returns chart for c-volume-hedged" width="100%">

| Metric | Value |
| --- | --- |
| Return % p.a. | -23 |
| Days active | 53 |
| Starting capital | 9921.35 |
| Current capital | 9589.67€ |

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
      <td><a target='_blank' href='https://finance.yahoo.com/quote/UUP'>UUP</a></td>
      <td>156.473845</td>
      <td>27.42</td>
      <td>4290.51</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/DBMF'>DBMF</a></td>
      <td>105.545476</td>
      <td>25.84</td>
      <td>2727.30</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/GLD'>GLD</a></td>
      <td>13.578113</td>
      <td>188.55</td>
      <td>2560.15</td>
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
      <td>0.72</td>
    </tr>
    <tr>
      <th>Cumulative Return</th>
      <td>-0.03</td>
    </tr>
    <tr>
      <th>CAGR﹪</th>
      <td>-0.15</td>
    </tr>
    <tr>
      <th>Sharpe</th>
      <td>-2.25</td>
    </tr>
    <tr>
      <th>Prob. Sharpe Ratio</th>
      <td>0.16</td>
    </tr>
    <tr>
      <th>Sortino</th>
      <td>-2.61</td>
    </tr>
    <tr>
      <th>Sortino/√2</th>
      <td>-1.84</td>
    </tr>
    <tr>
      <th>Omega</th>
      <td>0.55</td>
    </tr>
    <tr>
      <th>Max Drawdown</th>
      <td>-0.05</td>
    </tr>
    <tr>
      <th>Longest DD Days</th>
      <td>42</td>
    </tr>
    <tr>
      <th>Gain/Pain Ratio</th>
      <td>-0.46</td>
    </tr>
    <tr>
      <th>Gain/Pain (1M)</th>
      <td>-0.71</td>
    </tr>
    <tr>
      <th>Payoff Ratio</th>
      <td>0.73</td>
    </tr>
    <tr>
      <th>Profit Factor</th>
      <td>0.55</td>
    </tr>
    <tr>
      <th>Common Sense Ratio</th>
      <td>0.35</td>
    </tr>
    <tr>
      <th>CPC Index</th>
      <td>0.17</td>
    </tr>
    <tr>
      <th>Tail Ratio</th>
      <td>0.65</td>
    </tr>
    <tr>
      <th>Outlier Win Ratio</th>
      <td>7.08</td>
    </tr>
    <tr>
      <th>Outlier Loss Ratio</th>
      <td>4.72</td>
    </tr>
    <tr>
      <th>MTD</th>
      <td>0</td>
    </tr>
    <tr>
      <th>3M</th>
      <td>-0.03</td>
    </tr>
    <tr>
      <th>6M</th>
      <td>-0.03</td>
    </tr>
    <tr>
      <th>YTD</th>
      <td>0</td>
    </tr>
    <tr>
      <th>1Y</th>
      <td>-0.03</td>
    </tr>
    <tr>
      <th>3Y (ann.)</th>
      <td>-0.15</td>
    </tr>
    <tr>
      <th>5Y (ann.)</th>
      <td>-0.15</td>
    </tr>
    <tr>
      <th>10Y (ann.)</th>
      <td>-0.15</td>
    </tr>
    <tr>
      <th>All-time (ann.)</th>
      <td>-0.15</td>
    </tr>
    <tr>
      <th>Avg. Drawdown</th>
      <td>-0.02</td>
    </tr>
    <tr>
      <th>Avg. Drawdown Days</th>
      <td>16</td>
    </tr>
    <tr>
      <th>Recovery Factor</th>
      <td>0.72</td>
    </tr>
    <tr>
      <th>Ulcer Index</th>
      <td>0.03</td>
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
      <td>2023-11-22 00:10:12.120618</td>
      <td>Buy</td>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/DBMF'>DBMF</a></td>
      <td>27.410000</td>
      <td>2897.347509</td>
      <td>79416.29</td>
    </tr>
    <tr>
      <td>2023-11-22 00:10:12.093244</td>
      <td>Buy</td>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/UUP'>UUP</a></td>
      <td>29.240000</td>
      <td>4582.168437</td>
      <td>133982.60</td>
    </tr>
    <tr>
      <td>2023-11-22 00:10:12.064163</td>
      <td>Buy</td>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/GLD'>GLD</a></td>
      <td>185.350006</td>
      <td>2520.484054</td>
      <td>467171.73</td>
    </tr>
    <tr>
      <td>2023-11-21 00:10:12.036796</td>
      <td>Buy</td>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/DBMF'>DBMF</a></td>
      <td>27.400000</td>
      <td>2885.737634</td>
      <td>79069.21</td>
    </tr>
    <tr>
      <td>2023-11-21 00:10:12.004980</td>
      <td>Buy</td>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/UUP'>UUP</a></td>
      <td>29.209999</td>
      <td>4567.082418</td>
      <td>133404.47</td>
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
      <td>9589.67€</td>
    </tr>
    <tr>
      <td>2024-01-01</td>
      <td>9553.46€</td>
    </tr>
    <tr>
      <td>2023-12-31</td>
      <td>9553.46€</td>
    </tr>
    <tr>
      <td>2023-12-30</td>
      <td>9553.46€</td>
    </tr>
    <tr>
      <td>2023-12-29</td>
      <td>9553.46€</td>
    </tr>
    <tr>
      <td>2023-12-28</td>
      <td>9552.87€</td>
    </tr>
    <tr>
      <td>2023-12-28</td>
      <td>9557.16€</td>
    </tr>
    <tr>
      <td>2023-12-27</td>
      <td>9557.16€</td>
    </tr>
    <tr>
      <td>2023-12-26</td>
      <td>9644.3€</td>
    </tr>
    <tr>
      <td>2023-12-25</td>
      <td>9639.28€</td>
    </tr>
    <tr>
      <td>2023-12-24</td>
      <td>9639.28€</td>
    </tr>
    <tr>
      <td>2023-12-23</td>
      <td>9639.28€</td>
    </tr>
    <tr>
      <td>2023-12-22</td>
      <td>9639.28€</td>
    </tr>
    <tr>
      <td>2023-12-21</td>
      <td>9621.0€</td>
    </tr>
    <tr>
      <td>2023-12-20</td>
      <td>9638.49€</td>
    </tr>
    <tr>
      <td>2023-12-19</td>
      <td>9636.87€</td>
    </tr>
    <tr>
      <td>2023-12-18</td>
      <td>9638.26€</td>
    </tr>
    <tr>
      <td>2023-12-17</td>
      <td>9902.66€</td>
    </tr>
    <tr>
      <td>2023-12-16</td>
      <td>9902.66€</td>
    </tr>
    <tr>
      <td>2023-12-15</td>
      <td>9902.66€</td>
    </tr>
    <tr>
      <td>2023-12-14</td>
      <td>9879.54€</td>
    </tr>
    <tr>
      <td>2023-12-13</td>
      <td>9935.34€</td>
    </tr>
    <tr>
      <td>2023-12-12</td>
      <td>9938.3€</td>
    </tr>
    <tr>
      <td>2023-12-11</td>
      <td>9968.01€</td>
    </tr>
    <tr>
      <td>2023-12-10</td>
      <td>9975.87€</td>
    </tr>
    <tr>
      <td>2023-12-09</td>
      <td>9975.87€</td>
    </tr>
    <tr>
      <td>2023-12-08</td>
      <td>9975.87€</td>
    </tr>
    <tr>
      <td>2023-12-07</td>
      <td>9962.13€</td>
    </tr>
    <tr>
      <td>2023-12-06</td>
      <td>10008.28€</td>
    </tr>
    <tr>
      <td>2023-12-06</td>
      <td>10003.05€</td>
    </tr>
    <tr>
      <td>2023-11-22</td>
      <td>10014.2€</td>
    </tr>
    <tr>
      <td>2023-11-21</td>
      <td>10018.2€</td>
    </tr>
    <tr>
      <td>2023-11-20</td>
      <td>9957.27€</td>
    </tr>
    <tr>
      <td>2023-11-19</td>
      <td>9985.0€</td>
    </tr>
    <tr>
      <td>2023-11-16</td>
      <td>9991.46€</td>
    </tr>
    <tr>
      <td>2023-11-15</td>
      <td>10017.47€</td>
    </tr>
    <tr>
      <td>2023-11-14</td>
      <td>9860.45€</td>
    </tr>
    <tr>
      <td>2023-11-13</td>
      <td>9993.46€</td>
    </tr>
    <tr>
      <td>2023-11-12</td>
      <td>9985.0€</td>
    </tr>
    <tr>
      <td>2023-11-10</td>
      <td>9921.35€</td>
    </tr>
  </tbody>
</table>