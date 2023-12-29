---
date: "2023-12-29" # 2021-07-14
title: "static-manual-sharpeopt-l2"
image: "images/plots/static-manual-sharpeopt-l2.png"
author: "justin-guese"
draft: false
pctgain: 50
---

## Introduction to our strategy

created in basebot

## Quick Summary

<img src="/images/plots/static-manual-sharpeopt-l2.png" alt = "returns chart for static-manual-sharpeopt-l2" width="100%">

| Metric | Value |
| --- | --- |
| Return % p.a. | 50 |
| Days active | 48 |
| Starting capital | 10000 |
| Current capital | 16884.35€ |

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
      <td>ETH-USD</td>
      <td>1.954529</td>
      <td>2315.86</td>
      <td>4526.41</td>
    </tr>
    <tr>
      <td>TSLA</td>
      <td>13.112828</td>
      <td>250.63</td>
      <td>3286.47</td>
    </tr>
    <tr>
      <td>NVDA</td>
      <td>4.475467</td>
      <td>496.41</td>
      <td>2221.67</td>
    </tr>
    <tr>
      <td>LLY</td>
      <td>3.699339</td>
      <td>581.45</td>
      <td>2150.98</td>
    </tr>
    <tr>
      <td>PGR</td>
      <td>4.996344</td>
      <td>159.04</td>
      <td>794.62</td>
    </tr>
    <tr>
      <td>UNH</td>
      <td>1.057598</td>
      <td>525.44</td>
      <td>555.70</td>
    </tr>
    <tr>
      <td>URA</td>
      <td>18.814410</td>
      <td>27.71</td>
      <td>521.35</td>
    </tr>
    <tr>
      <td>AAPL</td>
      <td>2.413577</td>
      <td>192.26</td>
      <td>464.03</td>
    </tr>
    <tr>
      <td>BTC-USD</td>
      <td>0.008946</td>
      <td>42098.51</td>
      <td>376.62</td>
    </tr>
    <tr>
      <td>USD</td>
      <td>368.602408</td>
      <td>1.00</td>
      <td>368.60</td>
    </tr>
    <tr>
      <td>W1TA.DE</td>
      <td>11.612243</td>
      <td>31.02</td>
      <td>360.21</td>
    </tr>
    <tr>
      <td>NOC</td>
      <td>0.559623</td>
      <td>467.23</td>
      <td>261.47</td>
    </tr>
    <tr>
      <td>DBE</td>
      <td>12.331581</td>
      <td>19.30</td>
      <td>238.00</td>
    </tr>
    <tr>
      <td>DG</td>
      <td>1.531187</td>
      <td>136.49</td>
      <td>208.99</td>
    </tr>
    <tr>
      <td>WM</td>
      <td>1.024449</td>
      <td>178.93</td>
      <td>183.30</td>
    </tr>
    <tr>
      <td>VDE</td>
      <td>1.503508</td>
      <td>117.31</td>
      <td>176.38</td>
    </tr>
    <tr>
      <td>DBO</td>
      <td>7.884130</td>
      <td>13.98</td>
      <td>110.22</td>
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
      <td>1.0</td>
    </tr>
    <tr>
      <th>Cumulative Return</th>
      <td>0.07</td>
    </tr>
    <tr>
      <th>CAGR﹪</th>
      <td>0.43</td>
    </tr>
    <tr>
      <th>Sharpe</th>
      <td>2.76</td>
    </tr>
    <tr>
      <th>Prob. Sharpe Ratio</th>
      <td>0.84</td>
    </tr>
    <tr>
      <th>Sortino</th>
      <td>4.53</td>
    </tr>
    <tr>
      <th>Sortino/√2</th>
      <td>3.2</td>
    </tr>
    <tr>
      <th>Omega</th>
      <td>1.61</td>
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
      <td>0.68</td>
    </tr>
    <tr>
      <th>Gain/Pain (1M)</th>
      <td>-</td>
    </tr>
    <tr>
      <th>Payoff Ratio</th>
      <td>1.44</td>
    </tr>
    <tr>
      <th>Profit Factor</th>
      <td>1.61</td>
    </tr>
    <tr>
      <th>Common Sense Ratio</th>
      <td>2.05</td>
    </tr>
    <tr>
      <th>CPC Index</th>
      <td>1.23</td>
    </tr>
    <tr>
      <th>Tail Ratio</th>
      <td>1.27</td>
    </tr>
    <tr>
      <th>Outlier Win Ratio</th>
      <td>2.41</td>
    </tr>
    <tr>
      <th>Outlier Loss Ratio</th>
      <td>3.54</td>
    </tr>
    <tr>
      <th>MTD</th>
      <td>0.04</td>
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
      <td>0.07</td>
    </tr>
    <tr>
      <th>1Y</th>
      <td>0.07</td>
    </tr>
    <tr>
      <th>3Y (ann.)</th>
      <td>0.43</td>
    </tr>
    <tr>
      <th>5Y (ann.)</th>
      <td>0.43</td>
    </tr>
    <tr>
      <th>10Y (ann.)</th>
      <td>0.43</td>
    </tr>
    <tr>
      <th>All-time (ann.)</th>
      <td>0.43</td>
    </tr>
    <tr>
      <th>Avg. Drawdown</th>
      <td>-0.01</td>
    </tr>
    <tr>
      <th>Avg. Drawdown Days</th>
      <td>5</td>
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
      <td>2.63</td>
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
      <td>16884.35€</td>
    </tr>
    <tr>
      <td>28.12.2023</td>
      <td>17116.82€</td>
    </tr>
    <tr>
      <td>27.12.2023</td>
      <td>17064.57€</td>
    </tr>
    <tr>
      <td>26.12.2023</td>
      <td>16679.49€</td>
    </tr>
    <tr>
      <td>25.12.2023</td>
      <td>16703.58€</td>
    </tr>
    <tr>
      <td>24.12.2023</td>
      <td>16710.16€</td>
    </tr>
    <tr>
      <td>23.12.2023</td>
      <td>16738.71€</td>
    </tr>
    <tr>
      <td>22.12.2023</td>
      <td>16775.75€</td>
    </tr>
    <tr>
      <td>21.12.2023</td>
      <td>16671.76€</td>
    </tr>
    <tr>
      <td>20.12.2023</td>
      <td>16373.88€</td>
    </tr>
    <tr>
      <td>19.12.2023</td>
      <td>16633.52€</td>
    </tr>
    <tr>
      <td>18.12.2023</td>
      <td>16663.84€</td>
    </tr>
    <tr>
      <td>17.12.2023</td>
      <td>16624.01€</td>
    </tr>
    <tr>
      <td>16.12.2023</td>
      <td>16618.7€</td>
    </tr>
    <tr>
      <td>15.12.2023</td>
      <td>16648.57€</td>
    </tr>
    <tr>
      <td>14.12.2023</td>
      <td>16740.48€</td>
    </tr>
    <tr>
      <td>13.12.2023</td>
      <td>16619.69€</td>
    </tr>
    <tr>
      <td>12.12.2023</td>
      <td>16323.56€</td>
    </tr>
    <tr>
      <td>11.12.2023</td>
      <td>16380.13€</td>
    </tr>
    <tr>
      <td>10.12.2023</td>
      <td>16841.45€</td>
    </tr>
    <tr>
      <td>09.12.2023</td>
      <td>16827.56€</td>
    </tr>
    <tr>
      <td>08.12.2023</td>
      <td>16864.91€</td>
    </tr>
    <tr>
      <td>07.12.2023</td>
      <td>16752.13€</td>
    </tr>
    <tr>
      <td>06.12.2023</td>
      <td>16433.3€</td>
    </tr>
    <tr>
      <td>06.12.2023</td>
      <td>16549.83€</td>
    </tr>
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