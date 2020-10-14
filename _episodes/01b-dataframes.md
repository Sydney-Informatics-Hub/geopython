---
title: "01b. Python Fundamentals - shapefiles and dataframes"
teaching: 10
exercises: 0
questions:
- "What else can Python do?"
- "What are libraries and packages?"
objectives:
- "Learn the ."
keypoints:
- "Shapefiles"
- "Pandas dataframes"
---

## Dealing with other data types
Python can deal with basically any type of data you throw at it. The community have provided many packages that make things easy, today we will look at the "pyshp" (for dealing with shapefiles) and "pandas" (great for tables and time series) packages.

Data for this exercised was downloaded from http://www.bom.gov.au/water/groundwater/explorer/map.shtml

# Shapefiles
Shapefiles are a very common file format for GIS data.


```python
#Load the required modules
import shapefile

#NOTE: Weirdly and confusingly, this package is called "pyshp" but you call it via the name "shapefile"
```


```python
help(shapefile)
#Or check out the help pages https://github.com/GeospatialPython/pyshp
```

    Help on module shapefile:
    
    NAME
        shapefile
    
    FILE
    ...
    



```python
#Set the filename
boreshape='../data/shp_torrens_river/NGIS_BoreLine.shp'

#read in the file
shapeRead = shapefile.Reader(boreshape)

#And save out some of the shape file attributes
recs    = shapeRead.records()
shapes  = shapeRead.shapes()
fields  = shapeRead.fields
Nshp    = len(shapes)
```


```python
print(Nshp) #print the Number of items in the shapefile
```

    7635



```python
fields[:]#print the fields
```




    [('DeletionFlag', 'C', 1, 0),
     ['HydroID', 'N', 10, 0],
     ['HydroCode', 'C', 30, 0],
     ['BoreID', 'N', 10, 0],
     ['TopElev', 'F', 19, 11],
     ['BottomElev', 'F', 19, 11],
     ['HGUID', 'N', 10, 0],
     ['HGUNumber', 'N', 10, 0],
     ['NafHGUNumb', 'N', 10, 0],
     ['SHAPE_Leng', 'F', 19, 11]]




```python
recs[0] #print the first record, then this is a list that can be subscripted further
```




    [32001999, '652800645', 30027773, 6.74, -74.26, 31000043, 1042, 104005, 0.0]




```python
shapes[0].points #print the point values of the first shape
```




    [(591975.5150000006, -3816141.8817), (591975.5150000006, -3816141.8817)]



Shapefiles are not a native python format, but the community have developed tools for exploring them. The package we have used "pyshp" imported with the name "shapefile" (for some non-consistent weird reason), is one example of working with shapefiles. Alternatives exist.

## More table manipulation


```python
#Import the module
import pandas
```


```python
#read in the data
log_data=pandas.read_csv("../data/shp_torrens_river/NGIS_LithologyLog.csv",\
                         header=0,sep=',',skipinitialspace=True,quotechar ='"',\
                         usecols=list(range(0,13)),\
                         skiprows=[453,456,458,460,689,697,720,723,726,839,880,884,885,890,898,934])

#This data was weird because it has quotation marks to signify inches inside comments within the file, 
#making automatic reading of it tricky
```


```python
log_data           # print the first 30 and last 30 rows
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
      <th>OBJECTID</th>
      <th>BoreID</th>
      <th>HydroCode</th>
      <th>RefElev</th>
      <th>RefElevDesc</th>
      <th>FromDepth</th>
      <th>ToDepth</th>
      <th>TopElev</th>
      <th>BottomElev</th>
      <th>MajorLithCode</th>
      <th>MinorLithCode</th>
      <th>Description</th>
      <th>Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1769789</td>
      <td>30062892</td>
      <td>662815923</td>
      <td>57.25</td>
      <td>NGS</td>
      <td>18.0</td>
      <td>19.5</td>
      <td>39.25</td>
      <td>37.75</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Clay</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1769790</td>
      <td>30062892</td>
      <td>662815923</td>
      <td>57.25</td>
      <td>NGS</td>
      <td>19.5</td>
      <td>22.0</td>
      <td>37.75</td>
      <td>35.25</td>
      <td>ROCK</td>
      <td>None</td>
      <td>Rocks and sand</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1769791</td>
      <td>30062892</td>
      <td>662815923</td>
      <td>57.25</td>
      <td>NGS</td>
      <td>22.0</td>
      <td>24.0</td>
      <td>35.25</td>
      <td>33.25</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Clay</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1770725</td>
      <td>30141910</td>
      <td>662816624</td>
      <td>4.0</td>
      <td>NGS</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>4.0</td>
      <td>-2.0</td>
      <td>None</td>
      <td>None</td>
      <td>No sample</td>
      <td>SAGeodata</td>
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
    </tr>
    <tr>
      <th>70154</th>
      <td>4120347</td>
      <td>30304050</td>
      <td>652802882</td>
      <td>None</td>
      <td>UNK</td>
      <td>0.0</td>
      <td>0.3</td>
      <td>None</td>
      <td>None</td>
      <td>FILL</td>
      <td>None</td>
      <td>Fill</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70155</th>
      <td>4120348</td>
      <td>30304050</td>
      <td>652802882</td>
      <td>None</td>
      <td>UNK</td>
      <td>0.3</td>
      <td>0.8</td>
      <td>None</td>
      <td>None</td>
      <td>SAND</td>
      <td>None</td>
      <td>Clayey sand</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70156</th>
      <td>4120349</td>
      <td>30304050</td>
      <td>652802882</td>
      <td>None</td>
      <td>UNK</td>
      <td>0.8</td>
      <td>3.5</td>
      <td>None</td>
      <td>None</td>
      <td>SAND</td>
      <td>None</td>
      <td>Sand</td>
      <td>SAGeodata</td>
    </tr>
  </tbody>
</table>
<p>70157 rows × 13 columns</p>
</div>




```python
# add a new column as a function of existing columns
log_data['Thickness'] = log_data.ToDepth - log_data.FromDepth
```


```python
type(log_data)     # see what Python type the DataFrame is
```




    pandas.core.frame.DataFrame




```python
log_data.head(3)    # print the first 3 rows
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
      <th>OBJECTID</th>
      <th>BoreID</th>
      <th>HydroCode</th>
      <th>RefElev</th>
      <th>RefElevDesc</th>
      <th>FromDepth</th>
      <th>ToDepth</th>
      <th>TopElev</th>
      <th>BottomElev</th>
      <th>MajorLithCode</th>
      <th>MinorLithCode</th>
      <th>Description</th>
      <th>Source</th>
      <th>Thickness</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1769789</td>
      <td>30062892</td>
      <td>662815923</td>
      <td>57.25</td>
      <td>NGS</td>
      <td>18.0</td>
      <td>19.5</td>
      <td>39.25</td>
      <td>37.75</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Clay</td>
      <td>SAGeodata</td>
      <td>1.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1769790</td>
      <td>30062892</td>
      <td>662815923</td>
      <td>57.25</td>
      <td>NGS</td>
      <td>19.5</td>
      <td>22.0</td>
      <td>37.75</td>
      <td>35.25</td>
      <td>ROCK</td>
      <td>None</td>
      <td>Rocks and sand</td>
      <td>SAGeodata</td>
      <td>2.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1769791</td>
      <td>30062892</td>
      <td>662815923</td>
      <td>57.25</td>
      <td>NGS</td>
      <td>22.0</td>
      <td>24.0</td>
      <td>35.25</td>
      <td>33.25</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Clay</td>
      <td>SAGeodata</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
log_data.index     # “the index” (aka “the labels”). 
#Pandas is great for using timeseries data, where the index can be the timestamps
```




    RangeIndex(start=0, stop=70157, step=1)




```python
log_data.columns   # column names (which is “an index”)
```




    Index([u'OBJECTID', u'BoreID', u'HydroCode', u'RefElev', u'RefElevDesc',
           u'FromDepth', u'ToDepth', u'TopElev', u'BottomElev', u'MajorLithCode',
           u'MinorLithCode', u'Description', u'Source', u'Thickness'],
          dtype='object')




```python
log_data.dtypes    # data types of each column
```




    OBJECTID           int64
    BoreID             int64
    HydroCode          int64
    RefElev           object
    RefElevDesc       object
    FromDepth        float64
    ToDepth          float64
    TopElev           object
    BottomElev        object
    MajorLithCode     object
    MinorLithCode     object
    Description       object
    Source            object
    Thickness        float64
    dtype: object




```python
log_data.shape     # number of rows and columns
```




    (70157, 14)




```python
log_data.values    # underlying numpy array — df are stored as numpy arrays for effeciencies.
```




    array([[1769789L, 30062892L, 662815923L, ..., 'Clay', 'SAGeodata', 1.5],
           [1769790L, 30062892L, 662815923L, ..., 'Rocks and sand',
            'SAGeodata', 2.5],
           [1769791L, 30062892L, 662815923L, ..., 'Clay', 'SAGeodata', 2.0],
           ...,
           [4120347L, 30304050L, 652802882L, ..., 'Fill', 'SAGeodata', 0.3],
           [4120348L, 30304050L, 652802882L, ..., 'Clayey sand', 'SAGeodata',
            0.5],
           [4120349L, 30304050L, 652802882L, ..., 'Sand', 'SAGeodata', 2.7]],
          dtype=object)




```python
#log_data['MajorLithCode']         # select one column
##Equivalent to 
#log_data.MajorLithCode 
##and
#log_data.iloc[:,9]
```


```python
type(log_data['MajorLithCode'])   # determine datatype of column (e.g., Series)
```




    pandas.core.series.Series




```python
#describe the data frame
log_data.describe(include='all')     
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
      <th>OBJECTID</th>
      <th>BoreID</th>
      <th>HydroCode</th>
      <th>RefElev</th>
      <th>RefElevDesc</th>
      <th>FromDepth</th>
      <th>ToDepth</th>
      <th>TopElev</th>
      <th>BottomElev</th>
      <th>MajorLithCode</th>
      <th>MinorLithCode</th>
      <th>Description</th>
      <th>Source</th>
      <th>Thickness</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>7.015700e+04</td>
      <td>7.015700e+04</td>
      <td>7.015700e+04</td>
      <td>70157</td>
      <td>70157</td>
      <td>70157.000000</td>
      <td>70157.000000</td>
      <td>70157</td>
      <td>70157</td>
      <td>70157</td>
      <td>70157</td>
      <td>70157</td>
      <td>70157</td>
      <td>70157.000000</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>5068</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>27777</td>
      <td>27878</td>
      <td>81</td>
      <td>42</td>
      <td>33598</td>
      <td>39</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>top</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>NGS</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Clay</td>
      <td>SAGeodata</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>18514</td>
      <td>44946</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>18514</td>
      <td>18514</td>
      <td>25857</td>
      <td>62797</td>
      <td>4603</td>
      <td>70119</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>2.505842e+06</td>
      <td>3.018201e+07</td>
      <td>6.624491e+08</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>24.942443</td>
      <td>30.626594</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>5.684151</td>
    </tr>
    <tr>
      <th>std</th>
      <td>9.276598e+05</td>
      <td>8.068098e+04</td>
      <td>2.130462e+06</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>45.435866</td>
      <td>48.609957</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>9.943264</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.769789e+06</td>
      <td>3.002715e+07</td>
      <td>6.528000e+08</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.010000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1.932799e+06</td>
      <td>3.014558e+07</td>
      <td>6.628129e+08</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.800000</td>
      <td>4.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1.999036e+06</td>
      <td>3.018487e+07</td>
      <td>6.628196e+08</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7.000000</td>
      <td>11.580000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.800000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>3.967159e+06</td>
      <td>3.025487e+07</td>
      <td>6.628248e+08</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>25.900000</td>
      <td>34.750000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>4.120349e+06</td>
      <td>3.030405e+07</td>
      <td>6.728042e+08</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>610.300000</td>
      <td>620.160000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>300.500000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# summarise a panda Series
log_data.FromDepth.describe()   # describe a single column
```




    count    70157.000000
    mean        24.942443
    std         45.435866
    min          0.000000
    25%          0.800000
    50%          7.000000
    75%         25.900000
    max        610.300000
    Name: FromDepth, dtype: float64




```python
#calculate mean of 5th column ("FromDepth")
log_data.iloc[:,5].mean()      
```




    24.9424428068475




```python
#alternate method to calculate mean of FromDepth column (the 5th one)
log_data["FromDepth"].mean()    
```




    24.9424428068475




```python
#Count how many Lith Codes there are
lithCounts=log_data.MajorLithCode.value_counts()
```


```python
#Print the lithcodes, use .index or .values 
lithCounts
```




    CLYU    25857
    SAND    12772
    SLAT     4069
    FILL     4020
    SDST     3207
    TPSL     2767
    GRVL     2445
    QTZT     1891
    SHLE     1601
    SCHT     1576
    ROCK     1572
    LMST     1571
    SILT     1436
    None      874
    SLST      530
    MDST      528
    STON      474
    SOIL      441
    QUAR      251
    BITM      205
    SPST      190
    SHEL      181
    DLOM      169
    LOAM      143
    CLYS      119
    CORL      117
    MARL      115
    GNSS       99
    RUBL       90
    UKN        82
            ...  
    BASE       13
    MANM       13
    PEAT       12
    TRAV       10
    COAL        8
    WKST        7
    BSLT        6
    CAAR        6
    PYRT        5
    SLAG        5
    GPSM        5
    CAVE        3
    WOOD        2
    PEGM        2
    CLYW        2
    CLYR        2
    VOLC        2
    OPCA        2
    CLLV        2
    HFLS        1
    ARKS        1
    ALDG        1
    DIOR        1
    LMSD        1
    DUST        1
    FOSS        1
    REGO        1
    SCOR        1
    CALU        1
    SANN        1
    Name: MajorLithCode, Length: 81, dtype: int64




```python
#plot a bar chart of the lith codes
lithCounts.plot.bar(rot=90,figsize=(15,5))
```




    <matplotlib.axes._subplots.AxesSubplot at 0x9f13990>




```python
#Plot a bar chart of the lith codes for the rarer lithologies
lithCounts[(lithCounts < 50)].plot.bar(rot=90,figsize=(15,5))
```




    <matplotlib.axes._subplots.AxesSubplot at 0xa410b70>




![png](../fig/fig-01shp-boreholes.png)



```python
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
 
# example data
mu = np.mean(log_data['Thickness'].values) # mean of distribution
sigma = np.std(log_data['Thickness'].values) # standard deviation of distribution
x = log_data['Thickness'].values
# the histogram of the data
plt.hist(x, bins=[0,0.25,0.5,0.75,1.0,1.25,1.5,1.75,2,2.25,2.5,2.75,3.0], alpha=0.5)
plt.xlabel('Thickness (m)')
plt.ylabel('Count')
mystring="Histogram with a mean of "+ str(mu)
plt.title(mystring)
 
# Tweak spacing to prevent clipping of ylabel
#plt.subplots_adjust(left=0.15)
plt.show()



```


![png](../fig/fig-01shp-hist.png)



```python
# import numpy as np
# cmap = plt.get_cmap('viridis')
# colors = cmap(np.linspace(0, 1, len(lithCounts.index)))
# colors

# for row in log_data.itertuples():
#     boreid=row[3]
#     for ind,value in enumerate(recs):  
#         try:
#             value.index(boreid)
#             print(recs)
#         except:
#             continue
#     #(row[3])



# for ind, value in enumerate(recs):
#     #Get the lat lon value
#     lon=value[18]
#     lat=value[17]
#     #Get the Lithology unit
#     value[]
    
#     #Now plot it
#     plt.plot(lon,lat,"|")
```

# Exercise
Go to http://www.bom.gov.au/water/groundwater/explorer/map.shtml and pick another River Region. Download the dataset in "Shapefile" format (this will downlaod the csv also). Once you have the data, follow the same routines as above and see what you can find out about the river region. 

