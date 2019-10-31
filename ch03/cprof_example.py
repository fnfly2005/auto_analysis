#!/usr/bin/python
#coding:utf-8
"""
numpy Linear algebra (numpy.linalg) nl.eigvals()
计算一般矩阵的特征值

numpy Random sampling (numpy.random) nr.randn() 
numpy Mathematical functions np.absolute()
numpy Mathematical functions np.maximum()
"""
import numpy as np
from numpy.linalg import eigvals

def run_experiment(niter=100):
    K=100
    results = []
    for _ in range(niter):
        mat= np.random.randn(K,K)
        max_eigenvalue = np.abs(eigvals(mat)).max()
        results.append(max_eigenvalue)
    return results

some_results = run_experiment()
print('Largest one we saw: %s' % np.max(some_results))
