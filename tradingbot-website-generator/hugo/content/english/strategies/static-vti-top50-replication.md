---
date: "2024-01-04" # 2021-07-14
title: "static-vti-top50-replication"
image: "images/plots/static-vti-top50-replication.png"
author: "justin-guese"
draft: false
pctgain: 29
---

## Introduction to our strategy

jupyternotebooks/nasdaqreplicationtest.ipynb

## Quick Summary

<img src="/images/plots/static-vti-top50-replication.png" alt = "returns chart for static-vti-top50-replication" width="100%">

| Metric | Value |
| --- | --- |
| Return % p.a. | 29 |
| Days active | 54 |
| Starting capital | 10000 |
| Current capital | 10579.6€ |

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
      <td>181.29</td>
      <td>1406.50</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/MSFT'>MSFT</a></td>
      <td>3.522106</td>
      <td>371.83</td>
      <td>1309.62</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/AMZN'>AMZN</a></td>
      <td>4.050774</td>
      <td>146.38</td>
      <td>592.95</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/NVDA'>NVDA</a></td>
      <td>1.121336</td>
      <td>480.04</td>
      <td>538.29</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/GOOGL'>GOOGL</a></td>
      <td>2.756449</td>
      <td>138.50</td>
      <td>381.77</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/META'>META</a></td>
      <td>1.095656</td>
      <td>344.56</td>
      <td>377.52</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/TSLA'>TSLA</a></td>
      <td>1.360834</td>
      <td>241.78</td>
      <td>329.02</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/GOOG'>GOOG</a></td>
      <td>2.297724</td>
      <td>139.96</td>
      <td>321.59</td>
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
      <td>172.82</td>
      <td>256.75</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/UNH'>UNH</a></td>
      <td>0.458747</td>
      <td>545.63</td>
      <td>250.31</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/AVGO'>AVGO</a></td>
      <td>0.205747</td>
      <td>1063.93</td>
      <td>218.90</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/JNJ'>JNJ</a></td>
      <td>1.277291</td>
      <td>161.14</td>
      <td>205.82</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/LLY'>LLY</a></td>
      <td>0.321152</td>
      <td>628.37</td>
      <td>201.80</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/V'>V</a></td>
      <td>0.727984</td>
      <td>260.27</td>
      <td>189.47</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/XOM'>XOM</a></td>
      <td>1.753291</td>
      <td>103.42</td>
      <td>181.33</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/PG'>PG</a></td>
      <td>1.132281</td>
      <td>149.02</td>
      <td>168.73</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/HD'>HD</a></td>
      <td>0.476920</td>
      <td>341.40</td>
      <td>162.82</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/MA'>MA</a></td>
      <td>0.375844</td>
      <td>422.40</td>
      <td>158.76</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/MRK'>MRK</a></td>
      <td>1.182639</td>
      <td>117.04</td>
      <td>138.42</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/ABBV'>ABBV</a></td>
      <td>0.845040</td>
      <td>161.63</td>
      <td>136.58</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/COST'>COST</a></td>
      <td>0.211285</td>
      <td>643.19</td>
      <td>135.90</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/CVX'>CVX</a></td>
      <td>0.818203</td>
      <td>152.45</td>
      <td>124.73</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/BAC'>BAC</a></td>
      <td>3.554639</td>
      <td>34.10</td>
      <td>121.21</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/ADBE'>ADBE</a></td>
      <td>0.211450</td>
      <td>570.97</td>
      <td>120.73</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/PEP'>PEP</a></td>
      <td>0.683738</td>
      <td>173.13</td>
      <td>118.38</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/KO'>KO</a></td>
      <td>1.897760</td>
      <td>60.06</td>
      <td>113.98</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/CRM'>CRM</a></td>
      <td>0.448545</td>
      <td>251.78</td>
      <td>112.93</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/AMD'>AMD</a></td>
      <td>0.804636</td>
      <td>136.50</td>
      <td>109.83</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/WMT'>WMT</a></td>
      <td>0.688223</td>
      <td>158.61</td>
      <td>109.16</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/MCD'>MCD</a></td>
      <td>0.365050</td>
      <td>295.39</td>
      <td>107.83</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/ABT'>ABT</a></td>
      <td>0.892127</td>
      <td>110.75</td>
      <td>98.80</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/TMO'>TMO</a></td>
      <td>0.184133</td>
      <td>535.77</td>
      <td>98.65</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/NFLX'>NFLX</a></td>
      <td>0.205932</td>
      <td>473.71</td>
      <td>97.55</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/WFC'>WFC</a></td>
      <td>1.962283</td>
      <td>49.68</td>
      <td>97.49</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/ACN'>ACN</a></td>
      <td>0.284184</td>
      <td>338.71</td>
      <td>96.26</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/LIN'>LIN</a></td>
      <td>0.230139</td>
      <td>410.04</td>
      <td>94.37</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/INTC'>INTC</a></td>
      <td>1.857019</td>
      <td>46.94</td>
      <td>87.17</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/QCOM'>QCOM</a></td>
      <td>0.634716</td>
      <td>136.56</td>
      <td>86.68</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/DIS'>DIS</a></td>
      <td>0.940152</td>
      <td>90.28</td>
      <td>84.88</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/CMCSA'>CMCSA</a></td>
      <td>1.952098</td>
      <td>42.72</td>
      <td>83.39</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/PFE'>PFE</a></td>
      <td>2.751531</td>
      <td>29.22</td>
      <td>80.40</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/CSCO'>CSCO</a></td>
      <td>1.551841</td>
      <td>50.08</td>
      <td>77.72</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/BA'>BA</a></td>
      <td>0.311121</td>
      <td>247.65</td>
      <td>77.05</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/TXN'>TXN</a></td>
      <td>0.457781</td>
      <td>164.63</td>
      <td>75.36</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/PM'>PM</a></td>
      <td>0.763062</td>
      <td>96.67</td>
      <td>73.77</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/nan'>nan</a></td>
      <td>6.603320</td>
      <td>11.06</td>
      <td>73.03</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/DHR'>DHR</a></td>
      <td>0.310417</td>
      <td>231.68</td>
      <td>71.92</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/ORCL'>ORCL</a></td>
      <td>0.666759</td>
      <td>103.00</td>
      <td>68.68</td>
    </tr>
    <tr>
      <td><a target='_blank' href='https://finance.yahoo.com/quote/NEE'>NEE</a></td>
      <td>1.049302</td>
      <td>62.50</td>
      <td>65.58</td>
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
      <td>0.04</td>
    </tr>
    <tr>
      <th>CAGR﹪</th>
      <td>0.23</td>
    </tr>
    <tr>
      <th>Sharpe</th>
      <td>3.16</td>
    </tr>
    <tr>
      <th>Prob. Sharpe Ratio</th>
      <td>0.9</td>
    </tr>
    <tr>
      <th>Sortino</th>
      <td>5.48</td>
    </tr>
    <tr>
      <th>Sortino/√2</th>
      <td>3.88</td>
    </tr>
    <tr>
      <th>Omega</th>
      <td>1.86</td>
    </tr>
    <tr>
      <th>Max Drawdown</th>
      <td>-0.02</td>
    </tr>
    <tr>
      <th>Longest DD Days</th>
      <td>7</td>
    </tr>
    <tr>
      <th>Gain/Pain Ratio</th>
      <td>0.86</td>
    </tr>
    <tr>
      <th>Gain/Pain (1M)</th>
      <td>2.86</td>
    </tr>
    <tr>
      <th>Payoff Ratio</th>
      <td>1.39</td>
    </tr>
    <tr>
      <th>Profit Factor</th>
      <td>1.86</td>
    </tr>
    <tr>
      <th>Common Sense Ratio</th>
      <td>2.02</td>
    </tr>
    <tr>
      <th>CPC Index</th>
      <td>1.48</td>
    </tr>
    <tr>
      <th>Tail Ratio</th>
      <td>1.09</td>
    </tr>
    <tr>
      <th>Outlier Win Ratio</th>
      <td>4.1</td>
    </tr>
    <tr>
      <th>Outlier Loss Ratio</th>
      <td>2.73</td>
    </tr>
    <tr>
      <th>MTD</th>
      <td>-0.02</td>
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
      <td>-0.02</td>
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
      <td>3</td>
    </tr>
    <tr>
      <th>Recovery Factor</th>
      <td>2.39</td>
    </tr>
    <tr>
      <th>Ulcer Index</th>
      <td>0.01</td>
    </tr>
    <tr>
      <th>Serenity Index</th>
      <td>4.88</td>
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
      <td>10579.6€</td>
    </tr>
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