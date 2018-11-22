#!/usr/bin/python
#coding:utf-8
##################################
'''
Path: 
Description: 
Date: 
Version: v1.0
'''
##################################
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()
fig.suptitle('no asxes on this figure')

fig,ax_lst =plt.subplots(2,2)
fig.savefig("examples.jpg")
