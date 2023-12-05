# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 22:10:29 2023

@author: adalc
"""

import pygame

#Button class
class Button():
    def __init__(self,text,x,y,width,height,window,mode = 'free'):
        self.text = text
        self.width = width
        self.height = height
        if mode == 'center':
            pos_x = (window.get_width() - width)//2
            self.rect = pygame.Rect(pos_x,y,width,height)
        else:
            self.rect = pygame.Rect(x,y,width,height)
        
        self.clicked = False
    
    def draw(self,surface):
        action = False
        font = pygame.font.SysFont('Lucida Console', 24)
        text = font.render(self.text, True, (255,255,255))
        text_rect = text.get_rect(center = self.rect.center)
        
        #draw button on window
        pygame.draw.rect(surface,(45,70,80),self.rect,border_radius = 5)
        pygame.draw.rect(surface,(255,255,255),self.rect,1,5)
        
        
        surface.blit(text,text_rect)
        
        #get mouse position
        pos = pygame.mouse.get_pos()
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            
        return action
    


