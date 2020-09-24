
# Data Science for Geoscience

Let's use some standard Machine Learning tools available in Python packages to analyse some data.

We have a dataset (from Butterworth et al 2016) with a collection of tectonomagmatic parameters associated with the time and location of porphyry copper deposits. We want to determine which of these (if any) parameters are geologically important (or at least statistically significant) in relation to the formation of porphyry coppers.

Run the next cell to see an animation representing this data


![SegmentLocal](../data/MullerConvergenceSmall.gif "segment")

### Now, import most of the modules we need
By convention module loads go at the top of your workflows.


```python
import pandas #For dealing with data structures
import numpy as np #Data array manipulation
import scipy #Scientific Python, has lots of useful tools
import scipy.io #A specific sub-module for input/output of sci data

#scikit-learn tools to perform machine learning classification
#from sklearn import cross_validation
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing

#For making pretty figures
import matplotlib.pyplot as plt 

#For easy geographic projections on a map
import cartopy.crs as ccrs

#Import a set of tools we have made ourselves
from utils import *
```

    /usr/local/lib/python2.7/dist-packages/sklearn/ensemble/weight_boosting.py:29: DeprecationWarning: numpy.core.umath_tests is an internal NumPy module and should not be imported. It will be removed in a future NumPy release.
      from numpy.core.umath_tests import inner1d



    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-1-f32d98093359> in <module>()
         16 
         17 #For easy geographic projections on a map
    ---> 18 import cartopy.crs as ccrs
         19 
         20 #Import a set of tools we have made ourselves


    ImportError: No module named cartopy.crs


### Now load in the data


```python
#Use pandas to load in the machine learning dataset
ml_data=pandas.read_csv("../data/ml_data_points.csv",index_col=0)
```


```python
#Print out the dataset so we can see what it looks like
ml_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0 Present day longitude (degrees)</th>
      <th>1 Present day latitude (degrees)</th>
      <th>2 Reconstructed longitude (degrees)</th>
      <th>3 Reconstructed latitude (degrees)</th>
      <th>4 Age (Ma)</th>
      <th>5 Time before mineralisation (Myr)</th>
      <th>6 Seafloor age (Myr)</th>
      <th>7 Segment length (km)</th>
      <th>8 Slab length (km)</th>
      <th>9 Distance to trench edge (km)</th>
      <th>...</th>
      <th>11 Subducting plate parallel velocity (km/Myr)</th>
      <th>12 Overriding plate normal velocity (km/Myr)</th>
      <th>13 Overriding plate parallel velocity (km/Myr)</th>
      <th>14 Convergence normal rate (km/Myr)</th>
      <th>15 Convergence parallel rate (km/Myr)</th>
      <th>16 Subduction polarity (degrees)</th>
      <th>17 Subduction obliquity (degrees)</th>
      <th>18 Distance along margin (km)</th>
      <th>19 Subduction obliquity signed (radians)</th>
      <th>20 Ore Deposits Binary Flag (1 or 0)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-66.28</td>
      <td>-27.37</td>
      <td>-65.264812</td>
      <td>-28.103781</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>48.189707</td>
      <td>56.08069</td>
      <td>2436.30907</td>
      <td>2436.30907</td>
      <td>...</td>
      <td>40.63020</td>
      <td>-17.43987</td>
      <td>12.20271</td>
      <td>102.31471</td>
      <td>28.82518</td>
      <td>5.67505</td>
      <td>15.73415</td>
      <td>2269.19769</td>
      <td>0.274613</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-69.75</td>
      <td>-30.50</td>
      <td>-67.696759</td>
      <td>-31.970639</td>
      <td>12.0</td>
      <td>0.0</td>
      <td>52.321162</td>
      <td>56.09672</td>
      <td>2490.68735</td>
      <td>2490.68735</td>
      <td>...</td>
      <td>39.60199</td>
      <td>-22.80622</td>
      <td>13.40127</td>
      <td>115.35820</td>
      <td>27.39401</td>
      <td>5.78937</td>
      <td>13.35854</td>
      <td>1823.34107</td>
      <td>0.233151</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-66.65</td>
      <td>-27.27</td>
      <td>-65.128689</td>
      <td>-28.374772</td>
      <td>9.0</td>
      <td>0.0</td>
      <td>53.506085</td>
      <td>55.77705</td>
      <td>2823.54951</td>
      <td>2823.54951</td>
      <td>...</td>
      <td>45.32425</td>
      <td>-18.08485</td>
      <td>11.27500</td>
      <td>100.24282</td>
      <td>34.62444</td>
      <td>8.97218</td>
      <td>19.05520</td>
      <td>2269.19769</td>
      <td>0.332576</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-66.61</td>
      <td>-27.33</td>
      <td>-65.257928</td>
      <td>-28.311094</td>
      <td>8.0</td>
      <td>0.0</td>
      <td>51.317135</td>
      <td>55.90088</td>
      <td>2656.71724</td>
      <td>2656.71724</td>
      <td>...</td>
      <td>43.13319</td>
      <td>-17.78538</td>
      <td>11.72618</td>
      <td>101.21965</td>
      <td>31.92962</td>
      <td>7.42992</td>
      <td>17.50782</td>
      <td>2269.19769</td>
      <td>0.305569</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-66.55</td>
      <td>-27.40</td>
      <td>-65.366917</td>
      <td>-28.257580</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>49.340097</td>
      <td>56.09011</td>
      <td>2547.29585</td>
      <td>2547.29585</td>
      <td>...</td>
      <td>40.57322</td>
      <td>-17.43622</td>
      <td>12.23778</td>
      <td>102.25748</td>
      <td>28.80235</td>
      <td>5.65657</td>
      <td>15.73067</td>
      <td>2269.19769</td>
      <td>0.274552</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-66.57</td>
      <td>-27.28</td>
      <td>-65.217784</td>
      <td>-28.260958</td>
      <td>8.0</td>
      <td>0.0</td>
      <td>51.466451</td>
      <td>55.90088</td>
      <td>2656.71724</td>
      <td>2656.71724</td>
      <td>...</td>
      <td>43.13319</td>
      <td>-17.78538</td>
      <td>11.72618</td>
      <td>101.21965</td>
      <td>31.92962</td>
      <td>7.42992</td>
      <td>17.50782</td>
      <td>2269.19769</td>
      <td>0.305569</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-67.90</td>
      <td>-26.30</td>
      <td>-65.391160</td>
      <td>-28.036212</td>
      <td>14.0</td>
      <td>0.0</td>
      <td>59.705229</td>
      <td>56.14614</td>
      <td>2937.75395</td>
      <td>2937.75395</td>
      <td>...</td>
      <td>39.41149</td>
      <td>-23.26852</td>
      <td>13.45193</td>
      <td>116.11452</td>
      <td>27.28535</td>
      <td>5.46709</td>
      <td>13.22382</td>
      <td>2325.21126</td>
      <td>0.230799</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>-70.58</td>
      <td>-38.25</td>
      <td>-44.673534</td>
      <td>-42.077290</td>
      <td>85.0</td>
      <td>0.0</td>
      <td>12.269256</td>
      <td>55.39199</td>
      <td>2151.81813</td>
      <td>2151.81813</td>
      <td>...</td>
      <td>54.37230</td>
      <td>-64.95285</td>
      <td>1.30871</td>
      <td>78.24529</td>
      <td>41.27280</td>
      <td>15.23262</td>
      <td>27.81074</td>
      <td>1051.14453</td>
      <td>0.485389</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>-70.05</td>
      <td>-31.95</td>
      <td>-67.762375</td>
      <td>-33.560754</td>
      <td>13.0</td>
      <td>0.0</td>
      <td>52.536887</td>
      <td>56.09528</td>
      <td>2322.50643</td>
      <td>2322.50643</td>
      <td>...</td>
      <td>39.04452</td>
      <td>-22.55457</td>
      <td>13.52329</td>
      <td>115.01528</td>
      <td>26.79653</td>
      <td>5.64144</td>
      <td>13.11495</td>
      <td>1655.41651</td>
      <td>0.228899</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>-66.60</td>
      <td>-24.13</td>
      <td>-64.317484</td>
      <td>-25.721047</td>
      <td>13.0</td>
      <td>0.0</td>
      <td>60.362977</td>
      <td>56.15019</td>
      <td>3218.30664</td>
      <td>3218.30664</td>
      <td>...</td>
      <td>40.05359</td>
      <td>-23.55670</td>
      <td>13.30724</td>
      <td>116.18280</td>
      <td>27.99456</td>
      <td>5.64018</td>
      <td>13.54734</td>
      <td>2549.28917</td>
      <td>0.236446</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>-70.45</td>
      <td>-31.76</td>
      <td>-68.784462</td>
      <td>-33.002423</td>
      <td>10.0</td>
      <td>0.0</td>
      <td>45.120041</td>
      <td>56.07589</td>
      <td>2322.36788</td>
      <td>2322.36788</td>
      <td>...</td>
      <td>39.93994</td>
      <td>-16.74080</td>
      <td>12.40009</td>
      <td>100.67874</td>
      <td>28.22672</td>
      <td>5.74423</td>
      <td>15.66160</td>
      <td>1711.38826</td>
      <td>0.273346</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>-66.22</td>
      <td>-27.38</td>
      <td>-65.204374</td>
      <td>-28.113628</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>48.306817</td>
      <td>56.08069</td>
      <td>2436.30907</td>
      <td>2436.30907</td>
      <td>...</td>
      <td>40.63020</td>
      <td>-17.43987</td>
      <td>12.20271</td>
      <td>102.31471</td>
      <td>28.82518</td>
      <td>5.67505</td>
      <td>15.73415</td>
      <td>2269.19769</td>
      <td>0.274613</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>-66.76</td>
      <td>-25.14</td>
      <td>-64.016998</td>
      <td>-27.003955</td>
      <td>15.0</td>
      <td>0.0</td>
      <td>62.129534</td>
      <td>56.16073</td>
      <td>3106.42087</td>
      <td>3106.42087</td>
      <td>...</td>
      <td>39.39617</td>
      <td>-23.42293</td>
      <td>13.43823</td>
      <td>116.24982</td>
      <td>27.35698</td>
      <td>5.48309</td>
      <td>13.24243</td>
      <td>2437.24556</td>
      <td>0.231124</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>-67.75</td>
      <td>-29.00</td>
      <td>-67.077600</td>
      <td>-29.490617</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>43.574875</td>
      <td>55.58629</td>
      <td>2102.41843</td>
      <td>2102.41843</td>
      <td>...</td>
      <td>49.33884</td>
      <td>-18.97616</td>
      <td>9.25569</td>
      <td>83.52876</td>
      <td>40.42652</td>
      <td>14.89147</td>
      <td>25.82620</td>
      <td>2101.98857</td>
      <td>0.450752</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>-65.87</td>
      <td>-24.20</td>
      <td>-63.123395</td>
      <td>-26.056066</td>
      <td>15.0</td>
      <td>0.0</td>
      <td>63.266054</td>
      <td>56.16512</td>
      <td>3218.74892</td>
      <td>3218.74892</td>
      <td>...</td>
      <td>39.54822</td>
      <td>-23.52480</td>
      <td>13.39993</td>
      <td>116.27368</td>
      <td>27.54669</td>
      <td>5.52920</td>
      <td>13.32835</td>
      <td>2605.31534</td>
      <td>0.232624</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>-69.08</td>
      <td>-32.42</td>
      <td>-66.537432</td>
      <td>-34.163909</td>
      <td>14.0</td>
      <td>0.0</td>
      <td>55.833021</td>
      <td>56.10011</td>
      <td>2266.50887</td>
      <td>2266.50887</td>
      <td>...</td>
      <td>38.68944</td>
      <td>-22.46223</td>
      <td>13.59475</td>
      <td>114.88423</td>
      <td>26.44916</td>
      <td>5.55528</td>
      <td>12.96498</td>
      <td>1655.41651</td>
      <td>0.226282</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>-69.10</td>
      <td>-32.48</td>
      <td>-66.557288</td>
      <td>-34.224035</td>
      <td>14.0</td>
      <td>0.0</td>
      <td>55.698374</td>
      <td>56.10011</td>
      <td>2266.50887</td>
      <td>2266.50887</td>
      <td>...</td>
      <td>38.68944</td>
      <td>-22.46223</td>
      <td>13.59475</td>
      <td>114.88423</td>
      <td>26.44916</td>
      <td>5.55528</td>
      <td>12.96498</td>
      <td>1599.44790</td>
      <td>0.226282</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>-70.47</td>
      <td>-37.43</td>
      <td>-59.678626</td>
      <td>-42.444274</td>
      <td>45.0</td>
      <td>0.0</td>
      <td>33.873716</td>
      <td>59.02215</td>
      <td>2898.37931</td>
      <td>2898.37931</td>
      <td>...</td>
      <td>47.91525</td>
      <td>-23.22106</td>
      <td>13.76089</td>
      <td>46.73662</td>
      <td>16.26397</td>
      <td>19.13779</td>
      <td>19.18749</td>
      <td>1160.83787</td>
      <td>0.334885</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>-69.97</td>
      <td>-32.57</td>
      <td>-68.463093</td>
      <td>-33.685779</td>
      <td>9.0</td>
      <td>0.0</td>
      <td>42.654362</td>
      <td>56.06216</td>
      <td>2208.83713</td>
      <td>2208.83713</td>
      <td>...</td>
      <td>39.85835</td>
      <td>-16.61112</td>
      <td>12.39474</td>
      <td>100.48606</td>
      <td>28.08351</td>
      <td>5.71419</td>
      <td>15.61444</td>
      <td>1599.44790</td>
      <td>0.272523</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>-67.78</td>
      <td>-24.57</td>
      <td>-61.593566</td>
      <td>-28.340027</td>
      <td>29.0</td>
      <td>0.0</td>
      <td>62.586817</td>
      <td>56.27662</td>
      <td>3166.34885</td>
      <td>3166.34885</td>
      <td>...</td>
      <td>61.34638</td>
      <td>-26.29743</td>
      <td>13.51042</td>
      <td>80.21046</td>
      <td>42.83765</td>
      <td>4.55219</td>
      <td>28.10514</td>
      <td>2493.26622</td>
      <td>0.490527</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>-67.73</td>
      <td>-24.58</td>
      <td>-61.018469</td>
      <td>-28.503875</td>
      <td>31.0</td>
      <td>0.0</td>
      <td>60.707044</td>
      <td>56.28771</td>
      <td>3167.03056</td>
      <td>3167.03056</td>
      <td>...</td>
      <td>49.19831</td>
      <td>-25.66768</td>
      <td>0.93397</td>
      <td>79.70314</td>
      <td>42.80777</td>
      <td>4.35778</td>
      <td>28.23981</td>
      <td>2493.26622</td>
      <td>0.492878</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>-67.48</td>
      <td>-16.92</td>
      <td>-63.003008</td>
      <td>-19.875412</td>
      <td>23.0</td>
      <td>0.0</td>
      <td>69.678543</td>
      <td>54.87570</td>
      <td>3669.27017</td>
      <td>2439.17729</td>
      <td>...</td>
      <td>-17.66982</td>
      <td>-15.04259</td>
      <td>25.69831</td>
      <td>123.85464</td>
      <td>-42.57782</td>
      <td>-28.38757</td>
      <td>18.97156</td>
      <td>3050.40547</td>
      <td>-0.331116</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>-66.60</td>
      <td>-18.44</td>
      <td>-62.578351</td>
      <td>-21.113117</td>
      <td>21.0</td>
      <td>0.0</td>
      <td>70.534838</td>
      <td>55.66454</td>
      <td>3612.54939</td>
      <td>2605.14028</td>
      <td>...</td>
      <td>-1.89420</td>
      <td>-18.20578</td>
      <td>22.96976</td>
      <td>127.97605</td>
      <td>-23.93471</td>
      <td>-20.98566</td>
      <td>10.59336</td>
      <td>2995.47045</td>
      <td>-0.184889</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>-65.75</td>
      <td>-19.63</td>
      <td>-63.714471</td>
      <td>-21.080676</td>
      <td>12.0</td>
      <td>0.0</td>
      <td>60.823598</td>
      <td>55.50303</td>
      <td>3553.42217</td>
      <td>2882.78329</td>
      <td>...</td>
      <td>19.89490</td>
      <td>-20.45905</td>
      <td>17.94159</td>
      <td>119.42524</td>
      <td>3.14439</td>
      <td>-6.44167</td>
      <td>1.50821</td>
      <td>2939.82516</td>
      <td>0.026323</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>-66.45</td>
      <td>-20.95</td>
      <td>-64.190695</td>
      <td>-22.540135</td>
      <td>13.0</td>
      <td>0.0</td>
      <td>61.020386</td>
      <td>55.99733</td>
      <td>3442.22422</td>
      <td>2994.38907</td>
      <td>...</td>
      <td>10.50674</td>
      <td>-18.64111</td>
      <td>19.77099</td>
      <td>119.25076</td>
      <td>-8.00946</td>
      <td>-11.80177</td>
      <td>3.84249</td>
      <td>2772.84261</td>
      <td>-0.067064</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>-66.03</td>
      <td>-20.91</td>
      <td>-63.098522</td>
      <td>-22.903052</td>
      <td>16.0</td>
      <td>0.0</td>
      <td>65.871092</td>
      <td>56.00428</td>
      <td>3442.98002</td>
      <td>2995.02556</td>
      <td>...</td>
      <td>35.35649</td>
      <td>-18.54939</td>
      <td>19.88665</td>
      <td>124.00639</td>
      <td>18.44845</td>
      <td>-11.96498</td>
      <td>8.46184</td>
      <td>2772.84261</td>
      <td>0.147687</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>-66.00</td>
      <td>-18.70</td>
      <td>-61.712000</td>
      <td>-21.495872</td>
      <td>22.0</td>
      <td>0.0</td>
      <td>70.013126</td>
      <td>55.67032</td>
      <td>3613.52796</td>
      <td>2493.41553</td>
      <td>...</td>
      <td>-3.51536</td>
      <td>-18.22077</td>
      <td>23.52746</td>
      <td>128.19400</td>
      <td>-26.40642</td>
      <td>-21.05913</td>
      <td>11.63944</td>
      <td>2939.82516</td>
      <td>-0.203147</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>-66.79</td>
      <td>-18.14</td>
      <td>-63.024231</td>
      <td>-20.686871</td>
      <td>20.0</td>
      <td>0.0</td>
      <td>70.395841</td>
      <td>55.65934</td>
      <td>3611.66084</td>
      <td>2716.87097</td>
      <td>...</td>
      <td>16.86624</td>
      <td>-15.21540</td>
      <td>22.64065</td>
      <td>124.51078</td>
      <td>-2.43651</td>
      <td>-20.92246</td>
      <td>1.12106</td>
      <td>2995.47045</td>
      <td>-0.019566</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>-67.13</td>
      <td>-17.95</td>
      <td>-64.464057</td>
      <td>-19.817416</td>
      <td>15.0</td>
      <td>0.0</td>
      <td>63.034120</td>
      <td>55.66864</td>
      <td>3609.80078</td>
      <td>2827.69707</td>
      <td>...</td>
      <td>-5.47972</td>
      <td>-15.40119</td>
      <td>22.47903</td>
      <td>116.43995</td>
      <td>-26.62963</td>
      <td>-20.63831</td>
      <td>12.88192</td>
      <td>2995.47045</td>
      <td>-0.224832</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>-66.19</td>
      <td>-20.63</td>
      <td>-63.264040</td>
      <td>-22.624688</td>
      <td>16.0</td>
      <td>0.0</td>
      <td>65.666169</td>
      <td>56.00428</td>
      <td>3442.98002</td>
      <td>2995.02556</td>
      <td>...</td>
      <td>35.35649</td>
      <td>-18.54939</td>
      <td>19.88665</td>
      <td>124.00639</td>
      <td>18.44845</td>
      <td>-11.96498</td>
      <td>8.46184</td>
      <td>2828.75256</td>
      <td>0.147687</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>271</th>
      <td>-72.33</td>
      <td>-14.03</td>
      <td>-43.973999</td>
      <td>-18.605999</td>
      <td>90.0</td>
      <td>0.0</td>
      <td>46.965004</td>
      <td>53.81943</td>
      <td>53.81943</td>
      <td>53.81943</td>
      <td>...</td>
      <td>-15.07089</td>
      <td>-26.55968</td>
      <td>55.56235</td>
      <td>87.66024</td>
      <td>-75.30167</td>
      <td>-48.12510</td>
      <td>40.66315</td>
      <td>3432.78105</td>
      <td>-0.709706</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>272</th>
      <td>-71.36</td>
      <td>-16.77</td>
      <td>-63.446365</td>
      <td>-20.873889</td>
      <td>37.0</td>
      <td>0.0</td>
      <td>63.103498</td>
      <td>54.00632</td>
      <td>3833.23989</td>
      <td>2616.14510</td>
      <td>...</td>
      <td>-2.73216</td>
      <td>-18.46188</td>
      <td>20.28154</td>
      <td>30.01335</td>
      <td>-26.40449</td>
      <td>-45.88406</td>
      <td>41.33996</td>
      <td>3214.72056</td>
      <td>-0.721519</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>273</th>
      <td>-75.42</td>
      <td>-14.23</td>
      <td>-42.093183</td>
      <td>-16.444555</td>
      <td>169.0</td>
      <td>0.0</td>
      <td>31.178453</td>
      <td>55.06338</td>
      <td>1763.02133</td>
      <td>1763.02133</td>
      <td>...</td>
      <td>-4.12849</td>
      <td>-25.32762</td>
      <td>-11.14276</td>
      <td>48.87657</td>
      <td>-6.27320</td>
      <td>-36.76600</td>
      <td>7.31381</td>
      <td>3761.82099</td>
      <td>-0.127650</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>274</th>
      <td>-71.77</td>
      <td>-14.46</td>
      <td>-38.455216</td>
      <td>-21.454514</td>
      <td>147.0</td>
      <td>0.0</td>
      <td>18.810909</td>
      <td>53.08568</td>
      <td>378.68849</td>
      <td>378.68849</td>
      <td>...</td>
      <td>-8.02954</td>
      <td>15.55851</td>
      <td>-1.69346</td>
      <td>2.24631</td>
      <td>-23.67182</td>
      <td>-45.18213</td>
      <td>84.57921</td>
      <td>3378.69739</td>
      <td>-1.476186</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>275</th>
      <td>-71.26</td>
      <td>-14.95</td>
      <td>-65.424596</td>
      <td>-18.803204</td>
      <td>29.0</td>
      <td>0.0</td>
      <td>66.512280</td>
      <td>54.29476</td>
      <td>3994.37798</td>
      <td>2450.87623</td>
      <td>...</td>
      <td>-10.22916</td>
      <td>-6.43554</td>
      <td>29.13501</td>
      <td>91.28271</td>
      <td>-39.13317</td>
      <td>-45.46711</td>
      <td>23.20496</td>
      <td>3378.69739</td>
      <td>-0.405003</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>276</th>
      <td>-72.35</td>
      <td>-14.18</td>
      <td>-43.988093</td>
      <td>-18.756658</td>
      <td>90.0</td>
      <td>0.0</td>
      <td>47.272459</td>
      <td>53.81943</td>
      <td>53.81943</td>
      <td>53.81943</td>
      <td>...</td>
      <td>-15.07089</td>
      <td>-26.55968</td>
      <td>55.56235</td>
      <td>87.66024</td>
      <td>-75.30167</td>
      <td>-48.12510</td>
      <td>40.66315</td>
      <td>3432.78105</td>
      <td>-0.709706</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>277</th>
      <td>-70.71</td>
      <td>-17.05</td>
      <td>-39.999078</td>
      <td>-21.770647</td>
      <td>96.0</td>
      <td>0.0</td>
      <td>36.007148</td>
      <td>54.08174</td>
      <td>162.04490</td>
      <td>162.04490</td>
      <td>...</td>
      <td>36.47226</td>
      <td>-24.72799</td>
      <td>28.69589</td>
      <td>70.52321</td>
      <td>-2.45706</td>
      <td>-42.31875</td>
      <td>1.99540</td>
      <td>3160.06366</td>
      <td>-0.034826</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>278</th>
      <td>-70.70</td>
      <td>-17.04</td>
      <td>-36.875265</td>
      <td>-18.309643</td>
      <td>175.0</td>
      <td>0.0</td>
      <td>22.559148</td>
      <td>54.60965</td>
      <td>1218.84018</td>
      <td>1218.84018</td>
      <td>...</td>
      <td>-6.35767</td>
      <td>-26.33537</td>
      <td>-11.75503</td>
      <td>44.23328</td>
      <td>-10.67498</td>
      <td>-37.79588</td>
      <td>13.56796</td>
      <td>3160.06366</td>
      <td>-0.236806</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>279</th>
      <td>-78.32</td>
      <td>-7.02</td>
      <td>-43.242999</td>
      <td>-6.841283</td>
      <td>179.0</td>
      <td>0.0</td>
      <td>49.611590</td>
      <td>55.89641</td>
      <td>2711.85305</td>
      <td>1596.86159</td>
      <td>...</td>
      <td>13.32404</td>
      <td>-17.25388</td>
      <td>-18.84225</td>
      <td>65.67124</td>
      <td>7.99437</td>
      <td>-16.94379</td>
      <td>6.94065</td>
      <td>4708.08568</td>
      <td>0.121137</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>280</th>
      <td>-75.72</td>
      <td>-13.77</td>
      <td>-64.757482</td>
      <td>-19.539486</td>
      <td>50.0</td>
      <td>0.0</td>
      <td>60.354944</td>
      <td>58.46944</td>
      <td>5341.43760</td>
      <td>2034.25548</td>
      <td>...</td>
      <td>-42.53647</td>
      <td>-14.06479</td>
      <td>20.04088</td>
      <td>32.87906</td>
      <td>-69.20025</td>
      <td>-45.08501</td>
      <td>64.58624</td>
      <td>3816.97543</td>
      <td>-1.127243</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>281</th>
      <td>-79.12</td>
      <td>-6.36</td>
      <td>-78.028544</td>
      <td>-7.233651</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>30.223936</td>
      <td>56.09074</td>
      <td>5098.42994</td>
      <td>1116.94233</td>
      <td>...</td>
      <td>-7.45933</td>
      <td>-10.83602</td>
      <td>19.18249</td>
      <td>100.85991</td>
      <td>-26.02532</td>
      <td>-21.14447</td>
      <td>14.46867</td>
      <td>4764.10346</td>
      <td>-0.252526</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>282</th>
      <td>-78.58</td>
      <td>-7.12</td>
      <td>-54.564071</td>
      <td>-10.564834</td>
      <td>82.0</td>
      <td>0.0</td>
      <td>46.648170</td>
      <td>56.03899</td>
      <td>4197.66197</td>
      <td>2420.33906</td>
      <td>...</td>
      <td>66.11676</td>
      <td>-48.49003</td>
      <td>25.75732</td>
      <td>7.78757</td>
      <td>7.08388</td>
      <td>-18.11125</td>
      <td>42.29089</td>
      <td>4708.08568</td>
      <td>0.738115</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>283</th>
      <td>-72.99</td>
      <td>-14.46</td>
      <td>-42.501592</td>
      <td>-19.314625</td>
      <td>96.0</td>
      <td>0.0</td>
      <td>34.747511</td>
      <td>53.95757</td>
      <td>483.14517</td>
      <td>483.14517</td>
      <td>...</td>
      <td>26.56462</td>
      <td>-20.47556</td>
      <td>31.77166</td>
      <td>73.55263</td>
      <td>-11.76329</td>
      <td>-49.13269</td>
      <td>9.08638</td>
      <td>3432.78105</td>
      <td>-0.158587</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>284</th>
      <td>-73.13</td>
      <td>-14.16</td>
      <td>-35.160915</td>
      <td>-19.965081</td>
      <td>123.0</td>
      <td>0.0</td>
      <td>22.253615</td>
      <td>53.84601</td>
      <td>107.62515</td>
      <td>107.62515</td>
      <td>...</td>
      <td>-38.12518</td>
      <td>18.16685</td>
      <td>11.40468</td>
      <td>-27.67412</td>
      <td>-62.81134</td>
      <td>-46.19560</td>
      <td>66.22213</td>
      <td>3596.62819</td>
      <td>1.155794</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>285</th>
      <td>-76.14</td>
      <td>-12.98</td>
      <td>-75.197205</td>
      <td>-13.727852</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>41.334070</td>
      <td>55.20179</td>
      <td>4094.22610</td>
      <td>2010.73060</td>
      <td>...</td>
      <td>-42.36006</td>
      <td>-2.10172</td>
      <td>21.74221</td>
      <td>85.32352</td>
      <td>-63.76019</td>
      <td>-44.79865</td>
      <td>36.76987</td>
      <td>3872.17329</td>
      <td>-0.641755</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>286</th>
      <td>-77.77</td>
      <td>-8.22</td>
      <td>-48.726438</td>
      <td>-13.155596</td>
      <td>93.0</td>
      <td>0.0</td>
      <td>38.620709</td>
      <td>55.55865</td>
      <td>1200.29926</td>
      <td>1200.29926</td>
      <td>...</td>
      <td>4.17427</td>
      <td>-26.30695</td>
      <td>26.28761</td>
      <td>93.72629</td>
      <td>-39.71580</td>
      <td>-34.25660</td>
      <td>22.96443</td>
      <td>4484.40640</td>
      <td>-0.400805</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>287</th>
      <td>-78.32</td>
      <td>-7.30</td>
      <td>-67.977716</td>
      <td>-13.022918</td>
      <td>48.0</td>
      <td>0.0</td>
      <td>69.251599</td>
      <td>60.28450</td>
      <td>6235.12889</td>
      <td>1139.07589</td>
      <td>...</td>
      <td>5.58162</td>
      <td>-18.62962</td>
      <td>26.52718</td>
      <td>99.89145</td>
      <td>-30.40923</td>
      <td>-21.41626</td>
      <td>16.93144</td>
      <td>4652.07599</td>
      <td>-0.295509</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>288</th>
      <td>-78.36</td>
      <td>-6.91</td>
      <td>-65.683900</td>
      <td>-11.386309</td>
      <td>54.0</td>
      <td>0.0</td>
      <td>67.663673</td>
      <td>59.81299</td>
      <td>6244.18194</td>
      <td>1062.26412</td>
      <td>...</td>
      <td>-60.08473</td>
      <td>-58.82391</td>
      <td>-17.61409</td>
      <td>70.46503</td>
      <td>-61.43628</td>
      <td>-20.16371</td>
      <td>41.08417</td>
      <td>4708.08568</td>
      <td>-0.717054</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>289</th>
      <td>-69.66</td>
      <td>-15.00</td>
      <td>-31.613015</td>
      <td>-20.565025</td>
      <td>118.0</td>
      <td>0.0</td>
      <td>24.729140</td>
      <td>52.90695</td>
      <td>52.90695</td>
      <td>52.90695</td>
      <td>...</td>
      <td>-22.94916</td>
      <td>-19.59360</td>
      <td>-5.81896</td>
      <td>-91.24696</td>
      <td>-72.70845</td>
      <td>-57.63845</td>
      <td>38.54894</td>
      <td>3214.72056</td>
      <td>0.672806</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>290</th>
      <td>-78.00</td>
      <td>-8.79</td>
      <td>-40.622146</td>
      <td>-15.257170</td>
      <td>114.0</td>
      <td>0.0</td>
      <td>51.957456</td>
      <td>55.52943</td>
      <td>1142.11551</td>
      <td>1142.11551</td>
      <td>...</td>
      <td>-28.91285</td>
      <td>-19.42203</td>
      <td>-13.75269</td>
      <td>-37.16355</td>
      <td>-99.99890</td>
      <td>-33.06479</td>
      <td>69.61294</td>
      <td>4428.55551</td>
      <td>1.214975</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>291</th>
      <td>-75.35</td>
      <td>-13.93</td>
      <td>-42.117166</td>
      <td>-20.649809</td>
      <td>147.0</td>
      <td>0.0</td>
      <td>21.849639</td>
      <td>54.58950</td>
      <td>756.22695</td>
      <td>756.22695</td>
      <td>...</td>
      <td>-3.49496</td>
      <td>16.93548</td>
      <td>-0.38227</td>
      <td>8.84321</td>
      <td>-23.03796</td>
      <td>-39.74719</td>
      <td>69.00050</td>
      <td>3761.82099</td>
      <td>-1.204286</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>292</th>
      <td>-76.08</td>
      <td>-11.48</td>
      <td>-43.950095</td>
      <td>-16.842393</td>
      <td>101.0</td>
      <td>0.0</td>
      <td>36.355499</td>
      <td>54.85460</td>
      <td>1190.90698</td>
      <td>1190.90698</td>
      <td>...</td>
      <td>40.29418</td>
      <td>-31.96652</td>
      <td>41.93348</td>
      <td>71.76161</td>
      <td>-29.57451</td>
      <td>-38.50603</td>
      <td>22.39762</td>
      <td>4093.90633</td>
      <td>-0.390912</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>293</th>
      <td>-71.31</td>
      <td>-14.98</td>
      <td>-54.590235</td>
      <td>-17.500740</td>
      <td>67.0</td>
      <td>0.0</td>
      <td>43.612641</td>
      <td>54.73734</td>
      <td>3099.49143</td>
      <td>2441.70938</td>
      <td>...</td>
      <td>14.92243</td>
      <td>-24.92012</td>
      <td>14.00034</td>
      <td>32.93287</td>
      <td>-12.35373</td>
      <td>-41.81436</td>
      <td>20.56200</td>
      <td>3378.69739</td>
      <td>-0.358875</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>294</th>
      <td>-70.62</td>
      <td>-17.11</td>
      <td>-69.653196</td>
      <td>-17.852718</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>48.213227</td>
      <td>54.65641</td>
      <td>3328.53949</td>
      <td>2776.41720</td>
      <td>...</td>
      <td>-29.21665</td>
      <td>-4.83442</td>
      <td>21.27099</td>
      <td>94.66201</td>
      <td>-50.11097</td>
      <td>-37.72833</td>
      <td>27.89528</td>
      <td>3160.06366</td>
      <td>-0.486864</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>295</th>
      <td>-79.31</td>
      <td>-4.94</td>
      <td>-45.733206</td>
      <td>-10.589512</td>
      <td>154.0</td>
      <td>0.0</td>
      <td>48.474874</td>
      <td>56.13205</td>
      <td>2147.23928</td>
      <td>1813.38033</td>
      <td>...</td>
      <td>49.09540</td>
      <td>3.41154</td>
      <td>-30.37766</td>
      <td>39.38747</td>
      <td>23.80904</td>
      <td>12.23124</td>
      <td>31.15223</td>
      <td>5099.29243</td>
      <td>0.543709</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>296</th>
      <td>-78.67</td>
      <td>-6.73</td>
      <td>-70.657487</td>
      <td>-11.057387</td>
      <td>39.0</td>
      <td>0.0</td>
      <td>62.727249</td>
      <td>56.14919</td>
      <td>5373.67650</td>
      <td>1076.30110</td>
      <td>...</td>
      <td>13.21524</td>
      <td>-25.08597</td>
      <td>12.24246</td>
      <td>60.45651</td>
      <td>-7.46828</td>
      <td>-22.30925</td>
      <td>7.04216</td>
      <td>4708.08568</td>
      <td>-0.122909</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>297</th>
      <td>-75.09</td>
      <td>-13.69</td>
      <td>-37.112536</td>
      <td>-19.124363</td>
      <td>121.0</td>
      <td>0.0</td>
      <td>30.740063</td>
      <td>54.09642</td>
      <td>269.79929</td>
      <td>269.79929</td>
      <td>...</td>
      <td>-39.68330</td>
      <td>11.56758</td>
      <td>7.99788</td>
      <td>-19.41449</td>
      <td>-59.05957</td>
      <td>-46.36908</td>
      <td>71.80290</td>
      <td>3761.82099</td>
      <td>1.253197</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>298</th>
      <td>-71.31</td>
      <td>-14.91</td>
      <td>-38.398992</td>
      <td>-21.934657</td>
      <td>151.0</td>
      <td>0.0</td>
      <td>17.739843</td>
      <td>53.93117</td>
      <td>323.86191</td>
      <td>323.86191</td>
      <td>...</td>
      <td>-3.42257</td>
      <td>-17.25992</td>
      <td>-22.78837</td>
      <td>8.88338</td>
      <td>-7.68381</td>
      <td>-40.99490</td>
      <td>40.85864</td>
      <td>3378.69739</td>
      <td>-0.713118</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>299</th>
      <td>-70.61</td>
      <td>-17.25</td>
      <td>-37.243172</td>
      <td>-24.160112</td>
      <td>145.0</td>
      <td>0.0</td>
      <td>11.744395</td>
      <td>53.94534</td>
      <td>163.59542</td>
      <td>163.59542</td>
      <td>...</td>
      <td>-2.26253</td>
      <td>14.87833</td>
      <td>0.05195</td>
      <td>2.36178</td>
      <td>-23.78566</td>
      <td>-38.97366</td>
      <td>84.32944</td>
      <td>3160.06366</td>
      <td>-1.471826</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>300</th>
      <td>-76.13</td>
      <td>-11.60</td>
      <td>-43.993914</td>
      <td>-16.965040</td>
      <td>101.0</td>
      <td>0.0</td>
      <td>35.880790</td>
      <td>54.85460</td>
      <td>1190.90698</td>
      <td>1190.90698</td>
      <td>...</td>
      <td>40.29418</td>
      <td>-31.96652</td>
      <td>41.93348</td>
      <td>71.76161</td>
      <td>-29.57451</td>
      <td>-38.50603</td>
      <td>22.39762</td>
      <td>4093.90633</td>
      <td>-0.390912</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>301 rows × 21 columns</p>
</div>



There are 21 columns (python (usually) counts from 0) representing different parameters. Some of these parameters may be useful for us. Some are not. The final column contains a binary flag representing whether there is a known porphyry copper deposit at that location or not. The "non-deposits" are required to train our Machine Learning classifier what a porphyry deposit looks like, and also, what a porphyry deposit doesn't look like!

### Now let's perform our machine learning binary classification.


```python
#Change data format to numpy array for easy manipulation
ml_data_np=ml_data.values

#Set the indices of the parameters (features) to include in the ML
params=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# Alternatively try any 4 features you'd like to include!
#params=[6,9,14,17] 


#Save the number of parameters we have chosen
datalength=len(params)

#Normalise the data for Machine Learning
ml_data_norm=preprocessing.scale(ml_data_np[:,params])

#Create a 'feature vector' and a 'target classification vector'
features=ml_data_norm
targets=ml_data_np[:,20]

#Print out some info about our final dataset
print("Shape of ML data array: ", ml_data_norm.shape)
print("Positive (deposits) examples: ",np.shape(ml_data_np[ml_data_np[:,20]==1,:]))
print("Negative (non-deposits) examples: ",np.shape(ml_data_np[ml_data_np[:,20]==0,:]))
```

    ('Shape of ML data array: ', (301, 21))
    ('Positive (deposits) examples: ', (147, 21))
    ('Negative (non-deposits) examples: ', (154, 21))



```python
print('Make the classifiers')

print('Random Forest...')
#create and train the random forest
#multi-core CPUs can use: rf = RandomForestClassifier(n_estimators=100, n_jobs=2)
#n_estimators use between 64-128 doi: 10.1007/978-3-642-31537-4_13
rf = RandomForestClassifier(n_estimators=128, n_jobs=1,class_weight=None)
rf.fit(features,targets)
print("Done RF")

scores = cross_val_score(rf, features,targets, cv=10)
print("RF Scores: ",scores)
print("SCORE Mean: %.2f" % np.mean(scores), "STD: %.2f" % np.std(scores), "\n")

print("Targets (expected result):")
print(targets)

print("Prediction (actual result):")
print(rf.predict(features))
```

    Make the classifiers
    Random Forest...
    Done RF
    ('RF Scores: ', array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]))
    ('SCORE Mean: 1.00', 'STD: 0.00', '\n')
    Targets (expected result):
    [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.
     1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.
     1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.
     1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.
     1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.
     1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.
     1. 1. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
    Prediction (actual result):
    [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.
     1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.
     1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.
     1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.
     1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.
     1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.
     1. 1. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
     0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]



```python
#Make a list of labels for our chosen features
paramColumns=np.array(ml_data.columns)
paramLabels=paramColumns[params].tolist()

#Create a new figure
fig, ax = plt.subplots()

#Plot the bar graph
rects=ax.bar(np.arange(0, datalength, step=1),rf.feature_importances_)

#Label the axes
ax.set_xticks(np.arange(0, datalength, step=1))
ax.set_xticklabels(paramLabels,rotation=90)
ax.set_ylabel('Feature Importance')

#Print the feature importance to compare with plot
np.set_printoptions(precision=3,suppress=True)
print("Importance \t Feature")
for i,label in enumerate(paramLabels):
    print("%1.3f \t\t %s" % (rf.feature_importances_[i],label))

plt.show()

```

    Importance 	 Feature
    0.014 		 0 Present day longitude (degrees)
    0.013 		 1 Present day latitude (degrees)
    0.049 		 2 Reconstructed longitude (degrees)
    0.014 		 3 Reconstructed latitude (degrees)
    0.054 		 4 Age (Ma)
    0.000 		 5 Time before mineralisation (Myr)
    0.040 		 6 Seafloor age (Myr)
    0.018 		 7 Segment length (km)
    0.025 		 8 Slab length (km)
    0.032 		 9 Distance to trench edge (km)
    0.022 		 10 Subducting plate normal velocity (km/Myr)
    0.019 		 11 Subducting plate parallel velocity (km/Myr)
    0.027 		 12 Overriding plate normal velocity (km/Myr)
    0.022 		 13 Overriding plate parallel velocity (km/Myr)
    0.019 		 14 Convergence normal rate (km/Myr)
    0.013 		 15 Convergence parallel rate (km/Myr)
    0.016 		 16 Subduction polarity (degrees)
    0.031 		 17 Subduction obliquity (degrees)
    0.012 		 18 Distance along margin (km)
    0.015 		 19 Subduction obliquity signed (radians)
    0.546 		 20 Ore Deposits Binary Flag (1 or 0)



![png](output_10_1.png)


Now if we can measure the tectonomagmatic properties at some point. Based on our trained classifer we can predict a probability that porphyry copper deposits have formed


```python
#Apply the trained ML to our gridded data to determine the probabilities at each of the points
print('RF...')
pRF=np.array(rf.predict_proba(features))
print("Done RF")
```

    RF...
    Done RF


## Maps!


```python
filename="../data/EarthByte_Zahirovic_etal_2016_ESR_r888_AgeGrid-0.nc"
data = scipy.io.netcdf.netcdf_file(filename,'r')
data.variables
```




    OrderedDict([('lon', <scipy.io.netcdf.netcdf_variable at 0x7fec3cd7c190>),
                 ('lat', <scipy.io.netcdf.netcdf_variable at 0x7fec406d7150>),
                 ('z', <scipy.io.netcdf.netcdf_variable at 0x7fec3cd9fc90>)])




```python
varX=data.variables['lon'][:]
varY=data.variables['lat'][:]
varZ=np.array(data.variables['z'][:])
data.close()
```

    /usr/local/lib/python2.7/dist-packages/scipy/io/netcdf.py:317: RuntimeWarning: Cannot close a netcdf_file opened with mmap=True, when netcdf_variables or arrays referring to its data still exist. All data arrays obtained from such files refer directly to data on disk, and must be copied before the file can be cleanly closed. (See netcdf_file docstring for more information on mmap.)
      ), category=RuntimeWarning)



```python
#Make a figure object
plt.figure()

#Get the axes of the current figure, for manipulation
ax = plt.gca()

#Create a colormap from a predefined function
age_cmap=colormap_age()

#Put down the main dataset
im=ax.imshow(varZ,vmin=0,vmax=200,extent=[0,360,-90,90],origin='lower',aspect=1,cmap=age_cmap)

#Make a colorbar
cbar=plt.colorbar(im,fraction=0.025,pad=0.05,ticks=[0, 150],extend='max')
cbar.set_label('Age (Ma)', rotation=0)

#Clean up the default axis ticks
plt.yticks([-90,-45,0,45,90])
plt.xticks([0,90,180,270,360])

#Put labels on the figure
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

#Put a title on it
plt.title("Global Seafloor Age Grid \n (Zahirovic et al. 2016)")

plt.show()
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-11-94fa21453eab> in <module>()
          6 
          7 #Create a colormap from a predefined function
    ----> 8 age_cmap=colormap_age()
          9 
         10 #Put down the main dataset


    NameError: name 'colormap_age' is not defined



![png](output_16_1.png)


### For loops plotting shapefiles


```python
#Load in plate polygons for plotting
topologyFile='../data/topology_platepolygons_0.00Ma.shp'
[recs,shapes,fields,Nshp]=readTopologyPlatepolygonFile(topologyFile)
for i, nshp in enumerate(range(Nshp)):
    #if nshp!=35 and nshp!=36 and nshp!=23:
    #These are the plates that cross the dateline and cause 
        #banding errors
        polygonShape=shapes[nshp].points
        poly=np.array(polygonShape)
        plt.plot(poly[:,0], poly[:,1], c='k',zorder=1)
        
plt.show()
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-12-26a781502d9a> in <module>()
          1 #Load in plate polygons for plotting
          2 topologyFile='../data/topology_platepolygons_0.00Ma.shp'
    ----> 3 [recs,shapes,fields,Nshp]=readTopologyPlatepolygonFile(topologyFile)
          4 for i, nshp in enumerate(range(Nshp)):
          5     #if nshp!=35 and nshp!=36 and nshp!=23:


    NameError: name 'readTopologyPlatepolygonFile' is not defined



```python
filename="../data/topodata.nc"
data = scipy.io.netcdf.netcdf_file(filename,'r')

data.variables
```




    OrderedDict([('X', <scipy.io.netcdf.netcdf_variable at 0x7fec3cd4f0d0>),
                 ('Y', <scipy.io.netcdf.netcdf_variable at 0x7fec3cd4f450>),
                 ('elev', <scipy.io.netcdf.netcdf_variable at 0x7fec3cd4f590>)])




```python
topoX=data.variables['X'][:]
topoY=data.variables['Y'][:]
topoZ=np.array(data.variables['elev'][:])
data.close()
```

### Make a prettier map


```python
###Set up the figure
fig = plt.figure(figsize=(16,12),dpi=150)

ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([-85, -30, -55, 10])
ax.coastlines('50m', linewidth=0.8)

###Add the map grid lines and format them
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=2, color='gray', alpha=0.5, linestyle='-')

from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.ticker as mticker
from matplotlib import colorbar, colors

gl.xlabels_top = False
gl.ylabels_left = True
gl.ylabels_right = False
gl.xlines = False
gl.ylines = False
gl.xlocator = mticker.FixedLocator([-75,-60, -45,-30])
gl.ylocator = mticker.FixedLocator([-60, -45, -30, -15, 0,15])
ax.set_xticks([-75,-60, -45,-30])
ax.set_xticklabels([''])
ax.set_yticks([-60, -45, -30, -15, 0,15])
ax.set_yticklabels([''])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
#gl.xlabel_style = {'size': 15, 'color': 'gray'}
#gl.xlabel_style = {'color': 'black', 'weight': 'normal'}

print("Made base map")

###Plot a topography underlay image
#Make a lat lon grid to fit the topo grid
lons, lats = np.meshgrid(topoX,topoY)
im1=ax.pcolormesh(lons,lats,topoZ, shading="flat",cmap=plt.cm.gist_earth,transform=ccrs.PlateCarree())              
cbar=plt.colorbar(im1, ax=ax, orientation="horizontal", pad=0.02, fraction=0.05, shrink=0.2,extend='both')
cbar.set_label('Topography (m)')

print("Added topo")

###Plot shapefile polygon outlines
#Load in plate polygons for plotting
topologyFile='../data/topology_platepolygons_0.00Ma.shp'
[recs,shapes,fields,Nshp]=readTopologyPlatepolygonFile(topologyFile)
for i, nshp in enumerate(range(Nshp)):
    if nshp!=35 and nshp!=36 and nshp!=23:
    #These are the plates that cross the dateline and cause 
        #banding errors
        polygonShape=shapes[nshp].points
        poly=np.array(polygonShape)
        xh=poly[:,0]
        yh=poly[:,1]
        ax.plot(xh, yh, c='w',zorder=1)

print("Added shapes")
        
###Plot the ore deposit probability
xh = ml_data_np[ml_data_np[:,-1]==1,0]
yh= ml_data_np[ml_data_np[:,-1]==1,1]
l2 = ax.scatter(xh, yh, 500, marker='.',c=pRF[:147,1],cmap=plt.cm.copper,zorder=3,transform=ccrs.PlateCarree(),vmin=0,vmax=1)
#l2 = pmap.scatter(xh, yh, 20, marker='.',edgecolor='dimgrey',linewidth=0.5,c=pRF[:147,1],cmap=plt.cm.copper,zorder=3)
cbar=fig.colorbar(l2, ax=ax, orientation="horizontal", pad=0.05, fraction=0.05, shrink=0.2,ticks=[0,0.5,1.0])
cbar.set_clim(-0.1, 1.1)
cbar.set_label('Prediction Probability (%)')

###Plot the ore deposit Age
xh=ml_data_np[ml_data_np[:,-1]==1,0]
yh = ml_data_np[ml_data_np[:,-1]==1,1]
l2 = ax.scatter(xh, yh, 50, marker='.',c=ml_data_np[ml_data_np[:,-1]==1,4],cmap=plt.cm.hsv,zorder=3)
cbar=fig.colorbar(l2, ax=ax, orientation="horizontal", pad=0.1, fraction=0.05, shrink=0.2,extend='max',ticks=[0,50,100,150])
cbar.set_clim(0, 170)
cbar.set_label('Age of Deposit (Ma)')

print("Added deposit probability")

plt.show()
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-15-d2511d04c7e9> in <module>()
          2 fig = plt.figure(figsize=(16,12),dpi=150)
          3 
    ----> 4 ax = plt.axes(projection=ccrs.PlateCarree())
          5 ax.set_extent([-85, -30, -55, 10])
          6 ax.coastlines('50m', linewidth=0.8)


    NameError: name 'ccrs' is not defined



    <matplotlib.figure.Figure at 0x7fec3cc1f0d0>


# Exercise
Do the same analysis but using a different Machine Learning algorith for your classification. You can use this as a guide for picking a good classification algorithm https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html. 
Additionaly, determine which parameters are best for learning. For robust results ***learn*** which parameters are most important! 
Present your results on a map, and compare it with the Random Forrest method. Explain why the parameters you have chosen are probably the most important. Explain why there are differences in the ML algorithms.

# Datasets

Topography/Bathymetry
WORLDBATH: ETOPO5 5x5 minute Navy bathymetry. http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NGDC/.ETOPO5/
    
ML dataset. 
Expanded in Butterworth et al 2016 from a compilation made by by Bertrand et al 2016. https://doi.org/10.1002/2016TC004289

Shape files polygons: 
GPlates2.0. https://www.gplates.org/

Age Grid
Zahirovic etal 2016. ftp://ftp.earthbyte.org/Data_Collections/Zahirovic_etal_2016_ESR_AgeGrid/
    

```python

```


```python

```
