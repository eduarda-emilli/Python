# Faça um programa em Python que abra e reproduza o aúdio de um arquivo MP3

import pygame

# Inicializando o mixer PyGame
pygame.mixer.init()

# Inicializando o PyGame
pygame.init()

pygame.mixer.music.load('exercicios/mundo_01/ex021.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
