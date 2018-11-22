#!/usr/bin/python
#coding:utf-8
##################################
'''
Path: 
Description: 学习numpy
Date: 
Version: v1.0
'''
##################################
import numpy as np
my_array=np.array([1,2,3,4,5])
print my_array
print my_array.shape
my_array[0]=-1
print my_array
my_new_array = np.zeros((5))
print my_new_array
my_random_array = np.random.random((5))
print my_random_array
my_2d_array = np.zeros((2, 3)) 
print my_2d_array
my_2d_array_new = np.ones((2, 3)) 
print my_2d_array_new
my_array = np.array([[4, 5], [6, 1]])
print my_array[0][1]
my_array_column_2 = my_array[:, 1]
print my_array_column_2
a = np.array([[1.0, 2.0], [3.0, 4.0]])
b = np.array([[5.0, 6.0], [7.0, 8.0]])
