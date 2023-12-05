# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 09:10:12 2023

@author: adalc
"""

import numpy as np
import matplotlib.pyplot as plt
import random


plt.close('all')

gamma = 0.8
recompensa = np.array([[-1,-1,-1,-1,0,-1],
                       [-1,-1,-1,0,-1,100],
                       [-1,-1,-1,0,-1,-1],
                       [-1,0,0,-1,0,-1],
                       [0,-1,-1,0,-1,100],
                       [-1,0,-1,-1,0,1000]])
q_matrix = np.zeros(recompensa.shape)

#Lugares al que puede ir
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
    estado_actual = estado_inicio
    secuencia.append(estado_inicio)
    
    while(estado_actual != 5):
        accion = random.choice(accion_matrix[estado_actual])
        estado_siguiente = tran_matrix[estado_actual][accion]
        
        #Q(s1,a1),Q(s2,a2)... futuro
        recompensa_siguiente = []
        for accion_siguiente in accion_matrix[estado_siguiente]:
            recompensa_siguiente.append(q_matrix[estado_siguiente][accion_siguiente])
        
        #Ecuación Q
        q_estado = recompensa[estado_actual][accion] + gamma*max(recompensa_siguiente)
        q_matrix[estado_actual][accion] = q_estado #Memoria del ente
        
        estado_actual = estado_siguiente
        print(q_matrix,'\n')
        
        if estado_actual == 5:
            print('final')
            # recompensa_siguiente = []
            # for accion_siguiente in accion_matrix[estado_siguiente]:
            #     recompensa_siguiente.append(q_matrix[estado_siguiente][accion_siguiente])
            
            # #Ecuación Q
            # q_estado = recompensa[estado_actual][accion] + gamma*max(recompensa_siguiente)
            # q_matrix[estado_actual][accion] = q_estado #Memoria del ente
            # print('Meta')
            # print(q_matrix,'\n')
        
            








