# -*- coding: utf-8 -*-
"""
Harsh Nagarkar
Green Chinchilla
Challenge 5
"""
from __future__ import division
import matplotlib.pyplot as mplot
import pandas as pd
import math
import itertools
import numpy as np
  
global cnum


#calculating linnear regression
def regression(x,y,c):
     cor = np.corrcoef(x,y)
     slope = cor[0][1]*np.std(y)/np.std(x)
     intercept = np.mean(y)-slope*np.mean(x)
     linY = []
#     getting all predicted points
     for i in range(len(y)):
         linY.append(slope*x[i]+intercept)
#         test to find if it a signal or noise
     m = set(y)-set(linY)
     cnum = np.mean(list(m))
#     deciding factor
     if cnum<60:
         mplot.plot(x,linY,color="red")
#         calling polynomial regression functions
         polyregression(x,y,c)

     
#calculating ploy regression
def polyregression(x,y,c):
    degree = 5
#    sort was needed for getting right ordered points
    x = sorted(x)
    y = sorted(y,reverse=True)
    polyY = np.polyval(np.polyfit(x,y,degree),x)
    mplot.plot(x,polyY,color="blue")    
    
#---------------------------------------------------------------------------------------------------------
#reading file and getting unique frequencies
df = pd.read_csv('GreenChinchilla.csv',header=None)

#getting unique frequency
freq = df[1].unique()

#creating colors for graph
colors = itertools.cycle(["orange", "r", "g","b","violet"])
# looping through data
for i in range(len(freq)):
    pf = df.set_index([1])
    #choosing a frequency for data analysis
    value = pf.loc[freq[i]].values
    x,y = zip(*value)
    c = next(colors)
#    calling method
    regression(x,y,c)
    mplot.scatter(x,y, color=c)
    cnum = 0

#showwing plot
mplot.title('Time in ms VS Signal Intesity')
mplot.xlabel('Time-milliseconds')
mplot.ylabel('Signal Intensity')
mplot.show()