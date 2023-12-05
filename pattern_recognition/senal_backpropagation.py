# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 10:20:22 2022

@author: adalc
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import io


def pureline(n):
    a = 1*n
    return a

def sigmoide(n):
    a = 1/(1 + np.exp(-n))
    return a


plt.close('all')

senal1 = io.loadmat('senal_Total.mat')
senal2 = io.loadmat('complejo.mat')
patron = senal2['ECG']
maximo = np.max(np.abs(patron[170:240]))
patron = patron[170:240]/maximo


plt.figure()
plt.plot(patron)

#punto de inflexión por neurona
N1 = 200
W1 = np.random.rand(N1,1)*2-1 #valores de -1 a 1
b1 = np.random.rand(N1,1)*2-1

W2 = np.random.rand(1,N1)*2-1
b2 = np.random.rand(1,1)*2-1

alpha = 0.001
#pat = np.array([-2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0])
#target = 1 + np.sin((np.pi/4)*pat)
pat = np.zeros(24)
patron = np.zeros(24)

for i in range(0,70,3):
    pat[i] = i
    target.append(patron[i])


for j in range(3000):
    for i in range(len(pat)):
        #Forward propagation
        a0 = pat[i]
        n1 = W1.dot(a0) + b1
        a1 = sigmoide(n1)
        n2 = W2.dot(a1) + b2
        a2 = pureline(n2)
        error = target[i] - a2
        
        #Backpropagation
        df2 = 1
        s2 = (-2)*df2*error
        df1 = np.diagflat(np.multiply((1 - a1),(a1)))
        s1 = (df1.dot(W2.T)).dot(s2)
        
        #Update
        W1 = W1 - (alpha*s1*a0.T)
        b1 = b1 - (alpha*s1)
        W2 = W2 - (alpha*s2*a1.T)
        b2 = b2 - (alpha*s2)
        
        
x = np.arange(0,70,1)
# y =  1 + np.sin((np.pi/4)*x)
sal2 = np.zeros(np.size(x))

for ii in range(len(x)):
    a0 = x[ii]
    n1 = W1.dot(a0) + b1
    a1 = sigmoide(n1)
    n2 = W2.dot(a1) + b2
    sal2[ii] = pureline(n2)
    
plt.figure()
# plt.plot(x,y)
plt.plot(x,target)
plt.plot(x,sal2)

    
    
    
        
        
        




