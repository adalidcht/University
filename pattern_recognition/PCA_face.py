# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 10:29:20 2022

@author: adalc
"""

from skimage import io
import matplotlib.pyplot as plt
import numpy as np

#::::::::::::Cagar imagenes::::::::::::#
def cargar_foto(numper,numfoto): #Número de personas, número de fotos
    BDF = np.zeros((12000,(numper*numfoto))) #Base de datos | Modificar 12000 = filas
    for persona in range(numper):
        for foto in range(numfoto):
            root = 'S' + str(persona + 1) + '/' + 'F' + str(foto + 1) + '.jpg' #Abre las carpetas | S1..S5 F1 ... F6
            pic = np.ravel(io.imread(root)) #np.ravel Coloca las columnas en un solo vector columna como tensor | np.flatten hace lo mismo pero como matriz
            BDF[:,((numper*foto) + (persona))] = pic #P1: c0,c5,c10,... mezcla de fotos en las columnas
    return BDF

#::::::::::::::::::::::::::::::::::::::#

numper = 5
numfoto = 6
BD1 = cargar_foto(numper,numfoto)
unos = np.ones((1,BD1.shape[1])) #vector fila 1x(numper*numfoto) (30)
unos = unos.astype('float32')
media = np.array([np.mean(BD1, axis = 1)]) #Vector de 12000x1
BDPprom = BD1 - (media.T * unos) #BD1 - media(12000x30)

#:::::::::::::::PCA::::::::::::::::::::#

MC = np.dot((BDPprom.T),BDPprom) #Base de datos cuadrada, Multiplicación matriz con matriz |Es invertible
[EV,EF] = np.linalg.eig(MC) #EV eigenvalores, EF eigenvectores
RE = np.dot(BDPprom,EF) #Vectores de la base de datos
Pp = 25 #Patrones principales
MR = np.array(RE[:,:-(1 + Pp):-1]) #Último hasta el 24 [-1] | Matriz compacta esencial

#::::::::::::::::::::::::::::::::::::::#
sign = np.zeros((BD1.shape[1],Pp)) #signature
for i in range(0,BD1.shape[1]):
    sign[i,:] = np.dot(BDPprom[:,i].T,MR) #Cada renglón, esencial de cada foto

#:::::::::::::::::Prueba:::::::::::::::#
A = np.int(numper*np.random.random(1)) #Aleatoriia, iamgen de referencia
IPA = io.imread('S' + str(A + 1) + '/F7.jpg')
FA = np.ravel(IPA)
prom = FA - media

plt.subplot(1,2,1)
plt.imshow(np.reshape(FA,[120,100]),cmap = 'gray')
plt.title('Buscando a...')

salida = np.dot(prom,MR)
MS = np.zeros(BD1.shape[1]) #Martriz de salida
plt.subplot(1,2,2)
for i in range(BD1.shape[1]):   #Distancia euclidiana
    MS[i] = np.linalg.norm(sign[i,:] - salida) #Norma
    if(np.remainder(i,2) == 0): #RULETA
        plt.imshow(np.reshape(BD1[:,1],[120,100]),cmap = 'gray')
        plt.show(bloc = False)
        plt.pause(0.01)
C = np.argmin(MS) #DETERMINACIÓN
        

         
    

