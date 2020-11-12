# Python packages for working with shapefiles and tabular data

<div class="questions">  
### Questions

- How can I load shapefiles and tabular data into python?
- What are libraries and packages?
</div>

<div class="objectives">  
### Objectives

- Learn how to deal with specialty data types.
- Learn about pandas, pyshp, lasio, obspy.
</div>

## Dealing with other data types
Python can deal with basically any type of data you throw at it. The community have provided many packages that make things easy, today we will look at the "pyshp" (for dealing with shapefiles) and "pandas" (great for tables and time series) packages.

Data for this exercised was downloaded from http://www.bom.gov.au/water/groundwater/explorer/map.shtml

### Shapefiles
Shapefiles are a very common file format for GIS data.

## Dealing with other data types
Python can deal with basically any type of data you throw at it. The community have provided many packages that make things easy, today we will look at the "pyshp" (for dealing with shapefiles) and "pandas" (great for tables and time series) packages.

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
    
    DESCRIPTION
        shapefile.py
        Provides read and write support for ESRI Shapefiles.
        author: jlawhead<at>geospatialpython.com
        version: 2.1.2
        Compatible with Python versions 2.7-3.x
    
    CLASSES
        builtins.Exception(builtins.BaseException)
            ShapefileException
        builtins.list(builtins.object)
            ShapeRecords
            Shapes
        builtins.object
            Reader
            Shape
            ShapeRecord
            Writer
        
        class Reader(builtins.object)
         |  Reader(*args, **kwargs)
         |  
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
         |  __del__(self)
         |  
         |  __enter__(self)
         |      Enter phase of context manager.
         |  
         |  __exit__(self, exc_type, exc_val, exc_tb)
         |      Exit phase of context manager, close opened files.
         |  
         |  __init__(self, *args, **kwargs)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  __iter__(self)
         |      Iterates through the shapes/records in the shapefile.
         |  
         |  __len__(self)
         |      Returns the number of shapes/records in the shapefile.
         |  
         |  __str__(self)
         |      Use some general info on the shapefile as __str__
         |  
         |  close(self)
         |  
         |  iterRecords(self)
         |      Returns a generator of records in a dbf file.
         |      Useful for large shapefiles or dbf files.
         |  
         |  iterShapeRecords(self)
         |      Returns a generator of combination geometry/attribute records for
         |      all records in a shapefile.
         |  
         |  iterShapes(self)
         |      Returns a generator of shapes in a shapefile. Useful
         |      for handling large shapefiles.
         |  
         |  load(self, shapefile=None)
         |      Opens a shapefile from a filename or file-like
         |      object. Normally this method would be called by the
         |      constructor with the file name as an argument.
         |  
         |  load_dbf(self, shapefile_name)
         |      Attempts to load file with .dbf extension as both lower and upper case
         |  
         |  load_shp(self, shapefile_name)
         |      Attempts to load file with .shp extension as both lower and upper case
         |  
         |  load_shx(self, shapefile_name)
         |      Attempts to load file with .shx extension as both lower and upper case
         |  
         |  record(self, i=0)
         |      Returns a specific dbf record based on the supplied index.
         |  
         |  records(self)
         |      Returns all records in a dbf file.
         |  
         |  shape(self, i=0)
         |      Returns a shape object for a shape in the geometry
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
         |  
         |  ----------------------------------------------------------------------
         |  Readonly properties defined here:
         |  
         |  __geo_interface__
         |  
         |  shapeTypeName
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
        
        class Shape(builtins.object)
         |  Shape(shapeType=0, points=None, parts=None, partTypes=None)
         |  
         |  Methods defined here:
         |  
         |  __init__(self, shapeType=0, points=None, parts=None, partTypes=None)
         |      Stores the geometry of the different shape types
         |      specified in the Shapefile spec. Shape types are
         |      usually point, polyline, or polygons. Every shape type
         |      except the "Null" type contains points at some level for
         |      example vertices in a polygon. If a shape type has
         |      multiple shapes containing points within a single
         |      geometry record then those shapes are called parts. Parts
         |      are designated by their starting index in geometry record's
         |      list of shapes. For MultiPatch geometry, partTypes designates
         |      the patch type of each of the parts.
         |  
         |  ----------------------------------------------------------------------
         |  Readonly properties defined here:
         |  
         |  __geo_interface__
         |  
         |  shapeTypeName
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
        
        class ShapeRecord(builtins.object)
         |  ShapeRecord(shape=None, record=None)
         |  
         |  A ShapeRecord object containing a shape along with its attributes.
         |  Provides the GeoJSON __geo_interface__ to return a Feature dictionary.
         |  
         |  Methods defined here:
         |  
         |  __init__(self, shape=None, record=None)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Readonly properties defined here:
         |  
         |  __geo_interface__
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
        
        class ShapeRecords(builtins.list)
         |  ShapeRecords(iterable=(), /)
         |  
         |  A class to hold a list of ShapeRecord objects. Subclasses list to ensure compatibility with
         |  former work and to reuse all the optimizations of the builtin list.
         |  In addition to the list interface, this also provides the GeoJSON __geo_interface__
         |  to return a FeatureCollection dictionary.
         |  
         |  Method resolution order:
         |      ShapeRecords
         |      builtins.list
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __repr__(self)
         |      Return repr(self).
         |  
         |  ----------------------------------------------------------------------
         |  Readonly properties defined here:
         |  
         |  __geo_interface__
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.list:
         |  
         |  __add__(self, value, /)
         |      Return self+value.
         |  
         |  __contains__(self, key, /)
         |      Return key in self.
         |  
         |  __delitem__(self, key, /)
         |      Delete self[key].
         |  
         |  __eq__(self, value, /)
         |      Return self==value.
         |  
         |  __ge__(self, value, /)
         |      Return self>=value.
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __getitem__(...)
         |      x.__getitem__(y) <==> x[y]
         |  
         |  __gt__(self, value, /)
         |      Return self>value.
         |  
         |  __iadd__(self, value, /)
         |      Implement self+=value.
         |  
         |  __imul__(self, value, /)
         |      Implement self*=value.
         |  
         |  __init__(self, /, *args, **kwargs)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  __iter__(self, /)
         |      Implement iter(self).
         |  
         |  __le__(self, value, /)
         |      Return self<=value.
         |  
         |  __len__(self, /)
         |      Return len(self).
         |  
         |  __lt__(self, value, /)
         |      Return self<value.
         |  
         |  __mul__(self, value, /)
         |      Return self*value.
         |  
         |  __ne__(self, value, /)
         |      Return self!=value.
         |  
         |  __reversed__(self, /)
         |      Return a reverse iterator over the list.
         |  
         |  __rmul__(self, value, /)
         |      Return value*self.
         |  
         |  __setitem__(self, key, value, /)
         |      Set self[key] to value.
         |  
         |  __sizeof__(self, /)
         |      Return the size of the list in memory, in bytes.
         |  
         |  append(self, object, /)
         |      Append object to the end of the list.
         |  
         |  clear(self, /)
         |      Remove all items from list.
         |  
         |  copy(self, /)
         |      Return a shallow copy of the list.
         |  
         |  count(self, value, /)
         |      Return number of occurrences of value.
         |  
         |  extend(self, iterable, /)
         |      Extend list by appending elements from the iterable.
         |  
         |  index(self, value, start=0, stop=9223372036854775807, /)
         |      Return first index of value.
         |      
         |      Raises ValueError if the value is not present.
         |  
         |  insert(self, index, object, /)
         |      Insert object before index.
         |  
         |  pop(self, index=-1, /)
         |      Remove and return item at index (default last).
         |      
         |      Raises IndexError if list is empty or index is out of range.
         |  
         |  remove(self, value, /)
         |      Remove first occurrence of value.
         |      
         |      Raises ValueError if the value is not present.
         |  
         |  reverse(self, /)
         |      Reverse *IN PLACE*.
         |  
         |  sort(self, /, *, key=None, reverse=False)
         |      Sort the list in ascending order and return None.
         |      
         |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
         |      order of two equal elements is maintained).
         |      
         |      If a key function is given, apply it once to each list item and sort them,
         |      ascending or descending, according to their function values.
         |      
         |      The reverse flag can be set to sort in descending order.
         |  
         |  ----------------------------------------------------------------------
         |  Static methods inherited from builtins.list:
         |  
         |  __new__(*args, **kwargs) from builtins.type
         |      Create and return a new object.  See help(type) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes inherited from builtins.list:
         |  
         |  __hash__ = None
        
        class ShapefileException(builtins.Exception)
         |  An exception to handle shapefile specific problems.
         |  
         |  Method resolution order:
         |      ShapefileException
         |      builtins.Exception
         |      builtins.BaseException
         |      builtins.object
         |  
         |  Data descriptors defined here:
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.Exception:
         |  
         |  __init__(self, /, *args, **kwargs)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Static methods inherited from builtins.Exception:
         |  
         |  __new__(*args, **kwargs) from builtins.type
         |      Create and return a new object.  See help(type) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.BaseException:
         |  
         |  __delattr__(self, name, /)
         |      Implement delattr(self, name).
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __reduce__(...)
         |      Helper for pickle.
         |  
         |  __repr__(self, /)
         |      Return repr(self).
         |  
         |  __setattr__(self, name, value, /)
         |      Implement setattr(self, name, value).
         |  
         |  __setstate__(...)
         |  
         |  __str__(self, /)
         |      Return str(self).
         |  
         |  with_traceback(...)
         |      Exception.with_traceback(tb) --
         |      set self.__traceback__ to tb and return self.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors inherited from builtins.BaseException:
         |  
         |  __cause__
         |      exception cause
         |  
         |  __context__
         |      exception context
         |  
         |  __dict__
         |  
         |  __suppress_context__
         |  
         |  __traceback__
         |  
         |  args
        
        class Shapes(builtins.list)
         |  Shapes(iterable=(), /)
         |  
         |  A class to hold a list of Shape objects. Subclasses list to ensure compatibility with
         |  former work and to reuse all the optimizations of the builtin list.
         |  In addition to the list interface, this also provides the GeoJSON __geo_interface__
         |  to return a GeometryCollection dictionary.
         |  
         |  Method resolution order:
         |      Shapes
         |      builtins.list
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __repr__(self)
         |      Return repr(self).
         |  
         |  ----------------------------------------------------------------------
         |  Readonly properties defined here:
         |  
         |  __geo_interface__
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.list:
         |  
         |  __add__(self, value, /)
         |      Return self+value.
         |  
         |  __contains__(self, key, /)
         |      Return key in self.
         |  
         |  __delitem__(self, key, /)
         |      Delete self[key].
         |  
         |  __eq__(self, value, /)
         |      Return self==value.
         |  
         |  __ge__(self, value, /)
         |      Return self>=value.
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __getitem__(...)
         |      x.__getitem__(y) <==> x[y]
         |  
         |  __gt__(self, value, /)
         |      Return self>value.
         |  
         |  __iadd__(self, value, /)
         |      Implement self+=value.
         |  
         |  __imul__(self, value, /)
         |      Implement self*=value.
         |  
         |  __init__(self, /, *args, **kwargs)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  __iter__(self, /)
         |      Implement iter(self).
         |  
         |  __le__(self, value, /)
         |      Return self<=value.
         |  
         |  __len__(self, /)
         |      Return len(self).
         |  
         |  __lt__(self, value, /)
         |      Return self<value.
         |  
         |  __mul__(self, value, /)
         |      Return self*value.
         |  
         |  __ne__(self, value, /)
         |      Return self!=value.
         |  
         |  __reversed__(self, /)
         |      Return a reverse iterator over the list.
         |  
         |  __rmul__(self, value, /)
         |      Return value*self.
         |  
         |  __setitem__(self, key, value, /)
         |      Set self[key] to value.
         |  
         |  __sizeof__(self, /)
         |      Return the size of the list in memory, in bytes.
         |  
         |  append(self, object, /)
         |      Append object to the end of the list.
         |  
         |  clear(self, /)
         |      Remove all items from list.
         |  
         |  copy(self, /)
         |      Return a shallow copy of the list.
         |  
         |  count(self, value, /)
         |      Return number of occurrences of value.
         |  
         |  extend(self, iterable, /)
         |      Extend list by appending elements from the iterable.
         |  
         |  index(self, value, start=0, stop=9223372036854775807, /)
         |      Return first index of value.
         |      
         |      Raises ValueError if the value is not present.
         |  
         |  insert(self, index, object, /)
         |      Insert object before index.
         |  
         |  pop(self, index=-1, /)
         |      Remove and return item at index (default last).
         |      
         |      Raises IndexError if list is empty or index is out of range.
         |  
         |  remove(self, value, /)
         |      Remove first occurrence of value.
         |      
         |      Raises ValueError if the value is not present.
         |  
         |  reverse(self, /)
         |      Reverse *IN PLACE*.
         |  
         |  sort(self, /, *, key=None, reverse=False)
         |      Sort the list in ascending order and return None.
         |      
         |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
         |      order of two equal elements is maintained).
         |      
         |      If a key function is given, apply it once to each list item and sort them,
         |      ascending or descending, according to their function values.
         |      
         |      The reverse flag can be set to sort in descending order.
         |  
         |  ----------------------------------------------------------------------
         |  Static methods inherited from builtins.list:
         |  
         |  __new__(*args, **kwargs) from builtins.type
         |      Create and return a new object.  See help(type) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes inherited from builtins.list:
         |  
         |  __hash__ = None
        
        class Writer(builtins.object)
         |  Writer(target=None, shapeType=None, autoBalance=False, **kwargs)
         |  
         |  Provides write support for ESRI Shapefiles.
         |  
         |  Methods defined here:
         |  
         |  __del__(self)
         |  
         |  __enter__(self)
         |      Enter phase of context manager.
         |  
         |  __exit__(self, exc_type, exc_val, exc_tb)
         |      Exit phase of context manager, finish writing and close the files.
         |  
         |  __init__(self, target=None, shapeType=None, autoBalance=False, **kwargs)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  __len__(self)
         |      Returns the current number of features written to the shapefile. 
         |      If shapes and records are unbalanced, the length is considered the highest
         |      of the two.
         |  
         |  balance(self)
         |      Adds corresponding empty attributes or null geometry records depending
         |      on which type of record was created to make sure all three files
         |      are in synch.
         |  
         |  bbox(self)
         |      Returns the current bounding box for the shapefile which is
         |      the lower-left and upper-right corners. It does not contain the
         |      elevation or measure extremes.
         |  
         |  close(self)
         |      Write final shp, shx, and dbf headers, close opened files.
         |  
         |  field(self, name, fieldType='C', size='50', decimal=0)
         |      Adds a dbf field descriptor to the shapefile.
         |  
         |  line(self, lines)
         |      Creates a POLYLINE shape.
         |      Lines is a collection of lines, each made up of a list of xy values.
         |  
         |  linem(self, lines)
         |      Creates a POLYLINEM shape.
         |      Lines is a collection of lines, each made up of a list of xym values.
         |      If the m (measure) value is not included, it defaults to None (NoData).
         |  
         |  linez(self, lines)
         |      Creates a POLYLINEZ shape.
         |      Lines is a collection of lines, each made up of a list of xyzm values.
         |      If the z (elevation) value is not included, it defaults to 0.
         |      If the m (measure) value is not included, it defaults to None (NoData).
         |  
         |  mbox(self)
         |      Returns the current m extremes for the shapefile.
         |  
         |  multipatch(self, parts, partTypes)
         |      Creates a MULTIPATCH shape.
         |      Parts is a collection of 3D surface patches, each made up of a list of xyzm values.
         |      PartTypes is a list of types that define each of the surface patches.
         |      The types can be any of the following module constants: TRIANGLE_STRIP,
         |      TRIANGLE_FAN, OUTER_RING, INNER_RING, FIRST_RING, or RING.
         |      If the z (elavation) value is not included, it defaults to 0.
         |      If the m (measure) value is not included, it defaults to None (NoData).
         |  
         |  multipoint(self, points)
         |      Creates a MULTIPOINT shape.
         |      Points is a list of xy values.
         |  
         |  multipointm(self, points)
         |      Creates a MULTIPOINTM shape.
         |      Points is a list of xym values.
         |      If the m (measure) value is not included, it defaults to None (NoData).
         |  
         |  multipointz(self, points)
         |      Creates a MULTIPOINTZ shape.
         |      Points is a list of xyzm values.
         |      If the z (elevation) value is not included, it defaults to 0.
         |      If the m (measure) value is not included, it defaults to None (NoData).
         |  
         |  null(self)
         |      Creates a null shape.
         |  
         |  point(self, x, y)
         |      Creates a POINT shape.
         |  
         |  pointm(self, x, y, m=None)
         |      Creates a POINTM shape.
         |      If the m (measure) value is not set, it defaults to NoData.
         |  
         |  pointz(self, x, y, z=0, m=None)
         |      Creates a POINTZ shape.
         |      If the z (elevation) value is not set, it defaults to 0.
         |      If the m (measure) value is not set, it defaults to NoData.
         |  
         |  poly(self, polys)
         |      Creates a POLYGON shape.
         |      Polys is a collection of polygons, each made up of a list of xy values.
         |      Note that for ordinary polygons the coordinates must run in a clockwise direction.
         |      If some of the polygons are holes, these must run in a counterclockwise direction.
         |  
         |  polym(self, polys)
         |      Creates a POLYGONM shape.
         |      Polys is a collection of polygons, each made up of a list of xym values.
         |      Note that for ordinary polygons the coordinates must run in a clockwise direction.
         |      If some of the polygons are holes, these must run in a counterclockwise direction.
         |      If the m (measure) value is not included, it defaults to None (NoData).
         |  
         |  polyz(self, polys)
         |      Creates a POLYGONZ shape.
         |      Polys is a collection of polygons, each made up of a list of xyzm values.
         |      Note that for ordinary polygons the coordinates must run in a clockwise direction.
         |      If some of the polygons are holes, these must run in a counterclockwise direction.
         |      If the z (elevation) value is not included, it defaults to 0.
         |      If the m (measure) value is not included, it defaults to None (NoData).
         |  
         |  record(self, *recordList, **recordDict)
         |      Creates a dbf attribute record. You can submit either a sequence of
         |      field values or keyword arguments of field names and values. Before
         |      adding records you must add fields for the record values using the
         |      field() method. If the record values exceed the number of fields the
         |      extra ones won't be added. In the case of using keyword arguments to specify
         |      field/value pairs only fields matching the already registered fields
         |      will be added.
         |  
         |  shape(self, s)
         |  
         |  zbox(self)
         |      Returns the current z extremes for the shapefile.
         |  
         |  ----------------------------------------------------------------------
         |  Readonly properties defined here:
         |  
         |  shapeTypeName
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
    
    FUNCTIONS
        b(v, encoding='utf-8', encodingErrors='strict')
        
        bbox_contains(bbox1, bbox2)
            Tests whether bbox1 fully contains bbox2, returning a boolean
        
        bbox_overlap(bbox1, bbox2)
            Tests whether two bounding boxes overlap, returning a boolean
        
        calcsize(format, /)
            Return size in bytes of the struct described by the format string.
        
        is_string(v)
        
        organize_polygon_rings(rings)
            Organize a list of coordinate rings into one or more polygons with holes.
            Returns a list of polygons, where each polygon is composed of a single exterior
            ring, and one or more interior holes.
            
            Rings must be closed, and cannot intersect each other (non-self-intersecting polygon).
            Rings are determined as exteriors if they run in clockwise direction, or interior
            holes if they run in counter-clockwise direction. This method is used to construct
            GeoJSON (multi)polygons from the shapefile polygon shape type, which does not
            explicitly store the structure of the polygons beyond exterior/interior ring orientation.
        
        pack(...)
            pack(format, v1, v2, ...) -> bytes
            
            Return a bytes object containing the values v1, v2, ... packed according
            to the format string.  See help(struct) for more on format strings.
        
        ring_bbox(coords)
            Calculates and returns the bounding box of a ring.
        
        ring_contains_point(coords, p)
            Fast point-in-polygon crossings algorithm, MacMartin optimization.
            
            Adapted from code by Eric Haynes
            http://www.realtimerendering.com/resources/GraphicsGems//gemsiv/ptpoly_haines/ptinpoly.c
            
            Original description:
                Shoot a test ray along +X axis.  The strategy, from MacMartin, is to
                compare vertex Y values to the testing point's Y and quickly discard
                edges which are entirely to one side of the test ray.
        
        ring_contains_ring(coords1, coords2)
            Returns True if all vertexes in coords2 are fully inside coords1.
        
        ring_sample(coords, ccw=False)
            Return a sample point guaranteed to be within a ring, by efficiently
            finding the first centroid of a coordinate triplet whose orientation
            matches the orientation of the ring and passes the point-in-ring test.
            The orientation of the ring is assumed to be clockwise, unless ccw
            (counter-clockwise) is set to True.
        
        signed_area(coords)
            Return the signed area enclosed by a ring using the linear time
            algorithm. A value >= 0 indicates a counter-clockwise oriented ring.
        
        test(**kwargs)
            # Begin Testing
        
        u(v, encoding='utf-8', encodingErrors='strict')
        
        unpack(format, buffer, /)
            Return a tuple containing values unpacked according to the format string.
            
            The buffer's size in bytes must be calcsize(format).
            
            See help(struct) for more on format strings.
    
    DATA
        FIRST_RING = 4
        INNER_RING = 3
        MISSING = [None, '']
        MULTIPATCH = 31
        MULTIPOINT = 8
        MULTIPOINTM = 28
        MULTIPOINTZ = 18
        NODATA = -1e+39
        NULL = 0
        OUTER_RING = 2
        PARTTYPE_LOOKUP = {0: 'TRIANGLE_STRIP', 1: 'TRIANGLE_FAN', 2: 'OUTER_R...
        POINT = 1
        POINTM = 21
        POINTZ = 11
        POLYGON = 5
        POLYGONM = 25
        POLYGONZ = 15
        POLYLINE = 3
        POLYLINEM = 23
        POLYLINEZ = 13
        PYTHON3 = True
        RING = 5
        SHAPETYPE_LOOKUP = {0: 'NULL', 1: 'POINT', 3: 'POLYLINE', 5: 'POLYGON'...
        TRIANGLE_FAN = 1
        TRIANGLE_STRIP = 0
    
    VERSION
        2.1.2
    
    FILE
        /Users/darya/anaconda3/envs/python4pesa/lib/python3.8/site-packages/shapefile.py
    
    



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




    Record #0: [32001999, '652800645', 30027773, 6.74, -74.26, 31000043, 1042, 104005, 0.0]







    [32001999, '652800645', 30027773, 6.74, -74.26, 31000043, 1042, 104005, 0.0]






```python
shapes[0].points #print the point values of the first shape
```




    [(591975.5150000006, -3816141.8817), (591975.5150000006, -3816141.8817)]



<div class="challenge">

### Challenge. TODO

- Look at the data above. It provides the coordinates of the wells as points. 
- How many coordinates are provided for each well? Why do you think this is?

<details>
<summary>Solution</summary>

There are two coordinates. 
    
```python
```
</details>
</div>

Shapefiles are not a native python format, but the community have developed tools for exploring them. The package we have used "pyshp" imported with the name "shapefile" (for some non-consistent weird reason), is one example of working with shapefiles. Alternatives exist.

## More table manipulation


```python
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




    Index(['OBJECTID', 'BoreID', 'HydroCode', 'RefElev', 'RefElevDesc',
           'FromDepth', 'ToDepth', 'TopElev', 'BottomElev', 'MajorLithCode',
           'MinorLithCode', 'Description', 'Source', 'Thickness'],
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
log_data.values    # underlying numpy array — df are stored as numpy arrays for efficiencies.
```




    array([[1769789, 30062892, 662815923, ..., 'Clay', 'SAGeodata', 1.5],
           [1769790, 30062892, 662815923, ..., 'Rocks and sand', 'SAGeodata',
            2.5],
           [1769791, 30062892, 662815923, ..., 'Clay', 'SAGeodata', 2.0],
           ...,
           [4120347, 30304050, 652802882, ..., 'Fill', 'SAGeodata', 0.3],
           [4120348, 30304050, 652802882, ..., 'Clayey sand', 'SAGeodata',
            0.5],
           [4120349, 30304050, 652802882, ..., 'Sand', 'SAGeodata', 2.7]],
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
# summarise a pandas Series
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
            ...  
    REGO        1
    LMSD        1
    ARKS        1
    DIOR        1
    DUST        1
    Name: MajorLithCode, Length: 81, dtype: int64




```python
#plot a bar chart of the lith codes
lithCounts.plot.bar(rot=90,figsize=(15,5))
```




    <AxesSubplot:>




    
![png](01b-dataframes_files/01b-dataframes_35_1.png)
    



```python
#Plot a bar chart of the lith codes for the rarer lithologies
lithCounts[(lithCounts < 50)].plot.bar(rot=90,figsize=(15,5))
```




    <AxesSubplot:>




    
![png](01b-dataframes_files/01b-dataframes_36_1.png)
    



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


    
![png](01b-dataframes_files/01b-dataframes_37_0.png)
    



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
Go to [http://www.bom.gov.au/water/groundwater/explorer/map.shtml](http://www.bom.gov.au/water/groundwater/explorer/map.shtml) and pick another River Region. Download the dataset in "Shapefile" format (this will download the csv also). Once you have the data, follow the same routines as above and see what you can find out about the river region. 



# Log ASCII Files 

Python has some very specific packages/libraries. You can often create your own tools for doing niche tasks, but often you will find a variety of tools to make things simpler for you. We will show some simple tasks to perfrom on borehole data (in .las format) with the [lasio](https://lasio.readthedocs.io/en/latest/) library. 

This tutorial based off https://towardsdatascience.com/handling-big-volume-of-well-log-data-with-a-boosted-time-efficiency-with-python-dfe0319daf26

Original Data from:
https://sarigbasis.pir.sa.gov.au/WebtopEw/ws/samref/sarig1/image/DDD/PEDP013LOGS.zip

Title:	Cooper Basin selected well logs in LAS format.
Publication Date:	November 20
Prepared by:	Energy Resources Division, Department of the Premier and Cabinet
This Record URL:	https://sarigbasis.pir.sa.gov.au/WebtopEw/ws/samref/sarig1/wci/Record?r=0&m=1&w=catno=2040037





```python
#For plotting
import matplotlib.pyplot as plt

#Library specifically for "well data"
import lasio

#To read files
import glob

#For "regular expression manipulation"
import re
```


```python
#Build a list of filenames to read
read_files = glob.glob("data/WELL/*.las")
read_files
```




    ['data/WELL/BoolLagoon1.las',
     'data/WELL/Bungaloo1.las',
     'data/WELL/BeachportEast1.las',
     'data/WELL/BiscuitFlat1.las',
     'data/WELL/Balnaves.las',
     'data/WELL/Banyula.las',
     'data/WELL/Burrungule1.las',
     'data/WELL/Beachport1.las']




```python
#Cut out just the name of the well from the filenames
well_names = []
for file in read_files:
    print("FILE:", file)
    well=re.split('/|.las',file)
    print("SPLIT:", well)
    well_names.append(well[3])

print("There are ", len(well_names), "wells.")
print(well_names)
```

    FILE: data/WELL/BoolLagoon1.las
    SPLIT: ['data', 'WELL', 'BoolLagoon1', '']
    FILE: data/WELL/Bungaloo1.las
    SPLIT: ['data', 'WELL', 'Bungaloo1', '']
    FILE: data/WELL/BeachportEast1.las
    SPLIT: ['data', 'WELL', 'BeachportEast1', '']
    FILE: data/WELL/BiscuitFlat1.las
    SPLIT: ['data', 'WELL', 'BiscuitFlat1', '']
    FILE: data/WELL/Balnaves.las
    SPLIT: ['data', 'WELL', 'Balnaves', '']
    FILE: data/WELL/Banyula.las
    SPLIT: ['data', 'WELL', 'Banyula', '']
    FILE: data/WELL/Burrungule1.las
    SPLIT: ['data', 'WELL', 'Burrungule1', '']
    FILE: data/WELL/Beachport1.las
    SPLIT: ['data', 'WELL', 'Beachport1', '']
    There are  8 wells.
    ['', '', '', '', '', '', '', '']



```python
#Read in the log files to lasio
lases = []
for files in read_files:
    las = lasio.read(files)
    lases.append(las)
```


```python
#You can get an idea of what you can interogate using the help function
help(lases)
```

    Help on list object:
    
    class list(object)
     |  list(iterable=(), /)
     |  
     |  Built-in mutable sequence.
     |  
     |  If no argument is given, the constructor creates a new empty list.
     |  The argument must be an iterable if specified.
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __delitem__(self, key, /)
     |      Delete self[key].
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(...)
     |      x.__getitem__(y) <==> x[y]
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __iadd__(self, value, /)
     |      Implement self+=value.
     |  
     |  __imul__(self, value, /)
     |      Implement self*=value.
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __reversed__(self, /)
     |      Return a reverse iterator over the list.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  __setitem__(self, key, value, /)
     |      Set self[key] to value.
     |  
     |  __sizeof__(self, /)
     |      Return the size of the list in memory, in bytes.
     |  
     |  append(self, object, /)
     |      Append object to the end of the list.
     |  
     |  clear(self, /)
     |      Remove all items from list.
     |  
     |  copy(self, /)
     |      Return a shallow copy of the list.
     |  
     |  count(self, value, /)
     |      Return number of occurrences of value.
     |  
     |  extend(self, iterable, /)
     |      Extend list by appending elements from the iterable.
     |  
     |  index(self, value, start=0, stop=9223372036854775807, /)
     |      Return first index of value.
     |      
     |      Raises ValueError if the value is not present.
     |  
     |  insert(self, index, object, /)
     |      Insert object before index.
     |  
     |  pop(self, index=-1, /)
     |      Remove and return item at index (default last).
     |      
     |      Raises IndexError if list is empty or index is out of range.
     |  
     |  remove(self, value, /)
     |      Remove first occurrence of value.
     |      
     |      Raises ValueError if the value is not present.
     |  
     |  reverse(self, /)
     |      Reverse *IN PLACE*.
     |  
     |  sort(self, /, *, key=None, reverse=False)
     |      Sort the list in ascending order and return None.
     |      
     |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
     |      order of two equal elements is maintained).
     |      
     |      If a key function is given, apply it once to each list item and sort them,
     |      ascending or descending, according to their function values.
     |      
     |      The reverse flag can be set to sort in descending order.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __hash__ = None
    



```python
#This is just a regular Python list! But the list contains
#in this case, special objects known as "LasFile(s)" or lasio.las object.
#Get some details using help again
help(lases[1])
```

    Help on LASFile in module lasio.las object:
    
    class LASFile(builtins.object)
     |  LASFile(file_ref=None, **read_kwargs)
     |  
     |  LAS file object.
     |  
     |  Keyword Arguments:
     |      file_ref (file-like object, str): either a filename, an open file
     |          object, or a string containing the contents of a file.
     |  
     |  See these routines for additional keyword arguments you can use when
     |  reading in a LAS file:
     |  
     |  * :func:`lasio.reader.open_with_codecs` - manage issues relate to character
     |    encodings
     |  * :meth:`lasio.LASFile.read` - control how NULL values and errors are
     |    handled during parsing
     |  
     |  Attributes:
     |      encoding (str or None): the character encoding used when reading the
     |          file in from disk
     |  
     |  Methods defined here:
     |  
     |  __getitem__(self, key)
     |      Provide access to curve data.
     |      
     |      Arguments:
     |          key (str, int): either a curve mnemonic or the column index.
     |      
     |      Returns:
     |          1D :class:`numpy.ndarray` (the data for the curve)
     |  
     |  __init__(self, file_ref=None, **read_kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __setitem__(self, key, value)
     |      Append a curve.
     |      
     |      Arguments:
     |          key (str): the curve mnemonic
     |          value (1D data or CurveItem): either the curve data, or a CurveItem
     |      
     |      See :meth:`lasio.LASFile.append_curve_item` or
     |      :meth:`lasio.LASFile.append_curve` for more details.
     |  
     |  add_curve(self, *args, **kwargs)
     |      Deprecated. Use append_curve() or insert_curve() instead.
     |  
     |  add_curve_raw(self, mnemonic, data, unit='', descr='', value='')
     |      Deprecated. Use append_curve_item() or insert_curve_item() instead.
     |  
     |  append_curve(self, mnemonic, data, unit='', descr='', value='')
     |      Add a curve.
     |      
     |      Arguments:
     |          mnemonic (str): the curve mnemonic
     |          data (1D ndarray): the curve data
     |      
     |      Keyword Arguments:
     |          unit (str): curve unit
     |          descr (str): curve description
     |          value (int/float/str): value e.g. API code.
     |  
     |  append_curve_item(self, curve_item)
     |      Add a CurveItem.
     |      
     |      Args:
     |          curve_item (lasio.CurveItem)
     |  
     |  delete_curve(self, mnemonic=None, ix=None)
     |      Delete a curve.
     |      
     |      Keyword Arguments:
     |          ix (int): index of curve in LASFile.curves.
     |          mnemonic (str): mnemonic of curve.
     |      
     |      The index takes precedence over the mnemonic.
     |  
     |  df(self)
     |      Return data as a :class:`pandas.DataFrame` structure.
     |      
     |      The first Curve of the LASFile object is used as the pandas
     |      DataFrame's index.
     |  
     |  get_curve(self, mnemonic)
     |      Return CurveItem object.
     |      
     |      Arguments:
     |          mnemonic (str): the name of the curve
     |      
     |      Returns:
     |          :class:`lasio.CurveItem` (not just the data array)
     |  
     |  insert_curve(self, ix, mnemonic, data, unit='', descr='', value='')
     |      Insert a curve.
     |      
     |      Arguments:
     |          ix (int): position to insert curve at i.e. 0 for start.
     |          mnemonic (str): the curve mnemonic
     |          data (1D ndarray): the curve data
     |      
     |      Keyword Arguments:
     |          unit (str): curve unit
     |          descr (str): curve description
     |          value (int/float/str): value e.g. API code.
     |  
     |  insert_curve_item(self, ix, curve_item)
     |      Insert a CurveItem.
     |      
     |      Args:
     |          ix (int): position to insert CurveItem i.e. 0 for start
     |          curve_item (lasio.CurveItem)
     |  
     |  items(self)
     |      Return mnemonics and data for all curves.
     |  
     |  iteritems(self)
     |  
     |  iterkeys(self)
     |  
     |  itervalues(self)
     |  
     |  keys(self)
     |      Return curve mnemonics.
     |  
     |  match_raw_section(self, pattern, re_func='match', flags=re.IGNORECASE)
     |      Find raw section with a regular expression.
     |      
     |      Arguments:
     |          pattern (str): regular expression (you need to include the tilde)
     |      
     |      Keyword Arguments:
     |          re_func (str): either "match" or "search", see python ``re`` module.
     |          flags (int): flags for :func:`re.compile`
     |      
     |      Returns:
     |          dict
     |      
     |      Intended for internal use only.
     |  
     |  read(self, file_ref, ignore_data=False, read_policy='default', null_policy='strict', ignore_header_errors=False, ignore_comments=('#',), mnemonic_case='upper', index_unit=None, remove_data_line_filter='#', **kwargs)
     |      Read a LAS file.
     |      
     |      Arguments:
     |          file_ref (file-like object, str): either a filename, an open file
     |              object, or a string containing the contents of a file.
     |      
     |      Keyword Arguments:
     |          null_policy (str or list): see
     |              http://lasio.readthedocs.io/en/latest/data-section.html#handling-invalid-data-indicators-automatically
     |          ignore_data (bool): if True, do not read in any of the actual data,
     |              just the header metadata. False by default.
     |          ignore_header_errors (bool): ignore LASHeaderErrors (False by
     |              default)
     |          ignore_comments (tuple/str): ignore comments beginning with characters
     |              e.g. ``("#", '"')`` in header sections
     |          mnemonic_case (str): 'preserve': keep the case of HeaderItem mnemonics
     |                               'upper': convert all HeaderItem mnemonics to uppercase
     |                               'lower': convert all HeaderItem mnemonics to lowercase
     |          index_unit (str): Optionally force-set the index curve's unit to "m" or "ft"
     |          remove_data_line_filter (str, func): string or function for removing/ignoring lines
     |              in the data section e.g. a function which accepts a string (a line from the
     |              data section) and returns either True (do not parse the line) or False
     |              (parse the line). If this argument is a string it will instead be converted
     |              to a function which rejects all lines starting with that value e.g. ``"#"``
     |              will be converted to ``lambda line: line.strip().startswith("#")``
     |      
     |      See :func:`lasio.reader.open_with_codecs` for additional keyword
     |      arguments which help to manage issues relate to character encodings.
     |  
     |  set_data(self, array_like, names=None, truncate=False)
     |      Set the data for the LAS; actually sets data on individual curves.
     |      
     |      Arguments:
     |          array_like (array_like or :class:`pandas.DataFrame`): 2-D data array
     |      
     |      Keyword Arguments:
     |          names (list, optional): used to replace the names of the existing
     |              :class:`lasio.CurveItem` objects.
     |          truncate (bool): remove any columns which are not included in the
     |              Curves (~C) section.
     |      
     |      Note: you can pass a :class:`pandas.DataFrame` to this method.
     |  
     |  set_data_from_df(self, df, **kwargs)
     |      Set the LAS file data from a :class:`pandas.DataFrame`.
     |      
     |      Arguments:
     |          df (pandas.DataFrame): curve mnemonics are the column names.
     |              The depth column for the curves must be the index of the
     |              DataFrame.
     |      
     |      Keyword arguments are passed to :meth:`lasio.LASFile.set_data`.
     |  
     |  stack_curves(self, mnemonic, sort_curves=True)
     |      Stack multi-channel curve data to a numpy 2D ndarray. Provide a
     |      stub name (prefix shared by all curves that will be stacked) or a
     |      list of curve mnemonic strings.
     |      
     |      Keyword Arguments:
     |          mnemonic (str or list): Supply the first several characters of
     |              the channel set to be stacked. Alternatively, supply a list
     |              of the curve names (mnemonics strings) to be stacked.
     |          sort_curves (bool): Natural sort curves based on mnemonic prior
     |              to stacking.
     |      
     |      Returns:
     |          2-D numpy array
     |  
     |  to_csv(self, file_ref, mnemonics=True, units=True, units_loc='line', **kwargs)
     |      Export to a CSV file.
     |      
     |      Arguments:
     |          file_ref (open file-like object or str): a file-like object opening
     |              for writing, or a filename.
     |      
     |      Keyword Arguments:
     |          mnemonics (list, True, False): write mnemonics as a header line at the
     |              start. If list, use the supplied items as mnemonics. If True,
     |              use the curve mnemonics.
     |          units (list, True, False): as for mnemonics.
     |          units_loc (str or None): either 'line', '[]' or '()'. 'line' will put
     |              units on the line following the mnemonics (good for WellCAD).
     |              '[]' and '()' will put the units in either brackets or
     |              parentheses following the mnemonics, on the single header line
     |              (better for Excel)
     |          **kwargs: passed to :class:`csv.writer`. Note that if
     |              ``lineterminator`` is **not** specified here, then it will be
     |              sent to :class:`csv.writer` as ``lineterminator='\n'``.
     |  
     |  to_excel(self, filename)
     |      Export LAS file to a Microsoft Excel workbook.
     |      
     |      This function will raise an :exc:`ImportError` if ``openpyxl`` is not
     |      installed.
     |      
     |      Arguments:
     |          filename (str)
     |  
     |  to_json(self)
     |  
     |  to_json_old(self)
     |      deprecated: to_json_old version=0.25.1 since=20200507 remove=20210508
     |      replacement_options: to_json()
     |  
     |  values(self)
     |      Return data for each curve.
     |  
     |  write(self, file_ref, **kwargs)
     |      Write LAS file to disk.
     |      
     |      Arguments:
     |          file_ref (open file-like object or str): a file-like object opening
     |              for writing, or a filename.
     |      
     |      All ``**kwargs`` are passed to :func:`lasio.writer.write` -- please
     |      check the docstring of that function for more keyword arguments you can
     |      use here!
     |      
     |      Examples:
     |      
     |          >>> import lasio
     |          >>> las = lasio.read("tests/examples/sample.las")
     |          >>> with open('test_output.las', mode='w') as f:
     |          ...     las.write(f, version=2.0)   # <-- this method
     |  
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |  
     |  curvesdict
     |      Curve information and data from the Curves (~C) and data section..
     |      
     |      Returns:
     |          dict
     |  
     |  depth_ft
     |      Return the index as feet.
     |  
     |  depth_m
     |      Return the index as metres.
     |  
     |  header
     |      All header information
     |      
     |      Returns:
     |          dict
     |  
     |  index
     |      Return data from the first column of the LAS file data (depth/time).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  curves
     |      Curve information and data from the Curves (~C) and data section..
     |      
     |      Returns:
     |          :class:`lasio.SectionItems` object.
     |  
     |  data
     |  
     |  json
     |      Return object contents as a JSON string.
     |  
     |  other
     |      Header information from the Other (~O) section.
     |      
     |      Returns:
     |          str
     |  
     |  params
     |      Header information from the Parameter (~P) section.
     |      
     |      Returns:
     |          :class:`lasio.SectionItems` object.
     |  
     |  version
     |      Header information from the Version (~V) section.
     |      
     |      Returns:
     |          :class:`lasio.SectionItems` object.
     |  
     |  well
     |      Header information from the Well (~W) section.
     |      
     |      Returns:
     |          :class:`lasio.SectionItems` object.
    



```python
#From there we can get some info from each of the wells
j=0
for well in lases:
    #e.g. pull out the varaibles availble from the wells
    print("Wellid:", j, well_names[j])
    j+=1
    print(well.keys())
```

    Wellid: 0 
    ['DEPTH', 'CALI', 'DRHO', 'DT', 'GR', 'NPHI', 'PEF', 'RDEP', 'RHOB', 'RMED', 'SP']
    Wellid: 1 
    ['DEPTH', 'CALI', 'DRHO', 'DT', 'DTS', 'GR', 'NPHI', 'PEF', 'RDEP', 'RHOB', 'RMED', 'RMIC', 'SP']
    Wellid: 2 
    ['DEPTH', 'GR', 'RDEP', 'RMED', 'SP']
    Wellid: 3 
    ['DEPTH', 'CALI', 'DRHO', 'DT', 'GR', 'MINV', 'MNOR', 'NPHI', 'PEF', 'RDEP', 'RHOB', 'RMED', 'RMIC', 'SP']
    Wellid: 4 
    ['DEPTH', 'CALI', 'DRHO', 'DT', 'GR', 'MINV', 'MNOR', 'NPHI', 'PEF', 'RDEP', 'RHOB', 'RMED', 'RMIC', 'SP']
    Wellid: 5 
    ['DEPTH', 'CALI', 'DRHO', 'DT', 'GR', 'NPHI', 'RDEP', 'RHOB', 'RMED', 'SP']
    Wellid: 6 
    ['DEPTH', 'CALI', 'DT', 'GR', 'RDEP', 'RMED', 'SP']
    Wellid: 7 
    ['DEPTH', 'CALI', 'MINV', 'MNOR', 'RDEP', 'RMED', 'SP']



```python
#Set a wellid you want to explore more
wellid=1
```


```python
#Make a plot of one of the wells
plt.plot(lases[wellid]['DRHO'],lases[wellid]['DEPTH'])
```




    [<matplotlib.lines.Line2D at 0x7f842a6fb9a0>]




    
![png](01b-dataframes_files/01b-dataframes_49_1.png)
    


TODO: What does this plot show us??? What is the conclusion?


```python
#Get some more info out of the well data
print(lases[wellid].curves)
```

    Mnemonic  Unit   Value  Description                                                                                        
    --------  ----   -----  -----------                                                                                        
    DEPTH     M             Depth                                                                                              
    CALI      in            Caliper     CAL Spliced, Edited, bungaloo_1_mll_rtex_r1.dlis, bungaloo_1_mll_rtex_r2.dlis          
    DRHO      g/cm3         DenCorr     ZCOR Edited, bungaloo_1_mll_rtex_xyzdl_r6.dlis                                         
    DT        us/ft         Sonic       DT24 DT24.I Spliced, Edited, bungaloo_1_mll_rtex_r1.dlis, bungaloo_1_mll_rtex_r2.dlis  
    DTS       us/ft         ShearSonic  DTS , bungaloo_1_mll_rtex_r2.dlis                                                      
    GR        gAPI          GammaRay    GR Spliced, Edited, bungaloo_1_mll_rtex_r1.dlis, bungaloo_1_mll_rtex_r2.dlis           
    NPHI      dec           Neutron     CNC Edited, bungaloo_1_neutron_r2.dlis                                                 
    PEF       b/e           PEFactor    PE Edited, bungaloo_1_mll_rtex_xyzdl_r6.dlis                                           
    RDEP      ohmm          DeepRes     MLR4C Spliced, Edited, bungaloo_1_mll_rtex_r1.dlis, bungaloo_1_mll_rtex_r2.dlis        
    RHOB      g/cm3         Density     ZDNC Edited, bungaloo_1_mll_rtex_xyzdl_r6.dlis                                         
    RMED      ohmm          MedRes      MLR2C Spliced, Edited, bungaloo_1_mll_rtex_r1.dlis, bungaloo_1_mll_rtex_r2.dlis        
    RMIC      ohmm          MicroRes    RMLL Spliced, Edited, bungaloo_1_mll_rtex_r1.dlis, bungaloo_1_mll_rtex_r2.dlis         
    SP        mV            SponPot     SPWDH Edited, bungaloo_1_mll_rtex_r2.dlis                                              



```python
# Finally, make a reasonable plot
var = 'RHOB' 
print("Param:", var, "of well:", well_names[wellid])
plt.figure(figsize=(5,10))
plt.plot((lases[wellid][var]), (lases[wellid]['DEPTH']))

#And change some details on the plot
plt.xlabel(var); plt.ylabel("Depth (m)")
plt.grid(True)
plt.gca().invert_yaxis()
```

    Param: RHOB of well: 



    
![png](01b-dataframes_files/01b-dataframes_52_1.png)
    


TODO: Why is this plot reasonable? What does it show?

# SEGY Seismic data processing


```python
from obspy.io.segy.segy import _read_segy
import matplotlib.pyplot as plt
import numpy as np

#Adapted from https://agilescientific.com/blog/2016/9/21/x-lines-of-python-read-and-write-seg-y
#See the notebooks here for more good examples
#https://hub-binder.mybinder.ovh/user/agile-geoscience-xlines-n1mojurk
```


```python
#Set the filename of the segy data

filename="data/james/james_1959_pstm_tvfk_gain.sgy"

#Title: 2006 James 3D Seismic Survey.
#Author: White, A.
#Prepared by: Terrex Seismic Pty Ltd; Pioneer Surveys Pty Ltd; WestenGeco
#Tenement: PPL00182
#Operator: Santos Ltd
#https://sarigbasis.pir.sa.gov.au/WebtopEw/ws/samref/sarig1/wci/Record?r=0&m=1&w=catno=2035790
```


```python
stream = _read_segy(filename, headonly=True)
stream
```




    48832 traces in the SEG Y structure.




```python
one_trace = stream.traces[10000]

plt.figure(figsize=(16,2))
plt.plot(one_trace.data)
plt.show()
```


    
![png](01b-dataframes_files/01b-dataframes_58_0.png)
    



```python
data = np.stack(t.data for t in stream.traces[12320:12320+500])
```

    /Users/darya/anaconda3/envs/python4pesa/lib/python3.8/site-packages/IPython/core/interactiveshell.py:3338: FutureWarning: arrays to stack must be passed as a "sequence" type such as list or tuple. Support for non-sequence iterables such as generators is deprecated as of NumPy 1.16 and will raise an error in the future.
      if (await self.run_code(code, result,  async_=asy)):



```python
stream.traces[10000]
```




    Trace sequence number within line: 10001
    1001 samples, dtype=float32, 250.00 Hz




```python
data.shape
```




    (500, 1001)




```python
np.shape(stream.traces)
```




    (48832,)




```python
vm = np.percentile(data, 95)
print("The 95th percentile is {:.0f}; the max amplitude is {:.0f}".format(vm, data.max()))
```

    The 95th percentile is 4365; the max amplitude is 34148



```python
plt.imshow(data.T, cmap="Greys", vmin=-vm, vmax=vm, aspect='auto')
```




    <matplotlib.image.AxesImage at 0x7f8414587ac0>




    
![png](01b-dataframes_files/01b-dataframes_64_1.png)
    



```python
plt.figure(figsize=(16,8))
plt.imshow(data.T, cmap="RdBu", vmin=-vm, vmax=vm, aspect='auto')
plt.colorbar()
plt.show()
```


    
![png](01b-dataframes_files/01b-dataframes_65_0.png)
    



```python
print(stream.textual_file_header.decode())
```

    C 1 CLIENT SANTOS                 COMPANY                       CREW NO         C 2 LINE    2000.00 AREA JAMES3D                                                C 3 REEL NO           DAY-START OF REEL     YEAR      OBSERVER                  C 4 INSTRUMENT  MFG            MODEL            SERIAL NO                       C 5 DATA TRACES/RECORD 24569  AUXILIARY TRACES/RECORD       0 CDP FOLD    40    C 6 SAMPLE INTERVAL  4.00   SAMPLES/TRACE  1001 BITS/IN      BYTES/SAMPLE  4    C 7 RECORDING FORMAT        FORMAT THIS REEL SEG-Y  MEASUREMENT SYSTEM METERS   C 8 SAMPLE CODE FLOATING PT                                                     C09 JAMES 3D                                                                    C10 WESTERNGECO                                                                 C11 MARCH 2007                                                                  C12 VERSION : James3D_pstm_tvfk_gain                                            C13 FILTERED TRIM PSTM STACK                                                    C14                                                                             C15 GEOMETRY APPLY-TAR-MINP-                                                    C16 NOISE REDUCTION - SWATT                                                     C17  SC DECON - SCAC                                                            C18 RESIDUAL_STATICS                                                            C19  TRIM_STATICS - INVERSE_TAR - SORT                                          C20 PSTM  - SORT  - GAIN                                                        C21 TRIM_STATICS - STACK                                                        C22 SPECW_10-70HZ -TVF_10-75HZ-TRACE_BALANCE                                    C23                                                                             C24                                                                             C25                                                                             C26                                                                             C27                                                                             C28                                                                             C29                                                                             C30                                                                             C31                                                                             C32                                                                             C33                                                                             C34                                                                             C35                                                                             C36                                                                             C37                                                                             C38                                                                             C39                                                                             C40 END EBCDIC                                                                  



```python
print(stream.traces[50].header)
```

    trace_sequence_number_within_line: 51
    trace_sequence_number_within_segy_file: 51
    original_field_record_number: 2000
    trace_number_within_the_original_field_record: 1
    energy_source_point_number: 10055
    ensemble_number: 10055
    trace_number_within_the_ensemble: 51
    trace_identification_code: 1
    number_of_vertically_summed_traces_yielding_this_trace: 1
    number_of_horizontally_stacked_traces_yielding_this_trace: 24
    data_use: 1
    distance_from_center_of_the_source_point_to_the_center_of_the_receiver_group: 0
    receiver_group_elevation: 0
    surface_elevation_at_source: 0
    source_depth_below_surface: 0
    datum_elevation_at_receiver_group: 0
    datum_elevation_at_source: 0
    water_depth_at_source: 0
    water_depth_at_group: 0
    scalar_to_be_applied_to_all_elevations_and_depths: 1
    scalar_to_be_applied_to_all_coordinates: 1
    source_coordinate_x: 482680
    source_coordinate_y: 7035256
    group_coordinate_x: 482680
    group_coordinate_y: 7035256
    coordinate_units: 1
    weathering_velocity: 0
    subweathering_velocity: 0
    uphole_time_at_source_in_ms: 0
    uphole_time_at_group_in_ms: 0
    source_static_correction_in_ms: 0
    group_static_correction_in_ms: 0
    total_static_applied_in_ms: -70
    lag_time_A: 0
    lag_time_B: 0
    delay_recording_time: 0
    mute_time_start_time_in_ms: 0
    mute_time_end_time_in_ms: 20
    number_of_samples_in_this_trace: 1001
    sample_interval_in_ms_for_this_trace: 4000
    gain_type_of_field_instruments: 0
    instrument_gain_constant: 0
    instrument_early_or_initial_gain: 0
    correlated: 0
    sweep_frequency_at_start: 0
    sweep_frequency_at_end: 0
    sweep_length_in_ms: 0
    sweep_type: 0
    sweep_trace_taper_length_at_start_in_ms: 0
    sweep_trace_taper_length_at_end_in_ms: 0
    taper_type: 0
    alias_filter_frequency: 0
    alias_filter_slope: 0
    notch_filter_frequency: 0
    notch_filter_slope: 0
    low_cut_frequency: 0
    high_cut_frequency: 0
    low_cut_slope: 0
    high_cut_slope: 0
    year_data_recorded: 0
    day_of_year: 0
    hour_of_day: 0
    minute_of_hour: 0
    second_of_minute: 0
    time_basis_code: 0
    trace_weighting_factor: 0
    geophone_group_number_of_roll_switch_position_one: 0
    geophone_group_number_of_trace_number_one: 0
    geophone_group_number_of_last_trace: 0
    gap_size: 0
    over_travel_associated_with_taper: 0
    x_coordinate_of_ensemble_position_of_this_trace: 0
    y_coordinate_of_ensemble_position_of_this_trace: 0
    for_3d_poststack_data_this_field_is_for_in_line_number: 0
    for_3d_poststack_data_this_field_is_for_cross_line_number: -4587520
    shotpoint_number: 2000
    scalar_to_be_applied_to_the_shotpoint_number: 0
    trace_value_measurement_unit: 10055
    transduction_constant_mantissa: 0
    transduction_constant_exponent: 0
    transduction_units: 0
    device_trace_identifier: 0
    scalar_to_be_applied_to_times: 57
    source_type_orientation: 0
    source_energy_direction_mantissa: 0
    source_energy_direction_exponent: 584
    source_measurement_mantissa: 0
    source_measurement_exponent: 0
    source_measurement_unit: 0
    



```python
dt = stream.traces[0].header.sample_interval_in_ms_for_this_trace / 1e6
dt
```




    0.004



<div class="challenge">

### Challenge. TODO

- This needs a HW challenge!

<details>
<summary>Solution</summary>

...    
```python
```

<div class="keypoints">
### Key points
    
- Shapefiles
- Pandas dataframes
</div>






    0.004

