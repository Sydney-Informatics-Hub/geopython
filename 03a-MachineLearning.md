# Machine Learning for Geoscience

<div class="questions">  
### Questions

- What data science tools and techniques can be used in Python?
- How do I do it?
</div>

<div class="objectives">  
### Objectives

- Learn fundamental Machine Learning packages.
- Learn to further explore data.
</div>

Let's use some standard Machine Learning tools available in Python packages to analyse some data.

We have a dataset (from Butterworth et al. 2016) with a collection of tectonomagmatic parameters associated with the time and location of porphyry copper deposits. We want to determine which of these (if any) parameters are geologically important (or at least statistically significant) in relation to the formation of porphyry coppers.

Below is an animation of the tectonomagmatic evolution of the South American plate margin since 150Ma, representing many of the parameters in the data.

![SegmentLocal](./fig/MullerConvergenceSmall.gif "segment")

## Start by importing most of the modules we need
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
from matplotlib import cm

#For easy geographic projections on a map
import cartopy.crs as ccrs

#For dealing with shapefiles
import shapefile

```

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

    Shape of ML data array:  (301, 21)
    Positive (deposits) examples:  (147, 21)
    Negative (non-deposits) examples:  (154, 21)



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
    RF Scores:  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
    SCORE Mean: 1.00 STD: 0.00 
    
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
rects=ax.barh(np.arange(0, datalength, step=1),rf.feature_importances_)

#Label the axes
ax.set_yticks(np.arange(0, datalength, step=1))
ax.set_yticklabels(paramLabels)
ax.set_xlabel('Feature Importance')

#Print the feature importance to compare with plot
np.set_printoptions(precision=3,suppress=True)
print("Importance \t Feature")
for i,label in enumerate(paramLabels):
    print("%1.3f \t\t %s" % (rf.feature_importances_[i],label))

plt.show()

```

    Importance 	 Feature
    0.012 		 0 Present day longitude (degrees)
    0.011 		 1 Present day latitude (degrees)
    0.051 		 2 Reconstructed longitude (degrees)
    0.015 		 3 Reconstructed latitude (degrees)
    0.058 		 4 Age (Ma)
    0.000 		 5 Time before mineralisation (Myr)
    0.037 		 6 Seafloor age (Myr)
    0.014 		 7 Segment length (km)
    0.027 		 8 Slab length (km)
    0.026 		 9 Distance to trench edge (km)
    0.017 		 10 Subducting plate normal velocity (km/Myr)
    0.010 		 11 Subducting plate parallel velocity (km/Myr)
    0.021 		 12 Overriding plate normal velocity (km/Myr)
    0.012 		 13 Overriding plate parallel velocity (km/Myr)
    0.021 		 14 Convergence normal rate (km/Myr)
    0.011 		 15 Convergence parallel rate (km/Myr)
    0.011 		 16 Subduction polarity (degrees)
    0.025 		 17 Subduction obliquity (degrees)
    0.008 		 18 Distance along margin (km)
    0.016 		 19 Subduction obliquity signed (radians)
    0.598 		 20 Ore Deposits Binary Flag (1 or 0)



    
![png](03a-MachineLearning_files/03a-MachineLearning_11_1.png)
    


Now if we can measure the tectonomagmatic properties at some point. Based on our trained classifier we can predict a probability that porphyry copper deposits have formed



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
filename="../data/topodata.nc"
data = scipy.io.netcdf.netcdf_file(filename,'r')

data.variables
```




    OrderedDict([('X', <scipy.io.netcdf.netcdf_variable at 0x269572f8f48>),
                 ('Y', <scipy.io.netcdf.netcdf_variable at 0x269572f82c8>),
                 ('elev', <scipy.io.netcdf.netcdf_variable at 0x269551f4788>)])




```python
topoX=data.variables['X'][:]
topoY=data.variables['Y'][:]
topoZ=np.array(data.variables['elev'][:])

#Some file types and readers (like netcdf) can actually change the data directly on disk
#Good practice, is to close the file when done (for safety and memory saving)
data.close()
```

    c:\users\nbutter\miniconda3\envs\geopy\lib\site-packages\scipy\io\netcdf.py:317: RuntimeWarning: Cannot close a netcdf_file opened with mmap=True, when netcdf_variables or arrays referring to its data still exist. All data arrays obtained from such files refer directly to data on disk, and must be copied before the file can be cleanly closed. (See netcdf_file docstring for more information on mmap.)
      ), category=RuntimeWarning)



```python
#Make a figure object
plt.figure()

#Get the axes of the current figure, for manipulation
ax = plt.gca()

#Put down the main topography dataset
im=ax.imshow(topoZ,vmin=-5000,vmax=1000,extent=[0,360,-90,90],origin='upper',aspect=1,cmap=cm.gist_earth)

#Make a colorbar
cbar=plt.colorbar(im,fraction=0.025,pad=0.05,ticks=[-5000,0, 1000],extend='both')
cbar.set_label('Height \n ASL \n (m)', rotation=0)

#Clean up the default axis ticks
plt.yticks([-90,-45,0,45,90])
plt.xticks([0,90,180,270,360])

#Put labels on the figure
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

#Put a title on it
plt.title("Bathymetry and Topography of the World \n (ETOPO5 2020)")

plt.show()
```


    
![png](03a-MachineLearning_files/03a-MachineLearning_17_0.png)
    


### For loops plotting shapefiles



```python
#Load in plate polygons for plotting
topologyFile='../data/platepolygons/topology_platepolygons_0.00Ma.shp'

#read in the file
shapeRead = shapefile.Reader(topologyFile)

#And save out some of the shape file attributes
recs    = shapeRead.records()
shapes  = shapeRead.shapes()
fields  = shapeRead.fields
Nshp    = len(shapes)

for i, nshp in enumerate(range(Nshp)):
    #if nshp!=35 and nshp!=36 and nshp!=23:
    #These are the plates that cross the dateline and cause 
        #banding errors
        polygonShape=shapes[nshp].points
        poly=np.array(polygonShape)
        plt.plot(poly[:,0], poly[:,1], c='k',zorder=1)
        
plt.show()
```


    
![png](03a-MachineLearning_files/03a-MachineLearning_19_0.png)
    


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

gl.top_labels = False
gl.left_labels = True
gl.right_labels = False
gl.xlines = False
gl.ylines = False
gl.xlocator = mticker.FixedLocator([-75,-60, -45,-30])
gl.ylocator = mticker.FixedLocator([-60, -45, -30, -15, 0,15])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
#gl.xlabel_style = {'size': 15, 'color': 'gray'}
#gl.xlabel_style = {'color': 'black', 'weight': 'normal'}

print("Made base map")

###Plot a topography underlay image
#Make a lat lon grid to fit the topo grid
lons, lats = np.meshgrid(topoX,topoY)
im1=ax.pcolormesh(lons,lats,topoZ, shading="auto",cmap=plt.cm.gist_earth,transform=ccrs.PlateCarree())              
cbar=plt.colorbar(im1, ax=ax, orientation="horizontal", pad=0.02, fraction=0.05, shrink=0.2,extend='both')
cbar.set_label('Topography (m)')

print("Added topo")

###Plot shapefile polygon outlines
#Load in plate polygons for plotting
topologyFile='../data/platepolygons/topology_platepolygons_0.00Ma.shp'

#read in the file
shapeRead = shapefile.Reader(topologyFile)

#And save out some of the shape file attributes
recs    = shapeRead.records()
shapes  = shapeRead.shapes()
fields  = shapeRead.fields
Nshp    = len(shapes)

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
l2.set_clim(-0.1, 1.1)
cbar.set_label('Prediction Probability (%)')

###Plot the ore deposit Age
xh=ml_data_np[ml_data_np[:,-1]==1,0]
yh = ml_data_np[ml_data_np[:,-1]==1,1]
l2 = ax.scatter(xh, yh, 50, marker='.',c=ml_data_np[ml_data_np[:,-1]==1,4],cmap=plt.cm.hsv,zorder=3)
cbar=fig.colorbar(l2, ax=ax, orientation="horizontal", pad=0.1, fraction=0.05, shrink=0.2,extend='max',ticks=[0,50,100,150])
l2.set_clim(0, 170)
cbar.set_label('Age of Deposit (Ma)')

print("Added deposit probability")

plt.show()
```

    Made base map
    Added topo
    Added shapes
    Added deposit probability



    
![png](03a-MachineLearning_files/03a-MachineLearning_21_1.png)
    


## Exercise
Do the same analysis but using a different Machine Learning algorithm for your classification. You can use this as a guide for picking a good classification algorithm [https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html). 
Present your results on a map, and compare it with the Random Forest method. 

## Datasets

#### Topography/Bathymetry
WORLDBATH: ETOPO5 5x5 minute Navy bathymetry. http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NGDC/.ETOPO5/
    
#### ML dataset
Butterworth et al 2016 https://doi.org/10.1002/2016TC004289

#### Shapefile plate polygons
GPlates2.0. https://www.gplates.org/

<div class="keypoints">
### Key points

- Applying ML workflows
- Wrangling data.
</div>


