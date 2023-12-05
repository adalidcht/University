# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 08:43:27 2023

@author: adalc
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from sklearn import datasets
from yellowbrick.cluster import KElbowVisualizer
from sklearn.cluster import KMeans

plt.close('all')
#----Funciones
def cmeans(x,K,V,iters):
    # V = x[np.random.choice(range(len(x)),K,replace = False)]
    n = len(x) #datos
    car = x.shape[1]
    dist = np.zeros((K,n)) 
    
    
    for epocas in range(1000):
        for i in range(K): 
            for k in range(n):
                suma = 0.00000001
                for j in range(car):
                    suma = ((x[k,j] - V[i,j])**2) + suma
                dist[i,k] = suma
        
        #Pertenencia
        m = 2
        U = np.zeros((K,n))
            
        for i in range(K):
            for k in range(n):
                suma1 = 0
                for j in range(K):
                    suma1 = (dist[i,k]/dist[j,k])**(2/(m - 1)) + suma1
                U[i,k] = 1/suma1
        
        #actualización centroides
        for i in range(K):
            for j in range(car):
                suma2 = 0
                suma3 = 0.0000001
                for k in range(n):
                    suma2 = (U[i,k]**m * x[k,j]) + suma2
                    suma3 = (U[i,k]**m) + suma3
                V[i,j] = suma2/suma3
        
    print('Clases c-means:',len(V))  
    return U,V      
        
def kmeans(X,K,V,iters):
    # Inicializar los centroides aleatoriamente
    # V = X[np.random.choice(range(len(X)),K,replace = False)]
    
    for i in range(iters):
        # Calcular las distancias entre cada punto y los centroides
        distances = np.sqrt(((X - V[:, np.newaxis])**2).sum(axis = 2))
        
        # Asignar cada punto al centroide más cercano
        U = np.argmin(distances,axis = 0)
        
        # Actualizar los centroides como el promedio de los puntos asignados a cada uno
        V = np.array([X[U == k].mean(axis = 0) for k in range(K)])
        
    print('Clases k-means:',len(V)) 
    
    return U,V,distances

def metodo_codo(X,iters):
    sse1 = []
    sse2 = [] #Suma de errores cuadráticos
    for k in range(1, 11):
        V = X[np.random.choice(range(len(X)),k,replace = False)]
        U1,V1 = cmeans(X,k,V,iters)
        U2,V2 = kmeans(X,k,V,iters)
        sse1.append(np.sum((X - V1[np.argmin(U1,axis = 0)]) ** 2))
        sse2.append(np.sum((X - V2[U2]) ** 2))
    # Encontrar el punto de inflexión de la curva
    print(sse1)
    print(sse2)
    peaks1, _ = find_peaks(-np.diff(sse1),prominence = 1)
    peaks2, _ = find_peaks(-np.diff(sse2),prominence = 1)
    print(peaks1)
    print(peaks2)
    inflection_point1 = peaks1[0] + 1
    inflection_point2 = peaks2[0] + 1
        
    plt.plot(range(1, 11),sse1,marker = 'o',label = 'FCM')
    plt.plot(range(1, 11),sse2,marker = 'o',label = 'k-means')
    plt.plot(inflection_point1, sse1[inflection_point1 - 1],'ro',label = 'FCM elbow Point')
    plt.plot(inflection_point2, sse2[inflection_point2 - 1],'bo',label = 'k-means elbow Point')
    plt.title('Método del codo')
    plt.xlabel('Número de clusters')
    plt.ylabel('Suma de errores cuadráticos')
    plt.legend()

# def entropy(data):
#     # Calcular la frecuencia de cada clase
#     _, counts = np.unique(data, return_counts=True)
#     # Calcular la probabilidad de cada clase
#     p = counts / len(data)
#     # Calcular la entropía del conjunto de datos
#     entropy = -np.sum(p * np.log2(p))
#     return entropy

# def entropy_error(data, subsets):
#     # Calcular la entropía del conjunto de datos completo
#     data_entropy = entropy(data)
#     # Calcular la entropía ponderada de cada subconjunto de datos
#     weighted_entropy = sum(len(subset) / len(data) * entropy(subset) for subset in subsets)
#     # Restar la entropía ponderada de cada subconjunto de datos de la entropía del conjunto de datos completo para obtener el error de entropía
#     entropy_error = data_entropy - weighted_entropy
#     return entropy_error

# def entropy_error(V,U):
    
#     n_instances = len(U)
#     n_V = len(V)
#     classes = np.unique(U)
#     n_classes = len(classes)

#     # Calcular la frecuencia de cada clase en el conjunto de datos
#     freq_classes = np.zeros(n_classes)
#     for i in range(n_classes):
#         freq_classes[i] = np.sum(U == classes[i])

#     # Calcular la probabilidad de cada clase en el conjunto de datos
#     prob_classes = freq_classes / n_instances

#     # Calcular la entropía del conjunto de datos
#     entropy = -np.sum(prob_classes * np.log2(prob_classes))

#     # Calcular la entropía de cada clúster y sumarlas para obtener el error por entropía
#     cluster_entropy_sum = 0
#     for c in range(n_V):
#         # Calcular la frecuencia de cada clase en el clúster
#         freq_cluster_classes = np.zeros(n_classes)
#         for i in range(n_classes):
#             freq_cluster_classes[i] = np.sum(U[V[c]] == classes[i])

#         # Calcular la probabilidad de cada clase en el clúster
#         prob_cluster_classes = freq_cluster_classes / len(V[c])

#         # Calcular la entropía del clúster
#         cluster_entropy = -np.sum(prob_cluster_classes * np.log2(prob_cluster_classes))

#         # Sumar la entropía del clúster al error por entropía
#         cluster_entropy_sum += len(V[c]) * cluster_entropy

#     # Normalizar el error por entropía
#     entropy_error = 1 - cluster_entropy_sum / (n_instances * entropy)

#     return entropy_error

def error_entropia(U,c):
    suma1 = np.sum(U,axis = 0)
    u = np.sum(suma1)
    entropy = (-u*np.log2(u))/(U.shape[1] - c)
    return entropy

def entropy_error(labels, predicted_labels):
    predicted_labels = np.argmin(predicted_labels,axis = 0)
    n = len(np.unique(labels))
    k = len(np.unique(predicted_labels))
    H = 0
    for i in range(k):
        p_i = np.sum(predicted_labels == i) / n
        if p_i > 0:
            H -= p_i * np.sum(labels[predicted_labels == i] * np.log(labels[predicted_labels == i]))
    return H

def DistEu(dato,centros):
    distancia = []
    clases = len(centros)
    suma = 0
    for i in range(clases):
        suma = ((dato - centros[i])**2) + suma
        distancia.append(np.sqrt(suma))
    return distancia


def lvq(x,umbral):
    clases = 0
    centros = []
    for i in range(x.shape[0]):
        if (clases == 0):
            centros.append(x[i,:])
            clases = clases + 1
        dato = x[i,:]
        dis = DistEu(dato,centros)
        if (np.min(dis) >= umbral):
            # centros[dis.index(np.min(dis))] = (centros[dis.index(np.min(dis))] + dato)/2
            dis = DistEu(dato,centros)
            centros.append(dato)
            min_idx = np.where(dis == np.min(dis))[0][0]
            centros[min_idx] = (centros[min_idx] + dato)/2
            clases = clases + 1
    return centros
#----------------------------------------------------------------------------

iris = datasets.load_iris()
x = iris.data #dato de la flor #150
y = iris.target #tipo de flor #3
labels = np.zeros((150,1))
labels[50:100] = 1
labels[100:150] = 2


k = 3 #cluster
iteraciones = 1000

centroids = x[np.random.choice(range(len(x)),k,replace = False)]

U1,V1 = cmeans(x,k,centroids,iteraciones)
# print(V1)

U2,V2,U_d = kmeans(x,k,centroids,iteraciones)
# print(V2)

# metodo_codo(x,iteraciones)

# #Método del codo con sklearn
# plt.figure()
# km = KMeans(random_state=42)
# visualizer = KElbowVisualizer(km,k=(2,11))
# visualizer.fit(x)        # Fit the data to the visualizer
# visualizer.show()        # Finalize and render the figure

# e1 = entropy_error(V1, U1)
# e2 = entropy_error(V2, U2)

# e1 = error_entropia(U1,k)
# e2 = error_entropia(U_d,k)

# e1 = entropy_error(labels,U1)
# e2 = entropy_error(labels,U2)

# print('La entropía para Fuzzy c-means es: ',e1)
# print('La entropía para k-means es: ',e2)


cent = lvq(x,0.8)
print('LVQ clases:', len(cent))







# fig = plt.figure()
# ax = fig.add_subplot(111, projection = '3d')
# ax.scatter(x[0:49,0], x[0:49,1], x[0:49,2], c = 'b', marker = 'o')
# ax.scatter(x[50:99,0], x[50:99,1], x[50:99,2], c = 'g', marker = 'o')
# ax.scatter(x[100:149,0], x[100:149,1], x[100:149,2], c = 'k', marker = 'o')
# ax.scatter(V1[0,0], V1[0,1], V1[0,2], marker = 'P', c = 'r', s = 200, label = 'Clase 1')
# ax.scatter(V1[1,0], V1[1,1], V1[1,2], marker = '*', c = 'r', s = 200, label = 'Clase 2')
# ax.scatter(V1[2,0], V1[2,1], V1[2,2], marker = 'd', c = 'r', s = 200, label = 'Clase 3')
# ax.set_xlabel('Largo del sépalo')
# ax.set_ylabel('Ancho del sépalo')
# ax.set_zlabel('Largo del pétalo')
# ax.set_title('Fuzzy c-means')        
# ax.legend()   

# fig = plt.figure()
# ax = fig.add_subplot(111, projection = '3d')
# ax.scatter(x[0:49,0], x[0:49,1], x[0:49,2], c = 'b', marker = 'o')
# ax.scatter(x[50:99,0], x[50:99,1], x[50:99,2], c = 'g', marker = 'o')
# ax.scatter(x[100:149,0], x[100:149,1], x[100:149,2], c = 'k', marker = 'o')
# ax.scatter(V2[0,0], V2[0,1], V2[0,2], marker = 'P', c = 'r', s = 200, label = 'Clase 1')
# ax.scatter(V2[1,0], V2[1,1], V2[1,2], marker = '*', c = 'r', s = 200, label = 'Clase 2')
# ax.scatter(V2[2,0], V2[2,1], V2[2,2], marker = 'd', c = 'r', s = 200, label = 'Clase 3')
# ax.set_xlabel('Largo del sépalo')
# ax.set_ylabel('Ancho del sépalo')
# ax.set_zlabel('Largo del pétalo')
# ax.set_title('k-means')        
# ax.legend()   

        





