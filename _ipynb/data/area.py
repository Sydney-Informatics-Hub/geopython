#Import the libraries we will need
import shapefile
import numpy as np
import matplotlib.pyplot as plt 
import multiprocessing
from itertools import product
import time

#Read in the shapefile that we will use
sf = shapefile.Reader("data/platepolygons/topology_platepolygons_0.00Ma.shp")
recs    = sf.records()
shapes  = sf.shapes()
fields  = sf.fields
Nshp    = len(shapes)

def PolygonArea(nshp):
    start_time = time.time()
    polygonShape=shapes[nshp].points
    corners=np.array(polygonShape)
    n = len(corners) # of corners
    
    #Area calculation using Shoelace forula
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    time.sleep(0.2)
    
    endtime=time.time() - start_time
    print("Process {} Finished in {:0.4f}s.".format(nshp,endtime))
    return(area)


def make_global(shapes):
	global gshapes
	gshapes = shapes


def main():

	#Check how many cpus are availble on your computer
	print("CPUs availble:", multiprocessing.cpu_count())
	print("Shapes to calculate the area of:", Nshp)

	polygons=np.arange(Nshp)

	#Run the function for each polygon/plate in the shapefile:
	start_time = time.time()
	Areas1=[]

	for i in polygons:
		Areas1.append(PolygonArea(i))
	print("Final Runtime", time.time() - start_time)

	#Run it again, but this time, use the multiprocessing capabilities
	start_time = time.time()
	with multiprocessing.Pool(initializer=make_global, initargs=(shapes,)) as pool:
		Areas2 = pool.map(PolygonArea,polygons)

	print("Final Runtime", time.time() - start_time)

if __name__=='__main__':
	main()
