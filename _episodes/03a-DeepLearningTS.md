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

We are looking at temperature data in Sydney for the last 150 years with daily measurements (Based on an example from 
https://machinelearningmastery.com/time-series-prediction-lstm-recurrent-neural-networks-python-keras/). We want to predict what the future is going to look like. Note: the default values in the notebook restrict the length of dataset used in the analysis purely for time constraints. But feel free to adjust the numbers as you like. Using a GPU trained deep-learning framework to predict time series data. Specifically we are using a Long Short-Term Memory (LSTM) deep learning network

The data is from the Australian Bureau of Meteorology (BOM) representing the daily maximum temperatures for the last 150 years. http://www.bom.gov.au/jsp/ncc/cdio/weatherData/av?p_display_type=dailyZippedDataFile&p_stn_num=066214&p_c=-877001456&p_nccObsCode=122&p_startYear=2020

A problem might be, given the last few decades of temperature cycles, what will next years' be? Let's try and predict the future!


```python
#import all the libraries we need
import numpy
import time
import matplotlib.pyplot as plt
import pandas as pd
import math
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MaxAbsScaler 
```


```python
#Load in the dataset
filename='../data/sydney_temperature.csv'
dataframe = pd.read_csv(filename, usecols=[5], engine='python')
dataset = dataframe.dropna()
dataset = dataset.values
dataset = dataset.astype('float32')

# normalize the dataset to be betwenn 0 and 1
scaler = MinMaxScaler(feature_range=(0, 1))
datasetScaled = scaler.fit_transform(dataset)

```


```python
#Print some stats about the data
print(dataframe.describe())
```

           Maximum temperature (Degree C)
    count                    58316.000000
    mean                        21.731120
    std                          4.669517
    min                          7.700000
    25%                         18.200000
    50%                         21.600000
    75%                         24.900000
    max                         45.800000



```python
#Look at some of the data set
#This is the temperature throughout the year.
#The summer and winter cycles are obvious
#But there is a fair bit of variablity day-to-day
plt.plot(dataset[50000:])
plt.xlabel("Day")
plt.ylabel("Temperature (degrees Celsius)")
```




    Text(0, 0.5, 'Temperature (degrees Celsius)')




![png](../fig/fig-03DL-temperature.png.png)



```python
# split into train and test sets
#Use the first 58000 days as training
train=datasetScaled[50000:58000,:]
train=datasetScaled[0:58000,:]
#Use from 50000 to 58316 as testing set, 
#that means we will test on 8000 days we know the answer for, 
#leaving 316 that the algorithm has never seen!
test=datasetScaled[55000:,:]

print("Traing set is: ", train.shape)
print("Test set is: ", test.shape)
```

    Traing set is:  (58000, 1)
    Test set is:  (3316, 1)



```python
# convert an array of values into a dataset matrix
def create_dataset(dataset, look_back=1):
	dataX, dataY = [], []
	for i in range(len(dataset)-look_back-1):
		a = dataset[i:(i+look_back), 0]
		dataX.append(a)
		dataY.append(dataset[i + look_back, 0])
	return numpy.array(dataX), numpy.array(dataY)

# previous time steps to use as input variables to predict the next time period
look_back = 30 

# reshape into X=t and Y=t+look_back
trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)

# reshape input to be [samples, time steps, features]
trainX = numpy.reshape(trainX, (trainX.shape[0], trainX.shape[1], 1))
testX = numpy.reshape(testX, (testX.shape[0], testX.shape[1], 1))
```


```python
# create the LSTM network
#The network has a visible layer with 1 input, 
#a hidden layer with 4 LSTM blocks or neurons, 
#and an output layer that makes a single value prediction. 
#The default sigmoid activation function is used for the LSTM blocks. 
#The network is trained for 4 epochs and a batch size of 1 is used.

print("Running model...")
model = tf.keras.models.Sequential()

print("Adding LSTM.")
model.add(tf.keras.layers.LSTM(4, input_shape=(look_back, 1)))

print("Adding dense.")
model.add(tf.keras.layers.Dense(1))

print("Compiling.")
model.compile(loss='mean_squared_error', optimizer='adam')
```

    Running model...
    Adding LSTM.
    Adding dense.
    Compiling.



```python
#Fit the model, this takes the longest time
print("fitting...")
startT=time.time()
model.fit(trainX, trainY, epochs=4, batch_size=30, verbose=1)
endT=time.time()

print("Time taken: ", endT-startT)
```

    fitting...
    Train on 57969 samples
    Epoch 1/4
    57969/57969 [==============================] - 41s 699us/sample - loss: 0.0066
    Epoch 2/4
    57969/57969 [==============================] - 43s 741us/sample - loss: 0.0062
    Epoch 3/4
    57969/57969 [==============================] - 43s 745us/sample - loss: 0.0060
    Epoch 4/4
    57969/57969 [==============================] - 42s 731us/sample - loss: 0.0059
    Time taken:  169.15610480308533



```python
#Save or load the model
#model.save('kerasmodel.hdf5')
#model = tf.keras.models.load_model('kerasmodel.hdf5')
```


```python
#make predictions
trainPredict = model.predict(trainX)
testPredict = model.predict(testX)

# invert and rescale predictions
trainPredicti = scaler.inverse_transform(trainPredict)
trainYi = scaler.inverse_transform([trainY])
testPredicti = scaler.inverse_transform(testPredict)
testYi = scaler.inverse_transform([testY])

# calculate root mean squared error
trainScore = math.sqrt(mean_squared_error(trainYi[0], trainPredicti[:,0]))
print('Train Score: %.4f RMSE' % (trainScore))
testScore = math.sqrt(mean_squared_error(testYi[0], testPredicti[:,0]))
print('Test Score: %.4f RMSE' % (testScore))

```

    Train Score: 2.9142 RMSE
    Test Score: 2.9692 RMSE



```python
#PLOT the result

#Create a dataset that is the same size as the testing/training set 
dummyfull=numpy.ones((datasetScaled.shape[0]-test.shape[0],1))*numpy.mean(testPredict)
print(dummyfull.shape,testPredicti.shape,datasetScaled.shape)
testvec = numpy.concatenate((dummyfull,testPredict))

#Scale the data
transformer = MaxAbsScaler().fit(train[:])
testScale= transformer.transform(testvec)

print(trainPredict.shape,testPredict.shape,testvec.shape)

#do some funky things with the plotting just so we can look at a bit of it
zoomscale=-500
unseenPredicted = datasetScaled.shape[0]-train.shape[0]-50000

plt.plot(datasetScaled[zoomscale-unseenPredicted:])
plt.plot(train[zoomscale:],'r')
plt.plot(testScale[zoomscale-unseenPredicted:],'k')

plt.legend(["All Data","Training Data","Predicted data"])
plt.xlabel("Day")
plt.ylabel("Scaled Temperature")
plt.xlim([7800,8000])
plt.show()
```

    (55000, 1) (3285, 1) (58316, 1)
    (57969, 1) (3285, 1) (58285, 1)



![png](output_11_1.png)



```python

```


```python

```



## Run the straight python script to do everything in "batch" mode. 

Assuming the dataset, ```sydney_temperature.csv```, and python script, ```timeseries.py``` are in the same directory, to run in batch mode, simply envoke:
```
python timeseries.py
```
This script saves the figure to a file (instead of displaying it inline) and saves the model to a file also (for later use). The default looks at a much larger portion of the dataset than the Jupyter Notebook version defaults.
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




