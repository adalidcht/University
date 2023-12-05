# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 10:50:28 2022

@author: adalc
"""

import matplotlib.pyplot as plt
import numpy as np

#AND

#Neurona
def Delta_Rule_Log_Sigmoid(Weight, Pattern, Target, Alpha, bias):
    for i in range(len(Pattern)):
        x = Pattern[:,i] #x = p
        x = x[:,np.newaxis]
        n = Weight@x + bias #@ Multiplicación matricial
        out = 1/(1+np.exp(-n)) #Función
        DerF = out*(1 - out) #Derviada de la función
        error = Target[i] - out
        Delta = DerF*error # Deltab
        DeltaW = Alpha*Delta*x#.T Transpuesto
        Weight = Weight + DeltaW
        bias = bias + Delta
        
    return Weight,bias
        
        