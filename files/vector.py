#import packages
import numpy as np
import pandas as pd
import time 

#Create some data to work with
AllPubs = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
Users = pd.DataFrame(np.random.randint(0,100,size=(50, 1)), columns=list('A'))

#This could perhaps be the id of a person and the list of publications they have made. 
#You want to match up their publications with some other list, 
#perhaps the publications they made by using Artemis.

#Create an emtpy dataframe to fill with the resulting matches
totalSlow=pd.DataFrame(columns=AllPubs.columns)
totalFast=pd.DataFrame(columns=AllPubs.columns)


#Try the traditional nested for loop
tic=time.time()
for index,pub in AllPubs.iterrows():
  for index2,user in Users.iterrows():
    if user['A']==pub['A']:
      totalSlow=totalSlow.append(pub,ignore_index=True)
      
totalSlow=totalSlow.drop_duplicates()
toc=time.time()
print("Nested-loop Runtime:",toc-tic, "seconds")


#Try the vectorised
tic=time.time()
totalFast=AllPubs[AllPubs['A'].isin(Users.A.tolist())]
totalFast=totalSlow.drop_duplicates()
toc=time.time()
print("Vectorized Runtime:",toc-tic, "seconds")
