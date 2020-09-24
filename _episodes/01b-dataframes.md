---
title: "01b. Python Fundamentals - shapefiles and dataframes"
teaching: 10
exercises: 0
questions:
- "What else can Python do?"
- "What are libraries and packages?"
objectives:
- "Learn the ."
keypoints:
- "Shapefiles"
- "Pandas dataframes"
---

## Dealing with other data types
Python can deal with basically any type of data you throw at it. The community have provided many packages that make things easy, today we will look at the "pyshp" (for dealing with shapefiles) and "pandas" (great for tables nad time series) packages.

Data for this exercised was downloaded from http://www.bom.gov.au/water/groundwater/explorer/map.shtml

# Shapefiles
Shapefiles are a very common file format for GIS data.


```python
#Load the required modules
import shapefile

#NOTE: Weirdly and confusingly, this package is called "pyshp" but you call it via the name "shapefile"
```


```python
help(shapefile)
#Or check out the help pages https://github.com/GeospatialPython/pyshp
```

    Help on module shapefile:
    
    NAME
        shapefile
    
    FILE
        c:\users\nbutter\anaconda3\envs\pygeol\lib\site-packages\shapefile.py
    
    DESCRIPTION
        shapefile.py
        Provides read and write support for ESRI Shapefiles.
        author: jlawhead<at>geospatialpython.com
        date: 2017/08/24
        version: 1.2.12
        Compatible with Python versions 2.7-3.x
    
    CLASSES
        exceptions.Exception(exceptions.BaseException)
            ShapefileException
        Reader
        Writer
            Editor
        
        class Editor(Writer)
         |  Methods defined here:
         |  
         |  __init__(self, shapefile=None, shapeType=1, autoBalance=1)
         |  
         |  balance(self)
         |      Adds a corresponding empty attribute or null geometry record depending
         |      on which type of record was created to make sure all three files
         |      are in synch.
         |  
         |  delete(self, shape=None, part=None, point=None)
         |      Deletes the specified part of any shape by specifying a shape
         |      number, part number, or point number.
         |  
         |  point(self, x=None, y=None, z=None, m=None, shape=None, part=None, point=None, addr=None)
         |      Creates/updates a point shape. The arguments allows
         |      you to update a specific point by shape, part, point of any
         |      shape type.
         |  
         |  select(self, expr)
         |      Select one or more shapes (to be implemented)
         |  
         |  validate(self)
         |      An optional method to try and validate the shapefile
         |      as much as possible before writing it (not implemented).
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from Writer:
         |  
         |  bbox(self)
         |      Returns the current bounding box for the shapefile which is
         |      the lower-left and upper-right corners. It does not contain the
         |      elevation or measure extremes.
         |  
         |  field(self, name, fieldType='C', size='50', decimal=0)
         |      Adds a dbf field descriptor to the shapefile.
         |  
         |  line(self, parts=[], shapeType=3)
         |      Creates a line shape. This method is just a convienience method
         |      which wraps 'poly()'.
         |  
         |  mbox(self)
         |      Returns the current m extremes for the shapefile.
         |  
         |  null(self)
         |      Creates a null shape.
         |  
         |  poly(self, parts=[], shapeType=5, partTypes=[])
         |      Creates a shape that has multiple collections of points (parts)
         |      including lines, polygons, and even multipoint shapes. If no shape type
         |      is specified it defaults to 'polygon'. If no part types are specified
         |      (which they normally won't be) then all parts default to the shape type.
         |  
         |  record(self, *recordList, **recordDict)
         |      Creates a dbf attribute record. You can submit either a sequence of
         |      field values or keyword arguments of field names and values. Before
         |      adding records you must add fields for the record values using the
         |      fields() method. If the record values exceed the number of fields the
         |      extra ones won't be added. In the case of using keyword arguments to specify
         |      field/value pairs only fields matching the already registered fields
         |      will be added.
         |  
         |  save(self, target=None, shp=None, shx=None, dbf=None)
         |      Save the shapefile data to three files or
         |      three file-like objects. SHP and DBF files can also
         |      be written exclusively using saveShp, saveShx, and saveDbf respectively.
         |      If target is specified but not shp,shx, or dbf then the target path and
         |      file name are used.  If no options or specified, a unique base file name
         |      is generated to save the files and the base file name is returned as a 
         |      string.
         |  
         |  saveDbf(self, target)
         |      Save a dbf file.
         |  
         |  saveShp(self, target)
         |      Save an shp file.
         |  
         |  saveShx(self, target)
         |      Save an shx file.
         |  
         |  shape(self, i)
         |  
         |  shapes(self)
         |      Return the current list of shapes.
         |  
         |  zbox(self)
         |      Returns the current z extremes for the shapefile.
        
        class Reader
         |  Reads the three files of a shapefile as a unit or
         |  separately.  If one of the three files (.shp, .shx,
         |  .dbf) is missing no exception is thrown until you try
         |  to call a method that depends on that particular file.
         |  The .shx index file is used if available for efficiency
         |  but is not required to read the geometry from the .shp
         |  file. The "shapefile" argument in the constructor is the
         |  name of the file you want to open.
         |  
         |  You can instantiate a Reader without specifying a shapefile
         |  and then specify one later with the load() method.
         |  
         |  Only the shapefile headers are read upon loading. Content
         |  within each file is only accessed when required and as
         |  efficiently as possible. Shapefiles are usually not large
         |  but they can be.
         |  
         |  Methods defined here:
         |  
         |  __init__(self, *args, **kwargs)
         |  
         |  iterRecords(self)
         |      Serves up records in a dbf file as an iterator.
         |      Useful for large shapefiles or dbf files.
         |  
         |  iterShapeRecords(self)
         |      Returns a generator of combination geometry/attribute records for
         |      all records in a shapefile.
         |  
         |  iterShapes(self)
         |      Serves up shapes in a shapefile as an iterator. Useful
         |      for handling large shapefiles.
         |  
         |  load(self, shapefile=None)
         |      Opens a shapefile from a filename or file-like
         |      object. Normally this method would be called by the
         |      constructor with the file name as an argument.
         |  
         |  record(self, i=0)
         |      Returns a specific dbf record based on the supplied index.
         |  
         |  records(self)
         |      Returns all records in a dbf file.
         |  
         |  shape(self, i=0)
         |      Returns a shape object for a shape in the the geometry
         |      record file.
         |  
         |  shapeRecord(self, i=0)
         |      Returns a combination geometry and attribute record for the
         |      supplied record index.
         |  
         |  shapeRecords(self)
         |      Returns a list of combination geometry/attribute records for
         |      all records in a shapefile.
         |  
         |  shapes(self)
         |      Returns all shapes in a shapefile.
        
        class ShapefileException(exceptions.Exception)
         |  An exception to handle shapefile specific problems.
         |  
         |  Method resolution order:
         |      ShapefileException
         |      exceptions.Exception
         |      exceptions.BaseException
         |      __builtin__.object
         |  
         |  Data descriptors defined here:
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from exceptions.Exception:
         |  
         |  __init__(...)
         |      x.__init__(...) initializes x; see help(type(x)) for signature
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes inherited from exceptions.Exception:
         |  
         |  __new__ = <built-in method __new__ of type object>
         |      T.__new__(S, ...) -> a new object with type S, a subtype of T
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from exceptions.BaseException:
         |  
         |  __delattr__(...)
         |      x.__delattr__('name') <==> del x.name
         |  
         |  __getattribute__(...)
         |      x.__getattribute__('name') <==> x.name
         |  
         |  __getitem__(...)
         |      x.__getitem__(y) <==> x[y]
         |  
         |  __getslice__(...)
         |      x.__getslice__(i, j) <==> x[i:j]
         |      
         |      Use of negative indices is not supported.
         |  
         |  __reduce__(...)
         |  
         |  __repr__(...)
         |      x.__repr__() <==> repr(x)
         |  
         |  __setattr__(...)
         |      x.__setattr__('name', value) <==> x.name = value
         |  
         |  __setstate__(...)
         |  
         |  __str__(...)
         |      x.__str__() <==> str(x)
         |  
         |  __unicode__(...)
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors inherited from exceptions.BaseException:
         |  
         |  __dict__
         |  
         |  args
         |  
         |  message
        
        class Writer
         |  Provides write support for ESRI Shapefiles.
         |  
         |  Methods defined here:
         |  
         |  __init__(self, shapeType=None)
         |  
         |  bbox(self)
         |      Returns the current bounding box for the shapefile which is
         |      the lower-left and upper-right corners. It does not contain the
         |      elevation or measure extremes.
         |  
         |  field(self, name, fieldType='C', size='50', decimal=0)
         |      Adds a dbf field descriptor to the shapefile.
         |  
         |  line(self, parts=[], shapeType=3)
         |      Creates a line shape. This method is just a convienience method
         |      which wraps 'poly()'.
         |  
         |  mbox(self)
         |      Returns the current m extremes for the shapefile.
         |  
         |  null(self)
         |      Creates a null shape.
         |  
         |  point(self, x, y, z=0, m=0, shapeType=1)
         |      Creates a point shape.
         |  
         |  poly(self, parts=[], shapeType=5, partTypes=[])
         |      Creates a shape that has multiple collections of points (parts)
         |      including lines, polygons, and even multipoint shapes. If no shape type
         |      is specified it defaults to 'polygon'. If no part types are specified
         |      (which they normally won't be) then all parts default to the shape type.
         |  
         |  record(self, *recordList, **recordDict)
         |      Creates a dbf attribute record. You can submit either a sequence of
         |      field values or keyword arguments of field names and values. Before
         |      adding records you must add fields for the record values using the
         |      fields() method. If the record values exceed the number of fields the
         |      extra ones won't be added. In the case of using keyword arguments to specify
         |      field/value pairs only fields matching the already registered fields
         |      will be added.
         |  
         |  save(self, target=None, shp=None, shx=None, dbf=None)
         |      Save the shapefile data to three files or
         |      three file-like objects. SHP and DBF files can also
         |      be written exclusively using saveShp, saveShx, and saveDbf respectively.
         |      If target is specified but not shp,shx, or dbf then the target path and
         |      file name are used.  If no options or specified, a unique base file name
         |      is generated to save the files and the base file name is returned as a 
         |      string.
         |  
         |  saveDbf(self, target)
         |      Save a dbf file.
         |  
         |  saveShp(self, target)
         |      Save an shp file.
         |  
         |  saveShx(self, target)
         |      Save an shx file.
         |  
         |  shape(self, i)
         |  
         |  shapes(self)
         |      Return the current list of shapes.
         |  
         |  zbox(self)
         |      Returns the current z extremes for the shapefile.
    
    FUNCTIONS
        b(v)
        
        calcsize(...)
            Return size of C struct described by format string fmt.
        
        is_string(v)
        
        pack(...)
            Return string containing values v1, v2, ... packed according to fmt.
        
        signed_area(coords)
            Return the signed area enclosed by a ring using the linear time
            algorithm. A value >= 0 indicates a counter-clockwise oriented ring.
        
        test(**kwargs)
            # Begin Testing
        
        u(v)
        
        unpack(...)
            Unpack the string containing packed C structure data, according to fmt.
            Requires len(string) == calcsize(fmt).
    
    DATA
        MISSING = [None, '']
        MULTIPATCH = 31
        MULTIPOINT = 8
        MULTIPOINTM = 28
        MULTIPOINTZ = 18
        NULL = 0
        POINT = 1
        POINTM = 21
        POINTZ = 11
        POLYGON = 5
        POLYGONM = 25
        POLYGONZ = 15
        POLYLINE = 3
        POLYLINEM = 23
        POLYLINEZ = 13
        PYTHON3 = False
        __version__ = '1.2.12'
    
    VERSION
        1.2.12
    
    



```python
#Set the filename
boreshape='../data/shp_torrens_river/NGIS_BoreLine.shp'

#read in the file
shapeRead = shapefile.Reader(boreshape)

#And save out some of the shape file attributes
recs    = shapeRead.records()
shapes  = shapeRead.shapes()
fields  = shapeRead.fields
Nshp    = len(shapes)
```


```python
print(Nshp) #print the Number of items in the shapefile
```

    7635



```python
fields[:]#print the fields
```




    [('DeletionFlag', 'C', 1, 0),
     ['HydroID', 'N', 10, 0],
     ['HydroCode', 'C', 30, 0],
     ['BoreID', 'N', 10, 0],
     ['TopElev', 'F', 19, 11],
     ['BottomElev', 'F', 19, 11],
     ['HGUID', 'N', 10, 0],
     ['HGUNumber', 'N', 10, 0],
     ['NafHGUNumb', 'N', 10, 0],
     ['SHAPE_Leng', 'F', 19, 11]]




```python
recs[0] #print the first record, then this is a list that can be subscripted further
```




    [32001999, '652800645', 30027773, 6.74, -74.26, 31000043, 1042, 104005, 0.0]




```python
shapes[0].points #print the point values of the first shape
```




    [(591975.5150000006, -3816141.8817), (591975.5150000006, -3816141.8817)]



Shapefiles are not a native python format, but the community have developed tools for exploring them. The package we have used "pyshp" imported with the name "shapefile" (for some non-consistent weird reason), is one example of working with shapefiles. Alternatives exist.

## More table manipulation


```python
#Import the module
import pandas
```


```python
#read in the data
log_data=pandas.read_csv("../data/shp_torrens_river/NGIS_LithologyLog.csv",\
                         header=0,sep=',',skipinitialspace=True,quotechar ='"',\
                         usecols=list(range(0,13)),\
                         skiprows=[453,456,458,460,689,697,720,723,726,839,880,884,885,890,898,934])

#This data was weird because it has quotation marks to signify inches inside comments within the file, 
#making automatic reading of it tricky
```


```python
log_data           # print the first 30 and last 30 rows
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
      <th>OBJECTID</th>
      <th>BoreID</th>
      <th>HydroCode</th>
      <th>RefElev</th>
      <th>RefElevDesc</th>
      <th>FromDepth</th>
      <th>ToDepth</th>
      <th>TopElev</th>
      <th>BottomElev</th>
      <th>MajorLithCode</th>
      <th>MinorLithCode</th>
      <th>Description</th>
      <th>Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1769789</td>
      <td>30062892</td>
      <td>662815923</td>
      <td>57.25</td>
      <td>NGS</td>
      <td>18.0</td>
      <td>19.5</td>
      <td>39.25</td>
      <td>37.75</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Clay</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1769790</td>
      <td>30062892</td>
      <td>662815923</td>
      <td>57.25</td>
      <td>NGS</td>
      <td>19.5</td>
      <td>22.0</td>
      <td>37.75</td>
      <td>35.25</td>
      <td>ROCK</td>
      <td>None</td>
      <td>Rocks and sand</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1769791</td>
      <td>30062892</td>
      <td>662815923</td>
      <td>57.25</td>
      <td>NGS</td>
      <td>22.0</td>
      <td>24.0</td>
      <td>35.25</td>
      <td>33.25</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Clay</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1770725</td>
      <td>30141910</td>
      <td>662816624</td>
      <td>4.0</td>
      <td>NGS</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>4.0</td>
      <td>-2.0</td>
      <td>None</td>
      <td>None</td>
      <td>No sample</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1770726</td>
      <td>30141910</td>
      <td>662816624</td>
      <td>4.0</td>
      <td>NGS</td>
      <td>6.0</td>
      <td>15.0</td>
      <td>-2.0</td>
      <td>-11.0</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Clay - orange-red grey, mottled; stiff-sticky....</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1770727</td>
      <td>30141910</td>
      <td>662816624</td>
      <td>4.0</td>
      <td>NGS</td>
      <td>15.0</td>
      <td>18.0</td>
      <td>-11.0</td>
      <td>-14.0</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Sandy clay - red brown, grey, green, white mot...</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1770728</td>
      <td>30141910</td>
      <td>662816624</td>
      <td>4.0</td>
      <td>NGS</td>
      <td>18.0</td>
      <td>21.0</td>
      <td>-14.0</td>
      <td>-17.0</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Clay - red green mottled; stiff. fine sand, qtz.</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1770729</td>
      <td>30141910</td>
      <td>662816624</td>
      <td>4.0</td>
      <td>NGS</td>
      <td>21.0</td>
      <td>24.0</td>
      <td>-17.0</td>
      <td>-20.0</td>
      <td>SAND</td>
      <td>None</td>
      <td>Clayey sand - orange green mottled; stiff. fin...</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1770730</td>
      <td>30141910</td>
      <td>662816624</td>
      <td>4.0</td>
      <td>NGS</td>
      <td>24.0</td>
      <td>28.5</td>
      <td>-20.0</td>
      <td>-24.5</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Clay - red-green grey, mottled; stiff.</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1770731</td>
      <td>30141910</td>
      <td>662816624</td>
      <td>4.0</td>
      <td>NGS</td>
      <td>28.5</td>
      <td>30.0</td>
      <td>-24.5</td>
      <td>-26.0</td>
      <td>SAND</td>
      <td>None</td>
      <td>Clayey sand - red green, mottled; sticky. fine...</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1770732</td>
      <td>30141910</td>
      <td>662816624</td>
      <td>4.0</td>
      <td>NGS</td>
      <td>30.0</td>
      <td>34.5</td>
      <td>-26.0</td>
      <td>-30.5</td>
      <td>SAND</td>
      <td>GRVL</td>
      <td>Sand/gravel - fine sand - fine gravel, clear, ...</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1770733</td>
      <td>30141910</td>
      <td>662816624</td>
      <td>4.0</td>
      <td>NGS</td>
      <td>34.5</td>
      <td>36.0</td>
      <td>-30.5</td>
      <td>-32.0</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Clay - grey red mottled; soft - plastic.</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>12</th>
      <td>1770734</td>
      <td>30141910</td>
      <td>662816624</td>
      <td>4.0</td>
      <td>NGS</td>
      <td>36.0</td>
      <td>44.0</td>
      <td>-32.0</td>
      <td>-40.0</td>
      <td>SAND</td>
      <td>None</td>
      <td>Sand - fine-medium, clear, opaque, fe stained ...</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1770735</td>
      <td>30141910</td>
      <td>662816624</td>
      <td>4.0</td>
      <td>NGS</td>
      <td>44.0</td>
      <td>48.0</td>
      <td>-40.0</td>
      <td>-44.0</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Clay - grey green; stiff - plastic; minor fine...</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1770736</td>
      <td>30141910</td>
      <td>662816624</td>
      <td>4.0</td>
      <td>NGS</td>
      <td>48.0</td>
      <td>51.0</td>
      <td>-44.0</td>
      <td>-47.0</td>
      <td>None</td>
      <td>None</td>
      <td>No sample.</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>15</th>
      <td>1770737</td>
      <td>30141910</td>
      <td>662816624</td>
      <td>4.0</td>
      <td>NGS</td>
      <td>51.0</td>
      <td>54.0</td>
      <td>-47.0</td>
      <td>-50.0</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Clay - red green; plastic, sticky; minor fine-...</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1770738</td>
      <td>30141910</td>
      <td>662816624</td>
      <td>4.0</td>
      <td>NGS</td>
      <td>57.0</td>
      <td>64.0</td>
      <td>-53.0</td>
      <td>-60.0</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Clay - green grey; stiff. minor silt/fine sand...</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>17</th>
      <td>1770739</td>
      <td>30141910</td>
      <td>662816624</td>
      <td>4.0</td>
      <td>NGS</td>
      <td>64.0</td>
      <td>66.0</td>
      <td>-60.0</td>
      <td>-62.0</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Sandy clay - cream; fine sand.</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>18</th>
      <td>1770740</td>
      <td>30141910</td>
      <td>662816624</td>
      <td>4.0</td>
      <td>NGS</td>
      <td>66.0</td>
      <td>75.0</td>
      <td>-62.0</td>
      <td>-71.0</td>
      <td>SAND</td>
      <td>None</td>
      <td>Clayey sand - cream-pale green grey, fine sand...</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>19</th>
      <td>1770741</td>
      <td>30141910</td>
      <td>662816624</td>
      <td>4.0</td>
      <td>NGS</td>
      <td>75.0</td>
      <td>90.0</td>
      <td>-71.0</td>
      <td>-86.0</td>
      <td>SAND</td>
      <td>GRVL</td>
      <td>Sand/gravel - coarse (1-3mm), predominantly op...</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>20</th>
      <td>1770742</td>
      <td>30141910</td>
      <td>662816624</td>
      <td>4.0</td>
      <td>NGS</td>
      <td>90.0</td>
      <td>98.5</td>
      <td>-86.0</td>
      <td>-94.5</td>
      <td>SILT</td>
      <td>SAND</td>
      <td>Silt/sand - grey; fine sand (0.05-0.1mm), qtz,...</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1770743</td>
      <td>30141910</td>
      <td>662816624</td>
      <td>4.0</td>
      <td>NGS</td>
      <td>98.5</td>
      <td>114.0</td>
      <td>-94.5</td>
      <td>-110.0</td>
      <td>LMST</td>
      <td>None</td>
      <td>Limestone - shell and coral fragments (drill c...</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>22</th>
      <td>1770744</td>
      <td>30141910</td>
      <td>662816624</td>
      <td>4.0</td>
      <td>NGS</td>
      <td>114.0</td>
      <td>117.0</td>
      <td>-110.0</td>
      <td>-113.0</td>
      <td>SDST</td>
      <td>None</td>
      <td>Sandstone - yellow grey; interbedded with sand...</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>23</th>
      <td>1770745</td>
      <td>30141910</td>
      <td>662816624</td>
      <td>4.0</td>
      <td>NGS</td>
      <td>117.0</td>
      <td>125.0</td>
      <td>-113.0</td>
      <td>-121.0</td>
      <td>SDST</td>
      <td>LMST</td>
      <td>Sandstone/limestone - yellow grey; carbonate +...</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1770746</td>
      <td>30141910</td>
      <td>662816624</td>
      <td>4.0</td>
      <td>NGS</td>
      <td>125.0</td>
      <td>147.3</td>
      <td>-121.0</td>
      <td>-143.3</td>
      <td>SDST</td>
      <td>LMST</td>
      <td>Sandstone/limestone - grey white and grey; fin...</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>25</th>
      <td>1770747</td>
      <td>30141910</td>
      <td>662816624</td>
      <td>4.0</td>
      <td>NGS</td>
      <td>147.3</td>
      <td>148.3</td>
      <td>-143.3</td>
      <td>-144.3</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Clay - steel grey-blue; sticky. (munno para cl...</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>26</th>
      <td>1771871</td>
      <td>30141911</td>
      <td>662816625</td>
      <td>4.0</td>
      <td>UNK</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>4.0</td>
      <td>-2.0</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Silty clay - yellow brown; minor sand component.</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>27</th>
      <td>1771873</td>
      <td>30141911</td>
      <td>662816625</td>
      <td>4.0</td>
      <td>UNK</td>
      <td>6.0</td>
      <td>21.0</td>
      <td>-2.0</td>
      <td>-17.0</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Silty clay (gravel) - grey and brown, mottled;...</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>28</th>
      <td>1771874</td>
      <td>30141911</td>
      <td>662816625</td>
      <td>4.0</td>
      <td>UNK</td>
      <td>21.0</td>
      <td>36.0</td>
      <td>-17.0</td>
      <td>-32.0</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Silty clay (gravel) - grey and brown, mottled;...</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>29</th>
      <td>1771875</td>
      <td>30141911</td>
      <td>662816625</td>
      <td>4.0</td>
      <td>UNK</td>
      <td>36.0</td>
      <td>42.0</td>
      <td>-32.0</td>
      <td>-38.0</td>
      <td>SAND</td>
      <td>None</td>
      <td>Clayey sand - orange brown; fine (0.1mm) - coa...</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>...</th>
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
    <tr>
      <th>70127</th>
      <td>4120275</td>
      <td>30300938</td>
      <td>662829132</td>
      <td>None</td>
      <td>UNK</td>
      <td>0.0</td>
      <td>0.8</td>
      <td>None</td>
      <td>None</td>
      <td>SILT</td>
      <td>None</td>
      <td>Gravelly silt</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70128</th>
      <td>4120276</td>
      <td>30300938</td>
      <td>662829132</td>
      <td>None</td>
      <td>UNK</td>
      <td>0.8</td>
      <td>7.5</td>
      <td>None</td>
      <td>None</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Silty clay</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70129</th>
      <td>4120277</td>
      <td>30300938</td>
      <td>662829132</td>
      <td>None</td>
      <td>UNK</td>
      <td>7.5</td>
      <td>8.5</td>
      <td>None</td>
      <td>None</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Sandy clay</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70130</th>
      <td>4120278</td>
      <td>30300938</td>
      <td>662829132</td>
      <td>None</td>
      <td>UNK</td>
      <td>8.5</td>
      <td>10.0</td>
      <td>None</td>
      <td>None</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Gravelly/silty clay</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70131</th>
      <td>4120279</td>
      <td>30300938</td>
      <td>662829132</td>
      <td>None</td>
      <td>UNK</td>
      <td>10.0</td>
      <td>17.0</td>
      <td>None</td>
      <td>None</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Silty clay</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70132</th>
      <td>4120280</td>
      <td>30301335</td>
      <td>662829148</td>
      <td>None</td>
      <td>UNK</td>
      <td>0.0</td>
      <td>16.0</td>
      <td>None</td>
      <td>None</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Silty clay</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70133</th>
      <td>4120281</td>
      <td>30301339</td>
      <td>662829152</td>
      <td>None</td>
      <td>UNK</td>
      <td>0.0</td>
      <td>11.2</td>
      <td>None</td>
      <td>None</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Silty clay</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70134</th>
      <td>4120282</td>
      <td>30301339</td>
      <td>662829152</td>
      <td>None</td>
      <td>UNK</td>
      <td>11.2</td>
      <td>12.0</td>
      <td>None</td>
      <td>None</td>
      <td>GRVL</td>
      <td>None</td>
      <td>Gravels</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70135</th>
      <td>4120283</td>
      <td>30301339</td>
      <td>662829152</td>
      <td>None</td>
      <td>UNK</td>
      <td>12.0</td>
      <td>15.2</td>
      <td>None</td>
      <td>None</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Sandy clay</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70136</th>
      <td>4120284</td>
      <td>30301339</td>
      <td>662829152</td>
      <td>None</td>
      <td>UNK</td>
      <td>15.2</td>
      <td>17.0</td>
      <td>None</td>
      <td>None</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Sandy clay, clayey sand</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70137</th>
      <td>4120302</td>
      <td>30302253</td>
      <td>662829174</td>
      <td>None</td>
      <td>UNK</td>
      <td>0.0</td>
      <td>0.3</td>
      <td>None</td>
      <td>None</td>
      <td>SAND</td>
      <td>None</td>
      <td>Clayey sand dark brown</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70138</th>
      <td>4120303</td>
      <td>30302253</td>
      <td>662829174</td>
      <td>None</td>
      <td>UNK</td>
      <td>0.3</td>
      <td>1.1</td>
      <td>None</td>
      <td>None</td>
      <td>SAND</td>
      <td>None</td>
      <td>Sand clay orange brown</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70139</th>
      <td>4120304</td>
      <td>30302253</td>
      <td>662829174</td>
      <td>None</td>
      <td>UNK</td>
      <td>1.1</td>
      <td>4.5</td>
      <td>None</td>
      <td>None</td>
      <td>SAND</td>
      <td>None</td>
      <td>Clayey sand orange grey</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70140</th>
      <td>4120305</td>
      <td>30302252</td>
      <td>662829173</td>
      <td>None</td>
      <td>UNK</td>
      <td>0.0</td>
      <td>0.3</td>
      <td>None</td>
      <td>None</td>
      <td>SAND</td>
      <td>None</td>
      <td>Clayey sand dark brown</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70141</th>
      <td>4120306</td>
      <td>30302252</td>
      <td>662829173</td>
      <td>None</td>
      <td>UNK</td>
      <td>0.3</td>
      <td>1.1</td>
      <td>None</td>
      <td>None</td>
      <td>SAND</td>
      <td>None</td>
      <td>Sand clay orange brown</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70142</th>
      <td>4120307</td>
      <td>30302252</td>
      <td>662829173</td>
      <td>None</td>
      <td>UNK</td>
      <td>1.1</td>
      <td>4.5</td>
      <td>None</td>
      <td>None</td>
      <td>SAND</td>
      <td>None</td>
      <td>Clayey sand orange grey</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70143</th>
      <td>4120312</td>
      <td>30303742</td>
      <td>662829205</td>
      <td>None</td>
      <td>UNK</td>
      <td>0.0</td>
      <td>8.0</td>
      <td>None</td>
      <td>None</td>
      <td>FILL</td>
      <td>None</td>
      <td>Pug hole no returns</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70144</th>
      <td>4120313</td>
      <td>30303742</td>
      <td>662829205</td>
      <td>None</td>
      <td>UNK</td>
      <td>8.0</td>
      <td>17.0</td>
      <td>None</td>
      <td>None</td>
      <td>UKN</td>
      <td>None</td>
      <td>Cuttings lost into pug hole</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70145</th>
      <td>4120314</td>
      <td>30303990</td>
      <td>652802870</td>
      <td>None</td>
      <td>UNK</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>None</td>
      <td>None</td>
      <td>FILL</td>
      <td>None</td>
      <td>Fill material, gravel, sand, bricks, rubble</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70146</th>
      <td>4120315</td>
      <td>30303990</td>
      <td>652802870</td>
      <td>None</td>
      <td>UNK</td>
      <td>2.0</td>
      <td>2.2</td>
      <td>None</td>
      <td>None</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Clay grey brown, medium plasticity</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70147</th>
      <td>4120316</td>
      <td>30303990</td>
      <td>652802870</td>
      <td>None</td>
      <td>UNK</td>
      <td>2.2</td>
      <td>5.0</td>
      <td>None</td>
      <td>None</td>
      <td>SAND</td>
      <td>None</td>
      <td>Sand, grey to black, medium to coarse grained</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70148</th>
      <td>4120317</td>
      <td>30303994</td>
      <td>652802874</td>
      <td>None</td>
      <td>UNK</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>None</td>
      <td>None</td>
      <td>FILL</td>
      <td>None</td>
      <td>Fill - cobble sized lumps of slag with gravel ...</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70149</th>
      <td>4120318</td>
      <td>30303994</td>
      <td>652802874</td>
      <td>None</td>
      <td>UNK</td>
      <td>2.0</td>
      <td>5.0</td>
      <td>None</td>
      <td>None</td>
      <td>SAND</td>
      <td>None</td>
      <td>Silty sand - grey to black medium to coarse gr...</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70150</th>
      <td>4120343</td>
      <td>30304039</td>
      <td>662829228</td>
      <td>None</td>
      <td>UNK</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>None</td>
      <td>None</td>
      <td>FILL</td>
      <td>None</td>
      <td>Fill</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70151</th>
      <td>4120344</td>
      <td>30304039</td>
      <td>662829228</td>
      <td>None</td>
      <td>UNK</td>
      <td>1.0</td>
      <td>9.0</td>
      <td>None</td>
      <td>None</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Clay</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70152</th>
      <td>4120345</td>
      <td>30304039</td>
      <td>662829228</td>
      <td>None</td>
      <td>UNK</td>
      <td>9.0</td>
      <td>10.0</td>
      <td>None</td>
      <td>None</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Sandy clay</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70153</th>
      <td>4120346</td>
      <td>30304039</td>
      <td>662829228</td>
      <td>None</td>
      <td>UNK</td>
      <td>10.0</td>
      <td>12.5</td>
      <td>None</td>
      <td>None</td>
      <td>SAND</td>
      <td>None</td>
      <td>Clay sand</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70154</th>
      <td>4120347</td>
      <td>30304050</td>
      <td>652802882</td>
      <td>None</td>
      <td>UNK</td>
      <td>0.0</td>
      <td>0.3</td>
      <td>None</td>
      <td>None</td>
      <td>FILL</td>
      <td>None</td>
      <td>Fill</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70155</th>
      <td>4120348</td>
      <td>30304050</td>
      <td>652802882</td>
      <td>None</td>
      <td>UNK</td>
      <td>0.3</td>
      <td>0.8</td>
      <td>None</td>
      <td>None</td>
      <td>SAND</td>
      <td>None</td>
      <td>Clayey sand</td>
      <td>SAGeodata</td>
    </tr>
    <tr>
      <th>70156</th>
      <td>4120349</td>
      <td>30304050</td>
      <td>652802882</td>
      <td>None</td>
      <td>UNK</td>
      <td>0.8</td>
      <td>3.5</td>
      <td>None</td>
      <td>None</td>
      <td>SAND</td>
      <td>None</td>
      <td>Sand</td>
      <td>SAGeodata</td>
    </tr>
  </tbody>
</table>
<p>70157 rows × 13 columns</p>
</div>




```python
# add a new column as a function of existing columns
log_data['Thickness'] = log_data.ToDepth - log_data.FromDepth
```


```python
type(log_data)     # see what Python type the DataFrame is
```




    pandas.core.frame.DataFrame




```python
log_data.head(3)    # print the first 3 rows
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
      <th>OBJECTID</th>
      <th>BoreID</th>
      <th>HydroCode</th>
      <th>RefElev</th>
      <th>RefElevDesc</th>
      <th>FromDepth</th>
      <th>ToDepth</th>
      <th>TopElev</th>
      <th>BottomElev</th>
      <th>MajorLithCode</th>
      <th>MinorLithCode</th>
      <th>Description</th>
      <th>Source</th>
      <th>Thickness</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1769789</td>
      <td>30062892</td>
      <td>662815923</td>
      <td>57.25</td>
      <td>NGS</td>
      <td>18.0</td>
      <td>19.5</td>
      <td>39.25</td>
      <td>37.75</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Clay</td>
      <td>SAGeodata</td>
      <td>1.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1769790</td>
      <td>30062892</td>
      <td>662815923</td>
      <td>57.25</td>
      <td>NGS</td>
      <td>19.5</td>
      <td>22.0</td>
      <td>37.75</td>
      <td>35.25</td>
      <td>ROCK</td>
      <td>None</td>
      <td>Rocks and sand</td>
      <td>SAGeodata</td>
      <td>2.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1769791</td>
      <td>30062892</td>
      <td>662815923</td>
      <td>57.25</td>
      <td>NGS</td>
      <td>22.0</td>
      <td>24.0</td>
      <td>35.25</td>
      <td>33.25</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Clay</td>
      <td>SAGeodata</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
log_data.index     # “the index” (aka “the labels”). 
#Pandas is great for using timeseries data, where the index can be the timestamps
```




    RangeIndex(start=0, stop=70157, step=1)




```python
log_data.columns   # column names (which is “an index”)
```




    Index([u'OBJECTID', u'BoreID', u'HydroCode', u'RefElev', u'RefElevDesc',
           u'FromDepth', u'ToDepth', u'TopElev', u'BottomElev', u'MajorLithCode',
           u'MinorLithCode', u'Description', u'Source', u'Thickness'],
          dtype='object')




```python
log_data.dtypes    # data types of each column
```




    OBJECTID           int64
    BoreID             int64
    HydroCode          int64
    RefElev           object
    RefElevDesc       object
    FromDepth        float64
    ToDepth          float64
    TopElev           object
    BottomElev        object
    MajorLithCode     object
    MinorLithCode     object
    Description       object
    Source            object
    Thickness        float64
    dtype: object




```python
log_data.shape     # number of rows and columns
```




    (70157, 14)




```python
log_data.values    # underlying numpy array — df are stored as numpy arrays for effeciencies.
```




    array([[1769789L, 30062892L, 662815923L, ..., 'Clay', 'SAGeodata', 1.5],
           [1769790L, 30062892L, 662815923L, ..., 'Rocks and sand',
            'SAGeodata', 2.5],
           [1769791L, 30062892L, 662815923L, ..., 'Clay', 'SAGeodata', 2.0],
           ...,
           [4120347L, 30304050L, 652802882L, ..., 'Fill', 'SAGeodata', 0.3],
           [4120348L, 30304050L, 652802882L, ..., 'Clayey sand', 'SAGeodata',
            0.5],
           [4120349L, 30304050L, 652802882L, ..., 'Sand', 'SAGeodata', 2.7]],
          dtype=object)




```python
#log_data['MajorLithCode']         # select one column
##Equivalent to 
#log_data.MajorLithCode 
##and
#log_data.iloc[:,9]
```


```python
type(log_data['MajorLithCode'])   # determine datatype of column (e.g., Series)
```




    pandas.core.series.Series




```python
#describe the data frame
log_data.describe(include='all')     
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
      <th>OBJECTID</th>
      <th>BoreID</th>
      <th>HydroCode</th>
      <th>RefElev</th>
      <th>RefElevDesc</th>
      <th>FromDepth</th>
      <th>ToDepth</th>
      <th>TopElev</th>
      <th>BottomElev</th>
      <th>MajorLithCode</th>
      <th>MinorLithCode</th>
      <th>Description</th>
      <th>Source</th>
      <th>Thickness</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>7.015700e+04</td>
      <td>7.015700e+04</td>
      <td>7.015700e+04</td>
      <td>70157</td>
      <td>70157</td>
      <td>70157.000000</td>
      <td>70157.000000</td>
      <td>70157</td>
      <td>70157</td>
      <td>70157</td>
      <td>70157</td>
      <td>70157</td>
      <td>70157</td>
      <td>70157.000000</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>5068</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>27777</td>
      <td>27878</td>
      <td>81</td>
      <td>42</td>
      <td>33598</td>
      <td>39</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>top</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>NGS</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
      <td>CLYU</td>
      <td>None</td>
      <td>Clay</td>
      <td>SAGeodata</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>18514</td>
      <td>44946</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>18514</td>
      <td>18514</td>
      <td>25857</td>
      <td>62797</td>
      <td>4603</td>
      <td>70119</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>2.505842e+06</td>
      <td>3.018201e+07</td>
      <td>6.624491e+08</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>24.942443</td>
      <td>30.626594</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>5.684151</td>
    </tr>
    <tr>
      <th>std</th>
      <td>9.276598e+05</td>
      <td>8.068098e+04</td>
      <td>2.130462e+06</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>45.435866</td>
      <td>48.609957</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>9.943264</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.769789e+06</td>
      <td>3.002715e+07</td>
      <td>6.528000e+08</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.010000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1.932799e+06</td>
      <td>3.014558e+07</td>
      <td>6.628129e+08</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.800000</td>
      <td>4.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1.999036e+06</td>
      <td>3.018487e+07</td>
      <td>6.628196e+08</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7.000000</td>
      <td>11.580000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.800000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>3.967159e+06</td>
      <td>3.025487e+07</td>
      <td>6.628248e+08</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>25.900000</td>
      <td>34.750000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>4.120349e+06</td>
      <td>3.030405e+07</td>
      <td>6.728042e+08</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>610.300000</td>
      <td>620.160000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>300.500000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# summarise a panda Series
log_data.FromDepth.describe()   # describe a single column
```




    count    70157.000000
    mean        24.942443
    std         45.435866
    min          0.000000
    25%          0.800000
    50%          7.000000
    75%         25.900000
    max        610.300000
    Name: FromDepth, dtype: float64




```python
#calculate mean of 5th column ("FromDepth")
log_data.iloc[:,5].mean()      
```




    24.9424428068475




```python
#alternate method to calculate mean of FromDepth column (the 5th one)
log_data["FromDepth"].mean()    
```




    24.9424428068475




```python
#Count how many Lith Codes there are
lithCounts=log_data.MajorLithCode.value_counts()
```


```python
#Print the lithcodes, use .index or .values 
lithCounts
```




    CLYU    25857
    SAND    12772
    SLAT     4069
    FILL     4020
    SDST     3207
    TPSL     2767
    GRVL     2445
    QTZT     1891
    SHLE     1601
    SCHT     1576
    ROCK     1572
    LMST     1571
    SILT     1436
    None      874
    SLST      530
    MDST      528
    STON      474
    SOIL      441
    QUAR      251
    BITM      205
    SPST      190
    SHEL      181
    DLOM      169
    LOAM      143
    CLYS      119
    CORL      117
    MARL      115
    GNSS       99
    RUBL       90
    UKN        82
            ...  
    BASE       13
    MANM       13
    PEAT       12
    TRAV       10
    COAL        8
    WKST        7
    BSLT        6
    CAAR        6
    PYRT        5
    SLAG        5
    GPSM        5
    CAVE        3
    WOOD        2
    PEGM        2
    CLYW        2
    CLYR        2
    VOLC        2
    OPCA        2
    CLLV        2
    HFLS        1
    ARKS        1
    ALDG        1
    DIOR        1
    LMSD        1
    DUST        1
    FOSS        1
    REGO        1
    SCOR        1
    CALU        1
    SANN        1
    Name: MajorLithCode, Length: 81, dtype: int64




```python
#plot a bar chart of the lith codes
lithCounts.plot.bar(rot=90,figsize=(15,5))
```




    <matplotlib.axes._subplots.AxesSubplot at 0x9f13990>




```python
#Plot a bar chart of the lith codes for the rarer lithologies
lithCounts[(lithCounts < 50)].plot.bar(rot=90,figsize=(15,5))
```




    <matplotlib.axes._subplots.AxesSubplot at 0xa410b70>




![png](output_31_1.png)



```python
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
 
# example data
mu = np.mean(log_data['Thickness'].values) # mean of distribution
sigma = np.std(log_data['Thickness'].values) # standard deviation of distribution
x = log_data['Thickness'].values
# the histogram of the data
plt.hist(x, bins=[0,0.25,0.5,0.75,1.0,1.25,1.5,1.75,2,2.25,2.5,2.75,3.0], alpha=0.5)
plt.xlabel('Thickness (m)')
plt.ylabel('Count')
mystring="Histogram with a mean of "+ str(mu)
plt.title(mystring)
 
# Tweak spacing to prevent clipping of ylabel
#plt.subplots_adjust(left=0.15)
plt.show()



```


![png](output_32_0.png)



```python
# import numpy as np
# cmap = plt.get_cmap('viridis')
# colors = cmap(np.linspace(0, 1, len(lithCounts.index)))
# colors

# for row in log_data.itertuples():
#     boreid=row[3]
#     for ind,value in enumerate(recs):  
#         try:
#             value.index(boreid)
#             print(recs)
#         except:
#             continue
#     #(row[3])



# for ind, value in enumerate(recs):
#     #Get the lat lon value
#     lon=value[18]
#     lat=value[17]
#     #Get the Lithology unit
#     value[]
    
#     #Now plot it
#     plt.plot(lon,lat,"|")
```

# Exercise
Go to http://www.bom.gov.au/water/groundwater/explorer/map.shtml and pick another River Region. Download the dataset in "Shapefile" format (this will downlaod the csv also). Once you have the data, follow the same routines as above and see what you can find out about the river region. Submit your jupyter notebook for review.


```python

```
