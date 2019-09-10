# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 12:33:48 2019
Data Processing on collection of data
@author: Nikhil
"""

#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing data
dataset =pd.read_csv('D:/Nikhil_File/Machine Learning/Machine Learning A-Z Template Folder/Part 1 - Data Preprocessing/Data.csv')
#print(dataset) 
X=dataset.iloc[:,:-1].values#this take country, age, salary
Y=dataset.iloc[:,3].values  #this take Purcheased


#z=dataset.iloc[:,2].values
#print(z)
#z.dtype
#print(x) #print(y)


    
#Taking care of missing data

"""
DeprecationWarning: Class Imputer is deprecated;
     Imputer was deprecated in version 0.20 and will be removed in 0.22. 
     Import impute.SimpleImputer from sklearn instead.
     warnings.warn(msg, category=DeprecationWarning)
     
from sklearn.preprocessing import Imputer
imputer =Imputer(missing_values='NaN',strategy='mean',axis=0)
imputer =imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])"""

#dataset.dtypes


from sklearn.impute import SimpleImputer

"""In missing_values we have to use Numpy NaN value not 'NaN' otherwise it 
will take it as String and through 
ValueError: 'X' and 'missing_values' types are expected to be both numerical. 
Got X.dtype=float64 and  type(missing_values)=<class 'str'>.""" 
simpleImputer = SimpleImputer(missing_values=np.nan, strategy='mean')    
simpleImputer=simpleImputer.fit(X[:,1:3])
X[:,1:3]=simpleImputer.transform(X[:,1:3])
