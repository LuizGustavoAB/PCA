import pygame
from pygame.locals import *
pygame.init()

x = 400
y = 300
velocidade = 10


janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Caça Palavras')

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False


#teste utilizando o mouse
    #pygame.mouse.get_pos()
    #posX = pygame.mouse.get_pos()[0]
    #posY = pygame.mouse.get_pos()[1]
    #print(posX, posY)

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_RIGHT]:
        x += velocidade
    if comandos[pygame.K_LEFT]:
        x -= velocidade

    janela.fill((255, 255, 255))
    pygame.draw.circle(janela, (0, 255, 0), (x, y), 25)
    pygame.display.update()

pygame.quit()