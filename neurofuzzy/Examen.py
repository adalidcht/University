# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 08:55:30 2022

@author: adalc
"""
import numpy as np
import scipy.io.wavfile as waves
import matplotlib.pyplot as plt
import scipy.fftpack as fourier
import os
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.proj3d import proj_transform
from matplotlib.patches import FancyArrowPatch
from math import log

#-------------------------------------------------------#
#FUNCION GRAFICA PLANO 3D
def plano3d(intx,inty, intz):
    puntos = [[ float(intx), 0 , 0 ],[ 0 ,  float(inty), 0],[ 0 , 0 , float(intz)]]
    punto0,punto1,punto2 = puntos 
    
    Ax,Ay,Az = punto0
    Bx,By,Bz = punto1
    Cx,Cy,Cz = punto2
    
    ABx,ABy,ABz = [Bx-Ax,By-Ay,Bz-Az]
    ACx,ACy,ACz = [Cx-Ax,Cy-Ay,Cz-Az]
    ABcruzAC = [ABy*ACz - ABz*ACy,ABz*ACx - ABx*ACz,ABx*ACy - ABy*ACx]
    
    punto = np.array(punto0)
    vectorNormal = np.array(ABcruzAC) 
    d = -punto.dot(vectorNormal)
    
    xx,yy = np.meshgrid(range(0,6),range(0,6))
    z = (-vectorNormal[0]*xx - vectorNormal[1]*yy-d)*1./vectorNormal[2]
    return xx,yy,z

#Métodos para flecha 3D
class Arrow3D(FancyArrowPatch):

    def __init__(self, x, y, z, dx, dy, dz, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._xyz = (x, y, z)
        self._dxdydz = (dx, dy, dz)

    def draw(self, renderer):
        x1, y1, z1 = self._xyz
        dx, dy, dz = self._dxdydz
        x2, y2, z2 = (x1 + dx, y1 + dy, z1 + dz)

        xs, ys, zs = proj_transform((x1, x2), (y1, y2), (z1, z2), self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        super().draw(renderer)
        
    def do_3d_projection(self, renderer=None):
        x1, y1, z1 = self._xyz
        dx, dy, dz = self._dxdydz
        x2, y2, z2 = (x1 + dx, y1 + dy, z1 + dz)

        xs, ys, zs = proj_transform((x1, x2), (y1, y2), (z1, z2), self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))

        return np.min(zs) 
    
def _arrow3D(ax, x, y, z, dx, dy, dz, *args, **kwargs):
    '''Add an 3d arrow to an `Axes3D` instance.'''

    arrow = Arrow3D(x, y, z, dx, dy, dz, *args, **kwargs)
    ax.add_artist(arrow)

setattr(Axes3D, 'arrow3D', _arrow3D)
#-------------------------------------------------------#

#Entropia de Shannon
def EntropiaShannon(Audios):
    H = 0
    for i in range(len(Audios[:360])):
        H -= Audios[i]*log(1/Audios[i])/1e9
        
    H1 = 0
    for i in range(360,len(Audios[:1115])):
        H1 -= Audios[i]*log(1/Audios[i])/1e9
        
    H2 = 0
    for i in range(1115,len(Audios[:1607])):
        H2 -= Audios[i]*log(1/Audios[i])/1e9
    return[H,H1,H2]

def grafico(intx1,inty1,intz1,intx2,inty2,intz2):
    xx1,yy1,z1 = plano3d(intx1,inty1,intz1)
    xx2,yy2,z2 = plano3d(intx2,inty2,intz2)
    
    ax1.plot_surface(xx1,yy1,z1,alpha = 0.5,color = 'lightcoral')
    ax1.plot_surface(xx2,yy2,z2,alpha = 0.5,color = 'gold')
    
    ax1.arrow3D(3,3,3,W[0,0],W[0,1],W[0,2],mutation_scale = 20,fc = 'lightcoral')
    
    ax1.arrow3D(3,3,3,W[1,0],W[1,1],W[1,2],mutation_scale = 20,fc='gold')
    
    ax1.set_xlim(0.5,5.5)
    ax1.set_ylim(0.5,5.5)
    ax1.set_zlim(0,8)
    
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_zlabel('z')

#%%

plt.close('all')
direccion = 'D:\\adalc\\Documents\\UPIITA\\7to semestre\\Control neurodifuso\\Audios'

lista_archivos = os.listdir(direccion)
lista_archivos = lista_archivos[:]

lista_archivos = np.delete(lista_archivos,10,0).tolist()
listado=[]
num_images=0

data = [] 
fs = []
audio = []
spec = []
entropy = []
freq = []


#%%
plt.figure()
for i in range(len(lista_archivos)):
    fs.append(waves.read(lista_archivos[i])[0])
    data.append(waves.read(lista_archivos[i])[1])
    audio.append(data[i][:,0])
    
    L = len(audio[i])
    T = 1/fs[i]
    
    spec.append(np.abs(fourier.fft(audio[i]))[:L//2])
    freq.append(fourier.rfftfreq(L//2,T)[:L//2])
    plt.plot(freq[i], spec[i])

    entropy.append(EntropiaShannon(spec[i]))

plt.axvline(360,color = 'k')
plt.axvline(1115,color = 'k')
plt.axvline(1607,color = 'k')

fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')
for i in range(10):
    ax.scatter(entropy[i][0],entropy[i][1],entropy[i][2], color = 'r',marker = 'o')
    ax.scatter(entropy[i+10][0],entropy[i+10][1],entropy[i+10][2], color = 'b',marker = 'X')
    ax.scatter(entropy[i+20][0],entropy[i+20][1],entropy[i+20][2], color = 'g',marker = '^')
    
#%%

#Principal

T = []
for i in range(0,10,1):
    T.append(np.array([1,-1])[:, np.newaxis])
for i in range(10,20,1):
    T.append(np.array([1,1])[:, np.newaxis])
for i in range(20,30,1):
    T.append(np.array([-1,-1])[:, np.newaxis])

#variiables adaptativas
W = np.random.rand(2,3)
b = np.random.rand(2,1)

Epoca = 20000
a = np.array([0,0])

R = 0 #Correlación
for i in range(len(entropy)):
    R = R + 0.25*np.outer(entropy[i][:],np.transpose(entropy[i][:]))
    # print('Correlación\n',R)

eigenvalor,vector = np.linalg.eig(R)
landamax = max(eigenvalor)
alpha = 1/(4*landamax)*0.90

#Entrenamiento
for i in range(Epoca):
    for j in range(len(entropy)):
        a = np.dot(W,np.transpose(entropy[j][:]))[:, np.newaxis] + b
        e = np.float64(T[j] - a) #Error
        W = W + alpha*np.outer(e,(entropy[j][:]))
        b = b + alpha*e
    

intx1 = (-b[0,0])/W[0,0]/1.0e9
inty1 = (-b[0,0])/W[0,1]/1.0e9
intz1 = (-b[0,0])/W[0,2]/1.0e9

intx2 = (-b[1,0])/W[1,0]/1.0e9
inty2 = (-b[1,0])/W[1,1]/1.0e9
intz2 = (-b[1,0])/W[1,2]/1.0e9

#--------------------------------------------------------------------------------------
#Gráficas
fig = plt.figure()
ax1 = fig.add_subplot(111,projection = '3d')
for i in range(8):
    ax1.scatter(entropy[i][0],entropy[i][1],entropy[i][2], color = 'r',marker = 'o')
    ax1.scatter(entropy[i+10][0],entropy[i+10][1],entropy[i+10][2], color = 'b',marker = 'X')
    ax1.scatter(entropy[i+20][0],entropy[i+20][1],entropy[i+20][2], color = 'g',marker = '^')
    
grafico(intx1,inty1,intz1,intx2,inty2,intz2)
plt.title('Entrenamiento 80%')

#Gráficas
fig = plt.figure()
ax1 = fig.add_subplot(111,projection = '3d')
for i in range(8,10):
    ax1.scatter(entropy[i][0],entropy[i][1],entropy[i][2], color = 'r',marker = 'o')
    ax1.scatter(entropy[i+10][0],entropy[i+10][1],entropy[i+10][2], color = 'b',marker = 'X')
    ax1.scatter(entropy[i+20][0],entropy[i+20][1],entropy[i+20][2], color = 'g',marker = '^')
    
grafico(intx1,inty1,intz1,intx2,inty2,intz2)
plt.title('Validación 20%')

#Gráficas
fig = plt.figure()
ax1 = fig.add_subplot(111,projection = '3d')
for i in range(8):
    ax1.scatter(entropy[i][0],entropy[i][1],entropy[i][2], color = 'r',marker = '*')
    ax1.scatter(entropy[i+10][0],entropy[i+10][1],entropy[i+10][2], color = 'b',marker = '*')
    ax1.scatter(entropy[i+20][0],entropy[i+20][1],entropy[i+20][2], color = 'g',marker = '*')
for i in range(8,10):
    ax1.scatter(entropy[i][0],entropy[i][1],entropy[i][2], color = 'r',marker = 'o')
    ax1.scatter(entropy[i+10][0],entropy[i+10][1],entropy[i+10][2], color = 'b',marker = 'X')
    ax1.scatter(entropy[i+20][0],entropy[i+20][1],entropy[i+20][2], color = 'g',marker = '^')
    
grafico(intx1,inty1,intz1,intx2,inty2,intz2)
plt.title('Todos los datos 100%')



#----------------------------------------------------------------------
#Eficiencia 
erroneos = 0
for j in range(len(entropy)):
    ae = np.dot(W,np.transpose(entropy[j][:]))[:, np.newaxis] + b
    ae = np.where(ae<0,-1,1)
    error = T[j] - ae
    
    if (error[0] != 0 or error[1] != 0):
        erroneos = erroneos + 1

eficiencia = (30 - erroneos)*100/len(entropy)
print('La eficiencia es de \n',eficiencia,'%')
print('acertando en: ',30 - erroneos)


    
    
    
        
