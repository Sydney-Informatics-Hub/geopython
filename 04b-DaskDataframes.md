# Working with Big Data using Dask

<div class="questions">  
### Questions

- "Use a modern python library and elegant syntax for performance benefits"
- "How do I deal with large irregular data and show me some real world examples of Dask"
</div>

<div class="objectives">  
### Objectives

- "Intro to Dask concepts and High level datastructures"
- "Use dask dataframes"
- "Use dask delayed functions"
- "Deal with semi-structured and unstructured data in memory efficient and parallel manner"
- "Show me examples of using Dask on Large Datasets"
</div>

## DASK
Dask is a flexible library for parallel computing in Python.

Dask is composed of two parts:
Dynamic task scheduling optimized for computation. This is similar to Airflow, Luigi, Celery, or Make, but optimized for interactive computational workloads. “Big Data” collections like parallel arrays, dataframes, and lists that extend common interfaces like ***NumPy, Pandas, or Python iterators*** to larger-than-memory or distributed environments. These parallel collections run on top of dynamic task schedulers.

Dask emphasizes the following virtues:

* Familiar: Provides parallelized NumPy array and Pandas DataFrame objects
* Flexible: Provides a task scheduling interface for more custom workloads and integration with other projects.
* Native: Enables distributed computing in pure Python with access to the PyData stack.
* Fast: Operates with low overhead, low latency, and minimal serialization necessary for fast numerical algorithms
* Scales up: Runs resiliently on clusters with 1000s of cores
* Scales down: Trivial to set up and run on a laptop in a single process
* Responsive: Designed with interactive computing in mind, it provides rapid feedback and diagnostics to aid humans

<figure>
  <img src="./fig/dask_pic1.png" style="margin:10px;width:600px"/>
  <figcaption> Dask High Level Schema <a href="https://docs.dask.org/en/latest/">https://docs.dask.org/en/latest/</a></figcaption>
</figure><br>

Dask provides high level collections - these are ***Dask Dataframes, bags, and arrays***.
On a low level, dask dynamic task schedulers to scale up or down processes, and presents parallel computations by implementing task graphs. It provides an alternative to scaling out tasks instead of threading (IO Bound) and multiprocessing (cpu bound).

A Dask DataFrame is a large parallel DataFrame composed of many smaller Pandas DataFrames, split along the index. These Pandas DataFrames may live on disk for larger-than-memory computing on a single machine, or on many different machines in a cluster. One Dask DataFrame operation triggers many operations on the constituent Pandas DataFrames.

<figure>
  <img src="./fig/dask_pic2.png" style="margin:6px;width:400px"/>
  <figcaption> Dask High Level Schema <a href="https://docs.dask.org/en/latest/dataframe.html/">https://docs.dask.org/en/latest/dataframe.html/</a></figcaption>
</figure><br>

Common Use Cases:
Dask DataFrame is used in situations where Pandas is commonly needed, usually when Pandas fails due to data size or computation speed:
- Manipulating large datasets, even when those datasets don’t fit in memory
- Accelerating long computations by using many cores
- Distributed computing on large datasets with standard Pandas operations like groupby, join, and time series computations

Dask Dataframes **may not be the best choice** if:
your data fits comfortable in RAM - Use pandas only!
If you need a proper database.
You need functions not implemented by dask dataframes - see Dask Delayed.

## Dask Dataframes

We will load in some data to explore.


```python
#Import dask dataframe modules
import dask.dataframe as dd

#NOTE: to run this example (with diagrams) you will need to "pip install graphviz" and donwload graphviz
#https://graphviz.org/download/
import os
os.environ["PATH"] += os.pathsep + 'C:/APPS/Graphviz/bin'
```


```python
# Setup a parlalle LocalCluster that makes use of all the cores and RAM we have on a single machine
from dask.distributed import Client, LocalCluster
cluster = LocalCluster()
# explicitly connect to the cluster we just created
client = Client(cluster)
client
```




<table style="border: 2px solid white;">
<tr>
<td style="vertical-align: top; border: 0px solid white">
<h3 style="text-align: left;">Client</h3>
<ul style="text-align: left; list-style: none; margin: 0; padding: 0;">
  <li><b>Scheduler: </b>tcp://127.0.0.1:54234</li>
  <li><b>Dashboard: </b><a href='http://127.0.0.1:8787/status' target='_blank'>http://127.0.0.1:8787/status</a></li>
</ul>
</td>
<td style="vertical-align: top; border: 0px solid white">
<h3 style="text-align: left;">Cluster</h3>
<ul style="text-align: left; list-style:none; margin: 0; padding: 0;">
  <li><b>Workers: </b>4</li>
  <li><b>Cores: </b>8</li>
  <li><b>Memory: </b>34.21 GB</li>
</ul>
</td>
</tr>
</table>




```python
# Although this is small csv file, we'll reuse our same example from before!
# Load csv results from server into a Pandas DataFrame
df = dd.read_csv("../data/ml_data_points.csv")
```


```python
# We only see the metadata, the actual data are only computed when requested.
df
```




<div><strong>Dask DataFrame Structure:</strong></div>
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
      <th>Unnamed: 0</th>
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
      <th>10 Subducting plate normal velocity (km/Myr)</th>
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
    <tr>
      <th>npartitions=1</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th></th>
      <td>int64</td>
      <td>float64</td>
      <td>float64</td>
      <td>float64</td>
      <td>float64</td>
      <td>float64</td>
      <td>float64</td>
      <td>float64</td>
      <td>float64</td>
      <td>float64</td>
      <td>float64</td>
      <td>float64</td>
      <td>float64</td>
      <td>float64</td>
      <td>float64</td>
      <td>float64</td>
      <td>float64</td>
      <td>float64</td>
      <td>float64</td>
      <td>float64</td>
      <td>float64</td>
      <td>float64</td>
    </tr>
    <tr>
      <th></th>
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
      <td>...</td>
    </tr>
  </tbody>
</table>
</div>
<div>Dask Name: read-csv, 1 tasks</div>



The concept of splitting the dask dataframe into pandas sub dataframes can be seen by the ***nopartitians=10*** output. This is the number of partitians the dataframe is split into and in this case was automatically calibrated, but can be specified. There is a trade off between splitting data too much that improves memory management, and the number of extra tasks it generates. For instance, if you have a 1000 GB of data and are using 10 MB chunks, then you have 100,000 partitions. Every operation on such a collection will generate at least 100,000 tasks. But more on this later. For now lets become familiar with some basic Dataframe operations.

Let's inspect the data in its types, and also take the first 5 rows. 

By default, dataframe operations are ***lazy*** meaning no computation takes place until specified. The ***.compute()*** triggers such a computation - and we will see later on that it converts a dask dataframe into a pandas dataframe. ***head(rows)*** also triggers a computation - but is really helpful in exploring the underlying data.


```python
df.head(5)
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
      <th>Unnamed: 0</th>
      <th>0 Present day longitude (degrees)</th>
      <th>1 Present day latitude (degrees)</th>
      <th>2 Reconstructed longitude (degrees)</th>
      <th>3 Reconstructed latitude (degrees)</th>
      <th>4 Age (Ma)</th>
      <th>5 Time before mineralisation (Myr)</th>
      <th>6 Seafloor age (Myr)</th>
      <th>7 Segment length (km)</th>
      <th>8 Slab length (km)</th>
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
      <td>0</td>
      <td>-66.28</td>
      <td>-27.37</td>
      <td>-65.264812</td>
      <td>-28.103781</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>48.189707</td>
      <td>56.08069</td>
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
      <td>1</td>
      <td>-69.75</td>
      <td>-30.50</td>
      <td>-67.696759</td>
      <td>-31.970639</td>
      <td>12.0</td>
      <td>0.0</td>
      <td>52.321162</td>
      <td>56.09672</td>
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
      <td>2</td>
      <td>-66.65</td>
      <td>-27.27</td>
      <td>-65.128689</td>
      <td>-28.374772</td>
      <td>9.0</td>
      <td>0.0</td>
      <td>53.506085</td>
      <td>55.77705</td>
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
      <td>3</td>
      <td>-66.61</td>
      <td>-27.33</td>
      <td>-65.257928</td>
      <td>-28.311094</td>
      <td>8.0</td>
      <td>0.0</td>
      <td>51.317135</td>
      <td>55.90088</td>
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
      <td>4</td>
      <td>-66.55</td>
      <td>-27.40</td>
      <td>-65.366917</td>
      <td>-28.257580</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>49.340097</td>
      <td>56.09011</td>
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
  </tbody>
</table>
<p>5 rows × 22 columns</p>
</div>




```python
df.columns
```




    Index(['Unnamed: 0', '0 Present day longitude (degrees)',
           '1 Present day latitude (degrees)',
           '2 Reconstructed longitude (degrees)',
           '3 Reconstructed latitude (degrees)', '4 Age (Ma)',
           '5 Time before mineralisation (Myr)', '6 Seafloor age (Myr)',
           '7 Segment length (km)', '8 Slab length (km)',
           '9 Distance to trench edge (km)',
           '10 Subducting plate normal velocity (km/Myr)',
           '11 Subducting plate parallel velocity (km/Myr)',
           '12 Overriding plate normal velocity (km/Myr)',
           '13 Overriding plate parallel velocity (km/Myr)',
           '14 Convergence normal rate (km/Myr)',
           '15 Convergence parallel rate (km/Myr)',
           '16 Subduction polarity (degrees)', '17 Subduction obliquity (degrees)',
           '18 Distance along margin (km)',
           '19 Subduction obliquity signed (radians)',
           '20 Ore Deposits Binary Flag (1 or 0)'],
          dtype='object')




```python
#You can run typical pandas operations (generally faster! - but only noticeable on large data)
#group by operation - calculate the convergence rate by age. 
#Notice the compute() trigger that performs the operations.
#df.groupby('4 Age (Ma)')['14 Convergence normal rate (km/Myr)'].mean()
df.groupby('4 Age (Ma)')['14 Convergence normal rate (km/Myr)'].mean().compute()
```




    4 Age (Ma)
    1.0      66.594390
    3.0      86.227770
    4.0      76.746980
    5.0      86.430612
    6.0      96.153738
               ...    
    175.0    30.189475
    176.0    26.693450
    177.0    15.504740
    178.0    58.860860
    179.0    65.671240
    Name: 14 Convergence normal rate (km/Myr), Length: 126, dtype: float64



# We can break up the table into 4 partions to map out to each core:
df = df.repartition(npartitions=4)
df


```python
# Let's say we want to know the minimum last eruption year for all volcanoes
last_eruption_year_min = df['4 Age (Ma)'].mean()
last_eruption_year_min
```




    dd.Scalar<series-..., dtype=float64>




```python
# Instead of getting the actual value we see dd.Scalar, which represents a recipe for actually calculating this value
last_eruption_year_min.visualize(format='svg')
```




    
![svg](04b-DaskDataframes_files/04b-DaskDataframes_13_0.svg)
    




```python
# To get the value call the 'compute method'
# NOTE: this was slower than using pandas directly,,, for small data you often don't need to use parallel computing!
last_eruption_year_min.compute()
```




    66.19601328903654




```python
import numpy as np
shape = (1000, 4000)
ones_np = np.ones(shape)
ones_np
```




    array([[1., 1., 1., ..., 1., 1., 1.],
           [1., 1., 1., ..., 1., 1., 1.],
           [1., 1., 1., ..., 1., 1., 1.],
           ...,
           [1., 1., 1., ..., 1., 1., 1.],
           [1., 1., 1., ..., 1., 1., 1.],
           [1., 1., 1., ..., 1., 1., 1.]])




```python
print('%.1f MB' % (ones_np.nbytes / 1e6))
```

    32.0 MB



```python
import dask.array as da
ones = da.ones(shape)
ones
```




<table>
<tr>
<td>
<table>
  <thead>
    <tr><td> </td><th> Array </th><th> Chunk </th></tr>
  </thead>
  <tbody>
    <tr><th> Bytes </th><td> 32.00 MB </td> <td> 32.00 MB </td></tr>
    <tr><th> Shape </th><td> (1000, 4000) </td> <td> (1000, 4000) </td></tr>
    <tr><th> Count </th><td> 1 Tasks </td><td> 1 Chunks </td></tr>
    <tr><th> Type </th><td> float64 </td><td> numpy.ndarray </td></tr>
  </tbody>
</table>
</td>
<td>
<svg width="170" height="92" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="0" y1="0" x2="120" y2="0" style="stroke-width:2" />
  <line x1="0" y1="42" x2="120" y2="42" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="0" y1="0" x2="0" y2="42" style="stroke-width:2" />
  <line x1="120" y1="0" x2="120" y2="42" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="0.0,0.0 120.0,0.0 120.0,42.89879552186203 0.0,42.89879552186203" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="60.000000" y="62.898796" font-size="1.0rem" font-weight="100" text-anchor="middle" >4000</text>
  <text x="140.000000" y="21.449398" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(-90,140.000000,21.449398)">1000</text>
</svg>
</td>
</tr>
</table>




```python
chunk_shape = (1000, 1000)
ones = da.ones(shape, chunks=chunk_shape)
ones
```




<table>
<tr>
<td>
<table>
  <thead>
    <tr><td> </td><th> Array </th><th> Chunk </th></tr>
  </thead>
  <tbody>
    <tr><th> Bytes </th><td> 32.00 MB </td> <td> 8.00 MB </td></tr>
    <tr><th> Shape </th><td> (1000, 4000) </td> <td> (1000, 1000) </td></tr>
    <tr><th> Count </th><td> 4 Tasks </td><td> 4 Chunks </td></tr>
    <tr><th> Type </th><td> float64 </td><td> numpy.ndarray </td></tr>
  </tbody>
</table>
</td>
<td>
<svg width="170" height="92" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="0" y1="0" x2="120" y2="0" style="stroke-width:2" />
  <line x1="0" y1="42" x2="120" y2="42" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="0" y1="0" x2="0" y2="42" style="stroke-width:2" />
  <line x1="30" y1="0" x2="30" y2="42" />
  <line x1="60" y1="0" x2="60" y2="42" />
  <line x1="90" y1="0" x2="90" y2="42" />
  <line x1="120" y1="0" x2="120" y2="42" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="0.0,0.0 120.0,0.0 120.0,42.89879552186203 0.0,42.89879552186203" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="60.000000" y="62.898796" font-size="1.0rem" font-weight="100" text-anchor="middle" >4000</text>
  <text x="140.000000" y="21.449398" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(-90,140.000000,21.449398)">1000</text>
</svg>
</td>
</tr>
</table>




```python
ones.compute()
```




    array([[1., 1., 1., ..., 1., 1., 1.],
           [1., 1., 1., ..., 1., 1., 1.],
           [1., 1., 1., ..., 1., 1., 1.],
           ...,
           [1., 1., 1., ..., 1., 1., 1.],
           [1., 1., 1., ..., 1., 1., 1.],
           [1., 1., 1., ..., 1., 1., 1.]])




```python
ones.visualize(format='svg')
```




    
![svg](04b-DaskDataframes_files/04b-DaskDataframes_20_0.svg)
    




```python
sum_of_ones = ones.sum()
sum_of_ones.visualize(format='svg')
```




    
![svg](04b-DaskDataframes_files/04b-DaskDataframes_21_0.svg)
    




```python
fancy_calculation = (ones * ones[::-1, ::-1]).mean()
fancy_calculation.visualize(format='svg')
```




    
![svg](04b-DaskDataframes_files/04b-DaskDataframes_22_0.svg)
    




```python
bigshape = (200000, 4000)
big_ones = da.ones(bigshape, chunks=chunk_shape)
big_ones
```




<table>
<tr>
<td>
<table>
  <thead>
    <tr><td> </td><th> Array </th><th> Chunk </th></tr>
  </thead>
  <tbody>
    <tr><th> Bytes </th><td> 6.40 GB </td> <td> 8.00 MB </td></tr>
    <tr><th> Shape </th><td> (200000, 4000) </td> <td> (1000, 1000) </td></tr>
    <tr><th> Count </th><td> 800 Tasks </td><td> 800 Chunks </td></tr>
    <tr><th> Type </th><td> float64 </td><td> numpy.ndarray </td></tr>
  </tbody>
</table>
</td>
<td>
<svg width="79" height="170" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="0" y1="0" x2="29" y2="0" style="stroke-width:2" />
  <line x1="0" y1="6" x2="29" y2="6" />
  <line x1="0" y1="12" x2="29" y2="12" />
  <line x1="0" y1="18" x2="29" y2="18" />
  <line x1="0" y1="25" x2="29" y2="25" />
  <line x1="0" y1="31" x2="29" y2="31" />
  <line x1="0" y1="37" x2="29" y2="37" />
  <line x1="0" y1="43" x2="29" y2="43" />
  <line x1="0" y1="50" x2="29" y2="50" />
  <line x1="0" y1="56" x2="29" y2="56" />
  <line x1="0" y1="63" x2="29" y2="63" />
  <line x1="0" y1="69" x2="29" y2="69" />
  <line x1="0" y1="75" x2="29" y2="75" />
  <line x1="0" y1="81" x2="29" y2="81" />
  <line x1="0" y1="88" x2="29" y2="88" />
  <line x1="0" y1="94" x2="29" y2="94" />
  <line x1="0" y1="100" x2="29" y2="100" />
  <line x1="0" y1="106" x2="29" y2="106" />
  <line x1="0" y1="113" x2="29" y2="113" />
  <line x1="0" y1="120" x2="29" y2="120" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="0" y1="0" x2="0" y2="120" style="stroke-width:2" />
  <line x1="7" y1="0" x2="7" y2="120" />
  <line x1="14" y1="0" x2="14" y2="120" />
  <line x1="21" y1="0" x2="21" y2="120" />
  <line x1="29" y1="0" x2="29" y2="120" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="0.0,0.0 29.030629010473877,0.0 29.030629010473877,120.0 0.0,120.0" style="fill:#8B4903A0;stroke-width:0"/>

  <!-- Text -->
  <text x="14.515315" y="140.000000" font-size="1.0rem" font-weight="100" text-anchor="middle" >4000</text>
  <text x="49.030629" y="60.000000" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(-90,49.030629,60.000000)">200000</text>
</svg>
</td>
</tr>
</table>




```python
print('%.1f MB' % (big_ones.nbytes / 1e6))
```

    6400.0 MB



```python
big_calc = (big_ones * big_ones[::-1, ::-1]).mean()

result = big_calc.compute()
result
```




    1.0




```python
import time

def inc(x):
    time.sleep(0.1)
    return x + 1

def dec(x):
    time.sleep(0.1)
    return x - 1

def add(x, y):
    time.sleep(0.2)
    return x + y
```


```python
%%time
x = inc(1)
y = dec(2)
z = add(x, y)
z
```

    Wall time: 431 ms





    3




```python
import dask
inc = dask.delayed(inc)
dec = dask.delayed(dec)
add = dask.delayed(add)
```


```python
%%time
x = inc(1)
y = dec(2)
z = add(x, y)
z
```

    Wall time: 1.03 ms





    Delayed('add-4336c3e8-9b9a-47b3-8c33-5da47dd0128c')




```python
z.visualize(format='svg', rankdir='LR')
```




    
![svg](04b-DaskDataframes_files/04b-DaskDataframes_30_0.svg)
    




```python
%%time
z.compute()
```

    Wall time: 363 ms





    3



## Helpful Links:

Dask bag fundamentals
[https://docs.dask.org/en/latest/bag.html](https://docs.dask.org/en/latest/bag.html)

Bag API's:
[https://docs.dask.org/en/latest/bag-api.html](https://docs.dask.org/en/latest/bag.html)

Dask bag limitations:
[https://docs.dask.org/en/latest/shared.html](https://docs.dask.org/en/latest/bag.html)

Pangeo info:
[https://pangeo.io/#what-is-pangeo](https://pangeo.io/#what-is-pangeo)

Xarray:
[http://xarray.pydata.org/en/stable/](http://xarray.pydata.org/en/stable/)

Xarray API:
[http://xarray.pydata.org/en/stable/generated/xarray.open_dataset.html](http://xarray.pydata.org/en/stable/generated/xarray.open_dataset.html)

Dask Dataframe intro
[https://docs.dask.org/en/latest/dataframe.html](https://docs.dask.org/en/latest/dataframe.html)

API list for Dask Dataframes
[https://docs.dask.org/en/latest/dataframe.html](https://docs.dask.org/en/latest/dataframe-api.html)

What are decorators
[https://realpython.com/primer-on-python-decorators/](https://realpython.com/primer-on-python-decorators/)


<div class="keypoints">  
### Key Points

- "Dask builds on numpy and pandas APIs but operates in a parallel manner"
- "Computations are by default lazy and must be triggered - this reduces unneccessary computation time"
- "Dask Bag uses map filter and group by operations on python objects or semi/unstrucutred data"
- "dask.multiprocessing is under the hood"
- "Xarray is another option for holding netcdf data"
</div>
