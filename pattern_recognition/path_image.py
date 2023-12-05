# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 10:41:24 2022

@author: adalc
"""

import matplotlib.pyplot as plt
import numpy as np
import os
from skimage import io,color
from skimage.transform import rescale,resize,downscale_local_mean

path = 'Dirección carpeta'
path_list = os.listdir(path) #Listado de objetos de la carpeta
#path_list = path_list[1:3] #Selecciona los requeridos

img_list = []
num_img = []

for i in path_list():
    img_list.append('Dirección capeta' + i)
    
    
    
    gray = color.rgb2gray(io.imread(img_list[-1]))
    final = resize(gray,[25,25])
    
    


