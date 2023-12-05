#<================================ Primera parte ============================>#
#<=== Aquí manipulamos las imagenes

import os
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, transform

# Loading 
direccion = 'D:\\adalc\\Documents\\UPIITA\\7to semestre\\Reconocimiento de patrones\\Examen\\letras'

lista_archivos = os.listdir(direccion)
lista_archivos = lista_archivos[:10]

listado=[]
num_images=0

k = 0
base_datos01 = np.zeros((25*25, len(lista_archivos)))
for ii in lista_archivos:
    listado.append('D:\\adalc\\Documents\\UPIITA\\7to semestre\\Reconocimiento de patrones\\Examen\\letras\\'+ii)
    ima = io.imread(listado[-1])#color.rgb2gray( io.imread(listado[-1]) )
    ima = transform.resize(ima,[25,25])
    base_datos01[:,k] = np.ravel(ima)
    k += 1

plt.close('all')
plt.figure(0)
plt.imshow(np.reshape(base_datos01[:,1],[25,25]), cmap = 'gray')
plt.show()

#<================================ Segunda parte ============================>#
#<=== Aquí entrenamos el backpropagation
#<=== Arquitectura neuronal con 64 neuronas de entrada y 3 neuronas de salida

w1 = np.random.rand(3, 625) * 2 - 1
b1 = np.random.rand(3, 1)   * 2 - 1
# plt.figure(1)
# plt.imshow(np.reshape(w1[0,:],[25,25]), cmap='gray')

w2 = np.random.rand(625, 3) * 2 - 1
b2 = np.random.rand(625, 1) * 2 - 1

#target = np.diag(np.ones(base_datos01))
target = base_datos01

alpha = 0.001
aprendizaje = []
for j in range (1000): 
    suma = 0
    for i in range (target.shape[1]):
        a0 = base_datos01[:, i]
        a0 = a0[:, np.newaxis]
        n1 = w1@(a0) + b1
        a1 = 1 / (1 + np.exp(-n1))
        n2 = w2@(a1) + b2
        a2 = n2
        t  = target[:, i]
        t  = t[:, np.newaxis]
        e  = t - a2
        s2 = (-2)*1*e
        s1 = (np.diagflat((1-a1)*a1).dot(w2.T)).dot(s2)
        w2 = w2 - (alpha*s2*a1.T)
        b2 = b2 - (alpha*s2)
        w1 = w1 - (alpha*s1*a0.T)
        b1 = b1 - (alpha*s1)
        et = np.sum((np.sqrt(e**2))/625) #error cuadrático medio
        suma = suma + et
    aprendizaje.append(suma)

plt.figure()
plt.plot(aprendizaje)


#<================================ Tercera parte ============================>#
#<=== Se comprueba el entrenamiento el backpropagation

# Loading 
direccion = 'D:\\adalc\\Documents\\UPIITA\\7to semestre\\Reconocimiento de patrones\\Examen\\letras'

lista_archivos = os.listdir(direccion)
lista_archivos = lista_archivos[:10]

listado=[]
num_images=0

k = 0
base_datos02 = np.zeros((25*25, len(lista_archivos)))
for ii in lista_archivos:
    listado.append('D:\\adalc\\Documents\\UPIITA\\7to semestre\\Reconocimiento de patrones\\Examen\\letras\\'+ii)
    ima = io.imread(listado[-1])#color.rgb2gray( io.imread(listado[-1]) )
    ima = transform.resize(ima,[25,25])
    base_datos02[:,k] = np.ravel(ima)
    k += 1

salida = []
for i in range (target.shape[1]):
    a0 = base_datos02[:, i]
    a0 = a0[:, np.newaxis]
    n1 = w1@(a0) + b1
    a1 = 1 / (1 + np.exp(-n1))
    n2 = w2@(a1) + b2
    salida.append(n1)

# Import libraries
from mpl_toolkits import mplot3d
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

salida1 = np.array(salida)
for ii in range(2):
    ax.scatter( salida1[ii][0][0], salida1[ii][1][0], salida1[ii][2][0] )
    ax.text(    salida1[ii][0][0], salida1[ii][1][0], salida1[ii][2][0], ii )
    