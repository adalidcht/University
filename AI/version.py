# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 17:51:19 2023

@author: adalc
"""
import pygame
import numpy as np
import random

def draw_text(text,font,text_col,x,y,width = 500):
            img = font.render(text,True,text_col)
            window = pygame.display.set_mode((500,700))
            pos_x = (width - img.get_width())//2
            window.blit(img,(pos_x,y))

def click_Tabla(self,num,Turno):
    self.Tabla[:,num] = Turno
    

            
class Version:      
    def __init__(self):
        self.Sec = np.arange(1,10)[:,np.newaxis].T
        self.Tabla = np.zeros((1,9))
    
    
    
    def decide(self,Turno,state):
        if Turno == 1:
            num = state
            self.Tabla[:,num] = Turno
        if Turno == 2:
            num = 0;
            i = 1; 
            j = 2; 
            while num == 0:
                if i == 1:
                    s = [1,2,3]
                elif i == 2:
                    s = [4,5,6]
                elif i == 3:
                    s = [7,8,9]
                elif i == 4:
                    s = [1,4,7]
                elif i == 5:
                    s = [2,5,8]
                elif i == 6:
                    s = [3,6,9]
                elif i == 7:
                    s = [1,5,9]
                elif i == 8:
                    s = [3,5,7]
                elif i == 9 and j == 2:
                    j = 1
                    i = 1
                elif i == 9 and j == 1:
                    num = self.Sec[:,int(random.random() * self.Sec.shape[1])]
                
                if self.Tabla[:,s[0]] == j and self.Tabla[:,s[1]] == j and self.Tabla[:,s[2]] == 0:
                    num = s[2]
                elif self.Tabla[:,s[0]] == j and self.Tabla[:,s[1]] == 0 and self.Tabla[:,s[2]] == j:
                    num = s[1]
                elif self.Tabla[:,s[0]] == 0 and self.Tabla[:,s[1]] == j and self.Tabla[:,s[2]] == j:
                    num = s[0]
                    
                i = i + 1;
        click_Tabla(num,Turno)
        return int(num)
        

    
            
            

    
    
    
