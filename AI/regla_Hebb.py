# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 09:16:57 2023

@author: adalc
"""

import numpy as np
import matplotlib.pyplot as plt

def hardlimit(n):
    if (n > 0):
        a = 1
    else:
        a = 0
    return a
    
P0 = 0; W0 = 1 # Parámetros no condicionados
P1 = 1; W1 = 0 # Parámetros condicionados
b = -0.5 #Polarización
alpha = 0.1 #Razón de aprendizaje
gamma = 0.1

plt.ion()
for q in range(250):
    n = (W0*P0) + (W1*P1) + b
    a = hardlimit(n)
    if (q > 150):
        P0 = 0
        P1 = 0
    elif (q > 40):
        P0 = 0
        P1 = 1    
    elif (q > 30):
        P0 = 1
        P1 = 1
    elif (q > 20):
        P0 = 0
        P1 = 1
    elif (q > 10):
        P0 = 1
        P1 = 0
    
    #W1 = W1 + (alpha*a*P1)
    W1 = W1 + (alpha*a*P1) - gamma*W1 #Decaemiento
    
    plt.plot(q,W1,'*')
    plt.pause(0.3)
    
plt.ioff()
    
        
 

            