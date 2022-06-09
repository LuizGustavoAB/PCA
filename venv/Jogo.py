import time
import pygame, sys
from pygame.locals import *
from sys import exit
pygame.init()

x = 125
y = 25
x2 = 125
y2 = 680
velocidade = 10
white = (255, 255, 255)
image = pygame.image.load(r'D:\Trabalhos_Unigranrio\PCA\cacapalavras.png')
image2 = pygame.image.load(r'D:\Trabalhos_Unigranrio\PCA\respostas.png')
image3 = pygame.image.load(r'D:\Trabalhos_Unigranrio\PCA\descrições.png')
display_surface = pygame.display.set_mode((800, 800))
display_surface2 = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Caça Palavras')


while True:


    #teste utilizando o mouse
    #pygame.mouse.get_pos()
    #posX = pygame.mouse.get_pos()[0]
    #posY = pygame.mouse.get_pos()[1]
    #print(posX, posY)
    for event in pygame.event.get():
       if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.display.init()
            display_surface.fill(white)
            display_surface.blit(image, (x, y))
            display_surface.blit(image2, (x2, y2))

    #teste utilizando as setas pra mover a bola
    #comandos = pygame.key.get_pressed()
    #if comandos[pygame.K_UP]:
    #    y -= velocidade
    #if comandos[pygame.K_DOWN]:
    #    y += velocidade
    #if comandos[pygame.K_RIGHT]:
    #    x += velocidade
    #if comandos[pygame.K_LEFT]:
    #    x -= velocidade


    #pygame.draw.circle(display_surface, (0, 255, 0), (x, y), 25)
            pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            display_surface2 = pygame.display.set_mode((800, 800))
            display_surface2.fill(white)
            display_surface.blit(image3, (x, y))
            pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

pygame.quit()