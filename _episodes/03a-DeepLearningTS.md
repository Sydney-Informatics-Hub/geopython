---
title: "03a. -Deep Learning Time Series with Python, tensorflow, and a GPU"
teaching: 20
exercises: 20
questions:
- "Why is deep learning so special?"
- "What is a GPU and why do I care?"
objectives:
- "Set up your own Python environemnt"
- "Run a tensorflow job"
keypoints:
- "Roll-your-own software stack"
- "Getting the correct balance of versions for software stacks is imperative"
- "Not all GPUs are compliant with all software"
---

Python offers many ways to make use of the compute capability in your GPU. A very common application is deep learning using the tensorflow and keras packages. In this example we are going to look at forecasting a timeseries using recurrent neural netowrks based on the history of the time series itself.

### You can run through the steps on you local machine using the Jupyter notebook example

We are looking at temperature data in Sydney for the last 150 years with daily measurements. We want to predict what the future is going to look like. Note: the default values in the notebook restrict the length of dataset used in the analysis purely for time constraints. The batch mode version removes this restrition, but feel free to adjust the numbers as you like.

## Run the straight python script to do everything in "batch" mode. 

Assuming the dataset, ```sydney_temperature.csv```, and python script, ```timeseries.py``` are in the same directory, to run in batch mode, simply envoke:
```
python timeseries.py
```
This script saves the figure to a file (instead of displaying it inline) and saves the model to a file also (for later use). The default looks at a much larger portion of the dataset than the Jupyter Notebook version defaults.

### Running on Artemis

## Set up the environment

So far we have dealt with fairly well-behaved packages on Artmeis. There are ~~dozens~~ hundreds of maintained bits of software and libraries on Artemis. But there are thousands of users and often we need very particular versions and workflows, so keeping every combination of software centrally maintained is just not feasible. Instead, often we have to build our own programs from scratch (just how we built our **helloworld** example from source!). This is a useful skill to have when you move to other HPC facilities like our national collabraotive infastructure [NCI](http://nci.org.au/) and [Pawsey](https://pawsey.org.au/), where you will undoubtably have to set up your own environemnts to work in.


The first thing we need is a specifc python version. You can use the prebuilt environment with the command ```source /project/Training/GPUtraining/miniconda/bin/activate pyGPUk40``` - or follow these instructions to get it running in your own folder (which you will need to do when you are not using the Training project). 

```
cd /project/Training/GPUtraining/
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p miniconda

module load cuda/8.0.44
module load openmpi-gcc/3.0.0-cuda

miniconda/bin/conda create -n pyGPUk40 python=3.5
source miniconda/bin/activate pyGPUk40

pip install /usr/local/tensorflow/tensorflow-1.4.0-cp35-cp35m-linux_x86_64.whl
pip install keras==2.0.8
pip install pandas
pip install matplotlib
pip install sklearn
pip install h5py
```

Note: Artemis has some specific versions of tensorflow that it needs to install. These are located in the directory ```/usr/local/tensorflow/```. You can see the various verisons in there. We are using one that is compatible with the NVIDIA k40 GPUs on the Artemis training node. If using the NVIDIA v100 GPUs in the production environment, you will have to use a different combo of python/cuda/tensorflow/keras. Check compatability for [NVIDIA Drivers/CUDA](https://docs.nvidia.com/deploy/cuda-compatibility/index.html), [CUDA/Python/Tensorflow](https://www.tensorflow.org/install/source#tested_build_configurations).

Okay so we have our Python environment ready, we are now ready to submit our script to the scheduler! Use the ```runk40.pbs``` pbs script as a template:

```
#! /bin/bash

#PBS -P Training
#PBS -N k40ts 
#PBS -l select=1:ncpus=2:mem=2gb:ngpus=1
#PBS -l walltime=00:10:00
#PBS -q defaultQ

cd /project/Training/nathan

module load cuda/8.0.44
module load openmpi-gcc/3.0.0-cuda
source /project/Training/GPUtraining/miniconda/bin/activate pyGPUk40

#print out the version of tensorflow we are running
python -c 'import tensorflow as tf; print(tf.__version__)'
#Run the python script
python timeseries.py
```

And run the script with ```qsub runk40.pbs```. Then you can look for the output, in this case it trains a model and saves it as a *.hdf5 file. Plus it performs the prediction for us on this data. But you could train a model that takes a week on Artemis, save the model output to your local machine and do the small-scale stuff, like predicting on other datasets and retraining. The possibilites are endless!


Open up ```runv100.pbs```, what are the differences? This pbs script is made to run on the production Artemis nodes. So note the different versions in use here. In fact, if you try and run it, it will fail because the GPU is compatiblte with this version of tensorflow. Give it a go and see what failure feels like!




