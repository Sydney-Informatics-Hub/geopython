---
title: "6. Introducing dask Bag and more dask examples"
teaching: 20
exercises: 20
questions:
- "How do I deal with large irregular data and show me some real world examples of Dask"
objectives:
- "Deal with semi-structured and unstructured data in memory efficient and parallel manner"
- "Show me examples of using Dask on Large Datasets"
keypoints:
- "Dask Bag uses map filter and group by operations on python objects or semi/unstrucutred data"
- "dask.multiprocessing is under the hood"
- "Xarray for holding scientific data"
---

# What is Dask Bag
Dask Bag implements operations like map, filter, groupby and aggregations on collections of Python objects. It does this in parallel and in small memory using Python iterators.

Dask Bags are often used to do simple preprocessing on log files, JSON records, or other user defined Python objects

Execution on bags provide two ***benefits***:
1. ***Parallel:*** data is split up, allowing multiple cores or machines to execute in parallel
2. ***Iterating:*** data processes lazily, allowing smooth execution of ***larger-than-memory data***, even on a single machine within a single partition

By default, dask.bag uses dask.multiprocessing for computation. As a benefit, Dask bypasses the GIL and uses multiple cores on pure Python objects. As a drawback, Dask Bag doesn’t perform well on computations that include a great deal of inter-worker communication.

Because the multiprocessing scheduler requires moving functions between multiple processes, we encourage that Dask Bag users also install the cloudpickle library to enable the transfer of more complex functions

What are the ***drawbacks*** ?

 - Bag operations tend to be slower than array/DataFrame computations in the same way that standard Python containers tend to be slower than NumPy arrays and Pandas DataFrames
 
 - Bags are immutable and so you can not change individual elements
 
 - By default, bag relies on the multiprocessing scheduler, which has known limitations - the main ones being:
  	a, The multiprocessing scheduler must serialize data between workers and the central process, which can be expensive
	b, The multiprocessing scheduler must serialize functions between workers, which can fail. The Dask site recommends using 		cloudpickle to enable the transfer of more complex functions.

### To learn Bag - Lets get our hands dirty with some examples

Lets get back to ipython, ensuring that the dask conda environment is still activate.

~~~
qsub -I -P Training -l select=1:ncpus=2:mem=4GB -l walltime=00:20:00
source /project/Training/kmarTrain/miniconda3/bin/activate
conda activate dask
cd /project/Training/myname
ipython
~~~

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

### PANGEO GEOSCIENCE EXAMPLE
Pangeo is a community promoting open, reproducible, and scalable science.

In practice it is not realy a python package, but a collection of packages, supported datasets, tutorials and documentation used to promote scalable science. Its motivation was driven by data becoming increasingly large, the fragmentation of software making reproducability difficult, and a growing technology gap between industry and traditional science.

As such the Pangeo community supports using dask on HPC. We will run through an example of using our new found knowledge of dask on large dataset computation and visualisation.Specifically this pangeo example is a good illustration of dealing with an IO bound task.

The example we will submit is an altered version of Pangeos meteorology use case found here:
https://pangeo.io/use_cases/meteorology/newmann_ensemble_meteorology.html


### What is Xarray

Rather than using a dask dataframe, data is loaded from multiple netcdf files in the data folder relative to where the script resides. 
Xarray is an opensource python package that uses dask in its inner workings. Its design to make working with multi-dimensional data easier by introducing labels in the form of dimensions, coordinates and attributes on top of raw NumPy-like arrays, which allows for a more intuitive, more concise, and less error-prone developer experience.

It is particulary suited for working with netcdf files and is tightly integrated with dask parallel computing. 

Let's investigate a small portion of the data before looking at the complete script. Open an ipython terminal inside the data folder

~~~
cd /project/Training/myname/data
ipython
~~~

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



### Some links:

on dask bag fundamentals
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

<br>


