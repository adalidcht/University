# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 09:09:32 2023

@author: Eeduardo
"""
import matplotlib.pyplot as plt
import numpy as np
import random


gamma = 0.8 
recompensa = np.array([[-1,-1,-1,-1,0,-1],
                       [-1,-1,-1,0,-1,100],
                       [-1,-1,-1,0,-1,-1],
                       [-1,0,0,-1,0,-1],
                       [0,-1,-1,0,-1,100],
                       [-1,0,-1,-1,0,100]])
qmatrix = np.zeros(recompensa.shape)

tran_matrix = np.array([[-1,-1,-1,-1,4,-1],
                       [-1,-1,-1,3,-1,5],
                       [-1,-1,-1,3,-1,-1],
                       [-1,1,2,-1,4,-1],
                       [0,-1,-1,3,-1,5],
                       [-1,1,-1,-1,4,5]])

accion_matrix = [[4],[3,5],[3],[1,2,4],[0,3,5],[1,4,5]]

secuencia = []
for itera in range(100):
    estado_inicio = random.choice(list(range(0,recompensa.shape[0])))
    estado_actual = estado_inicio # numerbe from list
    secuencia.append(estado_inicio)
    
    while(estado_actual != 5):
        accion = random.choice(accion_matrix[estado_actual])
        estado_siguiente = tran_matrix[estado_actual][accion]
        recompensa_siguiente = []
        for accion_siguiente in accion_matrix[estado_siguiente]:
            recompensa_siguiente.append(qmatrix[estado_siguiente][accion_siguiente])
        qestado = recompensa[estado_actual][accion] + gamma*max(recompensa_siguiente)
        qmatrix[estado_actual][accion] = qestado      
        estado_actual = estado_siguiente
        print(qmatrix)
        print('===========')            
        print(estado_actual)
        if estado_actual == 5:
            print('meta alcanzada')    












                               
        
        
        