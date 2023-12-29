---
date: "2023-12-29" # 2021-07-14
title: "static-vti-top50-replication"
image: "images/plots/static-vti-top50-replication.png"
author: "justin-guese"
draft: false
pctgain: 47
---

## Introduction to our strategy

jupyternotebooks/nasdaqreplicationtest.ipynb

## Quick Summary

<img src="/images/plots/static-vti-top50-replication.png" alt = "returns chart for static-vti-top50-replication" width="100%">

| Metric | Value |
| --- | --- |
| Return % p.a. | 47 |
| Days active | 48 |
| Starting capital | 10000 |
| Current capital | 10774.57€ |

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
      <td>AAPL</td>
      <td>7.758277</td>
      <td>192.26</td>
      <td>1491.61</td>
    </tr>
    <tr>
      <td>MSFT</td>
      <td>3.522106</td>
      <td>375.85</td>
      <td>1323.78</td>
    </tr>
    <tr>
      <td>AMZN</td>
      <td>4.050774</td>
      <td>152.37</td>
      <td>617.22</td>
    </tr>
    <tr>
      <td>NVDA</td>
      <td>1.121336</td>
      <td>496.41</td>
      <td>556.64</td>
    </tr>
    <tr>
      <td>META</td>
      <td>1.095656</td>
      <td>353.58</td>
      <td>387.40</td>
    </tr>
    <tr>
      <td>GOOGL</td>
      <td>2.756449</td>
      <td>139.50</td>
      <td>384.52</td>
    </tr>
    <tr>
      <td>TSLA</td>
      <td>1.360834</td>
      <td>250.63</td>
      <td>341.07</td>
    </tr>
    <tr>
      <td>GOOG</td>
      <td>2.297724</td>
      <td>140.74</td>
      <td>323.38</td>
    </tr>
    <tr>
      <td>USD</td>
      <td>293.004113</td>
      <td>1.00</td>
      <td>293.00</td>
    </tr>
    <tr>
      <td>JPM</td>
      <td>1.485662</td>
      <td>170.06</td>
      <td>252.65</td>
    </tr>
    <tr>
      <td>UNH</td>
      <td>0.458747</td>
      <td>525.44</td>
      <td>241.04</td>
    </tr>
    <tr>
      <td>AVGO</td>
      <td>0.205747</td>
      <td>1117.75</td>
      <td>229.97</td>
    </tr>
    <tr>
      <td>JNJ</td>
      <td>1.277291</td>
      <td>156.10</td>
      <td>199.39</td>
    </tr>
    <tr>
      <td>V</td>
      <td>0.727984</td>
      <td>260.42</td>
      <td>189.58</td>
    </tr>
    <tr>
      <td>LLY</td>
      <td>0.321152</td>
      <td>581.45</td>
      <td>186.73</td>
    </tr>
    <tr>
      <td>XOM</td>
      <td>1.753291</td>
      <td>99.79</td>
      <td>174.96</td>
    </tr>
    <tr>
      <td>PG</td>
      <td>1.132281</td>
      <td>146.08</td>
      <td>165.40</td>
    </tr>
    <tr>
      <td>HD</td>
      <td>0.476920</td>
      <td>344.61</td>
      <td>164.35</td>
    </tr>
    <tr>
      <td>MA</td>
      <td>0.375844</td>
      <td>425.94</td>
      <td>160.09</td>
    </tr>
    <tr>
      <td>COST</td>
      <td>0.211285</td>
      <td>659.23</td>
      <td>139.29</td>
    </tr>
    <tr>
      <td>ABBV</td>
      <td>0.845040</td>
      <td>154.47</td>
      <td>130.53</td>
    </tr>
    <tr>
      <td>MRK</td>
      <td>1.182639</td>
      <td>109.00</td>
      <td>128.91</td>
    </tr>
    <tr>
      <td>ADBE</td>
      <td>0.211450</td>
      <td>597.79</td>
      <td>126.40</td>
    </tr>
    <tr>
      <td>CVX</td>
      <td>0.818203</td>
      <td>149.23</td>
      <td>122.10</td>
    </tr>
    <tr>
      <td>BAC</td>
      <td>3.554639</td>
      <td>33.65</td>
      <td>119.61</td>
    </tr>
    <tr>
      <td>AMD</td>
      <td>0.804636</td>
      <td>148.43</td>
      <td>119.43</td>
    </tr>
    <tr>
      <td>CRM</td>
      <td>0.448545</td>
      <td>263.68</td>
      <td>118.27</td>
    </tr>
    <tr>
      <td>PEP</td>
      <td>0.683738</td>
      <td>169.50</td>
      <td>115.89</td>
    </tr>
    <tr>
      <td>KO</td>
      <td>1.897760</td>
      <td>58.76</td>
      <td>111.51</td>
    </tr>
    <tr>
      <td>WMT</td>
      <td>0.688223</td>
      <td>157.66</td>
      <td>108.51</td>
    </tr>
    <tr>
      <td>MCD</td>
      <td>0.365050</td>
      <td>296.32</td>
      <td>108.17</td>
    </tr>
    <tr>
      <td>NFLX</td>
      <td>0.205932</td>
      <td>485.76</td>
      <td>100.03</td>
    </tr>
    <tr>
      <td>ACN</td>
      <td>0.284184</td>
      <td>350.51</td>
      <td>99.61</td>
    </tr>
    <tr>
      <td>ABT</td>
      <td>0.892127</td>
      <td>110.01</td>
      <td>98.14</td>
    </tr>
    <tr>
      <td>TMO</td>
      <td>0.184133</td>
      <td>530.27</td>
      <td>97.64</td>
    </tr>
    <tr>
      <td>WFC</td>
      <td>1.962283</td>
      <td>49.26</td>
      <td>96.66</td>
    </tr>
    <tr>
      <td>LIN</td>
      <td>0.230139</td>
      <td>410.83</td>
      <td>94.55</td>
    </tr>
    <tr>
      <td>INTC</td>
      <td>1.857019</td>
      <td>50.42</td>
      <td>93.63</td>
    </tr>
    <tr>
      <td>QCOM</td>
      <td>0.634716</td>
      <td>144.93</td>
      <td>91.99</td>
    </tr>
    <tr>
      <td>CMCSA</td>
      <td>1.952098</td>
      <td>43.69</td>
      <td>85.29</td>
    </tr>
    <tr>
      <td>DIS</td>
      <td>0.940152</td>
      <td>90.32</td>
      <td>84.91</td>
    </tr>
    <tr>
      <td>BA</td>
      <td>0.311121</td>
      <td>260.57</td>
      <td>81.07</td>
    </tr>
    <tr>
      <td>PFE</td>
      <td>2.751531</td>
      <td>28.65</td>
      <td>78.83</td>
    </tr>
    <tr>
      <td>CSCO</td>
      <td>1.551841</td>
      <td>50.38</td>
      <td>78.18</td>
    </tr>
    <tr>
      <td>TXN</td>
      <td>0.457781</td>
      <td>170.46</td>
      <td>78.03</td>
    </tr>
    <tr>
      <td>nan</td>
      <td>6.603320</td>
      <td>10.92</td>
      <td>72.11</td>
    </tr>
    <tr>
      <td>DHR</td>
      <td>0.310417</td>
      <td>231.58</td>
      <td>71.89</td>
    </tr>
    <tr>
      <td>PM</td>
      <td>0.763062</td>
      <td>93.87</td>
      <td>71.63</td>
    </tr>
    <tr>
      <td>ORCL</td>
      <td>0.666759</td>
      <td>105.34</td>
      <td>70.24</td>
    </tr>
    <tr>
      <td>NEE</td>
      <td>1.049302</td>
      <td>60.31</td>
      <td>63.28</td>
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
      <td>0.06</td>
    </tr>
    <tr>
      <th>CAGR﹪</th>
      <td>0.4</td>
    </tr>
    <tr>
      <th>Sharpe</th>
      <td>5.33</td>
    </tr>
    <tr>
      <th>Prob. Sharpe Ratio</th>
      <td>0.97</td>
    </tr>
    <tr>
      <th>Sortino</th>
      <td>10.4</td>
    </tr>
    <tr>
      <th>Sortino/√2</th>
      <td>7.35</td>
    </tr>
    <tr>
      <th>Omega</th>
      <td>2.9</td>
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
      <td>1.9</td>
    </tr>
    <tr>
      <th>Gain/Pain (1M)</th>
      <td>-</td>
    </tr>
    <tr>
      <th>Payoff Ratio</th>
      <td>1.63</td>
    </tr>
    <tr>
      <th>Profit Factor</th>
      <td>2.9</td>
    </tr>
    <tr>
      <th>Common Sense Ratio</th>
      <td>5.63</td>
    </tr>
    <tr>
      <th>CPC Index</th>
      <td>3.03</td>
    </tr>
    <tr>
      <th>Tail Ratio</th>
      <td>1.94</td>
    </tr>
    <tr>
      <th>Outlier Win Ratio</th>
      <td>3.73</td>
    </tr>
    <tr>
      <th>Outlier Loss Ratio</th>
      <td>3.14</td>
    </tr>
    <tr>
      <th>MTD</th>
      <td>0.03</td>
    </tr>
    <tr>
      <th>3M</th>
      <td>0.06</td>
    </tr>
    <tr>
      <th>6M</th>
      <td>0.06</td>
    </tr>
    <tr>
      <th>YTD</th>
      <td>0.06</td>
    </tr>
    <tr>
      <th>1Y</th>
      <td>0.06</td>
    </tr>
    <tr>
      <th>3Y (ann.)</th>
      <td>0.4</td>
    </tr>
    <tr>
      <th>5Y (ann.)</th>
      <td>0.4</td>
    </tr>
    <tr>
      <th>10Y (ann.)</th>
      <td>0.4</td>
    </tr>
    <tr>
      <th>All-time (ann.)</th>
      <td>0.4</td>
    </tr>
    <tr>
      <th>Avg. Drawdown</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Avg. Drawdown Days</th>
      <td>2</td>
    </tr>
    <tr>
      <th>Recovery Factor</th>
      <td>4.93</td>
    </tr>
    <tr>
      <th>Ulcer Index</th>
      <td>0</td>
    </tr>
    <tr>
      <th>Serenity Index</th>
      <td>12.83</td>
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
      <td>10774.57€</td>
    </tr>
    <tr>
      <td>28.12.2023</td>
      <td>10776.34€</td>
    </tr>
    <tr>
      <td>27.12.2023</td>
      <td>10776.34€</td>
    </tr>
    <tr>
      <td>26.12.2023</td>
      <td>10763.29€</td>
    </tr>
    <tr>
      <td>25.12.2023</td>
      <td>10730.96€</td>
    </tr>
    <tr>
      <td>24.12.2023</td>
      <td>10730.96€</td>
    </tr>
    <tr>
      <td>23.12.2023</td>
      <td>10730.96€</td>
    </tr>
    <tr>
      <td>22.12.2023</td>
      <td>10730.96€</td>
    </tr>
    <tr>
      <td>21.12.2023</td>
      <td>10725.36€</td>
    </tr>
    <tr>
      <td>20.12.2023</td>
      <td>10628.57€</td>
    </tr>
    <tr>
      <td>19.12.2023</td>
      <td>10763.41€</td>
    </tr>
    <tr>
      <td>18.12.2023</td>
      <td>10715.02€</td>
    </tr>
    <tr>
      <td>17.12.2023</td>
      <td>10640.98€</td>
    </tr>
    <tr>
      <td>16.12.2023</td>
      <td>10640.98€</td>
    </tr>
    <tr>
      <td>15.12.2023</td>
      <td>10640.98€</td>
    </tr>
    <tr>
      <td>14.12.2023</td>
      <td>10594.14€</td>
    </tr>
    <tr>
      <td>13.12.2023</td>
      <td>10615.17€</td>
    </tr>
    <tr>
      <td>12.12.2023</td>
      <td>10513.81€</td>
    </tr>
    <tr>
      <td>11.12.2023</td>
      <td>10453.66€</td>
    </tr>
    <tr>
      <td>10.12.2023</td>
      <td>10468.94€</td>
    </tr>
    <tr>
      <td>09.12.2023</td>
      <td>10468.94€</td>
    </tr>
    <tr>
      <td>08.12.2023</td>
      <td>10468.94€</td>
    </tr>
    <tr>
      <td>07.12.2023</td>
      <td>10416.81€</td>
    </tr>
    <tr>
      <td>06.12.2023</td>
      <td>10300.2€</td>
    </tr>
    <tr>
      <td>06.12.2023</td>
      <td>10334.62€</td>
    </tr>
    <tr>
      <td>22.11.2023</td>
      <td>10427.2€</td>
    </tr>
    <tr>
      <td>21.11.2023</td>
      <td>10386.05€</td>
    </tr>
    <tr>
      <td>20.11.2023</td>
      <td>10414.2€</td>
    </tr>
    <tr>
      <td>19.11.2023</td>
      <td>10316.5€</td>
    </tr>
    <tr>
      <td>16.11.2023</td>
      <td>10322.52€</td>
    </tr>
    <tr>
      <td>15.11.2023</td>
      <td>10288.27€</td>
    </tr>
    <tr>
      <td>14.11.2023</td>
      <td>10281.85€</td>
    </tr>
    <tr>
      <td>13.11.2023</td>
      <td>10126.04€</td>
    </tr>
    <tr>
      <td>12.11.2023</td>
      <td>10134.9€</td>
    </tr>
    <tr>
      <td>10.11.2023</td>
      <td>10134.9€</td>
    </tr>
  </tbody>
</table>