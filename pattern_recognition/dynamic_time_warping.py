# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 10:21:00 2022

@author: adalc
"""
import numpy as np


#Dynamic Time Warping
#Sakoe
#Shiva

senal1 = [0,0,1,1,0,0,-1,0,0,0,0]
senal2 = [0,0,0,0,1,1,0,0,0,-1,-0.5,0,0]

distancia = np.zeros((senal1.shpae[0],senal2.shape[0]))
for i in range(np.shape[0]):
    for j in range(senal2.shape[0]):
        distancia[i,j] = np.abs(A[i] - B[j])
        



