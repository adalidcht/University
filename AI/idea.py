# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 21:13:52 2023

@author: adalc
"""

import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Definir dimensiones de la pantalla
ANCHO_PANTALLA = 500
ALTO_PANTALLA = 500

# Crear pantalla
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Tic Tac Toe")

# Definir fuente
fuente = pygame.font.SysFont(None, 40)

# Función para mostrar mensaje en la pantalla
def mostrar_mensaje(mensaje, color):
    texto = fuente.render(mensaje, True, color)
    pantalla.blit(texto, (ANCHO_PANTALLA/2 - texto.get_width()/2, ALTO_PANTALLA/2 - texto.get_height()/2))

# Función para dibujar el tablero de Tic Tac Toe
def dibujar_tablero():
    # Dibujar líneas horizontales
    pygame.draw.line(pantalla, BLANCO, (0, ALTO_PANTALLA/3), (ANCHO_PANTALLA, ALTO_PANTALLA/3), 5)
    pygame.draw.line(pantalla, BLANCO, (0, 2*ALTO_PANTALLA/3), (ANCHO_PANTALLA, 2*ALTO_PANTALLA/3), 5)
    # Dibujar líneas verticales
    pygame.draw.line(pantalla, BLANCO, (ANCHO_PANTALLA/3, 0), (ANCHO_PANTALLA/3, ALTO_PANTALLA), 5)
    pygame.draw.line(pantalla, BLANCO, (2*ANCHO_PANTALLA/3, 0), (2*ANCHO_PANTALLA/3, ALTO_PANTALLA), 5)

# Función para dibujar la X o el O en una posición específica del tablero
def dibujar_simbolo(fila, columna, simbolo):
    x = columna * ANCHO_PANTALLA/3 + ANCHO_PANTALLA/6
    y = fila * ALTO_PANTALLA/3 + ALTO_PANTALLA/6
    if simbolo == 'X':
        pygame.draw.line(pantalla, ROJO, (x-ALTO_PANTALLA/6, y-ALTO_PANTALLA/6), (x+ALTO_PANTALLA/6, y+ALTO_PANTALLA/6), 5)
        pygame.draw.line(pantalla, ROJO, (x-ALTO_PANTALLA/6, y+ALTO_PANTALLA/6), (x+ALTO_PANTALLA/6, y-ALTO_PANTALLA/6), 5)
    elif simbolo == 'O':
        pygame.draw.circle(pantalla, ROJO, (int(x), int(y)), int(ALTO_PANTALLA/6), 5)

# Función para verificar si un jugador ha ganado
def verificar_ganador(tablero, jugador):
    # Verificar filas
    for fila in range(3):
        if tablero[fila][0] == jugador and tablero[fila][1] == jugador and tablero[fila][2] == jugador:
            return True

    # Verificar columnas
    for columna in range(3):
        if tablero[0][columna] == jugador and tablero[1][columna] == jugador and tablero[2][columna] == jugador:
            return True

    # Verificar diagonal principal
    if tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador:
        return True

    # Verificar diagonal secundaria
    if tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador:
        return True

    # Si no hay ganador, devolver False
    return False

# Función para reiniciar el juego
def reiniciar_juego():
    # Crear un nuevo tablero vacío
    tablero = [['', '', ''], ['', '', ''], ['', '', '']]
    # Iniciar jugando con X
    jugador_actual = 'X'
    # Devolver el tablero y el jugador actual
    return tablero, jugador_actual

# Función para dibujar el menú
def dibujar_menu():
    # Crear botones
    boton_jugar = pygame.Rect(ANCHO_PANTALLA/2-75, 200, 150, 50)
    boton_salir = pygame.Rect(ANCHO_PANTALLA/2-75, 300, 150, 50)
    # Dibujar botones
    pygame.draw.rect(pantalla, BLANCO, boton_jugar)
    pygame.draw.rect(pantalla, BLANCO, boton_salir)
    # Dibujar texto en botones
    texto_jugar = fuente.render("Jugar", True, NEGRO)
    texto_salir = fuente.render("Salir", True, NEGRO)
    pantalla.blit(texto_jugar, (ANCHO_PANTALLA/2 - texto_jugar.get_width()/2, 215))
    pantalla.blit(texto_salir, (ANCHO_PANTALLA/2 - texto_salir.get_width()/2, 315))

def dibujar_x(fila, columna):
    # Dibujar una X en la celda especificada
    x = columna * 200 + 100
    y = fila * 200 + 100
    pygame.draw.line(pantalla, (0, 0, 0), (x - 50, y - 50), (x + 50, y + 50), 5)
    pygame.draw.line(pantalla, (0, 0, 0), (x + 50, y - 50), (x - 50, y + 50), 5)

def dibujar_o(fila, columna):
    # Dibujar un círculo en la celda especificada
    x = columna * 200 + 100
    y = fila * 200 + 100
    pygame.draw.circle(pantalla, (0, 0, 0), (x, y), 50, 5)

def boton_jugar():
    # Dibujar el botón de Jugar
    boton = pygame.Rect(150, 450, 300, 100)
    pygame.draw.rect(pantalla, (0, 255, 0), boton, 5)

    # Escribir el texto en el botón de Jugar
    texto = fuente.render("Jugar", True, (0, 0, 0))
    x = 150 + (300 - texto.get_width()) / 2
    y = 450 + (100 - texto.get_height()) / 2
    pantalla.blit(texto, (x, y))

    # Devolver el rectángulo del botón de Jugar
    return boton

def dibujar_tablero(tablero):
    # Dibujar el tablero en la pantalla
    for fila in range(3):
        for columna in range(3):
            cuadrado = pygame.Rect(columna * 200, fila * 200, 200, 200)
            pygame.draw.rect(pantalla, (255, 255, 255), cuadrado, 5)

            if tablero[fila][columna] == 'X':
                dibujar_x(fila, columna)
            elif tablero[fila][columna] == 'O':
                dibujar_o(fila, columna)

def hay_ganador(tablero, jugador):
    # Verificar si hay un ganador en el tablero para el jugador especificado
    for i in range(3):
        if tablero[i][0] == jugador and tablero[i][1] == jugador and tablero[i][2] == jugador:
            return True
        if tablero[0][i] == jugador and tablero[1][i] == jugador and tablero[2][i] == jugador:
            return True
    if tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador:
        return True
    if tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador:
        return True
    return False

def mostrar_mensaje(mensaje1, mensaje2):
    # Mostrar un mensaje en la pantalla
    pantalla.fill(BLANCO)
    texto1 = fuente.render(mensaje1, True, NEGRO)
    texto2 = fuente.render(mensaje2, True, NEGRO)
    pantalla.blit(texto1, (ANCHO_PANTALLA/2 - texto1.get_width()/2, 200))
    pantalla.blit(texto2, (ANCHO_PANTALLA/2 - texto2.get_width()/2, 300))
    pygame.display.update()
    pygame.time.wait(3000)
    
    
def boton_salir():
    # Dibujar el botón de Salir
    boton = pygame.Rect(400, 450, 150, 100)
    pygame.draw.rect(pantalla, (255, 0, 0), boton, 5)

    # Escribir el texto en el botón de Salir
    texto = fuente.render("Salir", True, (0, 0, 0))
    x = 400 + (150 - texto.get_width()) / 2
    y = 450 + (100 - texto.get_height()) / 2
    pantalla.blit(texto, (x, y))

    # Devolver el rectángulo del botón de Salir
    return boton

def boton_reiniciar():
    # Dibujar el botón de Reiniciar
    boton = pygame.Rect(225, 450, 150, 100)
    pygame.draw.rect(pantalla, (0, 0, 255), boton, 5)

    # Escribir el texto en el botón de Reiniciar
    texto = fuente.render("Reiniciar", True, (0, 0, 0))
    x = 225 + (150 - texto.get_width()) / 2
    y = 450 + (100 - texto.get_height()) / 2
    pantalla.blit(texto, (x, y))

    # Devolver el rectángulo del botón de Reiniciar
    return boton

def dibujar_sim(fila, columna, jugador):
    x = columna * 200 + 100
    y = fila * 200 + 100

    if jugador == 1:
        pygame.draw.line(pantalla, (0, 0, 0), (x - 75, y - 75), (x + 75, y + 75), 10)
        pygame.draw.line(pantalla, (0, 0, 0), (x + 75, y - 75), (x - 75, y + 75), 10)
    else:
        pygame.draw.circle(pantalla, (0, 0, 0), (x, y), 75, 10)

def dibujar_menu():
    # Dibujar los botones en el menú principal
    pantalla.fill(BLANCO)
    texto_titulo = fuente.render("Tic Tac Toe", True, NEGRO)
    pantalla.blit(texto_titulo, (ANCHO_PANTALLA/2 - texto_titulo.get_width()/2, 100))

    boton_un_jugador = pygame.Rect

# Función principal del juego
def jugar_tic_tac_toe():
    # Iniciar juego
    juego_terminado = False
    jugando_menu = True
    tablero, jugador_actual = reiniciar_juego()

    # Bucle del juego
    while not juego_terminado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Si se hace clic en el botón de salir, salir del juego
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if jugando_menu:
                    if boton_jugar.collidepoint(event.pos):
                        jugando_menu = False
                    elif boton_salir.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                else:
                    # Verificar si se hizo clic en una casilla del tablero
                    x, y = event.pos
                    fila = int(y / (ALTO_PANTALLA/3))
                    columna = int(x / (ANCHO_PANTALLA/3))
                    if tablero[fila][columna] == '':
                        # Dibujar X o O en la casilla
                        dibujar_sim
                        if jugador_actual == 'X':
                            dibujar_x(fila, columna)
                            tablero[fila][columna] = 'X'
                            if hay_ganador(tablero, 'X'):
                                mostrar_mensaje("¡Ganaste!", "Haz clic en 'Reiniciar' para jugar de nuevo.")
                                jugando_menu = True
                            else:
                                jugador_actual = 'O'
                        else:
                            dibujar_o(fila, columna)
                            tablero[fila][columna] = 'O'
                            if hay_ganador(tablero, 'O'):
                                mostrar_mensaje("¡Perdiste!", "Haz clic en 'Reiniciar' para jugar de nuevo.")
                                jugando_menu = True
                            else:
                                jugador_actual = 'X'

            # Si se hace clic en el botón de reiniciar, reiniciar el juego
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if boton_reiniciar.collidepoint(event.pos):
                    tablero, jugador_actual = reiniciar_juego()

        # Dibujar el tablero
        dibujar_tablero(tablero)

        if jugando_menu:
            # Dibujar el menú
            dibujar_menu()
        else:
            # Dibujar botón de reiniciar
            boton_reiniciar = pygame.Rect(ANCHO_PANTALLA/2-75, 450, 150, 50)
            pygame.draw.rect(pantalla, BLANCO, boton_reiniciar)
            texto_reiniciar = fuente.render("Reiniciar", True, NEGRO)
            pantalla.blit(texto_reiniciar, (ANCHO_PANTALLA/2 - texto_reiniciar.get_width()/2, 465))

        pygame.display.update()
        reloj.tick(60)





# Iniciar pygame
pygame.init()

# Definir constantes
ANCHO_PANTALLA = 600
ALTO_PANTALLA = 600
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Crear la pantalla
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Tic Tac Toe")

# Crear fuente
fuente = pygame.font.SysFont(None, 36)

# Crear reloj
reloj = pygame.time.Clock()

# Iniciar el juego
jugar_tic_tac_toe()

# Salir de pygame
pygame.quit()
sys.exit()
    
    