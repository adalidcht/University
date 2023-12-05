# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 16:57:11 2023

@author: adalc
"""

import pygame

class Bullet:
    def __init__(self,window,window_width,window_height,gun):
        pos_x = window_width + 64
        pos_y = window_height + 64
        if gun == 2:
            circle_pos = (pos_x,pos_y) # posición del círculo
            circle_radius = 50 # radio del círculo
            pygame.draw.circle(window,(255,255,255),circle_pos,circle_radius,8)
        if gun == 1:
            line_thickness = 8
            pygame.draw.line(window,(255,255,255),(window_width + 20,window_height + 20),(pos_x + 44,pos_y + 44),line_thickness)
            pygame.draw.line(window,(255,255,255),(window_width + 108,window_height + 20),(pos_x - 44,pos_y + 44),line_thickness)
            