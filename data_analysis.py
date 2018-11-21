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
import sys
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[1],sep='\t',dayfirst=True, index_col='日期')

def deldf(*args):
    for a in args:
        del df[a]

deldf('数据源','月份','动销场次数','在线项目数','动销项目数','毛利额','战区')

print df.head(5)
df['销售额'].plot()
plt.show()
