#!/usr/bin/python
#coding:utf-8
##################################
'''
Path: 
Description: python绘图
Date: 
Version: v1.0
'''
##################################
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#指定不需要GUI的backendr(Agg, Cairo, PS, PDF or SVGr),避免远程绘图报错
plt.switch_backend('agg')

def loadData(datefile):
    df = pd.read_csv(datefile,sep='\t')# 读取数据
    return df[["日期","订单量"]] #组合两个数据列

def drawFigure(x,y):
    fig = plt.figure()
    fig.suptitle('no asxes on this figure')
    fig,ax_lst = plt.subplots(1,1) #图形矩阵数量
    ax_lst.plot(x,y)
    fig.savefig('/home/fannian/downloads/figure.png')#输出图片

if __name__ == '__main__':
    X = loadData('/home/fannian/downloads/dailysale.txt')
    print X.shape
    print X.iloc[0]
