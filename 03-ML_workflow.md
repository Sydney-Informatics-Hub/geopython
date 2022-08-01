# Machine Learning From Scratch

Most machine learning problems begin with a dataset, but before we can perform any kind of inference on that dataset we must create/wrangle/build it. This is often the most time-consuming and hard part of a successful machine learning workflow. There is no set procedure here, as all data is different, although there are a few simple methods we can take to make a useful dataset.

We will be using data from a submitted Manuscript (Butterworth and Barnett-Moore 2020) which was a finalist in the [Unearthed, ExploreSA: Gawler Challenge](https://unearthed.solutions/u/competitions/exploresa). You can visit the [original repo here](https://github.com/natbutter/gawler-exploration).

<br>

# Building a dataset of "targets" and "predictor variables"

The targets in an ML context can be a simple binary 1 or 0, or could be some category (classification), or the value of a particular parameter (regression problems). It is the "feature" of a dataset that we want to learn something about!

The "predictor/feature variables" are the qualities/parameters that may have some causal relationship with the "target".


## Step 1 - Determine our target variable
Let's explore our our main dataset.

### Deposit locations - mine and mineral occurrences
The most important dataset for this workflow is the currently known locations of mineral occurrences. Using the data we already know about these mineral deposits we will build a model to predict where future occurrences will be.


```python
# For working with shapefiles (packaged is called pyshp)
import shapefile
# For working with dataframes
import pandas as pd
```


```python
# Set the filename
mineshape="../data/MinesMinerals/mines_and_mineral_occurrences_all.shp"

# Set shapefile attributes and assign
sf = shapefile.Reader(mineshape)
fields = [x[0] for x in sf.fields][1:]
records = sf.records()
shps = [s.points for s in sf.shapes()]

# Write into a dataframe for easy use
df = pd.DataFrame(columns=fields, data=records)
```

View the metadata of the [South Australian all mines and mineral deposits](https://catalog.sarig.sa.gov.au/geonetwork/srv/eng/catalog.search#/metadata/a0e4b62c-ec88-44b8-a530-b4e744a6b414) to get a better understanding for what features we could use as a target.


```python
#See what the dataframe looks like
print(df.columns)

#For clean printing to html drop columns that contains annoying / and \ chars.
#And set max columns
pd.options.display.max_columns = 8
df.drop(columns=['REFERENCE','O_MAP_SYMB'])
```

    Index(['MINDEP_NO', 'DEP_NAME', 'REFERENCE', 'COMM_CODE', 'COMMODS',
           'COMMOD_MAJ', 'COMM_SPECS', 'GCHEM_ASSC', 'DISC_YEAR', 'CLASS_CODE',
           'OPER_TYPE', 'MAP_SYMB', 'STATUS_VAL', 'SIZE_VAL', 'GEOL_PROV',
           'DB_RES_RVE', 'DB_PROD', 'DB_DOC_IMG', 'DB_EXV_IMG', 'DB_DEP_IMG',
           'DB_DEP_FLE', 'COX_CLASS', 'REG_O_CTRL', 'LOC_O_CTRL', 'LOC_O_COM',
           'O_LITH_CDE', 'O_LITH01', 'O_STRAT_NM', 'H_LITH_CDE', 'H_LITH02',
           'H_STRAT_NM', 'H_MAP_SYMB', 'EASTING', 'NORTHING', 'ZONE', 'LONGITUDE',
           'LATITUDE', 'SVY_METHOD', 'HORZ_ACC', 'SRCE_MAP', 'SRCE_CNTRE',
           'COMMENTS', 'O_MAP_SYMB'],
          dtype='object')





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
      <th>MINDEP_NO</th>
      <th>DEP_NAME</th>
      <th>COMM_CODE</th>
      <th>COMMODS</th>
      <th>...</th>
      <th>HORZ_ACC</th>
      <th>SRCE_MAP</th>
      <th>SRCE_CNTRE</th>
      <th>COMMENTS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5219</td>
      <td>MOUNT DAVIES NO.2A</td>
      <td>Ni</td>
      <td>Nickel</td>
      <td>...</td>
      <td>2000.0</td>
      <td>500k meis</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>52</td>
      <td>ONE STONE</td>
      <td>Ni</td>
      <td>Nickel</td>
      <td>...</td>
      <td>500.0</td>
      <td>71-385</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td>8314</td>
      <td>HINCKLEY RANGE</td>
      <td>Fe</td>
      <td>Iron</td>
      <td>...</td>
      <td>500.0</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>3</th>
      <td>69</td>
      <td>KALKA</td>
      <td>V, ILM</td>
      <td>Vanadium, Ilmenite</td>
      <td>...</td>
      <td>100.0</td>
      <td>1 MILE</td>
      <td>mgt polygon on digital map</td>
      <td></td>
    </tr>
    <tr>
      <th>4</th>
      <td>65</td>
      <td>ECHIDNA</td>
      <td>Ni</td>
      <td>Nickel</td>
      <td>...</td>
      <td>20.0</td>
      <td>50K GEOL</td>
      <td>DH ECHIDNA PROSPECT</td>
      <td></td>
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
    </tr>
    <tr>
      <th>8672</th>
      <td>6937</td>
      <td>YARINGA</td>
      <td>QTZE</td>
      <td>Quartzite</td>
      <td>...</td>
      <td>200.0</td>
      <td>50k moc</td>
      <td>fenced yard</td>
      <td></td>
    </tr>
    <tr>
      <th>8673</th>
      <td>4729</td>
      <td>WELCHS</td>
      <td>SCHT</td>
      <td>Schist</td>
      <td>...</td>
      <td>20.0</td>
      <td>50k topo</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>8674</th>
      <td>4718</td>
      <td>ARCADIAN</td>
      <td>CLAY</td>
      <td>Clay</td>
      <td>...</td>
      <td>5.0</td>
      <td>Plan 1951-0327</td>
      <td>Pit</td>
      <td></td>
    </tr>
    <tr>
      <th>8675</th>
      <td>1436</td>
      <td>MCDONALD</td>
      <td>Au</td>
      <td>Gold</td>
      <td>...</td>
      <td>200.0</td>
      <td>50k moc</td>
      <td>qz float</td>
      <td></td>
    </tr>
    <tr>
      <th>8676</th>
      <td>8934</td>
      <td>FAIRFIELD FARM</td>
      <td>SAND</td>
      <td>Sand</td>
      <td>...</td>
      <td>20.0</td>
      <td></td>
      <td>pit</td>
      <td></td>
    </tr>
  </tbody>
</table>
<p>8677 rows × 41 columns</p>
</div>




```python
#We are building a model to target South Australia, so load in a map of it.
gawlshape="../data/SA/SA_STATE_POLYGON_shp"
shapeRead = shapefile.Reader(gawlshape)
shapes  = shapeRead.shapes()

#Save the boundary xy pairs in arrays we will use throughout the workflow
xval = [x[0] for x in shapes[1].points]
yval = [x[1] for x in shapes[1].points]
```


```python
# Subset the data, for a single Mineral target
commname='Mn'

#Pull out all the occurences of the commodity and go from there
comm=df[df['COMM_CODE'].str.contains(commname)]
comm=comm.reset_index(drop=True)
print("Shape of "+ commname, comm.shape)

# Can make further subsets of the data here if needed
#commsig=comm[comm.SIZE_VAL!="Low Significance"]
#comm=comm[comm.SIZE_VAL!="Low Significance"]
#comm=comm[comm.COX_CLASS == "Olympic Dam Cu-U-Au"]
#comm=comm[(comm.lon<max(xval)) & (comm.lon>min(xval)) & (comm.lat>min(yval)) & (comm.lat<max(yval))]

```

    Shape of Mn (115, 43)



```python
# For plotting
import matplotlib.pyplot as plt
```


```python
fig = plt.figure(figsize=(8,8))
ax = plt.axes()
ax.plot(df.LONGITUDE,df.LATITUDE,'b.',label="All Mineral Deposits")
ax.plot(comm.LONGITUDE,comm.LATITUDE,'yx',label=commname+" Deposits")

ax.plot(xval,yval,'grey',linestyle='--',linewidth=1,label='SA')
#ax.plot(comm.LONGITUDE, comm.LATITUDE, marker='o', linestyle='',markersize=5, color='y',label=commname+" Deposits")

plt.xlim(128.5,141.5)
plt.ylim(-38.5,-25.5)
plt.legend(loc=3)

plt.show()
```


    
![png](03-ML_workflow_files/03-ML_workflow_8_0.png)
    


## Step 2 - Wrangle the geophysical and geological datasets (predictor variables)
Many geophysical data are available for South Australia overlapping our target mineral locations. We may presume that certain mineral occurrences express a combination of geology and geophysics. We can train an algorithm to learn these associations and then use the same algorithm to make predictions for where unknown occurrences may be found. 

Here we load in the (slightly) pre-processed geophysical datasets and prepare them for further manipulations, data-mining, and machine learning. All of the full/raw datasets are available from https://map.sarig.sa.gov.au/. For this exercise we have simplified the datasets by reducing complexity and resolution. Grab additional processed datasets from [https://github.com/natbutter/gawler-exploration/tree/master/ML-DATA](https://github.com/natbutter/gawler-exploration/tree/master/ML-DATA)

### Resistivity xyz data


```python
#Read in the data
data_res=pd.read_csv("../data/AusLAMP_MT_Gawler_25.xyzr",
                     sep=',',header=0,names=['lat','lon','depth','resistivity'])
data_res
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
      <th>lat</th>
      <th>lon</th>
      <th>depth</th>
      <th>resistivity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-27.363931</td>
      <td>128.680796</td>
      <td>-25.0</td>
      <td>2.0007</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-27.659362</td>
      <td>128.662322</td>
      <td>-25.0</td>
      <td>1.9979</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-27.886602</td>
      <td>128.647965</td>
      <td>-25.0</td>
      <td>1.9948</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-28.061394</td>
      <td>128.636833</td>
      <td>-25.0</td>
      <td>1.9918</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-28.195844</td>
      <td>128.628217</td>
      <td>-25.0</td>
      <td>1.9885</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>11003</th>
      <td>-35.127716</td>
      <td>142.399588</td>
      <td>-25.0</td>
      <td>2.0079</td>
    </tr>
    <tr>
      <th>11004</th>
      <td>-35.230939</td>
      <td>142.408396</td>
      <td>-25.0</td>
      <td>2.0084</td>
    </tr>
    <tr>
      <th>11005</th>
      <td>-35.365124</td>
      <td>142.419903</td>
      <td>-25.0</td>
      <td>2.0085</td>
    </tr>
    <tr>
      <th>11006</th>
      <td>-35.539556</td>
      <td>142.434958</td>
      <td>-25.0</td>
      <td>2.0076</td>
    </tr>
    <tr>
      <th>11007</th>
      <td>-35.766303</td>
      <td>142.454694</td>
      <td>-25.0</td>
      <td>2.0049</td>
    </tr>
  </tbody>
</table>
<p>11008 rows × 4 columns</p>
</div>



This data is the Lat-Lon spatial location and the value of the feature at that location.


```python
fig = plt.figure(figsize=(8,8))
ax = plt.axes()
im=ax.scatter(data_res.lon,data_res.lat,s=4,c=data_res.resistivity,cmap="jet")
ax.plot(xval,yval,'grey',linestyle='--',linewidth=1,label='SA')
ax.plot(comm.LONGITUDE, comm.LATITUDE, marker='x', linestyle='',markersize=5, color='y',label=commname+" Deposits")

plt.xlim(128.5,141.5)
plt.ylim(-38.5,-25.5)
plt.legend(loc=3)

cbaxes = fig.add_axes([0.40, 0.18, 0.2, 0.015])
cbar = plt.colorbar(im, cax = cbaxes,orientation="horizontal",extend='both')
cbar.set_label('Resistivity $\Omega$.m', labelpad=10)
cbar.ax.xaxis.set_label_position('top')

plt.show()
```


    
![png](03-ML_workflow_files/03-ML_workflow_12_0.png)
    


### Faults and dykes vector polylines


```python
# For dealing with arrays 
import numpy as np
```


```python
#Get fault data neo
faultshape="../data/Faults/Faults.shp"
shapeRead = shapefile.Reader(faultshape)
shapes  = shapeRead.shapes()
Nshp    = len(shapes)

faultsNeo=[]
for i in range(0,Nshp):
    for j in shapes[i].points:
        faultsNeo.append([j[0],j[1]])
faultsNeo=np.array(faultsNeo)
faultsNeo
```




    array([[133.46269605, -27.41825034],
           [133.46770683, -27.42062991],
           [133.4723624 , -27.42259841],
           ...,
           [138.44613353, -35.36560605],
           [138.44160669, -35.36672662],
           [138.43805501, -35.36793484]])



This data is just a Lat-Lon location. Think how we can use this in a model.


```python
fig = plt.figure(figsize=(8,8))
ax = plt.axes()
plt.plot(faultsNeo[:,0],faultsNeo[:,1],'.',markersize=0.1,label="Neoproterozoic-Faults")
ax.plot(xval,yval,'grey',linestyle='--',linewidth=1,label='SA')
ax.plot(comm.LONGITUDE, comm.LATITUDE, marker='x', linestyle='',markersize=5, color='y',label=commname+" Deposits")

plt.xlim(128.5,141.5)
plt.ylim(-38.5,-25.5)
plt.legend(loc=3)

plt.show()
```


    
![png](03-ML_workflow_files/03-ML_workflow_17_0.png)
    


### Netcdf formatted raster grids - geophysics


```python
# For timing events
import time
# For making grids and reading netcdf data
import scipy
import scipy.io
```


```python
#Define a function to read the netcdf files
def readnc(filename):
    tic=time.time()
    rasterfile=filename
    data = scipy.io.netcdf_file(rasterfile,'r',mmap=False)
    xdata=data.variables['lon'][:]
    ydata=data.variables['lat'][:]
    zdata=np.array(data.variables['Band1'][:])
    data.close()
    
    toc=time.time()
    print("Loaded", rasterfile, "in", f'{toc-tic:.2f}s')
    print("Spacing x", f'{xdata[2]-xdata[1]:.2f}', 
          "y", f'{ydata[2]-ydata[1]:.2f}', 
          "Shape:", np.shape(zdata), "Min x:", np.min(xdata), "Max x:", np.max(xdata),
          "Min y:", np.min(ydata), f'Max y {np.max(ydata):.2f}')

    return(xdata,ydata,zdata,np.min(xdata),np.min(ydata),xdata[2]-xdata[1],ydata[2]-ydata[1])
```


```python
# Digital Elevation Model
x1,y1,z1,originx1,originy1,pixelx1,pixely1 = readnc("../data/sa-dem.nc")
# Total Magnetic Intensity
x2,y2,z2,originx2,originy2,pixelx2,pixely2 = readnc("../data/sa-mag-tmi.nc")
# Gravity
x3,y3,z3,originx3,originy3,pixelx3,pixely3 = readnc("../data/sa-grav.nc")
```

    Loaded ../data/sa-dem.nc in 0.01s
    Spacing x 0.01 y 0.01 Shape: (1208, 1201) Min x: 129.005 Max x: 141.005 Min y: -38.065 Max y -25.99
    Loaded ../data/sa-mag-tmi.nc in 0.00s
    Spacing x 0.01 y 0.01 Shape: (1208, 1201) Min x: 129.005 Max x: 141.005 Min y: -38.065 Max y -25.99
    Loaded ../data/sa-grav.nc in 0.00s
    Spacing x 0.01 y 0.01 Shape: (1208, 1201) Min x: 129.005 Max x: 141.005 Min y: -38.065 Max y -25.99



```python
fig = plt.figure(figsize=(8,8))
ax = plt.axes()
im=plt.pcolormesh(x1,y1,z1,cmap='Greys',shading='auto')
ax.plot(xval,yval,'grey',linestyle='--',linewidth=1,label='SA')
ax.plot(comm.LONGITUDE, comm.LATITUDE, marker='x', linestyle='',markersize=5, color='y',label=commname+" Deposits")

plt.xlim(128.5,141.5)
plt.ylim(-38.5,-25.5)
plt.legend(loc=3)

cbaxes = fig.add_axes([0.40, 0.18, 0.2, 0.015])
cbar = plt.colorbar(im, cax = cbaxes,orientation="horizontal",extend='both')
cbar.set_label('DEM (m)', labelpad=10)
cbar.ax.xaxis.set_label_position('top')

plt.show()
```


    
![png](03-ML_workflow_files/03-ML_workflow_22_0.png)
    


These data are raster grids. Essentially Lat-Lon-Value like the XYZ data, but represented in a different format.

### Categorical Geology in vector polygons


```python
#Archean basement geology
geolshape=shapefile.Reader("../data/Archaean_Early_Mesoprterzoic_polygons_shp/geology_archaean.shp")

recsArch   = geolshape.records()
shapesArch  = geolshape.shapes()
```


```python
# Print the field names in the shapefile
for i,field in enumerate(geolshape.fields):
    print(i-1,field[0]) 
```

    -1 DeletionFlag
    0 MAJORSTRAT
    1 SG_DESCRIP
    2 MAPUNIT
    3 SG_PROVINC
    4 DOMAIN
    5 AGE
    6 SEQUSET
    7 PRIMARYAGE
    8 OROGENYAGE
    9 INHERITAGE
    10 STRATNO
    11 STRATNAME
    12 STRATDESC
    13 GISCODE
    14 SUBDIVNAME
    15 SUBDIVSYMB
    16 PROVINCE
    17 MAXAGE
    18 MAXMOD
    19 MAXMETH
    20 MINAGE
    21 MINMOD
    22 MINMETH
    23 GLCODE



```python
fig = plt.figure(figsize=(8,8))
ax = plt.axes()

#index of the geology unit #4 #10 #12
geoindex = 4
#Gather all the unique Major Geology unit numbers
labs=[]
for i in recsArch:
    labs.append(i[geoindex])

geols = list(set(labs))

# Create a unique color for each geological unit label
color = plt.cm.tab20(np.linspace(0, 1, len(geols)))
cdict={}
for i, geol in enumerate(geols):
    cdict.update({geol:color[i]})
    
#Plot each of the geology polygons
legend1=[]
for i in range(len(shapesArch)):
    boundary = shapesArch[i].points
    xs = [x for x, y in shapesArch[i].points]
    ys = [y for x, y in shapesArch[i].points]
    c = cdict[recsArch[i][geoindex]]
    l1 = ax.fill(xs,ys,c=c,label=recsArch[i][geoindex])
    legend1.append(l1)
      
#Plot the extra stuff
l2 = ax.plot(xval,yval,'grey',linestyle='--',linewidth=1,label='SA')
l3 = ax.plot(comm.LONGITUDE, comm.LATITUDE, 
        marker='s', markeredgecolor='k', linestyle='',markersize=4, color='y',
        label=commname+" Deposits")

#Todo: Split the legends
#ax.legend([l2,l3],['SA',commname+" Deposits"],loc=3)

#Legend without duplicate values
handles, labels = ax.get_legend_handles_labels()
unique = [(h, l) for i, (h, l) in enumerate(zip(handles, labels)) if l not in labels[:i]]
ax.legend(*zip(*unique), bbox_to_anchor = (1.02, 1.01), ncol=3)

plt.xlim(128.5,141.5)
plt.ylim(-38.5,-25.5)
#plt.legend(loc=3) #bbox_to_anchor = (1.05, 0.6))

plt.show()
```


    
![png](03-ML_workflow_files/03-ML_workflow_27_0.png)
    


**Take a moment to appreciate the various methods you have used just to load the data!**

Now we need to think about what we actually want to achieve? What is our goal here? This will determine what kind of data analysis/manipulation we need to make here. Consider the flow diagram for [choosing the right machine learning method](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html).

## Step 3 - Assign geophys values to target locations

We need to assign the values of each of these geophysical datasets (predictor variables) to the target class (i.e. mineral deposit locations). 
The assumption being that the occurrence of some mineral deposit (e.g. Cu) is a function of x1, x2, x3, x4, x5, x6. 
Where the Resistivity is x1, the distance to a Neoprotezoic fault is x2, the value of DEM, magnetic TMI, and Gravity is x3, x4, and x5, and the geological basement unit is x6.


```python
# Make a Target DataFrame of the points we want to interrogate the features for
td1 = comm[['LONGITUDE', 'LATITUDE']].copy()
```

### Resistivity


```python
# For making KD Trees
import scipy.spatial
```


```python
# Define a function which "coregisters" a point from a bunch of other points.
def coregPoint(tree,point,region,retval='index'):
    '''
    Finds the nearest neighbour to a point from a bunch of other points
    tree - a scipy CKTree to search for the point over
    point - array([longitude,latitude])
    region - integer, same units as data
    '''
    dists, indexes = tree.query(point,k=1,distance_upper_bound=region) 

    if retval=='index':
        return (indexes)
    elif retval=='dists':
        return(dists)
    
```


```python
# Find the values of the resetivity grid for each lat/lon deposit location.

# Make a search-tree of the point-pairs for fast lookup of nearest matches
treeres = scipy.spatial.cKDTree(np.c_[data_res.lon,data_res.lat])

# Perform the search for each point
indexes = td1.apply(
    lambda x: coregPoint(treeres,np.array([x.LONGITUDE, x.LATITUDE]),1,retval='index'), axis=1)
```


```python
td1['res'] = data_res.loc[indexes].resistivity.values
td1
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
      <th>LONGITUDE</th>
      <th>LATITUDE</th>
      <th>res</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>139.179436</td>
      <td>-29.877637</td>
      <td>2.2135</td>
    </tr>
    <tr>
      <th>1</th>
      <td>138.808767</td>
      <td>-30.086296</td>
      <td>2.3643</td>
    </tr>
    <tr>
      <th>2</th>
      <td>138.752281</td>
      <td>-30.445684</td>
      <td>2.1141</td>
    </tr>
    <tr>
      <th>3</th>
      <td>138.530506</td>
      <td>-30.533225</td>
      <td>2.2234</td>
    </tr>
    <tr>
      <th>4</th>
      <td>138.887019</td>
      <td>-30.565479</td>
      <td>2.1982</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>110</th>
      <td>136.059715</td>
      <td>-34.327929</td>
      <td>3.4926</td>
    </tr>
    <tr>
      <th>111</th>
      <td>138.016821</td>
      <td>-35.733084</td>
      <td>2.0868</td>
    </tr>
    <tr>
      <th>112</th>
      <td>139.250036</td>
      <td>-34.250155</td>
      <td>1.9811</td>
    </tr>
    <tr>
      <th>113</th>
      <td>135.905480</td>
      <td>-34.425866</td>
      <td>2.7108</td>
    </tr>
    <tr>
      <th>114</th>
      <td>135.835578</td>
      <td>-34.509779</td>
      <td>3.1224</td>
    </tr>
  </tbody>
</table>
<p>115 rows × 3 columns</p>
</div>



### Faults


```python
#Same for the fault data 
# but this time we get the "distance to the point", rather than the value at that point.
treefaults = scipy.spatial.cKDTree(faultsNeo)

dists = td1.apply(
    lambda x: coregPoint(treefaults,np.array([x.LONGITUDE, x.LATITUDE]),100,retval='dists'), axis=1)
```


```python
td1['faults'] = dists
td1
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
      <th>LONGITUDE</th>
      <th>LATITUDE</th>
      <th>res</th>
      <th>faults</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>139.179436</td>
      <td>-29.877637</td>
      <td>2.2135</td>
      <td>0.010691</td>
    </tr>
    <tr>
      <th>1</th>
      <td>138.808767</td>
      <td>-30.086296</td>
      <td>2.3643</td>
      <td>0.103741</td>
    </tr>
    <tr>
      <th>2</th>
      <td>138.752281</td>
      <td>-30.445684</td>
      <td>2.1141</td>
      <td>0.006659</td>
    </tr>
    <tr>
      <th>3</th>
      <td>138.530506</td>
      <td>-30.533225</td>
      <td>2.2234</td>
      <td>0.013925</td>
    </tr>
    <tr>
      <th>4</th>
      <td>138.887019</td>
      <td>-30.565479</td>
      <td>2.1982</td>
      <td>0.007356</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>110</th>
      <td>136.059715</td>
      <td>-34.327929</td>
      <td>3.4926</td>
      <td>0.526835</td>
    </tr>
    <tr>
      <th>111</th>
      <td>138.016821</td>
      <td>-35.733084</td>
      <td>2.0868</td>
      <td>0.002451</td>
    </tr>
    <tr>
      <th>112</th>
      <td>139.250036</td>
      <td>-34.250155</td>
      <td>1.9811</td>
      <td>0.027837</td>
    </tr>
    <tr>
      <th>113</th>
      <td>135.905480</td>
      <td>-34.425866</td>
      <td>2.7108</td>
      <td>0.670323</td>
    </tr>
    <tr>
      <th>114</th>
      <td>135.835578</td>
      <td>-34.509779</td>
      <td>3.1224</td>
      <td>0.776152</td>
    </tr>
  </tbody>
</table>
<p>115 rows × 4 columns</p>
</div>



### Geophysics


```python
# Define a function which "coregisters" a point within a raster.
def get_coords_at_point(originx,originy,pixelx,pixely,lon,lat):
    '''
    Given a point in some coordinate reference (e.g. lat/lon)
    Find the closest point to that in an array (e.g. a raster)
    and return the index location of that point in the raster.
    INPUTS
        "output from "gdal_data.GetGeoTransform()"
    originx: first point in first axis
    originy: first point in second axis
    pixelx: difference between x points
    pixely: difference between y points
    
    lon: x/row-coordinate of interest
    lat: y/column-coordinate of interest
    
    RETURNS
    col: x index value from the raster
    row: y index value from the raster
    '''
    row = int((lon - originx)/pixelx)
    col = int((lat - originy)/pixely)

    return (col, row)


# Pass entire array of latlon and raster info to us in get_coords_at_point
def rastersearch(latlon,raster,originx,originy,pixelx,pixely):
    zlist=[]
    for lon,lat in zip(latlon.LONGITUDE,latlon.LATITUDE):
        try:
            zlist.append(raster[get_coords_at_point(originx,originy,pixelx,pixely,lon,lat)])
        except:
            zlist.append(np.nan)
            
    return(zlist)
```


```python
td1['dem'] = rastersearch(td1,z1,originx1,originy1,pixelx1,pixely1)
td1['mag'] = rastersearch(td1,z2,originx2,originy2,pixelx2,pixely2)
td1['grav'] = rastersearch(td1,z3,originx3,originy3,pixelx3,pixely3)
```


```python
td1
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
      <th>LONGITUDE</th>
      <th>LATITUDE</th>
      <th>res</th>
      <th>faults</th>
      <th>dem</th>
      <th>mag</th>
      <th>grav</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>139.179436</td>
      <td>-29.877637</td>
      <td>2.2135</td>
      <td>0.010691</td>
      <td>187.297424</td>
      <td>-118.074890</td>
      <td>1.852599</td>
    </tr>
    <tr>
      <th>1</th>
      <td>138.808767</td>
      <td>-30.086296</td>
      <td>2.3643</td>
      <td>0.103741</td>
      <td>179.499237</td>
      <td>-209.410507</td>
      <td>-12.722121</td>
    </tr>
    <tr>
      <th>2</th>
      <td>138.752281</td>
      <td>-30.445684</td>
      <td>2.1141</td>
      <td>0.006659</td>
      <td>398.336823</td>
      <td>-159.566422</td>
      <td>-6.249788</td>
    </tr>
    <tr>
      <th>3</th>
      <td>138.530506</td>
      <td>-30.533225</td>
      <td>2.2234</td>
      <td>0.013925</td>
      <td>335.983429</td>
      <td>-131.176437</td>
      <td>-11.665316</td>
    </tr>
    <tr>
      <th>4</th>
      <td>138.887019</td>
      <td>-30.565479</td>
      <td>2.1982</td>
      <td>0.007356</td>
      <td>554.278198</td>
      <td>-192.363297</td>
      <td>-1.025702</td>
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
    </tr>
    <tr>
      <th>110</th>
      <td>136.059715</td>
      <td>-34.327929</td>
      <td>3.4926</td>
      <td>0.526835</td>
      <td>45.866119</td>
      <td>-244.067841</td>
      <td>11.410070</td>
    </tr>
    <tr>
      <th>111</th>
      <td>138.016821</td>
      <td>-35.733084</td>
      <td>2.0868</td>
      <td>0.002451</td>
      <td>145.452789</td>
      <td>-203.566940</td>
      <td>18.458364</td>
    </tr>
    <tr>
      <th>112</th>
      <td>139.250036</td>
      <td>-34.250155</td>
      <td>1.9811</td>
      <td>0.027837</td>
      <td>276.489319</td>
      <td>-172.889587</td>
      <td>-1.714886</td>
    </tr>
    <tr>
      <th>113</th>
      <td>135.905480</td>
      <td>-34.425866</td>
      <td>2.7108</td>
      <td>0.670323</td>
      <td>162.431747</td>
      <td>569.713684</td>
      <td>15.066316</td>
    </tr>
    <tr>
      <th>114</th>
      <td>135.835578</td>
      <td>-34.509779</td>
      <td>3.1224</td>
      <td>0.776152</td>
      <td>89.274399</td>
      <td>64.385925</td>
      <td>24.267015</td>
    </tr>
  </tbody>
</table>
<p>115 rows × 7 columns</p>
</div>




```python
# Check we got it right.
# Plot a grid, and our interrogated points

fig = plt.figure(figsize=(8,8))
ax = plt.axes()
im=plt.pcolormesh(x3,y3,z3,cmap='jet',shading='auto',vmin=min(td1.grav),vmax=max(td1.grav))
#ax.plot(xval,yval,'grey',linestyle='--',linewidth=1,label='SA')
#ax.plot(comm.LONGITUDE, comm.LATITUDE, marker='o', linestyle='',markersize=5, color='y',label=commname+" Deposits")

ax.scatter(td1.LONGITUDE, td1.LATITUDE, s=20, c=td1.grav,
           label=commname+" Gravity",cmap='jet',vmin=min(td1.grav),vmax=max(td1.grav),edgecolors='white')

plt.xlim(138,140)
plt.ylim(-32,-30)
plt.legend(loc=3)

cbaxes = fig.add_axes([0.40, 0.18, 0.2, 0.015])
cbar = plt.colorbar(im, cax = cbaxes,orientation="horizontal",extend='both')
cbar.set_label('Gravity (gal)', labelpad=10)
cbar.ax.xaxis.set_label_position('top')

plt.show()
```


    
![png](03-ML_workflow_files/03-ML_workflow_42_0.png)
    


### Geology


```python
# For dealing with shapefile components
from shapely.geometry import Point
from shapely.geometry import shape

#Define a function to find what polygon a point lives inside (speed imporivements can be made here)
def shapeExplore(lon,lat,shapes,recs,record):
    #'record' is the column index you want returned
    for i in range(len(shapes)):
        boundary = shapes[i]
        if Point((lon,lat)).within(shape(boundary)):
            return(recs[i][record])
    #if you have been through the loop with no result
    return('-9999')
```


```python
%%time
geoindex = 4
td1['geol']=td1.apply(lambda x: shapeExplore(x.LONGITUDE, x.LATITUDE, shapesArch,recsArch,geoindex), axis=1)
```

    CPU times: user 6.23 s, sys: 0 ns, total: 6.23 s
    Wall time: 6.22 s



```python
td1
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
      <th>LONGITUDE</th>
      <th>LATITUDE</th>
      <th>res</th>
      <th>faults</th>
      <th>dem</th>
      <th>mag</th>
      <th>grav</th>
      <th>geol</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>139.179436</td>
      <td>-29.877637</td>
      <td>2.2135</td>
      <td>0.010691</td>
      <td>187.297424</td>
      <td>-118.074890</td>
      <td>1.852599</td>
      <td>Crustal element Muloorina</td>
    </tr>
    <tr>
      <th>1</th>
      <td>138.808767</td>
      <td>-30.086296</td>
      <td>2.3643</td>
      <td>0.103741</td>
      <td>179.499237</td>
      <td>-209.410507</td>
      <td>-12.722121</td>
      <td>Crustal element Adelaide</td>
    </tr>
    <tr>
      <th>2</th>
      <td>138.752281</td>
      <td>-30.445684</td>
      <td>2.1141</td>
      <td>0.006659</td>
      <td>398.336823</td>
      <td>-159.566422</td>
      <td>-6.249788</td>
      <td>Crustal element Adelaide</td>
    </tr>
    <tr>
      <th>3</th>
      <td>138.530506</td>
      <td>-30.533225</td>
      <td>2.2234</td>
      <td>0.013925</td>
      <td>335.983429</td>
      <td>-131.176437</td>
      <td>-11.665316</td>
      <td>Crustal element Adelaide</td>
    </tr>
    <tr>
      <th>4</th>
      <td>138.887019</td>
      <td>-30.565479</td>
      <td>2.1982</td>
      <td>0.007356</td>
      <td>554.278198</td>
      <td>-192.363297</td>
      <td>-1.025702</td>
      <td>Crustal element Adelaide</td>
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
    </tr>
    <tr>
      <th>110</th>
      <td>136.059715</td>
      <td>-34.327929</td>
      <td>3.4926</td>
      <td>0.526835</td>
      <td>45.866119</td>
      <td>-244.067841</td>
      <td>11.410070</td>
      <td>Cleve, Spencer, Olympic Domains</td>
    </tr>
    <tr>
      <th>111</th>
      <td>138.016821</td>
      <td>-35.733084</td>
      <td>2.0868</td>
      <td>0.002451</td>
      <td>145.452789</td>
      <td>-203.566940</td>
      <td>18.458364</td>
      <td>Crustal element Kanmantoo SW</td>
    </tr>
    <tr>
      <th>112</th>
      <td>139.250036</td>
      <td>-34.250155</td>
      <td>1.9811</td>
      <td>0.027837</td>
      <td>276.489319</td>
      <td>-172.889587</td>
      <td>-1.714886</td>
      <td>Crustal element Kanmantoo Main</td>
    </tr>
    <tr>
      <th>113</th>
      <td>135.905480</td>
      <td>-34.425866</td>
      <td>2.7108</td>
      <td>0.670323</td>
      <td>162.431747</td>
      <td>569.713684</td>
      <td>15.066316</td>
      <td>Cleve Domain</td>
    </tr>
    <tr>
      <th>114</th>
      <td>135.835578</td>
      <td>-34.509779</td>
      <td>3.1224</td>
      <td>0.776152</td>
      <td>89.274399</td>
      <td>64.385925</td>
      <td>24.267015</td>
      <td>Cleve Domain</td>
    </tr>
  </tbody>
</table>
<p>115 rows × 8 columns</p>
</div>



**Congrats, you now have an ML dataset ready to go!**

Almost... but what is the target? Let's make a binary classifier.

## Step 4 - Generate a "non-deposit" dataset
We have a set of locations where a certain mineral deposit occurs along with the values of various geophysical parameters at those locations. To identify what values of the geophysics are associated with a mineral deposit then we need a representation of the "background noise" of those parameters, i.e. what the values are when there is no mineral deposit.

This step is important. There are numerous ways to generate our non-deposit set, each with different benefits and trade-offs. The randomisation of points throughout *some* domain appears to be robust. But you must think, is this domain a reasonable estimation of "background" geophysics/geology? Why are you picking these locations as non-deposits? Will they be over/under-representing actual deposits? Will they be over/under-representing actual non-deposits?


```python
#Now make a set of "non-deposits" using a random location within our exploration area
lats_rand=np.random.uniform(low=min(df.LATITUDE), high=max(df.LATITUDE), size=len(comm.LATITUDE))
lons_rand=np.random.uniform(low=min(df.LONGITUDE), high=max(df.LONGITUDE), size=len(comm.LONGITUDE))

print("Produced", len(lats_rand),len(lons_rand), "latitude-longitude pairs for non-deposits.")
```

    Produced 115 115 latitude-longitude pairs for non-deposits.



```python
# Where are these randomised "non deposits"
fig = plt.figure(figsize=(8,8))
ax = plt.axes()

ax.plot(xval,yval,'grey',linestyle='--',linewidth=1,label='SA')

ax.plot(lons_rand, lats_rand, 
        marker='.', linestyle='',markersize=1, color='b',label="Random Samples")

ax.plot(td1.LONGITUDE, td1.LATITUDE, 
        marker='x', linestyle='',markersize=5, color='y',label=commname+" Deposits")

plt.xlim(128.5,141.5)
plt.ylim(-38.5,-25.5)
plt.legend(loc=3)

plt.show()
```


    
![png](03-ML_workflow_files/03-ML_workflow_49_0.png)
    


We must do the same coregistration/interrogation of the different data layers for our randomised "non-deposit" data.


```python
%%time

td2 = pd.DataFrame({'LONGITUDE': lons_rand, 'LATITUDE': lats_rand})
                   
# Res
indexes = td2.apply(
    lambda x: coregPoint(treeres,np.array([x.LONGITUDE, x.LATITUDE]),10,retval='index'), axis=1)
    
td2['res'] = data_res.loc[indexes].resistivity.values

# Faults
td2['faults'] = td2.apply(
    lambda x: coregPoint(treefaults,np.array([x.LONGITUDE, x.LATITUDE]),100,retval='dists'), axis=1)

# Geophys
td2['dem'] = rastersearch(td2,z1,originx1,originy1,pixelx1,pixely1)
td2['mag'] = rastersearch(td2,z2,originx2,originy2,pixelx2,pixely2)
td2['grav'] = rastersearch(td2,z3,originx3,originy3,pixelx3,pixely3)

#Geology
td2['geol']=td2.apply(lambda x: shapeExplore(x.LONGITUDE, x.LATITUDE, shapesArch,recsArch,geoindex), axis=1)
```

    CPU times: user 15.3 s, sys: 0 ns, total: 15.3 s
    Wall time: 15.3 s



```python
#Add flag indicating classification label
td1['deposit']=1
td2['deposit']=0
```


```python
fv = pd.concat([td1,td2],axis=0,ignore_index=True)
fv
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
      <th>LONGITUDE</th>
      <th>LATITUDE</th>
      <th>res</th>
      <th>faults</th>
      <th>...</th>
      <th>mag</th>
      <th>grav</th>
      <th>geol</th>
      <th>deposit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>139.179436</td>
      <td>-29.877637</td>
      <td>2.2135</td>
      <td>0.010691</td>
      <td>...</td>
      <td>-118.074890</td>
      <td>1.852599</td>
      <td>Crustal element Muloorina</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>138.808767</td>
      <td>-30.086296</td>
      <td>2.3643</td>
      <td>0.103741</td>
      <td>...</td>
      <td>-209.410507</td>
      <td>-12.722121</td>
      <td>Crustal element Adelaide</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>138.752281</td>
      <td>-30.445684</td>
      <td>2.1141</td>
      <td>0.006659</td>
      <td>...</td>
      <td>-159.566422</td>
      <td>-6.249788</td>
      <td>Crustal element Adelaide</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>138.530506</td>
      <td>-30.533225</td>
      <td>2.2234</td>
      <td>0.013925</td>
      <td>...</td>
      <td>-131.176437</td>
      <td>-11.665316</td>
      <td>Crustal element Adelaide</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>138.887019</td>
      <td>-30.565479</td>
      <td>2.1982</td>
      <td>0.007356</td>
      <td>...</td>
      <td>-192.363297</td>
      <td>-1.025702</td>
      <td>Crustal element Adelaide</td>
      <td>1</td>
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
    </tr>
    <tr>
      <th>225</th>
      <td>137.379563</td>
      <td>-27.239945</td>
      <td>1.9918</td>
      <td>1.585305</td>
      <td>...</td>
      <td>-49.557037</td>
      <td>-14.879361</td>
      <td>Noolyeana Domain</td>
      <td>0</td>
    </tr>
    <tr>
      <th>226</th>
      <td>132.160057</td>
      <td>-33.464682</td>
      <td>-0.8385</td>
      <td>0.717271</td>
      <td>...</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>Nuyts, Cleve, Spencer, Gawler Range Volcanics</td>
      <td>0</td>
    </tr>
    <tr>
      <th>227</th>
      <td>136.717075</td>
      <td>-33.605361</td>
      <td>2.6090</td>
      <td>0.443433</td>
      <td>...</td>
      <td>-228.808777</td>
      <td>7.512496</td>
      <td>Cleve Domain</td>
      <td>0</td>
    </tr>
    <tr>
      <th>228</th>
      <td>136.970578</td>
      <td>-30.732843</td>
      <td>1.9818</td>
      <td>0.656012</td>
      <td>...</td>
      <td>466.422302</td>
      <td>-20.277115</td>
      <td>Cleve, Spencer, Olympic Domains</td>
      <td>0</td>
    </tr>
    <tr>
      <th>229</th>
      <td>138.328646</td>
      <td>-35.060603</td>
      <td>0.5226</td>
      <td>0.088926</td>
      <td>...</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td></td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>230 rows × 9 columns</p>
</div>




```python
# Save all our hard work to a csv file for more hacking to come!
fv.to_csv('../data/fv.csv',index=False)
```

# Exploratory Data Analysis

This is often the point you receive the data in (if you are using any well-formed datasets). But in reality 90% of the time is doing weird data wrangling steps like what we have done. Then 9% is spent exploring your dataset and understanding it more, dealing with missing data, observing correlations. This is often an iterative process. Let's do some simple visualisations.

Note: the last 1% of time is actually applying the ML algorithm! 

Note2: These percentages are totally made up, but feeeel about right.


```python
#Get information about index type and column types, non-null values and memory usage.
fv.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 230 entries, 0 to 229
    Data columns (total 9 columns):
     #   Column     Non-Null Count  Dtype  
    ---  ------     --------------  -----  
     0   LONGITUDE  230 non-null    float64
     1   LATITUDE   230 non-null    float64
     2   res        230 non-null    float64
     3   faults     230 non-null    float64
     4   dem        227 non-null    float64
     5   mag        227 non-null    float64
     6   grav       227 non-null    float64
     7   geol       230 non-null    object 
     8   deposit    230 non-null    int64  
    dtypes: float64(7), int64(1), object(1)
    memory usage: 16.3+ KB



```python
# For nice easy data vis plots
import seaborn as sns
```


```python
missingNo = fv.isnull().sum(axis = 0).sort_values(ascending = False)
missingNo = missingNo[missingNo.values  > 0]
missingNo

sns.barplot(x=missingNo.values, y=missingNo.index);
```


    
![png](03-ML_workflow_files/03-ML_workflow_58_0.png)
    



```python
import upsetplot
```


```python
missing_cols = missingNo.index[:5].tolist()
missing_counts = (fv.loc[:, missing_cols]
                  .isnull()
                  .groupby(missing_cols)
                  .size())

upsetplot.plot(missing_counts);
```


    
![png](03-ML_workflow_files/03-ML_workflow_60_0.png)
    



```python
# Plot historgrams and scatter plots for each combination of features.
sns.pairplot(fv,hue='deposit',palette="Set1",diag_kind="auto")
```




    <seaborn.axisgrid.PairGrid at 0x7f5676a4d880>




    
![png](03-ML_workflow_files/03-ML_workflow_61_1.png)
    



```python
#Plot a heatmap for how correlated each of the features are
corr = fv.corr() 

sns.heatmap(corr,
            cmap=plt.cm.BrBG, 
            vmin=-0.5, vmax=0.5, 
            square=True,
            xticklabels=True, yticklabels=True,
            );
```


    
![png](03-ML_workflow_files/03-ML_workflow_62_0.png)
    



```python
for i in ['res', 'faults', 'dem', 'mag', 'grav']:
    ax = sns.boxplot(x='deposit',y=i, data=fv)
    plt.show()
```


    
![png](03-ML_workflow_files/03-ML_workflow_63_0.png)
    



    
![png](03-ML_workflow_files/03-ML_workflow_63_1.png)
    



    
![png](03-ML_workflow_files/03-ML_workflow_63_2.png)
    



    
![png](03-ML_workflow_files/03-ML_workflow_63_3.png)
    



    
![png](03-ML_workflow_files/03-ML_workflow_63_4.png)
    


# Machine Learning

We now have a clean dataset, we know a bit about, let's try and measure some inferences.

### ML Classification
This is where the ML classifier is defined. We can substitue our favourite ML technique here, and tune model variables as desired. As always the [scikit-learn documentation](https://scikit-learn.org/stable/user_guide.html) is a great starting point to learn how these algorithms work.


```python
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

from sklearn.neural_network import MLPClassifier
```


```python
#Create the 'feature vector' and a 'target classification vector'
features=fv.dropna().iloc[:,2:-1]
targets=fv.dropna().deposit

features.columns
```




    Index(['res', 'faults', 'dem', 'mag', 'grav', 'geol'], dtype='object')




```python
numfts = ['res', 'faults', 'dem', 'mag', 'grav']
catfts = ['geol']
```


```python
for i in features.geol:
    if not isinstance(i, str):
        print(i)
```


```python
#Create the ML classifier with numerical and categorical data
#Scale, and replace missing values
numeric_transformer = Pipeline(steps=[
    ('imputer',SimpleImputer(missing_values=-9999., strategy='median')),
    ('scaler', StandardScaler())])

#Encode categorical data and fill missing values with default 0
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))])

#Combine numerical and categorical data
preprocessor = ColumnTransformer(transformers=[
        ('num', numeric_transformer, numfts),
        ('cat', categorical_transformer, catfts)])

# Append classifier to preprocessing pipeline.
# Now we have a full prediction pipeline.
rf = Pipeline(steps=[('preprocessor', preprocessor),
                ('classifier', RandomForestClassifier(random_state=1))])
                #('classifier', MLPClassifier(solver='adam', alpha=0.001, max_iter=10000))])

```


```python
print('Tranining the Clasifier...')
rf.fit(features,targets)

print("Done RF. Now scoring...")
scores = cross_val_score(rf, features,targets, cv=5)

print("RF 5-fold cross validation Scores:", scores)
print("SCORE Mean: %.2f" % np.mean(scores), "STD: %.2f" % np.std(scores), "\n")

plt.plot(targets.values,'b-',label='Target (expected)')
plt.plot(rf.predict(features),'rx',label='Prediction')
plt.xlabel("Feature set")
plt.ylabel("Target/Prediction")
plt.legend(loc=7)
```

    Tranining the Clasifier...
    Done RF. Now scoring...
    RF 5-fold cross validation Scores: [0.97777778 0.88888889 0.95555556 1.         0.79545455]
    SCORE Mean: 0.92 STD: 0.07 
    





    <matplotlib.legend.Legend at 0x7f8733744f10>




    
![png](03-ML_workflow_files/03-ML_workflow_71_2.png)
    



```python
print("Features:",np.shape(features),"Targets:",np.shape(targets))
rf.fit(features,targets)
scores = cross_val_score(rf, features,targets, cv=5)
print("RF CV-Scores: ",scores)
print("CV-SCORE Mean: %.2f" % np.mean(scores), "STD: %.2f" % np.std(scores))
#print("OOB score:",rf.steps[-1][1].oob_score_)

print("Targets (expected result):")
print(targets.values)
print("Prediction (actual result):")
print(rf.predict(features))
```

    Features: (224, 6) Targets: (224,)
    RF CV-Scores:  [0.97777778 0.88888889 0.95555556 1.         0.79545455]
    CV-SCORE Mean: 0.92 STD: 0.07
    Targets (expected result):
    [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
     1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
     1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
     1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
     0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
     0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
     0 0]
    Prediction (actual result):
    [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
     1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
     1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
     1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
     0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
     0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
     0 0]



```python
# Gather the importance measures
ft_imp=[]
ft_lab=[]

for i,lab in enumerate(np.append(numfts,rf['preprocessor'].transformers_[1][1]['onehot'].get_feature_names_out(catfts))):
    ft_imp.append(rf.steps[-1][1].feature_importances_[i])
    ft_lab.append(lab)
```


```python
#Make the bar plot
ft_imps, ft_labs = (list(t) for t in zip(*sorted(zip(ft_imp,ft_lab))))
datalength=len(ft_imp)

#Create a new figure
fig,ax = plt.subplots(figsize=(4,10))

#Plot the bar graph
rects=ax.barh(np.arange(0, datalength, step=1),ft_imps)
ax.set_yticks(np.arange(0, datalength, step=1))
ax.set_yticklabels(ft_labs)
ax.set_xlabel('Feature Importance')
print("From the Random Forest ML algorithm\nthese are the the most significant features for predicting the target bins.\n")

plt.show()
```

    From the Random Forest ML algorithm
    these are the the most significant features for predicting the target bins.
    



    
![png](03-ML_workflow_files/03-ML_workflow_74_1.png)
    


# Find where to dig!

Now we have a trained model we can pass it NEW data, that is values for all the geopysical parameters, and it will give us a prediction for whether there is a deposit there or not. Simple.


```python
res1= [2.2,2.2]
faults1 = [0.01,2.2]
dem1 = [187,2.2]
mag1= [-118,2.2]
grav = [1.8,2.2]
geol = ['Crustal element Muloorina','Crustal element Muloorina']

targets = pd.DataFrame({'res':res1,'faults':faults1,'dem':dem1,'mag':mag1,'grav':grav,'geol':geol})
print(targets)
#print(targets.reshape(1, -11))
rf.predict_proba(targets)
```

       res  faults    dem    mag  grav                       geol
    0  2.2    0.01  187.0 -118.0   1.8  Crustal element Muloorina
    1  2.2    2.20    2.2    2.2   2.2  Crustal element Muloorina





    array([[0.18, 0.82],
           [0.81, 0.19]])




```python
# Better - Make a grid of target locations over an entire area
#100x100 takes about 1 hour! 10x10 takes about 1 minute
grid_x, grid_y = np.mgrid[130:140:10j,-36:-26:10j]

# Now we want to get the geophys values for every single point on this grid
# Which we will then apply our model to!
```


```python
%%time

tdf = pd.DataFrame({'LONGITUDE': grid_x.reshape(grid_x.size), 'LATITUDE': grid_y.reshape(grid_y.size)})
                   
# Res
indexes = tdf.apply(
    lambda x: coregPoint(treeres,np.array([x.LONGITUDE, x.LATITUDE]),10,retval='index'), axis=1)

tdf['res'] = data_res.loc[indexes].resistivity.values
print("Done res")

# Faults
tdf['faults'] = tdf.apply(
    lambda x: coregPoint(treefaults,np.array([x.LONGITUDE, x.LATITUDE]),100,retval='dists'), axis=1)
print("Done faults")

# Geophys
tdf['dem'] = rastersearch(tdf,z1,originx1,originy1,pixelx1,pixely1)
tdf['mag'] = rastersearch(tdf,z2,originx2,originy2,pixelx2,pixely2)
tdf['grav'] = rastersearch(tdf,z3,originx3,originy3,pixelx3,pixely3)
print("Done rasters")

# Geology
tdf['geol']=tdf.apply(lambda x: shapeExplore(x.LONGITUDE, x.LATITUDE, shapesArch,recsArch,geoindex), axis=1)
print("Done!")
```

    Done res
    Done faults
    Done rasters
    Done!
    CPU times: user 17min 19s, sys: 155 ms, total: 17min 19s
    Wall time: 17min 19s



```python
# Save all our hard work to a csv file for more hacking to come!
tdf.to_csv('../data/tdf_10.csv',index=False)
#tdf.read_csv('data/tdf_100.csv') #Read the file in if you need
```


```python
#Apply the trained ML to our gridded data to determine the probabilities at each of the points
print('RF...')
pRF_map=np.array(rf.predict_proba(tdf.iloc[:,2:]))
print("Done RF")
```

    RF...
    Done RF



```python
#X, Y = np.meshgrid(xi, yi)
gridZ = scipy.interpolate.griddata((tdf.LONGITUDE, tdf.LATITUDE), pRF_map[:,1], (grid_x, grid_y),method='linear')
```


```python
fig = plt.figure(figsize=(10,10))
ax = plt.axes()
im=plt.pcolormesh(grid_x,grid_y,gridZ,cmap='bwr',shading='auto')
ax.plot(xval,yval,'grey',linestyle='--',linewidth=1,label='SA')
ax.plot(fv[fv.deposit==1].LONGITUDE, fv[fv.deposit==1].LATITUDE, 
        marker='x', linestyle='',markersize=5, color='y',label=commname+" Deposits")
ax.plot(fv[fv.deposit==0].LONGITUDE, fv[fv.deposit==0].LATITUDE, 
        marker='.', linestyle='',markersize=1, color='b',label="Random Samples")

plt.xlim(128.5,141.5)
plt.ylim(-38.5,-25.5)
plt.legend(loc=3)

cbaxes = fig.add_axes([0.40, 0.18, 0.2, 0.015])
cbar = plt.colorbar(im, cax = cbaxes,orientation="horizontal")
cbar.set_label('Probability of Mineral Depost', labelpad=10)
cbar.ax.xaxis.set_label_position('top')

plt.show()
```


    
![png](03-ML_workflow_files/03-ML_workflow_82_0.png)
    

