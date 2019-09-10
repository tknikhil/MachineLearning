# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 05:19:01 2019

@author: Nikhil
"""

hat_height_cm =25
my_height_cm = 190

total_height_meters = hat_height_cm + my_height_cm/100

#this will print wrong answer
print("Height in Meter ",total_height_meters, "?")

#this will print expected answer
total_height = (hat_height_cm+my_height_cm)/100
print("Height in meters ",total_height)

print(min(3,6,1))

print(max(3,6,1))

print(abs(32))
print(abs(-32))

print(float(10))
print(int(3.33))
print(int('803')+1)