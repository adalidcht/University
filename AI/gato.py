# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 21:21:33 2023

@author: adalc
"""

import pygame
import random
import time
import button
import tile
import bullet
import version



pygame.quit()
pygame.init()

#Create window
window_width = 500
window_height = 700
window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Vence a Skynet')


def draw_text(text,font,text_col,x,y,mode = 'free',width = window_width):
    img = font.render(text,True,text_col)
    if mode == 'center':
        pos_x = (width - img.get_width())//2
        #pos_y = (window_height - img.get_height())//2
        window.blit(img,(pos_x,y))
    else:
        window.blit(img,(x,y))
        
run = True
menu_state = 'main'

#Fonts
font = pygame.font.SysFont('Lucida Console',35)
#colour
text_col = (255,255,255)

start_game1 = button.Button("Skynet 1.0",125,300,170,50,window,'center')
start_game2 = button.Button("Skynet 2.0",125,360,170,50,window,'center')
exit_game = button.Button("Salir",125,600,170,50,window,'center')

state1 = True
state2 = True
state3 = True
state4 = True
state5 = True
state6 = True
state7 = True
state8 = True
state9 = True

Turno = int(random.random() * 2) + 1


#Game loop
while run == True:
    
    
    window.fill((52,78,91))
    draw_text('Vence a Skynet',font,text_col,40,20,'center')
    
    
    
    if menu_state == 'main':
        # if start_game1.draw(window):
        #     pass
        if start_game2.draw(window):
            menu_state = 'skynet_pre2'
        if exit_game.draw(window):
            run = False
            
    if menu_state == 'skynet_pre2':

        board = pygame.Rect(49,199,402,402)
        pygame.draw.rect(window,(255,255,255),board,4)
        pygame.draw.line(window,(255,255,255),(183,199),(183,600),4)
        pygame.draw.line(window,(255,255,255),(317,199),(317,600),4)
        pygame.draw.line(window,(255,255,255),(49,333),(450,333),4)
        pygame.draw.line(window,(255,255,255),(49,467),(450,467),4)
        
        start_sk = button.Button("Empezar",125,100,170,50,window,'center')
        
        if start_sk.draw(window):
            menu_state = 'skynet2'

    
    if menu_state == 'skynet2':
        board = pygame.Rect(49,199,402,402)
        tiles = tile.Tile()
        num = 0
        
        
        
        if Turno == 1:
            draw_text('Turno Humano',pygame.font.SysFont('Lucida Console',35),(255,178.5,178.5),40,60,'center')
        if Turno == 2:
            draw_text('Turno Skynet',pygame.font.SysFont('Lucida Console',35),(255,178.5,178.5),40,60,'center')
            game = version.Version()
            num = game.decide(Turno)
            print(num)
            
        
        
        if tiles.draw(window,53,203,state1) or num == 1:
            state1 = False
            if Turno == 1:
                Turno = 2
            else:
                Turno = 1
        if tiles.draw(window,53 + 133,203,state2 or num == 2):
            state2 = False
            if Turno == 1:
                Turno = 2
            else:
                Turno = 1
        if tiles.draw(window,53 + 133 * 2,203,state3 or num == 3):
            state3 = False
            if Turno == 1:
                Turno = 2
            else:
                Turno = 1
        if tiles.draw(window,53,203 + 133,state4 or num == 4):
            state4 = False
            if Turno == 1:
                Turno = 2
            else:
                Turno = 1
        if tiles.draw(window,53 + 133,203 + 133,state5 or num == 5):
            state5 = False
            if Turno == 1:
                Turno = 2
            else:
                Turno = 1
        if tiles.draw(window,53 + 133 * 2,203 + 133,state6 or num == 6):
            state6 = False
            if Turno == 1:
                Turno = 2
            else:
                Turno = 1
        if tiles.draw(window,53,203 + 133 * 2,state7 or num == 7):
            state7 = False
            if Turno == 1:
                Turno = 2
            else:
                Turno = 1
        if tiles.draw(window,53 + 133,203 + 132 * 2,state8 or num == 8):
            state8 = False
            if Turno == 1:
                Turno = 2
            else:
                Turno = 1
        if tiles.draw(window,53 + 133 * 2,203 + 133 * 2,state9 or num == 9):
            state9 = False
            if Turno == 1:
                Turno = 2
            else:
                Turno = 1

        
        if state1 == False:
            pygame.draw.rect(window,(52,78,91),(53,203,128,128))
            bullet.Bullet(window,53,203,Turno)
        if state2 == False:
            pygame.draw.rect(window,(52,78,91),(53 + 133,203,128,128))
            bullet.Bullet(window,53 + 133,203,Turno)
        if state3 == False:
            pygame.draw.rect(window,(52,78,91),(53 + 133 * 2,203,128,128))
            bullet.Bullet(window,53 + 133 * 2,203,Turno)
        if state4 == False:
            pygame.draw.rect(window,(52,78,91),(53,203 + 133,128,128))
            bullet.Bullet(window,53,203 + 133,Turno)
        if state5 == False:
            pygame.draw.rect(window,(52,78,91),(53 + 133,203 + 133,128,128))
            bullet.Bullet(window,53 + 133,203 + 133,Turno)
        if state6 == False:
            pygame.draw.rect(window,(52,78,91),(53 + 133 * 2,203 + 133,128,128))
            bullet.Bullet(window,53 + 133 * 2,203 + 133,Turno)
        if state7 == False:
            pygame.draw.rect(window,(52,78,91),(53,203 + 133 * 2,128,128))
            bullet.Bullet(window,53,203 + 133 * 2,Turno)
        if state8 == False:
            pygame.draw.rect(window,(52,78,91),(53 + 133,203 + 132 * 2,128,128))
            bullet.Bullet(window,53 + 133,203 + 132 * 2,Turno)
        if state9 == False:
            pygame.draw.rect(window,(52,78,91),(53 + 133 * 2,203 + 133 * 2,128,128))
            bullet.Bullet(window,53 + 133 * 2,203 + 133 * 2,Turno)
            
            
            
        
        pygame.draw.rect(window,(255,255,255),board,4)
        pygame.draw.line(window,(255,255,255),(183,199),(183,600),4)
        pygame.draw.line(window,(255,255,255),(317,199),(317,600),4)
        pygame.draw.line(window,(255,255,255),(49,333),(450,333),4)
        pygame.draw.line(window,(255,255,255),(49,467),(450,467),4)
        
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #Cerrar la ventana
            run = False
    
    # Actualizar la ventana
    pygame.display.update()
    

pygame.quit()





