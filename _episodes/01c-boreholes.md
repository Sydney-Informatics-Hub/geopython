---
title: "01c. Python Fundamentals - niche packages"
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
read_files = glob.glob("WELL/*.las")
read_files
```




    ['WELL/Balnaves.las',
     'WELL/Banyula.las',
     'WELL/Beachport1.las',
     'WELL/BeachportEast1.las',
     'WELL/BiscuitFlat1.las',
     'WELL/BoolLagoon1.las',
     'WELL/Bungaloo1.las',
     'WELL/Burrungule1.las']




```python
#Cut out just the name of the well from the filenames
well_names = []
for file in read_files:
    print("FILE:", file)
    well=re.split('/|\.',file)
    print("SPLIT:", well)
    well_names.append(well[1])

print("There are ", len(well_names), "wells.")
print(well_names)
```

    FILE: WELL/Balnaves.las
    SPLIT: ['WELL', 'Balnaves', 'las']
    FILE: WELL/Banyula.las
    SPLIT: ['WELL', 'Banyula', 'las']
    FILE: WELL/Beachport1.las
    SPLIT: ['WELL', 'Beachport1', 'las']
    FILE: WELL/BeachportEast1.las
    SPLIT: ['WELL', 'BeachportEast1', 'las']
    FILE: WELL/BiscuitFlat1.las
    SPLIT: ['WELL', 'BiscuitFlat1', 'las']
    FILE: WELL/BoolLagoon1.las
    SPLIT: ['WELL', 'BoolLagoon1', 'las']
    FILE: WELL/Bungaloo1.las
    SPLIT: ['WELL', 'Bungaloo1', 'las']
    FILE: WELL/Burrungule1.las
    SPLIT: ['WELL', 'Burrungule1', 'las']
    There are  8 wells.
    ['Balnaves', 'Banyula', 'Beachport1', 'BeachportEast1', 'BiscuitFlat1', 'BoolLagoon1', 'Bungaloo1', 'Burrungule1']



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
...
    



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
...


```python
#From there we can get some info from each of the wells
j=0
for well in lases:
    #e.g. pull out the varaibles availble from the wells
    print("Wellid:", j, well_names[j])
    j+=1
    print(well.keys())
```

    Wellid: 0 Balnaves
    ['DEPTH', 'CALI', 'DRHO', 'DT', 'GR', 'MINV', 'MNOR', 'NPHI', 'PEF', 'RDEP', 'RHOB', 'RMED', 'RMIC', 'SP']
    Wellid: 1 Banyula
    ['DEPTH', 'CALI', 'DRHO', 'DT', 'GR', 'NPHI', 'RDEP', 'RHOB', 'RMED', 'SP']
    Wellid: 2 Beachport1
    ['DEPTH', 'CALI', 'MINV', 'MNOR', 'RDEP', 'RMED', 'SP']
    Wellid: 3 BeachportEast1
    ['DEPTH', 'GR', 'RDEP', 'RMED', 'SP']
    Wellid: 4 BiscuitFlat1
    ['DEPTH', 'CALI', 'DRHO', 'DT', 'GR', 'MINV', 'MNOR', 'NPHI', 'PEF', 'RDEP', 'RHOB', 'RMED', 'RMIC', 'SP']
    Wellid: 5 BoolLagoon1
    ['DEPTH', 'CALI', 'DRHO', 'DT', 'GR', 'NPHI', 'PEF', 'RDEP', 'RHOB', 'RMED', 'SP']
    Wellid: 6 Bungaloo1
    ['DEPTH', 'CALI', 'DRHO', 'DT', 'DTS', 'GR', 'NPHI', 'PEF', 'RDEP', 'RHOB', 'RMED', 'RMIC', 'SP']
    Wellid: 7 Burrungule1
    ['DEPTH', 'CALI', 'DT', 'GR', 'RDEP', 'RMED', 'SP']



```python
#Set a wellid you want to explore more
wellid=1
```


```python
#Make a plot of one of the wells
plt.plot(lases[wellid]['DRHO'],lases[wellid]['DEPTH'])
```




    [<matplotlib.lines.Line2D at 0x7f22c1519890>]




    
![png](fig/fig-01-well.png)
    



```python
#Get some more info out of the well data
print(lases[wellid].curves)
```

    Mnemonic  Unit   Value  Description                                         
    --------  ----   -----  -----------                                         
    DEPTH     M             Depth                                               
    CALI      in            Caliper     CALI Edited, Spliced, BANYU001.G01.lis  
    DRHO      g/cm3         DenCorr     DRHO Edited, BANYU001.G01.lis           
    DT        us/ft         Sonic       DT Edited, Spliced, BANYU001.G01.lis    
    GR        gAPI          GammaRay    GR Spliced, BANYU001.G01.lis            
    NPHI      dec           Neutron     NPHI Edited, BANYU001.G01.lis           
    RDEP      ohmm          DeepRes     ILD Spliced, BANYU001.G01.lis           
    RHOB      g/cm3         Density     RHOB Edited, BANYU001.G01.lis           
    RMED      ohmm          MedRes      ILM Spliced, BANYU001.G01.lis           
    SP        mV            SponPot     SP Spliced, BANYU001.G01.lis            



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

    Param: RHOB of well: Banyula



    
![png](fig-01-prettywell.png)
    



```python

```
