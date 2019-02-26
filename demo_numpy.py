#!/usr/bin/python
#coding:utf-8
'''
Description: 学习numpy
矩阵的形状、修改矩阵的元素、生成0矩阵&1矩阵&随机矩阵、生成单位矩阵、点乘、矩阵运算
等差数组矩阵、矩阵求和
'''
import numpy as np

class ArrayDemo(object):
    def __init__(self,arr_var):
        self.arr = np.array(arr_var)
        self.shape = self.arr.shape #shape属性返回x行乘y列的数组形状

    def setVar(self,key,var):
        self.arr[key] = var

    def builtArray(self,tupe,status=0):
        if status == 0:
            return np.zeros(tupe)#返回0矩阵
        elif status == 1:
            return np.ones(tupe)#返回1矩阵
        else:
            return np.random.random(tupe)#返回0-1的随机数矩阵

    def eyeArray(self,num):
        return np.eye(num)#返回num*num单位矩阵

    def atmArray(self,sta,end,num):
        return np.linspace(sta,end,num=num)#返回等差数列矩阵,sta开始-end结束-num步长

    def dotArray(self,ar):
        return self.arr.dot(ar)#ar2点乘ar1: 结果获得ar2的行数和ar1的列数
        
    def tasArray(self):
        return self.arr.T#返回矩阵的转置矩阵

    def sumArray(self):
        return self.arr.sum()#计算矩阵所有元素和

    def randomArray(self,ar):
        #返回一个洗牌后的矩阵
        num = np.random.permutation(len(ar))
        return ar[num] #ar[array] 返回一个按array给出的索引排序的矩阵

if __name__ == '__main__':
    ar1 = ArrayDemo([[1.,2.], [7.,4.], [3.,5.]])
    ar2 = ArrayDemo([[4.,5.,1.], [6.,1.,4.]])
    rad = ar1.builtArray((2,3),2)
    
    print ar2.randomArray(ar2.arr)
    print ar2.dotArray(ar1.arr)
    print rad + 1#常规加减乘除，若是常数，则对矩阵每个元素进行;若是矩阵,则必须相同形状
