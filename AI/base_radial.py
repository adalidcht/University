# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 09:29:55 2023

@author: adalc
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

plt.close('all')

puntos = 50
x = np.linspace(-5,5,puntos).reshape(1,-1)
y = 2 * np.cos(x) + np.sin(3 * x) + 5

plt.figure(0)
plt.plot(x,y,'o-r')

#%%
#------------Primera capa (no supervisado)----------
neuronas = 30
model = KMeans(n_clusters = neuronas)
model.fit(x.T)
clases = model.cluster_centers_
print(clases)

sigma = (max(clases) - min(clases))/np.sqrt(2 * neuronas)
sigma = sigma[0]

W1 = np.zeros((puntos,neuronas))

for i in range(puntos):
    for j in range(neuronas):
        distancia = np.linalg.norm(x[0,i] - clases[j],2)
        W1[i,j] = np.exp((-1/(sigma ** 2)) * distancia ** 2)


#------------Segunda capa (Supervisado)----------

W2 = np.dot(np.linalg.pinv(W1),y.T) #Pseudoinversa

#------------------------------------------------
Puntos = 200
x_new = np.linspace(-5,5,Puntos).reshape(1,-1)
g = np.zeros((Puntos,neuronas))

for i in range(Puntos):
    for j in range(neuronas):
        distancia = np.linalg.norm(x_new[0,i] - clases[j],2)
        g[i,j] = np.exp((-1/(sigma**2)) * distancia**2)



y_new = np.dot(g,W2)

plt.plot(x_new.T,y_new)
        
        
        
        


