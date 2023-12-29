---
date: "2023-12-29" # 2021-07-14
title: "static-manual-sharpeopt-l2-renewed"
image: "images/plots/static-manual-sharpeopt-l2-renewed.png"
author: "justin-guese"
draft: false
pctgain: 29
---

## Introduction to our strategy

an updated version of manual-static-sharpeopt-l2

## Quick Summary

<img src="/images/plots/static-manual-sharpeopt-l2-renewed.png" alt = "returns chart for static-manual-sharpeopt-l2-renewed" width="100%">

| Metric | Value |
| --- | --- |
| Return % p.a. | 29 |
| Days active | 48 |
| Starting capital | 10000 |
| Current capital | 16805.54€ |

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
      <td>1.241400</td>
      <td>2315.86</td>
      <td>2874.91</td>
    </tr>
    <tr>
      <td>LLY</td>
      <td>2.914792</td>
      <td>581.45</td>
      <td>1694.81</td>
    </tr>
    <tr>
      <td>NVDA</td>
      <td>3.208727</td>
      <td>496.41</td>
      <td>1592.84</td>
    </tr>
    <tr>
      <td>VDE</td>
      <td>9.051930</td>
      <td>117.31</td>
      <td>1061.88</td>
    </tr>
    <tr>
      <td>BTC-USD</td>
      <td>0.019763</td>
      <td>42098.51</td>
      <td>831.98</td>
    </tr>
    <tr>
      <td>DBE</td>
      <td>38.037990</td>
      <td>19.30</td>
      <td>734.13</td>
    </tr>
    <tr>
      <td>DBO</td>
      <td>45.777634</td>
      <td>13.98</td>
      <td>639.97</td>
    </tr>
    <tr>
      <td>PGR</td>
      <td>3.993536</td>
      <td>159.04</td>
      <td>635.13</td>
    </tr>
    <tr>
      <td>TSLA</td>
      <td>2.153598</td>
      <td>250.63</td>
      <td>539.76</td>
    </tr>
    <tr>
      <td>WM</td>
      <td>2.914667</td>
      <td>178.93</td>
      <td>521.52</td>
    </tr>
    <tr>
      <td>URA</td>
      <td>18.310399</td>
      <td>27.71</td>
      <td>507.38</td>
    </tr>
    <tr>
      <td>AAPL</td>
      <td>2.458590</td>
      <td>192.26</td>
      <td>472.69</td>
    </tr>
    <tr>
      <td>NOC</td>
      <td>1.000713</td>
      <td>467.23</td>
      <td>467.56</td>
    </tr>
    <tr>
      <td>DBA</td>
      <td>21.905591</td>
      <td>20.75</td>
      <td>454.54</td>
    </tr>
    <tr>
      <td>UNH</td>
      <td>0.721910</td>
      <td>525.44</td>
      <td>379.32</td>
    </tr>
    <tr>
      <td>FNDX</td>
      <td>5.449708</td>
      <td>61.90</td>
      <td>337.34</td>
    </tr>
    <tr>
      <td>VIS</td>
      <td>1.522344</td>
      <td>220.17</td>
      <td>335.17</td>
    </tr>
    <tr>
      <td>AMD</td>
      <td>2.193003</td>
      <td>148.43</td>
      <td>325.51</td>
    </tr>
    <tr>
      <td>XAIX.DE</td>
      <td>3.154311</td>
      <td>100.26</td>
      <td>316.25</td>
    </tr>
    <tr>
      <td>RWL</td>
      <td>3.685339</td>
      <td>85.22</td>
      <td>314.06</td>
    </tr>
    <tr>
      <td>VTV</td>
      <td>1.647309</td>
      <td>149.35</td>
      <td>246.03</td>
    </tr>
    <tr>
      <td>DBMF</td>
      <td>8.559254</td>
      <td>25.72</td>
      <td>220.14</td>
    </tr>
    <tr>
      <td>MSFT</td>
      <td>0.561107</td>
      <td>375.85</td>
      <td>210.89</td>
    </tr>
    <tr>
      <td>W1TA.DE</td>
      <td>6.383903</td>
      <td>31.02</td>
      <td>198.03</td>
    </tr>
    <tr>
      <td>IWDA.AS</td>
      <td>2.393711</td>
      <td>81.87</td>
      <td>195.97</td>
    </tr>
    <tr>
      <td>VFH</td>
      <td>2.106489</td>
      <td>92.21</td>
      <td>194.24</td>
    </tr>
    <tr>
      <td>VAW</td>
      <td>0.950194</td>
      <td>190.17</td>
      <td>180.70</td>
    </tr>
    <tr>
      <td>VDC</td>
      <td>0.743968</td>
      <td>190.88</td>
      <td>142.01</td>
    </tr>
    <tr>
      <td>FAS</td>
      <td>1.504391</td>
      <td>82.27</td>
      <td>123.77</td>
    </tr>
    <tr>
      <td>USD</td>
      <td>0.003750</td>
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
      <td>1.0</td>
    </tr>
    <tr>
      <th>Cumulative Return</th>
      <td>0.04</td>
    </tr>
    <tr>
      <th>CAGR﹪</th>
      <td>0.23</td>
    </tr>
    <tr>
      <th>Sharpe</th>
      <td>2.39</td>
    </tr>
    <tr>
      <th>Prob. Sharpe Ratio</th>
      <td>0.81</td>
    </tr>
    <tr>
      <th>Sortino</th>
      <td>3.91</td>
    </tr>
    <tr>
      <th>Sortino/√2</th>
      <td>2.76</td>
    </tr>
    <tr>
      <th>Omega</th>
      <td>1.51</td>
    </tr>
    <tr>
      <th>Max Drawdown</th>
      <td>-0.02</td>
    </tr>
    <tr>
      <th>Longest DD Days</th>
      <td>18</td>
    </tr>
    <tr>
      <th>Gain/Pain Ratio</th>
      <td>0.55</td>
    </tr>
    <tr>
      <th>Gain/Pain (1M)</th>
      <td>-</td>
    </tr>
    <tr>
      <th>Payoff Ratio</th>
      <td>1.51</td>
    </tr>
    <tr>
      <th>Profit Factor</th>
      <td>1.51</td>
    </tr>
    <tr>
      <th>Common Sense Ratio</th>
      <td>1.65</td>
    </tr>
    <tr>
      <th>CPC Index</th>
      <td>1.14</td>
    </tr>
    <tr>
      <th>Tail Ratio</th>
      <td>1.1</td>
    </tr>
    <tr>
      <th>Outlier Win Ratio</th>
      <td>2.27</td>
    </tr>
    <tr>
      <th>Outlier Loss Ratio</th>
      <td>3.42</td>
    </tr>
    <tr>
      <th>MTD</th>
      <td>0.03</td>
    </tr>
    <tr>
      <th>3M</th>
      <td>0.04</td>
    </tr>
    <tr>
      <th>6M</th>
      <td>0.04</td>
    </tr>
    <tr>
      <th>YTD</th>
      <td>0.04</td>
    </tr>
    <tr>
      <th>1Y</th>
      <td>0.04</td>
    </tr>
    <tr>
      <th>3Y (ann.)</th>
      <td>0.23</td>
    </tr>
    <tr>
      <th>5Y (ann.)</th>
      <td>0.23</td>
    </tr>
    <tr>
      <th>10Y (ann.)</th>
      <td>0.23</td>
    </tr>
    <tr>
      <th>All-time (ann.)</th>
      <td>0.23</td>
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
      <td>1.95</td>
    </tr>
    <tr>
      <th>Ulcer Index</th>
      <td>0.01</td>
    </tr>
    <tr>
      <th>Serenity Index</th>
      <td>2.72</td>
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
      <td>16805.54€</td>
    </tr>
    <tr>
      <td>28.12.2023</td>
      <td>16945.91€</td>
    </tr>
    <tr>
      <td>27.12.2023</td>
      <td>16917.07€</td>
    </tr>
    <tr>
      <td>26.12.2023</td>
      <td>16701.1€</td>
    </tr>
    <tr>
      <td>25.12.2023</td>
      <td>16706.29€</td>
    </tr>
    <tr>
      <td>24.12.2023</td>
      <td>16709.75€</td>
    </tr>
    <tr>
      <td>23.12.2023</td>
      <td>16731.67€</td>
    </tr>
    <tr>
      <td>22.12.2023</td>
      <td>16754.67€</td>
    </tr>
    <tr>
      <td>21.12.2023</td>
      <td>16674.38€</td>
    </tr>
    <tr>
      <td>20.12.2023</td>
      <td>16480.67€</td>
    </tr>
    <tr>
      <td>19.12.2023</td>
      <td>16665.88€</td>
    </tr>
    <tr>
      <td>18.12.2023</td>
      <td>16695.28€</td>
    </tr>
    <tr>
      <td>17.12.2023</td>
      <td>16665.85€</td>
    </tr>
    <tr>
      <td>16.12.2023</td>
      <td>16668.07€</td>
    </tr>
    <tr>
      <td>15.12.2023</td>
      <td>16686.83€</td>
    </tr>
    <tr>
      <td>14.12.2023</td>
      <td>16781.49€</td>
    </tr>
    <tr>
      <td>13.12.2023</td>
      <td>16743.31€</td>
    </tr>
    <tr>
      <td>12.12.2023</td>
      <td>16468.4€</td>
    </tr>
    <tr>
      <td>11.12.2023</td>
      <td>16500.21€</td>
    </tr>
    <tr>
      <td>10.12.2023</td>
      <td>16780.05€</td>
    </tr>
    <tr>
      <td>09.12.2023</td>
      <td>16772.94€</td>
    </tr>
    <tr>
      <td>08.12.2023</td>
      <td>16805.01€</td>
    </tr>
    <tr>
      <td>07.12.2023</td>
      <td>16661.68€</td>
    </tr>
    <tr>
      <td>06.12.2023</td>
      <td>16449.22€</td>
    </tr>
    <tr>
      <td>06.12.2023</td>
      <td>16519.17€</td>
    </tr>
    <tr>
      <td>22.11.2023</td>
      <td>16393.2€</td>
    </tr>
    <tr>
      <td>21.11.2023</td>
      <td>16284.83€</td>
    </tr>
    <tr>
      <td>20.11.2023</td>
      <td>16366.93€</td>
    </tr>
    <tr>
      <td>19.11.2023</td>
      <td>16174.3€</td>
    </tr>
    <tr>
      <td>16.11.2023</td>
      <td>16048.61€</td>
    </tr>
    <tr>
      <td>15.11.2023</td>
      <td>16260.19€</td>
    </tr>
    <tr>
      <td>14.11.2023</td>
      <td>16255.14€</td>
    </tr>
    <tr>
      <td>13.11.2023</td>
      <td>16254.25€</td>
    </tr>
    <tr>
      <td>12.11.2023</td>
      <td>16131.1€</td>
    </tr>
    <tr>
      <td>10.11.2023</td>
      <td>16178.36€</td>
    </tr>
  </tbody>
</table>