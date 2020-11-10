---
title: "02a. Mapping with Cartopy"
teaching: 20
exercises: 20
questions:
- "What mapping features are availble in Python?"
- "How to use Cartopy?"
objectives:
- "Learn about cartopy"
- "Learn different approaches to plots and mapping"
keypoints:
- "Read the docs to learn more"
- "More ways to wrangle data"
- "New ways to plot data"
---

#  Cartopy

Is a mapping and imaging package originating from the Met. Office in the UK. The home page for the package is http://scitools.org.uk/cartopy/. Like many python packages, the [documentation](http://scitools.org.uk/cartopy/docs/latest/index.html) is patchy and the best way to learn is to try to do things and ask other people who have figured out this and that. 

We are going to work through a number of the examples and try to extend them to do the kinds of things you might find interesting and useful in the future. The examples are in the form of a [gallery](http://scitools.org.uk/cartopy/docs/latest/gallery.html)

You might also want to look at the [list of map projections](http://scitools.org.uk/cartopy/docs/latest/crs/projections.html) from time to time. Not all maps can be plotted in every projection (sometimes because of bugs and sometimes because they are not supposed to work for the data you have) but you can try them and see what happens.

Cartopy is built on top of a lot of the matplotlib graphing tools. It works by introducing a series of projections associated with the axes of a graph. On top of that there is a big toolkit for reading in images, finding data from standard web feeds, and manipulating geographical objects. Many, many libraries are involved and sometimes things break. Luckily the installation that is built for this course is about as reliable as we can ever get. I'm just warning you, though, that it can be quite tough if you want to put this on your laptop from scratch.






## Let's get started

We have a number of imports that we will need almost every time. 

If we are going to plot anything then we need to include **matplotlib**.




```python
%pylab inline

import matplotlib.pyplot as plt

import cartopy
import cartopy.crs as ccrs
```

    Populating the interactive namespace from numpy and matplotlib



```python
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()
ax.coastlines()

```




    <cartopy.mpl.feature_artist.FeatureArtist at 0x7f5bae6a2b38>




    
![png](fig/fig-02map-map1.png)
    


The simplest plot: global map using the default image built into the package and adding coastlines


```python

fig = plt.figure(figsize=(12, 12), facecolor="none")
ax  = plt.axes(projection=ccrs.Mercator())

    # make the map global rather than have it zoom in to
    # the extents of any plotted data
    
ax.set_global()
ax.coastlines()  
ax.stock_img()


```




    <matplotlib.image.AxesImage at 0x7f5bae5bb358>




    
![png](fig-02map-map2.png)
    


Try changing the projection - either look at the list in the link I gave you above or use the tab-completion feature of iPython to see what ``ccrs`` has available ( not everything will be a projection, but you can see what works and what breaks ).

Here is how you can plot a region instead of the globe:


```python

fig = plt.figure(figsize=(12, 12), facecolor="none")
ax  = plt.axes(projection=ccrs.Robinson())    
ax.set_extent([0, 40, 28, 48])

ax.coastlines(resolution='50m')  
ax.stock_img()

```




    <matplotlib.image.AxesImage at 0x7f5bae5a4a20>




    
![png](fig-02map-map3.png)
    



```python
help(ax.stock_img)
```

    Help on method stock_img in module cartopy.mpl.geoaxes:
    
    stock_img(name='ne_shaded') method of cartopy.mpl.geoaxes.GeoAxesSubplot instance
        Add a standard image to the map.
        
        Currently, the only (and default) option is a downsampled version of
        the Natural Earth shaded relief raster.
    



```python

```




# Handling images

We will work with images which are in **geotiff** format. These are standard image files (i.e. they are ``.tif`` files) but they also contain information on the coordinates and the base projection of the image. There are various tools for making and converting these images but one important thing to know is that they are the becoming a standard that you are very likely to encounter as a way to store data and deliver it on the web. If you download tiles of data served up as google earth layers, you may well find that you have a geotiff. 

Here is an example - it uses the **gdal** library for manipulating geospatial data. The image is a freely available download of the NASA *blue marble* image set which I retrieved for you.


```python
%pylab inline

import cartopy
import gdal
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
```

    Populating the interactive namespace from numpy and matplotlib



```python
globalmarble      = gdal.Open("../../Data/Resources/BlueMarbleNG-TB_2004-06-01_rgb_3600x1800.TIFF")
globalmarble_img  = globalmarble.ReadAsArray().transpose(1,2,0)

# Note that we convert the gdal object into an image array - and also have to re-organise the data 
# This is a numpy call that you can look up to see what it does and you can also look
# at the original array data to see what is there.
```


```python
fig = plt.figure(figsize=(12, 12), facecolor="none")
plt.imshow(globalmarble_img)
```




    <matplotlib.image.AxesImage at 0x7f33be45fef0>




    
![png](fig-02map-map4.png)
    


This looks really nice but it is just the original image plotted in its original shape. 

The gdal object can tell you the projection which applies to the original data and various other attributes. This might not seems particularly useful at this point, but it is helpful to realise that there is a lot of information being passed around behind the scenes when you use these tools.



```python
print ("1 - ", globalmarble.GetProjection(), "\n")
print ("2 - ", globalmarble.GetDescription(), "\n")
print ("3 - ", globalmarble.GetMetadata(), "\n")
print ("4 - ", globalmarble.GetGeoTransform())
```

    1 -  GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433],AUTHORITY["EPSG","4326"]] 
    
    2 -  ../../Data/Resources/BlueMarbleNG-TB_2004-06-01_rgb_3600x1800.TIFF 
    
    3 -  {'AREA_OR_POINT': 'Area', 'TIFFTAG_RESOLUTIONUNIT': '1 (unitless)', 'TIFFTAG_XRESOLUTION': '1', 'TIFFTAG_YRESOLUTION': '1'} 
    
    4 -  (-180.0, 0.1, 0.0, 90.0, 0.0, -0.1)


### Projections

What if we want to use a different projection for the image. For example, we might want to use this as a background to plot some other information. How does this work ?

Let's try what we used before to plot with a different projection. Specifically, let's try an orthographic projection which should wrap the image around a sphere and show us the disk from a particular orientation. Here is one I made earlier ... the output should look like this:

<img src="../../Data/Reference/OrthographicProjectionBlueMarble.png" width=30%>



```python
fig = plt.figure(figsize=(12, 12), facecolor="none")
ax = plt.axes(projection=ccrs.Orthographic())
plt.imshow(globalmarble_img, zorder=0)
ax.coastlines(color="Yellow", zorder=1)  
plt.show()

```


    
![png](fig-02map-map5.png)
    


OK, that didn't look like the sample image that I claimed it should and the reason is that we didn't tell the plotting routines what the original projection for the data was. Here is the fix: tell the ``imshow`` command the transformation of the original data - (this can take a little while to process).


```python
fig = plt.figure(figsize=(12, 12), facecolor="none")
ax = plt.axes(projection=ccrs.Orthographic())
plt.imshow(globalmarble_img, zorder=0, transform=ccrs.PlateCarree())
ax.coastlines(color="Yellow", zorder=1)  

plt.show()

```


    
![png](fig-02map-map6.png)
    


You can try other projections here, though I have found quite a few do not behave in quite the way you expect !

Feel free to play with these data which are global magnetic intensity, the global etopo database of topography and bathymetry in color format and a black/white (height only) version of the same thing, all of them have the base projection of **PlateCarree**. Note that we can define a variable which points to this function and pass it into the transform argument of ``imshow``


```python
base_projection   = ccrs.PlateCarree() 

globalmag         = gdal.Open("../../Data/Resources/EMAG2_image_V2.tif")
globalmag_img     = globalmag.ReadAsArray().transpose(1,2,0)
globalmag_img_s   = globalmag_img[::2,::2,::]
del(globalmag)

globaletopo       = gdal.Open("../../Data/Resources/color_etopo1_ice_low.tif")
globaletopo_img   = globaletopo.ReadAsArray().transpose(1,2,0)
del(globaletopo)
```


```python
print (globalmag_img.shape)
print (globalmag_img_s.shape)
print (globalmarble_img.shape)
```

    (5400, 10800, 3)
    (2700, 5400, 3)
    (1800, 3600, 3)



```python
# Global pretty map ... can you make one centred on Australia and save it to an image ?

#projection = ccrs.Orthographic(central_longitude=80.0, central_latitude=30.0, globe=None)
this_projection = ccrs.PlateCarree()

global_extent     = [-180.0, 180.0, -90.0, 90.0]

fig = plt.figure(figsize=(12, 12), facecolor="none")
ax = plt.axes(projection=this_projection)
ax.imshow(globalmag_img_s, origin='upper', transform=base_projection, extent=global_extent)
ax.imshow(globalmarble_img, origin='upper', transform=base_projection, extent=global_extent, alpha=0.5)
ax.coastlines(color="yellow")

plt.show()
```


    
![png](fig-02map-map7.png)
    





