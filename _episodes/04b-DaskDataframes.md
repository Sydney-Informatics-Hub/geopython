---
title: "04b. Dask and Dask Dataframes"
teaching: 25
exercises: 5
questions:
- "Use a modern python library and elegant syntax for performance benefits"
- "How do I deal with large irregular data and show me some real world examples of Dask"
objectives:
- "Intro to Dask concepts and High level datastructures"
- "Use dask dataframes"
- "Use dask delayed functions"
- "Deal with semi-structured and unstructured data in memory efficient and parallel manner"
- "Show me examples of using Dask on Large Datasets"
keypoints:
- "Dask builds on numpy and pandas APIs but operates in a parallel manner"
- "Computations are by default lazy and must be triggered - this reduces unneccessary computation time"
- "Dask Bag uses map filter and group by operations on python objects or semi/unstrucutred data"
- "dask.multiprocessing is under the hood"
- "Xarray for holding scientific data"
---

# DASK
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
  <img src="{{ page.root }}/fig/dask_pic1.png" style="margin:10px;width:600px"/>
  <figcaption> Dask High Level Schema <a href="https://docs.dask.org/en/latest/">https://docs.dask.org/en/latest/</a></figcaption>
</figure><br>

Dask provides high level collections - these are ***Dask Dataframes, bags, and arrays***.
On a low level, dask dynamic task schedulers to scale up or down processes, and presents parallel computations by implementing task graphs. It provides an alternative to scaling out tasks instead of threading (IO Bound) and multiprocessing (cpu bound).

A Dask DataFrame is a large parallel DataFrame composed of many smaller Pandas DataFrames, split along the index. These Pandas DataFrames may live on disk for larger-than-memory computing on a single machine, or on many different machines in a cluster. One Dask DataFrame operation triggers many operations on the constituent Pandas DataFrames.

<figure>
  <img src="{{ page.root }}/fig/dask_pic2.png" style="margin:6px;width:400px"/>
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


# Dask Dataframes

We will generate some data using one of the python files makedata.py by importing it in ipython. 
~~~
import makedata
data = makedata.data()
data
~~~
{: .python}

The data is preloaded into a dask dataframe. Notice the output to data shows the dataframe metadata.  

The concept of splitting the dask dataframe into pandas sub dataframes can be seen by the ***nopartitians=10*** output. This is the number of partitians the dataframe is split into and in this case was automatically calibrated, but can be specified. There is a trade off between splitting data too much that improves memory management, and the number of extra tasks it generates. For instance, if you have a 1000 GB of data and are using 10 MB chunks, then you have 100,000 partitions. Every operation on such a collection will generate at least 100,000 tasks. But more on this later. For now lets become familiar with some basic Dataframe operations.

Let's inspect the data in its types, and also take the first 5 rows. 

By default, dataframe operations are ***lazy*** meaning no computation takes place until specified. The ***.compute()*** triggers such a computation - and we will see later on that it converts a dask dataframe into a pandas dataframe. ***head(rows)*** also triggers a computation - but is really helpful in exploring the underlying data.
~~~
data.dtypes
data.head(5)
~~~
{: .python}

You should see the below output
~~~
In [6]: data.head(5)
Out[6]:
   age     occupation          telephone  ...       street-address          city  income
0   54  Acupuncturist     (528) 747-6949  ...  1242 Gough Crescent  Laguna Beach  116640
1   38   Shelf Filler       111.247.5833  ...       10 Brook Court     Paragould   57760
2   29    Tax Manager       035-458-1895  ...  278 Homestead Trace    Scottsdale   33640
3   19      Publisher  +1-(018)-082-3905  ...     310 Ada Sideline    East Ridge   14440
4   25      Stationer     1-004-960-0770  ...        711 Card Mall     Grayslake   2500
~~~
{: .output}

Let's perform some familiar operations for those who use pandas.

filter operation - filter people who are older than 60 and assign to another dask array called data2

~~~
data2 = data[data.age > 60]
~~~
{: .python}

Apply a function to a column
~~~
data.income.apply(lambda x: x * 1000).head(5)
~~~
{: .python}

Assign values to a new column

~~~
data = data.assign(dummy = 1)
~~~
{: .python}

group by operation - calculate the average incomes by occupation. Notice the compute() trigger that performs the operations.

~~~
data.groupby('occupation').income.mean().compute()
~~~
{: .python}

A memory efficient style is to create pipelines of operations and trigger a final compute at the end. 
~~~
datapipe = data[data.age < 20]
datapipe = datapipe.groupby('income').mean()
datapipe.head(4)
~~~
{: .python}

~~~
        age
income
10240   16.0
11560   17.0
12960   18.0
14440   19.0
~~~
{: .output}

Chaining syntax can also be used to do the same thing, but keep readability in your code in mind.
~~~
pandasdata = (data[data.age < 20].groupby('income').mean()).compute()
~~~
{: .python}

sort operation - get the occupations with the largest people working in them
~~~
data.occupation.value_counts().nlargest(5).compute()
~~~
{: .python}

write the output of a filter result to csv
~~~
data[data.city == 'Madison Heights'].compute().to_csv('Madison.csv')
~~~
{: .python}

# Dask Delayed with custom made operations

What if you need to run your own function, or a function outside of the pandas subset that dask dataframes make available? Dask delayed is your friend. It uses ***python decorator syntax*** to convert a function into a lazy executable. The functions can then be applied to build data pipeline operations in a similar manner to what we have just encountered.

Let's explore a larger example of using dask dataframes and dask delayed functions.

In the ```/files``` directory, use your preferred editor to view the ```complex_system.py``` file. This script uses dask delayed functions that are applied to a sequence of data using pythonic ***list comprehension syntax*** . The code simulates financial defaults in a very theoretical way, and outputs the summation of these predicted defaults. 

~~~
Delayed('add-c62bfd969d75abe76f3d8dcf2a9ef99c')
407.5
~~~
{: .output}

<br>

## Exercise 2:
Given what you know of dask delayed function, please alter the file called ```computepi_pawsey.py```, which calculated estimates of pi without using extra parallel libraries, and alter the code with a dask delayed wrapper to make it lazy and fast 

<br>

## Exercise 1:
The above script is a great example of dask delayed functions that are applied to lists, made in an elegant pythonic syntax. Let's try using these delayed default functions on our data of income and occupations. 

Make your own lazy function using the decorator syntax, and perform the computation you have described on a column of the data previously used in the makedata.data() helper file. For bonus points perform an aggregation on this column.

<br>

# Dask Bag
Dask Bag implements operations like map, filter, groupby and aggregations on collections of Python objects. It does this in parallel and in small memory using Python iterators.

Dask Bags are often used to do simple preprocessing on log files, JSON records, or other user defined Python objects

Execution on bags provide two ***benefits***:
1. ***Parallel:*** data is split up, allowing multiple cores or machines to execute in parallel
2. ***Iterating:*** data processes lazily, allowing smooth execution of ***larger-than-memory data***, even on a single machine within a single partition

By default, dask.bag uses dask.multiprocessing for computation. As a benefit, Dask bypasses the GIL and uses multiple cores on pure Python objects. As a drawback, Dask Bag doesn’t perform well on computations that include a great deal of inter-worker communication.

Because the multiprocessing scheduler requires moving functions between multiple processes, we encourage that Dask Bag users also install the cloudpickle library to enable the transfer of more complex functions

What are the ***drawbacks*** ?

* Bag operations tend to be slower than array/DataFrame computations in the same way that standard Python containers tend to be slower than NumPy arrays and Pandas DataFrames
* Bags are immutable and so you can not change individual elements
* By default, bag relies on the multiprocessing scheduler, which has known limitations - the main ones being: 
  	a, The multiprocessing scheduler must serialize data between workers and the central process, which can be expensive
	b, The multiprocessing scheduler must serialize functions between workers, which can fail. The Dask site recommends using cloudpickle to enable the transfer of more complex functions.

We will investigate data located on the web that logs all juypter notebook instances run on the net. Two files are 
1. Log files of every entry specific to a certain day
2. An index of daily log files

Before we start, some python packages are needed. Types these commands directly into ipython
~~~
import dask.bag as db
import json
import os
import re
import time
~~~
{: .bash}

Investigate underlying data by reading text file that houses daily data into a bag. First few rows are displayed
~~~
db.read_text('https://archive.analytics.mybinder.org/events-2018-11-03.jsonl').take(3)
~~~
{: .bash}

The output should give you a task for the underlying data in the daily log files. Essential this is a text file in json format.
~~~
('{"timestamp": "2018-11-03T00:00:00+00:00", "schema": "binderhub.jupyter.org/launch", "version": 1, "provider": "GitHub", "spe                c": "Qiskit/qiskit-tutorial/master", "status": "success"}\n',
 '{"timestamp": "2018-11-03T00:00:00+00:00", "schema": "binderhub.jupyter.org/launch", "version": 1, "provider": "GitHub", "spe                c": "ipython/ipython-in-depth/master", "status": "success"}\n',
 '{"timestamp": "2018-11-03T00:00:00+00:00", "schema": "binderhub.jupyter.org/launch", "version": 1, "provider": "GitHub", "spe                c": "QISKit/qiskit-tutorial/master", "status": "success"}\n')

~~~
{: .output}


Index file loaded as a bag. No data transfer or computation kicked off - just organising mapping the file to a json structure
~~~
index = db.read_text('https://archive.analytics.mybinder.org/index.jsonl').map(json.loads)
index
index.take(2)
~~~
{: .bash}

These files aren't big at all - a sign is the number of partitians of 1. Dask would automatically split the data up for large data. 
~~~
In [5]: index = db.read_text('https://archive.analytics.mybinder.org/index.jsonl').map(json.loads)
In [6]: index
Out[6]: dask.bag<loads, npartitions=1>
In [7]: index.take(2)
Out[7]:
({'name': 'events-2018-11-03.jsonl', 'date': '2018-11-03', 'count': '7057'},
 {'name': 'events-2018-11-04.jsonl', 'date': '2018-11-04', 'count': '7489'})
~~~
{: .output}

We can perform some operations on these two files. Please note the Dask Bag API (in the provided links section) for the signatures of available functions and their requirements.

Read the index file as a dask bag and perform a mapping of the data to the function json.loads(). This function loads strings into a json object - given it adheres to the json structure.

~~~
index = db.read_text('https://archive.analytics.mybinder.org/index.jsonl').map(json.loads)
print(index)
~~~
{: .bash}

# PANGEO EXAMPLE
Pangeo is a community promoting open, reproducible, and scalable science.

In practice it is not realy a python package, but a collection of packages, supported datasets, tutorials and documentation used to promote scalable science. Its motivation was driven by data becoming increasingly large, the fragmentation of software making reproducability difficult, and a growing technology gap between industry and traditional science.

As such the Pangeo community supports using dask on HPC. We will run through an example of using our new found knowledge of dask on large dataset computation and visualisation.Specifically this pangeo example is a good illustration of dealing with an IO bound task.

The example we will submit is an altered version of Pangeos meteorology use case found here:
https://pangeo.io/use_cases/meteorology/newmann_ensemble_meteorology.html


## Xarray

Rather than using a dask dataframe, data is loaded from multiple netcdf files in the data folder relative to where the script resides. 
Xarray is an opensource python package that uses dask in its inner workings. Its design to make working with multi-dimensional data easier by introducing labels in the form of dimensions, coordinates and attributes on top of raw NumPy-like arrays, which allows for a more intuitive, more concise, and less error-prone developer experience.

It is particulary suited for working with netcdf files and is tightly integrated with dask parallel computing. 

Let's investigate a small portion of the data before looking at the complete script. Open an ipython terminal inside the data folder

And have a look at the data
~~~
import xarray as xr
data = xr.open_dataset('conus_daily_eighth_2008_ens_mean.nc4')
data
~~~
{: .python}

You should see the following metadata that holds 3 dimenstional information (latitude, longditude and time) on temperature and precipitation measurements.
~~~

In [41]: data = xr.open_dataset('conus_daily_eighth_2008_ens_mean.nc4')

In [42]: data
Out[42]:
<xarray.Dataset>
Dimensions:    (lat: 224, lon: 464, time: 366)
Coordinates:
  * time       (time) datetime64[ns] 2008-01-01 2008-01-02 ... 2008-12-31
  * lat        (lat) float64 25.12 25.25 25.38 25.5 ... 52.62 52.75 52.88 53.0
  * lon        (lon) float64 -124.9 -124.8 -124.6 -124.5 ... -67.25 -67.12 -67.0
Data variables:
    elevation  (lat, lon) float64 ...
    pcp        (time, lat, lon) float32 ...
    t_mean     (time, lat, lon) float32 ...
    t_range    (time, lat, lon) float32 ...
Attributes:
    history:      Wed Oct 24 13:59:29 2018: ncks -4 -L 1 conus_daily_eighth_2...
    NCO:          netCDF Operators version 4.7.4 (http://nco.sf.net)
    institution:  National Center fo Atmospheric Research (NCAR), Boulder, CO...
    title:        CONUS daily 12-km gridded ensemble precipitation and temper...
~~~
{: .output}

Find out how large is the file.
~~~
print('memory gb',format(data.nbytes / 1e9))
~~~
{: .python}

What is the average elevation over lat and long dimensions.
~~~
data.elevation.mean()
~~~
{: .python}

~~~
In [50]: data.elevation.mean()
Out[50]:
<xarray.DataArray 'elevation' ()>
array(709.99515723)
~~~
{: .output}


What is the average elevation for each longitude
~~~
data.elevation.mean(dim='lat')
~~~
{: .python}

Exit from your ipython session. Now we will now run a script to the scheduler that loads multiple files, performs calculations on the xarray data and plots the results.

Steps to do:
1. In the files directory, open the python script we will run called pangeo.py.
~~~
cd /project/Training/myname/files
nano pangeo.py
~~~

2. Alter the instance of the Client() object by redirecting the path in the local_directory argument to your /project/Training/myname folder. The Client object sets up a local cluster that uses all availble resources. In this case it is created on one compute node. The optional local_directory specifies a storage area that allows dask to copy temporary data on if RAM is insufficient to work on large datasets - i.e. its a path where dask can spill over some data to still perform data calculations. 

3. Notice the xarray open_mfdaset function loads multiple files that match a naming pattern. Chunking size is specific to the axis ***time***, one chunck for each year. 

4. Submit the ```pangeo.pbs``` file to the scheduler.
~~~
qsub pangeo.pbs
~~~

Png files should be created based on calculation in the code that measure the variance in temperatures (max minus min observations). As seen before, these calculations are triggered by a ***.compute()*** call. Two images are created, with one demostrating how we can persist the xarray dataset in memory for quick retrievals via the ***.persist()*** call. 

Lets see the image. If you have X11 forwarding enabled you can view it directly from artemis. Alternatively, use scp to copy it locally and view.
~~~
module load imagemagick
display variance_temp.png &
~~~

<figure>
  <img src="{{ page.root }}/fig/USA_Temp.png" style="margin:10px;width:600px"/>
  <figcaption> Dask Temperature visualisation </figcaption>
</figure><br>



# Helpful Links:

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

