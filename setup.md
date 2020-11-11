---
title: Setup
layout: page
root: "."
---

# 1. Get a Python client
We generally use and recommend Miniconda Python distribution: [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html). But feel free to use whatever one works for you (and the course materials). We will be using Miniconda3-py37_4.8.3.

You can get this specific version here for:

* [Windows 64 bit Download](https://repo.anaconda.com/miniconda/Miniconda3-py37_4.8.3-Windows-x86_64.exe)

* [Mac OSX Download](https://repo.anaconda.com/miniconda/Miniconda3-py37_4.8.3-MacOSX-x86_64.pkg)

* [Linux Download](https://repo.anaconda.com/miniconda/Miniconda3-py37_4.8.3-Linux-x86_64.sh)

Follow the prompts (the default recommendations in the installer are generally fine.) 
Once installed, launch an "Anaconda Prompt" from the Start Menu / Applications Folder to begin your Python adventure. 

<br>

# 2. Setup your Python environment (install required packages and libraries)

Next we need to set up an environment with all the additional packages and libraries we will be using throughout the course.

* Launch an Anaconda Prompt (or equivalent).
* Type in each of these commands sequentially. Each should take a minute or so to complete:

~~~
conda create -n geopy python=3.7

conda activate geopy

conda install pip

pip install numpy==1.18 pandas==1.0.1 matplotlib==3.3.2 pyshp==2.1.2 lasio==0.28 obspy==1.2.2 scipy==1.4.1 scikit-learn==0.23 

conda install -c conda-forge cartopy=0.18

pip install tensorflow==2.3 

python -m pip install "dask[complete]"

pip install jupyter==1.0 
~~~

At anytime in the future you can install additional packages or create seperate environments. We will discuss this more in the course. This particular environment should have the correct balance of versions with any dependencies accounted for.

Also, setup your workspace where we will be creating files and generating data, you can do this in your prompt (or just in Windows Explorer/OSX Finder). For me I will be working in top-level folder on my Desktop called ```geopython``` and a subdirectory called ```notebooks```.

~~~
cd C:\Users\Administrator\Desktop\
mkdir geopython
cd geopython
mkdir notebooks
cd notebooks
~~~

Now type:

~~~
python
~~~

to launch Python!

![png](fig/setup-python.png)

<br>

# 3. Download the data

Download the data (280 MB inflated to 500 MB) for all the exercises from here:

Extract this to a directory you can work in.
Your file tree should look like something like this

![png](fig/setup-folder.png)


```
.
|-- geopython
|   +-- notebooks
|   +-- data
|       |   +-- ...

```

<br>

# Other Options

## Google Colab

If the above options do not work for you, [Google Colab](https://colab.research.google.com/) can be used for an on-demand Python notebook. You will require a Google Account for this.

## Docker

If you are familiar with Docker you may use our Docker image (to be provided).

<br>


{% include links.md %}
