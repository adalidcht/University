# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 09:10:34 2023

@author: adalc
"""
    
from skimage import io, data, color
import numpy as np
import numpy.matlib
import matplotlib.pyplot as plt
#==================================================================#

plt.close('all')

nfil = 60 #60
ncol = 100 #100
nras = 3


som = np.random.rand(nfil, ncol, nras) #valor de neuronas

plt.ion()
# plt.figure(1)
# plt.subplot(1, 2, 1)
# plt.imshow(som)

# datos = np.random.rand(100, nras) #Entrada
ima = io.imread('simpson2.jpg')/255.0

plt.figure(1)
plt.imshow(ima)

x = int(input('Numero de muestras: '))
pos = np.int16(plt.ginput(x))

datos = ima[pos[:,1],pos[:,0],:]

plt.close(1)

plt.figure(2)
plt.subplot(1,2,1)
plt.imshow(ima)




x = np.linspace(0, 100, ncol) #100
y = np.linspace(0, 60, nfil) #60
x, y = np.meshgrid(x, y)

epocas = 10 #5 #Evolución
alpha0 = 0.5 #aprendizaje | debe cambiar epoca por epoca, rapido a lento
decay = 0.05 
sgm0 = 20 #vecindario original | campana, reducir el vecindario

for t in range(epocas):
    alpha = alpha0 * np.exp(-t * decay)
    sgm = sgm0 * np.exp(-t * decay)
    ven = np.ceil(sgm*3) #se reduce
   
    for i in range(len(datos)): #numero de veces que se presentan los datos
        vector = datos[i, :] #colores a aprender
        columna = som.reshape(nfil*ncol, 3) 
        d = 0
        for n in range(3):
            d = d + (vector[n]-columna[:, n])**2 #distancia euclidiana de las entradas y las neuronas
        DISTAN = np.sqrt(d)
        ind = np.argmin(DISTAN)
        bmfil, bmcol = np.unravel_index(ind, [nfil, ncol]) #encontrar la parte mas cercana en la matriz
        #ventana de actualización
        g = np.exp( -( ( (x-bmcol)**2) + ((y-bmfil)**2) ) / (2*sgm*sgm) ) 
        ffil = int( np.max( [0, bmfil-ven] ) )
        tfil = int( np.min( [bmfil+ven, nfil] ) )
        fcol = int( np.max( [0, bmcol-ven] ) )
        tcol = int( np.min( [bmcol+ven, ncol] ) )
        #vecindario y valores
        #Arregla el problema de las orillas
        vecindad = som[ffil:tfil, fcol:tcol, :]
        a, b, c = vecindad.shape
        T = np.ones(vecindad.shape)
        T[:,:,0] = T[:,:,0] * vector[0]
        T[:,:,1] = T[:,:,1] * vector[1]
        T[:,:,2] = T[:,:,2] * vector[2]
        # T = np.reshape(np.tile(vector, (1, a*b)), [a, b, nras])
       
        G = np.ones(vecindad.shape) #vecindario
        G[:,:,0] = g[ffil:tfil, fcol:tcol]
        G[:,:,1] = g[ffil:tfil, fcol:tcol]
        G[:,:,2] = g[ffil:tfil, fcol:tcol]
        # G = np.tile(g[ffil-1:tfil+2, fcol-1:tcol+2], [1, 1, 3])
       
        vecindad = vecindad + (alpha*G*(T-vecindad)) #ecuación de aprendizaje
       
        som[ffil:tfil, fcol:tcol, :] = vecindad 
        
        print('[',t,',',i,']','1')
        plt.subplot(1, 2, 2)
        plt.imshow(som)
        plt.pause(0.05)
        plt.show()

plt.title('Ya terminó')


imasal = io.imread('simpson1.jpg')/255.0
retina = np.zeros((imasal.shape))



for i in range(imasal.shape[0]):

    for j in range(imasal.shape[1]): #numero de veces que se presentan los datos
        pixel = imasal[i,j,:]
        columna = som.reshape(nfil*ncol,3)
        d = 0
        for n in range(3):
            d = d + (pixel[n]-columna[:, n])**2 #distancia euclidiana de las entradas y las neuronas
        DISTAN = np.sqrt(d)
        ind = np.argmin(DISTAN)
        bmfil, bmcol = np.unravel_index(ind, [nfil, ncol]) #encontrar la parte mas cercana en la matriz
        retina[i,j,:] = som[bmfil,bmcol,:]
        
        print('[',i,',',j,']','2')
        # plt.imshow(retina)
        # plt.pause(0.05)
        # plt.show()

plt.figure(3)
plt.subplot(1,2,1)
plt.imshow(retina)
plt.title('Coloreada')

plt.subplot(1,2,2)
plt.imshow(imasal)
plt.title('Original')
        
        
        
        
        
        