# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:02:15 2019
Data Processing by using seprate data

Note --:> This Code os for R language there you can find EXACT CODE  

@author: Nikhil
"""

#importing the libraries
import numpy as np
import matpotlib.pyplot as plt
import pandas as pd

#importing data CSV file 
dataset = pd.read_csv('D:/Nikhil_File/Machine Learning/Machine Learning A-Z Template Folder/Part 1 - Data Preprocessing/Data.csv')

#Taking care of missing values
dataset$Age = elif(is.na(dataset$Age),ave(dataset$Age,FUN= function(x) mean(x ,na.rm = TRUE)),dataset$Age)
