# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 19:46:19 2019
Data Preprocessing Templates
@author: Nikhil
"""

#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing data
dataset =pd.read_csv('D:/Nikhil_File/Machine Learning/Machine Learning A-Z Template Folder/Part 1 - Data Preprocessing/Data.csv')
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,3].values  
    
#Spliting the data into the Traning set and Test set
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test =train_test_split(X,Y,test_size=0.2,random_state=0)

#Feature Scalling 
"""from sklearn.preprocessing import StandardScaler
sc_X =StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)"""



