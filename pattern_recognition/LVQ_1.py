# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 20:04:34 2022

@author: tomas
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from skimage import io,data
from mpl_toolkits import mplot3d


#-----------------------------------------------------------------------------#
#En esta sección cargamos la imagen y obtenemos sus medidas
imagen = io.imread('ImagenSintetica.jpg')
plt.figure(0)
plt.imshow(imagen)

filas = imagen.shape[0] #número de filas
columnas = imagen.shape[1] #número de columnas
capas = imagen.shape[2] #número de capas

#-----------------------------------------------------------------------------#
#::PREPROCESAMIENTO DE LOS PIXELES::#

#Este ciclo for introduce todos los pixeles de la imagen en un array de numpy

pixeles = []
for i in range(0,filas,1):
    for j in range(0,columnas,1):
        pixel = imagen[i,j,:]
        pixeles.append(pixel)

new_pixeles = np.array(pixeles,dtype=np.float32) 

#Ya que no es posible trabajar
#matemáticamente con datos de tipo uint, convertimos cada pixel a tipo float
#agregándolos ahora a una lista, colocando primero cada elemento de cada pixel
#en un vector auxiliar, para después concatenar ese vector auxiliar en la lista

#lista de todos los pixeles
#convertimos el array de numpy a lista
good_pixeles = [] 
for elemento in new_pixeles:
    aux = []
    for j in range(len(elemento)):
        aux.append(elemento[j])
        good_pixeles.append(aux)
        
#Una vez creada la lista de pixeles, realizaremos una nueva lista, pero que no
#contenga pixeles repetidos. Esto acortará el número de datos, así como 
#evitará que se generen demasiadas clases "ruido".

work_pixeles = []
 
for elemento in good_pixeles:
    if elemento not in work_pixeles:
        work_pixeles.append(elemento)

#-----------------------------------------------------------------------------#
#::PROCESAMIENTO DE LOS DATOS::#

clases = [] 

for i in range(0,len(work_pixeles),1): 
    pix = work_pixeles[i]
    if len(clases) == 0:
        clases.append(pix)
    else:
        down_umbral = []
        distancias = []
        for k in range(len(clases)):
            d0 = np.sqrt((clases[k][0]-pixel[0])**2
                         +(clases[k][1]-pixel[1])**2
                         +(clases[k][2]-pixel[2])**2)
            umbral = 330.5
            if d0 <= umbral:
                down_umbral.append(clases[k])
                distancias.append(d0)
        if len(down_umbral) == 0:
            clases.append(pix)
        else:
            posicion_minimo = distancias.index(min(distancias))
            aux = [pix,down_umbral[posicion_minimo]]
            prom = np.mean(aux,axis=0)
            for h in range(len(clases)):
                if (clases[h][0] == down_umbral[posicion_minimo][0] 
                    and clases[h][1] == down_umbral[posicion_minimo][1] 
                    and clases[h][2] == down_umbral[posicion_minimo][2]): 
                    clases[h] = prom
                else:
                    continue

#El proceso es el siguiente: Primero declaramos los ciclos que barrerán toda
#la matriz de datos, se revisa si la lista de clases esta vacía, y se agrega
#el primer pixel. Cuando la lista de clases ya cuenta con un elemento, inicia
#la comparación de los datos. Se generan dos vectores: "down_umbral" y 
#"distancias", los cuales se vacían al cambiar el pixel en comparación. 
#Se recorre la lista de clases, sacando distancia euclidiana de cada una de
#estas al pixel en turno; si alguna distancia resulta menor al umbral 
#seleccionado, esta se agrega al vector "distancia", asi como la clase que con
#la que se comparó el pixel, teniendo entonces que el vector "down_umbral" y el
#vector "distancias deben tener siempre la misma longitud en el instante de 
#comparación. Si durante el recorrido de comparaciones no existió ninguna 
#distancia menor al umbral, la longitud del vector "down_umbral" sera entonces
#igual a cero, y se agregará ese pixel a la lista de clases. Si sucede que el 
#vector "down_umbral" si tiene elementos, entonces ese pixel forma parte de
#alguna clase ya encontrada anteriormente, por lo cual entonces obtenemos la
#posición de la mínima distancia, para saber que clase generó este mínimo y asi
#sacar el promedio entre esta y el pixel comparado. El promedio se sustituye
#donde se encuentre la clase dentro de la lista de clases. 

#-----------------------------------------------------------------------------#
#::LIMPIEZA DE LAS CLASES::#

# Debido al proceso anterior, es posible que la sustitución del promedio suceda 
# en más de un lugar dentro de la lista de clases, además de que nuevamente 
# debemos convertir el arreglo de numpy a una lista con la que se pueda operar.

new_clases = np.array(clases,dtype = np.float32)
centros = []
good_clases = [] #lista de todos los pixeles
for elemento in new_clases: #convertimos el array de numpy a lista
    aux = []
    for j in range(len(elemento)):
        aux.append(elemento[j])
        good_clases.append(aux) #agregamos cada elmemento a una lista
        
#Por último, eliminamos las clases repetidas, y las agregamos al vector
# "centros". Su longitud será igual al número de clases que haya arrojado
# el programa        
        
# for elemento in good_clases:
#     if elemento not in centros:
#         centros.append(elemento)        
print(f"Con umbral de {umbral} aparecen {len(clases)} clases")
        


        
    
    
            


      
              
                    



                
            
            
        
                    
                
            
        
        
        
 


            
                 
                
            
            

        
        
        
            
        
        

