---
date: "2024-01-03" # 2021-07-14
title: "static-vti-top50-replication"
image: "images/plots/static-vti-top50-replication.png"
author: "justin-guese"
draft: false
pctgain: 34
---

## Introduction to our strategy

jupyternotebooks/nasdaqreplicationtest.ipynb

## Quick Summary

<img src="/images/plots/static-vti-top50-replication.png" alt = "returns chart for static-vti-top50-replication" width="100%">

| Metric | Value |
| --- | --- |
| Return % p.a. | 34 |
| Days active | 53 |
| Starting capital | 10000 |
| Current capital | 10635.76€ |

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
      <td><a target='_blank' href='https://finance.yahoo.com/quote/AAPL'>AAPL</a></td>
      <td>7.758277</td>
      <td>185.12</td>
      <td>1436.21</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/MSFT'>MSFT</a></td>
      <td>3.522106</td>
      <td>371.70</td>
      <td>1309.17</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/AMZN'>AMZN</a></td>
      <td>4.050774</td>
      <td>150.07</td>
      <td>607.90</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/NVDA'>NVDA</a></td>
      <td>1.121336</td>
      <td>478.99</td>
      <td>537.11</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/GOOGL'>GOOGL</a></td>
      <td>2.756449</td>
      <td>138.21</td>
      <td>380.97</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/META'>META</a></td>
      <td>1.095656</td>
      <td>345.31</td>
      <td>378.34</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/TSLA'>TSLA</a></td>
      <td>1.360834</td>
      <td>241.99</td>
      <td>329.31</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/GOOG'>GOOG</a></td>
      <td>2.297724</td>
      <td>139.55</td>
      <td>320.65</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/USD'>USD</a></td>
      <td>293.004113</td>
      <td>1.00</td>
      <td>293.00</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/JPM'>JPM</a></td>
      <td>1.485662</td>
      <td>171.15</td>
      <td>254.27</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/UNH'>UNH</a></td>
      <td>0.458747</td>
      <td>546.00</td>
      <td>250.48</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/AVGO'>AVGO</a></td>
      <td>0.205747</td>
      <td>1069.45</td>
      <td>220.04</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/JNJ'>JNJ</a></td>
      <td>1.277291</td>
      <td>160.04</td>
      <td>204.42</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/LLY'>LLY</a></td>
      <td>0.321152</td>
      <td>606.41</td>
      <td>194.75</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/V'>V</a></td>
      <td>0.727984</td>
      <td>258.05</td>
      <td>187.86</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/XOM'>XOM</a></td>
      <td>1.753291</td>
      <td>101.94</td>
      <td>178.73</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/PG'>PG</a></td>
      <td>1.132281</td>
      <td>148.13</td>
      <td>167.72</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/HD'>HD</a></td>
      <td>0.476920</td>
      <td>340.69</td>
      <td>162.48</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/MA'>MA</a></td>
      <td>0.375844</td>
      <td>419.43</td>
      <td>157.64</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/COST'>COST</a></td>
      <td>0.211285</td>
      <td>652.91</td>
      <td>137.95</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/MRK'>MRK</a></td>
      <td>1.182639</td>
      <td>114.67</td>
      <td>135.61</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/ABBV'>ABBV</a></td>
      <td>0.845040</td>
      <td>160.44</td>
      <td>135.58</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/CVX'>CVX</a></td>
      <td>0.818203</td>
      <td>149.04</td>
      <td>121.94</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/ADBE'>ADBE</a></td>
      <td>0.211450</td>
      <td>575.08</td>
      <td>121.60</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/BAC'>BAC</a></td>
      <td>3.554639</td>
      <td>33.47</td>
      <td>118.97</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/PEP'>PEP</a></td>
      <td>0.683738</td>
      <td>173.45</td>
      <td>118.59</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/KO'>KO</a></td>
      <td>1.897760</td>
      <td>59.94</td>
      <td>113.75</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/CRM'>CRM</a></td>
      <td>0.448545</td>
      <td>253.48</td>
      <td>113.70</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/WMT'>WMT</a></td>
      <td>0.688223</td>
      <td>159.54</td>
      <td>109.80</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/AMD'>AMD</a></td>
      <td>0.804636</td>
      <td>136.05</td>
      <td>109.47</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/MCD'>MCD</a></td>
      <td>0.365050</td>
      <td>296.75</td>
      <td>108.33</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/TMO'>TMO</a></td>
      <td>0.184133</td>
      <td>541.33</td>
      <td>99.68</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/ABT'>ABT</a></td>
      <td>0.892127</td>
      <td>110.01</td>
      <td>98.14</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/ACN'>ACN</a></td>
      <td>0.284184</td>
      <td>342.45</td>
      <td>97.32</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/NFLX'>NFLX</a></td>
      <td>0.205932</td>
      <td>471.69</td>
      <td>97.14</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/WFC'>WFC</a></td>
      <td>1.962283</td>
      <td>48.63</td>
      <td>95.43</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/LIN'>LIN</a></td>
      <td>0.230139</td>
      <td>408.86</td>
      <td>94.09</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/INTC'>INTC</a></td>
      <td>1.857019</td>
      <td>47.60</td>
      <td>88.39</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/QCOM'>QCOM</a></td>
      <td>0.634716</td>
      <td>137.98</td>
      <td>87.58</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/DIS'>DIS</a></td>
      <td>0.940152</td>
      <td>90.57</td>
      <td>85.15</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/CMCSA'>CMCSA</a></td>
      <td>1.952098</td>
      <td>43.26</td>
      <td>84.45</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/PFE'>PFE</a></td>
      <td>2.751531</td>
      <td>29.58</td>
      <td>81.39</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/CSCO'>CSCO</a></td>
      <td>1.551841</td>
      <td>50.07</td>
      <td>77.70</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/BA'>BA</a></td>
      <td>0.311121</td>
      <td>248.57</td>
      <td>77.34</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/TXN'>TXN</a></td>
      <td>0.457781</td>
      <td>166.80</td>
      <td>76.36</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/nan'>nan</a></td>
      <td>6.603320</td>
      <td>11.04</td>
      <td>72.90</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/PM'>PM</a></td>
      <td>0.763062</td>
      <td>95.10</td>
      <td>72.57</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/DHR'>DHR</a></td>
      <td>0.310417</td>
      <td>233.13</td>
      <td>72.37</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/ORCL'>ORCL</a></td>
      <td>0.666759</td>
      <td>103.11</td>
      <td>68.75</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/NEE'>NEE</a></td>
      <td>1.049302</td>
      <td>60.79</td>
      <td>63.79</td>
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
      <td>0.05</td>
    </tr>
    <tr>
      <th>CAGR﹪</th>
      <td>0.27</td>
    </tr>
    <tr>
      <th>Sharpe</th>
      <td>3.66</td>
    </tr>
    <tr>
      <th>Prob. Sharpe Ratio</th>
      <td>0.92</td>
    </tr>
    <tr>
      <th>Sortino</th>
      <td>6.46</td>
    </tr>
    <tr>
      <th>Sortino/√2</th>
      <td>4.57</td>
    </tr>
    <tr>
      <th>Omega</th>
      <td>2.08</td>
    </tr>
    <tr>
      <th>Max Drawdown</th>
      <td>-0.01</td>
    </tr>
    <tr>
      <th>Longest DD Days</th>
      <td>7</td>
    </tr>
    <tr>
      <th>Gain/Pain Ratio</th>
      <td>1.08</td>
    </tr>
    <tr>
      <th>Gain/Pain (1M)</th>
      <td>4.9</td>
    </tr>
    <tr>
      <th>Payoff Ratio</th>
      <td>1.43</td>
    </tr>
    <tr>
      <th>Profit Factor</th>
      <td>2.08</td>
    </tr>
    <tr>
      <th>Common Sense Ratio</th>
      <td>2.26</td>
    </tr>
    <tr>
      <th>CPC Index</th>
      <td>1.75</td>
    </tr>
    <tr>
      <th>Tail Ratio</th>
      <td>1.09</td>
    </tr>
    <tr>
      <th>Outlier Win Ratio</th>
      <td>4.11</td>
    </tr>
    <tr>
      <th>Outlier Loss Ratio</th>
      <td>2.8</td>
    </tr>
    <tr>
      <th>MTD</th>
      <td>-0.01</td>
    </tr>
    <tr>
      <th>3M</th>
      <td>0.05</td>
    </tr>
    <tr>
      <th>6M</th>
      <td>0.05</td>
    </tr>
    <tr>
      <th>YTD</th>
      <td>-0.01</td>
    </tr>
    <tr>
      <th>1Y</th>
      <td>0.05</td>
    </tr>
    <tr>
      <th>3Y (ann.)</th>
      <td>0.27</td>
    </tr>
    <tr>
      <th>5Y (ann.)</th>
      <td>0.27</td>
    </tr>
    <tr>
      <th>10Y (ann.)</th>
      <td>0.27</td>
    </tr>
    <tr>
      <th>All-time (ann.)</th>
      <td>0.27</td>
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
      <td>3.74</td>
    </tr>
    <tr>
      <th>Ulcer Index</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Serenity Index</th>
      <td>8.0</td>
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
      <td>10635.76€</td>
    </tr>
    <tr>
      <td>2024-01-01</td>
      <td>10742.87€</td>
    </tr>
    <tr>
      <td>2023-12-31</td>
      <td>10742.87€</td>
    </tr>
    <tr>
      <td>2023-12-30</td>
      <td>10742.87€</td>
    </tr>
    <tr>
      <td>2023-12-29</td>
      <td>10742.87€</td>
    </tr>
    <tr>
      <td>2023-12-28</td>
      <td>10774.57€</td>
    </tr>
    <tr>
      <td>2023-12-28</td>
      <td>10776.34€</td>
    </tr>
    <tr>
      <td>2023-12-27</td>
      <td>10776.34€</td>
    </tr>
    <tr>
      <td>2023-12-26</td>
      <td>10763.29€</td>
    </tr>
    <tr>
      <td>2023-12-25</td>
      <td>10730.96€</td>
    </tr>
    <tr>
      <td>2023-12-24</td>
      <td>10730.96€</td>
    </tr>
    <tr>
      <td>2023-12-23</td>
      <td>10730.96€</td>
    </tr>
    <tr>
      <td>2023-12-22</td>
      <td>10730.96€</td>
    </tr>
    <tr>
      <td>2023-12-21</td>
      <td>10725.36€</td>
    </tr>
    <tr>
      <td>2023-12-20</td>
      <td>10628.57€</td>
    </tr>
    <tr>
      <td>2023-12-19</td>
      <td>10763.41€</td>
    </tr>
    <tr>
      <td>2023-12-18</td>
      <td>10715.02€</td>
    </tr>
    <tr>
      <td>2023-12-17</td>
      <td>10640.98€</td>
    </tr>
    <tr>
      <td>2023-12-16</td>
      <td>10640.98€</td>
    </tr>
    <tr>
      <td>2023-12-15</td>
      <td>10640.98€</td>
    </tr>
    <tr>
      <td>2023-12-14</td>
      <td>10594.14€</td>
    </tr>
    <tr>
      <td>2023-12-13</td>
      <td>10615.17€</td>
    </tr>
    <tr>
      <td>2023-12-12</td>
      <td>10513.81€</td>
    </tr>
    <tr>
      <td>2023-12-11</td>
      <td>10453.66€</td>
    </tr>
    <tr>
      <td>2023-12-10</td>
      <td>10468.94€</td>
    </tr>
    <tr>
      <td>2023-12-09</td>
      <td>10468.94€</td>
    </tr>
    <tr>
      <td>2023-12-08</td>
      <td>10468.94€</td>
    </tr>
    <tr>
      <td>2023-12-07</td>
      <td>10416.81€</td>
    </tr>
    <tr>
      <td>2023-12-06</td>
      <td>10300.2€</td>
    </tr>
    <tr>
      <td>2023-12-06</td>
      <td>10334.62€</td>
    </tr>
    <tr>
      <td>2023-11-22</td>
      <td>10427.2€</td>
    </tr>
    <tr>
      <td>2023-11-21</td>
      <td>10386.05€</td>
    </tr>
    <tr>
      <td>2023-11-20</td>
      <td>10414.2€</td>
    </tr>
    <tr>
      <td>2023-11-19</td>
      <td>10316.5€</td>
    </tr>
    <tr>
      <td>2023-11-16</td>
      <td>10322.52€</td>
    </tr>
    <tr>
      <td>2023-11-15</td>
      <td>10288.27€</td>
    </tr>
    <tr>
      <td>2023-11-14</td>
      <td>10281.85€</td>
    </tr>
    <tr>
      <td>2023-11-13</td>
      <td>10126.04€</td>
    </tr>
    <tr>
      <td>2023-11-12</td>
      <td>10134.9€</td>
    </tr>
    <tr>
      <td>2023-11-10</td>
      <td>10134.9€</td>
    </tr>
  </tbody>
</table>