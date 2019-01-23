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

#path = '/home/fannian/downloads/'
path = '/Users/fannian/Documents/'

def loadData(datefile):
    df = pd.read_csv(datefile,sep='\t')# 读取数据
    df['日期']=pd.to_datetime(df['日期'],format='%Y-%m-%d') # 字符串to日期
    df = df[['日期','订单量']] #选取并组合数据
    return df.sort_values(by='日期') #排序

def drawFigure(x,y):
    fig = plt.figure()
    fig.suptitle('no asxes on this figure')
    fig,ax_lst = plt.subplots(1,1) #图形矩阵数量
    ax_lst.plot(x,y) #设置x轴，y轴值
    fig.savefig(path + 'figure.png')#输出图片

if __name__ == '__main__':
    X = loadData(path + 'dailysale.txt')
    print X.shape #查看矩阵形状
    drawFigure(X.iloc[:,0:1],X.iloc[:,1:2]) #对列进行切片
