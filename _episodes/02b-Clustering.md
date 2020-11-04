---
title: "02b. Clustering of data using sci-kit learn"
teaching: 20
exercises: 20
questions:
- "How can I learn more information about my data?"
- "What unsupervised approaches are availbe in Python?"
objectives:
- "Learn about the scikit-learn Kmeans algorithm"
- "Plot 3D data"
keypoints:
- "Read the docs to learn more"
- "More ways to wrangle data"
- "New ways to plot data"
---

Here we want to explore a neat an efficient away of exploring a (seisimic tomography) dataset in Python. We will be using a Machine Learning algorithm known as [K-Means clustering](https://scikit-learn.org/stable/modules/clustering.html#k-means). 

Data is from: * Li, C., van der Hilst, R. D., Engdahl, E. R., and Burdick, S. (2008), A new global model for P wave speed variations in Earth's mantle, Geochem. Geophys. Geosyst., 9, Q05018, doi:10.1029/2007GC001806 *


```python
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
```

Load in the tomography data set. Assign the column vectors to unique variables (for clarity).

```python
tomo=np.loadtxt('data/ggge1202-sup-0002-ds01.txt', skiprows=1)

lat=tomo[:,0]
lon=tomo[:,1]
depth=tomo[:,2]
dvp=tomo[:,3]
```

Now run the clustering algorithm

```python
kmeans = KMeans(n_clusters=10, random_state=0).fit(dvp.reshape(-1, 1))

#When completed, check the clusters the algorithm has identified.
print(kmeans.cluster_centers_)

```python
Note, many functions have been "parallelised" and tuned to best take advantage of your computer, see e.g. for more details [https://scikit-learn.org/stable/modules/computing.html#parallelism](https://scikit-learn.org/stable/modules/computing.html#parallelism)


Choose one of the clusters to visualise, and subset the data into new vectors accordingly

```python
centre=0

latClust=lat[kmeans.labels_==centre]
lonClust=lon[kmeans.labels_==centre]
depthClust=depth[kmeans.labels_==centre]
dvpClust=dvp[kmeans.labels_==centre]
```

Finally, plot the results!
```
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(lon, lat, -depth, c=dvp)
```
