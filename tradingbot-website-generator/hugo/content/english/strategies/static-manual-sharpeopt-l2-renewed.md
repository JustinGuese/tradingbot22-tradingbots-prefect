---
date: "2024-01-04" # 2021-07-14
title: "static-manual-sharpeopt-l2-renewed"
image: "images/plots/static-manual-sharpeopt-l2-renewed.png"
author: "justin-guese"
draft: false
pctgain: 19
---

## Introduction to our strategy

an updated version of manual-static-sharpeopt-l2

## Quick Summary

<img src="/images/plots/static-manual-sharpeopt-l2-renewed.png" alt = "returns chart for static-manual-sharpeopt-l2-renewed" width="100%">

| Metric | Value |
| --- | --- |
| Return % p.a. | 19 |
| Days active | 54 |
| Starting capital | 10000 |
| Current capital | 16641.96€ |

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
      <td>1.241400</td>
      <td>2277.53</td>
      <td>2827.32</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/LLY'>LLY</a></td>
      <td>2.914792</td>
      <td>628.37</td>
      <td>1831.57</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/NVDA'>NVDA</a></td>
      <td>3.208727</td>
      <td>480.04</td>
      <td>1540.32</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/VDE'>VDE</a></td>
      <td>9.051930</td>
      <td>120.07</td>
      <td>1086.87</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/BTC-USD'>BTC-USD</a></td>
      <td>0.019763</td>
      <td>44189.07</td>
      <td>873.29</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/DBE'>DBE</a></td>
      <td>38.037990</td>
      <td>19.57</td>
      <td>744.40</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/PGR'>PGR</a></td>
      <td>3.993536</td>
      <td>164.55</td>
      <td>657.14</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/DBO'>DBO</a></td>
      <td>45.777634</td>
      <td>14.10</td>
      <td>645.46</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/WM'>WM</a></td>
      <td>2.914667</td>
      <td>180.17</td>
      <td>525.14</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/TSLA'>TSLA</a></td>
      <td>2.153598</td>
      <td>241.78</td>
      <td>520.70</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/URA'>URA</a></td>
      <td>18.310399</td>
      <td>27.30</td>
      <td>499.87</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/NOC'>NOC</a></td>
      <td>1.000713</td>
      <td>481.37</td>
      <td>481.71</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/DBA'>DBA</a></td>
      <td>21.905591</td>
      <td>20.63</td>
      <td>451.91</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/AAPL'>AAPL</a></td>
      <td>2.458590</td>
      <td>181.29</td>
      <td>445.72</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/UNH'>UNH</a></td>
      <td>0.721910</td>
      <td>545.63</td>
      <td>393.90</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/FNDX'>FNDX</a></td>
      <td>5.449708</td>
      <td>61.65</td>
      <td>335.97</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/VIS'>VIS</a></td>
      <td>1.522344</td>
      <td>215.85</td>
      <td>328.60</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/RWL'>RWL</a></td>
      <td>3.685339</td>
      <td>85.31</td>
      <td>314.40</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/XAIX.DE'>XAIX.DE</a></td>
      <td>3.154311</td>
      <td>97.70</td>
      <td>308.18</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/AMD'>AMD</a></td>
      <td>2.193003</td>
      <td>136.50</td>
      <td>299.34</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/VTV'>VTV</a></td>
      <td>1.647309</td>
      <td>150.24</td>
      <td>247.49</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/DBMF'>DBMF</a></td>
      <td>8.559254</td>
      <td>25.92</td>
      <td>221.86</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/MSFT'>MSFT</a></td>
      <td>0.561107</td>
      <td>371.83</td>
      <td>208.64</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/IWDA.AS'>IWDA.AS</a></td>
      <td>2.393711</td>
      <td>81.63</td>
      <td>195.40</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/VFH'>VFH</a></td>
      <td>2.106489</td>
      <td>92.28</td>
      <td>194.39</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/W1TA.DE'>W1TA.DE</a></td>
      <td>6.383903</td>
      <td>29.80</td>
      <td>190.24</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/VAW'>VAW</a></td>
      <td>0.950194</td>
      <td>187.29</td>
      <td>177.96</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/VDC'>VDC</a></td>
      <td>0.743968</td>
      <td>191.91</td>
      <td>142.77</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/FAS'>FAS</a></td>
      <td>1.504391</td>
      <td>83.89</td>
      <td>126.20</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/USD'>USD</a></td>
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
      <td>2024-01-03</td>
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
      <td>0.03</td>
    </tr>
    <tr>
      <th>CAGR﹪</th>
      <td>0.15</td>
    </tr>
    <tr>
      <th>Sharpe</th>
      <td>1.57</td>
    </tr>
    <tr>
      <th>Prob. Sharpe Ratio</th>
      <td>0.73</td>
    </tr>
    <tr>
      <th>Sortino</th>
      <td>2.46</td>
    </tr>
    <tr>
      <th>Sortino/√2</th>
      <td>1.74</td>
    </tr>
    <tr>
      <th>Omega</th>
      <td>1.31</td>
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
      <td>0.33</td>
    </tr>
    <tr>
      <th>Gain/Pain (1M)</th>
      <td>7.38</td>
    </tr>
    <tr>
      <th>Payoff Ratio</th>
      <td>1.31</td>
    </tr>
    <tr>
      <th>Profit Factor</th>
      <td>1.31</td>
    </tr>
    <tr>
      <th>Common Sense Ratio</th>
      <td>1.51</td>
    </tr>
    <tr>
      <th>CPC Index</th>
      <td>0.86</td>
    </tr>
    <tr>
      <th>Tail Ratio</th>
      <td>1.15</td>
    </tr>
    <tr>
      <th>Outlier Win Ratio</th>
      <td>2.45</td>
    </tr>
    <tr>
      <th>Outlier Loss Ratio</th>
      <td>3.21</td>
    </tr>
    <tr>
      <th>MTD</th>
      <td>0</td>
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
      <td>0</td>
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
      <td>-0.01</td>
    </tr>
    <tr>
      <th>Avg. Drawdown Days</th>
      <td>6</td>
    </tr>
    <tr>
      <th>Recovery Factor</th>
      <td>1.46</td>
    </tr>
    <tr>
      <th>Ulcer Index</th>
      <td>0.01</td>
    </tr>
    <tr>
      <th>Serenity Index</th>
      <td>1.54</td>
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
      <td>2024-01-03</td>
      <td>16641.96€</td>
    </tr>
    <tr>
      <td>2024-01-02</td>
      <td>16822.35€</td>
    </tr>
    <tr>
      <td>2024-01-01</td>
      <td>16792.67€</td>
    </tr>
    <tr>
      <td>2023-12-31</td>
      <td>16709.42€</td>
    </tr>
    <tr>
      <td>2023-12-30</td>
      <td>16723.63€</td>
    </tr>
    <tr>
      <td>2023-12-29</td>
      <td>16696.05€</td>
    </tr>
    <tr>
      <td>2023-12-28</td>
      <td>16805.54€</td>
    </tr>
    <tr>
      <td>2023-12-28</td>
      <td>16945.91€</td>
    </tr>
    <tr>
      <td>2023-12-27</td>
      <td>16917.07€</td>
    </tr>
    <tr>
      <td>2023-12-26</td>
      <td>16701.1€</td>
    </tr>
    <tr>
      <td>2023-12-25</td>
      <td>16706.29€</td>
    </tr>
    <tr>
      <td>2023-12-24</td>
      <td>16709.75€</td>
    </tr>
    <tr>
      <td>2023-12-23</td>
      <td>16731.67€</td>
    </tr>
    <tr>
      <td>2023-12-22</td>
      <td>16754.67€</td>
    </tr>
    <tr>
      <td>2023-12-21</td>
      <td>16674.38€</td>
    </tr>
    <tr>
      <td>2023-12-20</td>
      <td>16480.67€</td>
    </tr>
    <tr>
      <td>2023-12-19</td>
      <td>16665.88€</td>
    </tr>
    <tr>
      <td>2023-12-18</td>
      <td>16695.28€</td>
    </tr>
    <tr>
      <td>2023-12-17</td>
      <td>16665.85€</td>
    </tr>
    <tr>
      <td>2023-12-16</td>
      <td>16668.07€</td>
    </tr>
    <tr>
      <td>2023-12-15</td>
      <td>16686.83€</td>
    </tr>
    <tr>
      <td>2023-12-14</td>
      <td>16781.49€</td>
    </tr>
    <tr>
      <td>2023-12-13</td>
      <td>16743.31€</td>
    </tr>
    <tr>
      <td>2023-12-12</td>
      <td>16468.4€</td>
    </tr>
    <tr>
      <td>2023-12-11</td>
      <td>16500.21€</td>
    </tr>
    <tr>
      <td>2023-12-10</td>
      <td>16780.05€</td>
    </tr>
    <tr>
      <td>2023-12-09</td>
      <td>16772.94€</td>
    </tr>
    <tr>
      <td>2023-12-08</td>
      <td>16805.01€</td>
    </tr>
    <tr>
      <td>2023-12-07</td>
      <td>16661.68€</td>
    </tr>
    <tr>
      <td>2023-12-06</td>
      <td>16449.22€</td>
    </tr>
    <tr>
      <td>2023-12-06</td>
      <td>16519.17€</td>
    </tr>
    <tr>
      <td>2023-11-22</td>
      <td>16393.2€</td>
    </tr>
    <tr>
      <td>2023-11-21</td>
      <td>16284.83€</td>
    </tr>
    <tr>
      <td>2023-11-20</td>
      <td>16366.93€</td>
    </tr>
    <tr>
      <td>2023-11-19</td>
      <td>16174.3€</td>
    </tr>
    <tr>
      <td>2023-11-16</td>
      <td>16048.61€</td>
    </tr>
    <tr>
      <td>2023-11-15</td>
      <td>16260.19€</td>
    </tr>
    <tr>
      <td>2023-11-14</td>
      <td>16255.14€</td>
    </tr>
    <tr>
      <td>2023-11-13</td>
      <td>16254.25€</td>
    </tr>
    <tr>
      <td>2023-11-12</td>
      <td>16131.1€</td>
    </tr>
    <tr>
      <td>2023-11-10</td>
      <td>16178.36€</td>
    </tr>
  </tbody>
</table>