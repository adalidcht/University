# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 18:16:33 2022

@author: adalc
"""

import numpy as np 
import matplotlib.pyplot as plt 
import scipy.stats as stats
import statistics as sts
from scipy.stats import multivariate_normal
from pylab import figure
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from skimage.color import rgb2hsv
from skimage import io,color

plt.close('all')

persona1 = io.imread('piel1.jpg')
persona2 = io.imread('piel2.jpg')

hsv1 = color.rgb2hsv(persona1)
hsv2 = color.rgb2hsv(persona2)

hue1 = hsv1[:,:,0]
hue2 = hsv2[:,:,0]
sat1 = hsv1[:,:,1]
sat2 = hsv2[:,:,1]

sample = int(input('Muestras a tomar: '))

fig,axs = plt.subplots(1,2,squeeze = False) 
fig.suptitle('Personas para muestras')
axs[0,0].imshow(persona1)
axs[0,1].imshow(persona2)

fig,axs = plt.subplots(1,2,squeeze = False) 
fig.suptitle('Persona 1')
axs[0,0].imshow(hue1)
axs[0,0].set_title('Hue')
axs[0,1].imshow(sat1)
axs[0,1].set_title('Saturation')

print('Seleccione las muestras de Hue')
sample_h1 = np.int32(plt.ginput(sample))
print('Seleccione las muestras de Saturation') 
sample_s1 = np.int32(plt.ginput(sample))

fig,axs = plt.subplots(1,2,squeeze = False) 
fig.suptitle('Persona 2')
axs[0,0].imshow(hue2)
axs[0,0].set_title('Hue')
axs[0,1].imshow(sat2)
axs[0,1].set_title('Saturation')

print('Seleccione las muestras de Hue')
sample_h2 = np.int32(plt.ginput(sample))
print('Seleccione las muestras de Saturation') 
sample_s2 = np.int32(plt.ginput(sample))


valor_h1 = hue1[sample_h1[:,1],sample_h1[:,0]]
valor_h2 = hue2[sample_h2[:,1],sample_h2[:,0]]
valor_s1 = sat1[sample_s1[:,1],sample_s1[:,0]]
valor_s2 = sat2[sample_s2[:,1],sample_s2[:,0]]

#Promedios
prom_intermedioh = (valor_h1+valor_h2)/2
prom_intermedios = (valor_s1+valor_s2)/2
promedio_h = sum(prom_intermedioh)/sample
promedio_s = sum(prom_intermedios)/sample

#Varianza
var_h = np.var(prom_intermedioh)
var_s = np.var(prom_intermedios)

#Desviación estándar
st_dev_h = sts.pstdev(prom_intermedioh) #Manual si no funciona
st_dev_s = sts.pstdev(prom_intermedios)

#Creación de objetos

norm_pruebah1 = stats.norm(promedio_h,0.04)
norm_pruebas1 = stats.norm(promedio_s,0.4)
norm_pruebah2 = stats.norm(promedio_h,0.0004)
norm_pruebas2 = stats.norm(promedio_s,0.004)
normh = stats.norm(promedio_h,st_dev_h)
norms = stats.norm(promedio_s,st_dev_s)

xhp1 = np.linspace(norm_pruebah1.ppf(0.01),norm_pruebah1.ppf(0.99), 100)
xsp1 = np.linspace(norm_pruebas1.ppf(0.01),norm_pruebas1.ppf(0.99), 100)
xhp2 = np.linspace(norm_pruebah2.ppf(0.01),norm_pruebah2.ppf(0.99), 100)
xsp2 = np.linspace(norm_pruebas2.ppf(0.01),norm_pruebas2.ppf(0.99), 100)

xh = np.linspace(normh.ppf(0.01),normh.ppf(0.99), 100)
xs = np.linspace(norms.ppf(0.01),norms.ppf(0.99), 100)
#Gráficas de la Función de Densidad de Probabilidad
plt.figure(4)
plt.plot(xh,normh.pdf(xh),'-b',lw = 5,alpha = 0.6)

plt.plot(xs,norms.pdf(xs),'-g',lw = 5,alpha = 0.6)

plt.plot(xh,normh.pdf(xhp1),'-r',lw = 5,alpha = 0.6)

plt.plot(xs,norms.pdf(xsp1),'-c',lw = 5,alpha = 0.6)

plt.plot(xh,normh.pdf(xhp2),'-m',lw = 5,alpha = 0.6)

plt.plot(xs,norms.pdf(xsp2),'-y',lw = 5,alpha = 0.6)
plt.legend(['Hue','Saturation','Hp1','Sp1','Hp2','Sp2'])

#Límites para las decisiones
# limh_inf = promedio_h - st_dev_h
# lims_inf = promedio_s - st_dev_s
# limh_sup = promedio_h + st_dev_h
# lims_sup = promedio_s + st_dev_s

piel1 = np.zeros((persona1.shape[0],persona1.shape[1]))
piel2 = np.zeros((persona2.shape[0],persona2.shape[1]))

#Decisión de piel
for i in range(persona1.shape[0]):
    for j in range(persona1.shape[1]):
        # if hsv1[i,j,0] > limh_inf and hsv1[i,j,0] < limh_sup and hsv1[i,j,1] > lims_inf and hsv1[i,j,1] < lims_sup:
        if hsv1[i,j,0] > min(prom_intermedioh) and hsv1[i,j,0] < max(prom_intermedioh) and hsv1[i,j,1] > min(prom_intermedios) and hsv1[i,j,1] < max(prom_intermedios):
            piel1[i,j] = 1
        
for i in range(persona2.shape[0]):
    for j in range(persona2.shape[1]):
        # if hsv2[i,j,0] > limh_inf and hsv2[i,j,0] < limh_sup and hsv2[i,j,1] > lims_inf and hsv2[i,j,1] < lims_sup:
        if hsv2[i,j,0] > min(prom_intermedioh) and hsv2[i,j,0] < max(prom_intermedioh) and hsv2[i,j,1] > min(prom_intermedios) and hsv2[i,j,1] < max(prom_intermedios):
            piel2[i,j] = 1

#Figuras de la piel reconocida
plt.figure(5)
plt.imshow(piel1, cmap = 'gray')

plt.figure(6)
plt.imshow(piel2, cmap = 'gray')

plt.show()


#Create grid and multivariate normal

X,Y = np.meshgrid(xh,xs)
pos = np.dstack((X,Y))
# pos = np.empty(X.shape + (2,))
# pos[:, :, 0] = X; pos[:, :, 1] = Y
rv = multivariate_normal([promedio_h,promedio_s],[[var_h,0],[0,var_s]])

fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')
ax.plot_surface(X, Y, rv.pdf(pos),cmap
                ='viridis',linewidth=0)
ax.set_xlabel('Hue')
ax.set_ylabel('Saturation')
ax.set_zlabel('Z')
plt.show()








