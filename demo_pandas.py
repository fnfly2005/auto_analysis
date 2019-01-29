#!/usr/bin/python
#coding:utf-8
##################################
'''
Path: 
Description: 分析
Date: 2018-11-20
Version: v1.0
'''
##################################
import pandas as pd
import matplotlib.pyplot as plt
path="/Users/fannian/Downloads/dim_myshow_project.txt"

df = pd.read_csv(path,\
    sep='\t',\
    dtype={"soleagent":int})#指定列字段类型

print df.describe() #描述统计

#dt=df['销售额'].groupby('日期').sum() #group by & sum 函数
#dt.plot() #绘图
#plt.savefig(sys.argv[2])#输出图片
