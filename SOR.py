# -*- coding: utf-8 -*-
"""
Created on Thu May 26 12:36:50 2022

@author: yuuki
"""
import numpy as np

def Progress(k,x):
    print(k)
    for val in x:
        print('{:.8f}\n'.format(val),end="")
    
    
def SOR(N,A,y,omega,M):
    q = 0;
    x = np.zeros(N)
    z = np.zeros(N)                         #前回の値との比較用
    Progress(0,x)
    print()
    
    while True:
        q += 1;
        z = np.copy(x)
        for i in range(N):
            total = 0
            for j in range(N):
                if i != j:
                    total += A[i][j]*x[j]
            x[i] = omega*(y[i]-total)/A[i][j]+(1-omega)*x[i]
        z = abs(x - z)                      #前回の値との差の絶対値
        Progress(q,x)
        print(z)
        print()
        if (sum(z))/N < (eps*sum(x))/N:     #収束判定
            break
    return x

N = 2                                       #未知数の個数
A = np.array([[5,4],[2,3]])                 #係数行列
y = np.array([13,8])                        #定数ベクトル
omega = 1.2                                 #加速係数
M = 21                                      #反復回数
eps = 0.0000001                             #収束判定値
    
x = SOR(N,A,y,omega,eps)

    
input("Plz push enter key.")