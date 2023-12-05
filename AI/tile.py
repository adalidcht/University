# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 23:42:43 2023

@author: adalc
"""
import pygame

class Tile():
    def __init__(self,width = 128,height = 128):
        self.width = width
        self.height = height
        self.clicked = False
    
        
    
    
    def draw(self,surface,x,y,state):
        action = False
        
        if state == True:
            self.tile = pygame.Rect(x,y,self.width,self.height)
            pygame.draw.rect(surface,(45,70,80),self.tile)
            
            #get mouse position
            pos = pygame.mouse.get_pos()
            #check mouseover and clicked conditions
            if self.tile.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            pass
                
        return action
        