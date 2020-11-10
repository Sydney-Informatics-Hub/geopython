---
title: Setup
layout: page
root: "."
---

# 1. Get a Python client
We generally use and recommend Miniconda Python distribution: [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html). But feel free to use whatever one works for you. We will be using Miniconda3-py37_4.8.3.

You can get this specific version here for:

* [Windows 64 bit Download](https://repo.anaconda.com/miniconda/Miniconda3-py37_4.8.3-Windows-x86_64.exe)

* [Mac OSX Download](https://repo.anaconda.com/miniconda/Miniconda3-py37_4.8.3-MacOSX-x86_64.pkg)

* [Linux Download](https://repo.anaconda.com/miniconda/Miniconda3-py37_4.8.3-Linux-x86_64.sh)


<br>

# 2. Setup your Python environemnt (install required packages and libraries)
To run all the commands in your own Python installation, you can set up an environemnt with something like this:

~~~
conda create -n geopython
pip install 
~~~

# 3. Download the data

Download the data from all the exercises from here:

Extract this .

Your file tree should look like this

geopython
  |
  |--notebooks
  |--data


<br>

# Other Options

## Docker

## For Windows use WSL with Ubuntu 

Install Ubuntu or some other Linux distro on the Windows Subsystem for Linux see [here for details](https://ubuntu.com/tutorials/tutorial-ubuntu-on-windows#1-overview). This one will give you a full suite of Linux functions and I like it for emulating Linux.

```
 sudo apt-get update
 sudo apt-get install build-essential
 sudo apt install libopenmpi-dev
 pip install dask==2.11.0 distributed==2.11.0 netCDF4==1.5.3 numpy==1.18.1 pandas==1.0.1 scipy==1.4.1 xarray==0.15.0 mpi4py==3.0.3 jupyter pyshp pandas swifter shapely
 ```

## Google Colab



<br>


{% include links.md %}
