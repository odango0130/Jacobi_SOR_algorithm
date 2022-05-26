# -*- coding: utf-8 -*-
"""
Created on Wed May 25 23:40:17 2022

@author: yuuki
"""
import numpy as np

def Progress(k,x):
    print(k)
    for val in x:
        print('{:.8f}'.format(val),end='')
        print()
        
def Jacobi(N,A,y,eps):
    x = np.zeros(N)
    z = np.zeros(N)
    Progress(0,x)
    print()
    q = 0
    #for k in range(1,M+1):
    while True:
        q += 1
        a = np.copy(x)
        for i in range(N):
            total = 0
            for j in range(N):
                if i != j:
                    total += A[i][j]*x[j]
            z[i] = (y[i]-total)/A[i][j]
            
        for i in range(N):
            x[i] = z[i]
        a = abs(x - a)   
        Progress(q,x)
        print(x)
        print(a)
        print()
        if (sum(a))/N < (eps*sum(x))/N:     #収束判定
            break
    return x

N = 2
A = np.array([[5,4],[2,3]])
y = [13,8]
M = 41
eps = 0.0001

x = Jacobi(N,A,y,eps)

input("Please push Enter Key.")
