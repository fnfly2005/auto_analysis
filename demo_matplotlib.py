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
import sys

fig=plt.figure()
fig.suptitle('no asxes on this figure')

fig,ax_lst =plt.subplots(1,1) #图形矩阵数量
fig.savefig(sys.argv[1])#输出图片
