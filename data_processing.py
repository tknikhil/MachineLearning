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
simpleImputer = SimpleImputer(missing_values=np.nan, strategy='mean',verbose=0)    
simpleImputer=simpleImputer.fit(X[:,1:3])
X[:,1:3]=simpleImputer.transform(X[:,1:3])


"""
Note :-Every Time if I close this code  and open again I need ot re Import 
every thing by running the code from to bottom other wise 'UNKNOWN RANDOM
VauleError'
"""


#Encoding Catagorcal Data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labencoder_x =LabelEncoder()
X[:,0]=labencoder_x.fit_transform(X[:,0])#selecting Country column
onehotencoder=OneHotEncoder(categorical_features=[0])#converting it into float64 formate
X=onehotencoder.fit_transform(X).toarray()#make column for each unique country value

lablencoder_y=LabelEncoder()
Y=lablencoder_y.fit_transform(Y)#converting object into int32

#Spliting the data into the Traning set and Test set
"""
Note:- the purpose of this code is to split the column which we going to do 
prediction into to two further more column Test and Training so that we 
train our training column for prediction and test weather our logic is understandable
by Machine in test column so that it will use the same logic for further prediction
if the same data comes again
"""
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test =train_test_split(X,Y,test_size=0.2,random_state=0)#because of 0.2 it will take 2 test case and 8 training case

#Feature Scalling 
#need to have Knowledge of Euclidean Distance and Standardisation and Normalisation
from sklearn.preprocessing import StandardScaler
sc_X =StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)


































