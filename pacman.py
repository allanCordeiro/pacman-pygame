import pygame

pygame.init()
# constantes
AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
RAIO = 20
VELOCIDADE = 1
tela = pygame.display.set_mode((640, 480), 0)
x = 10
y = 10
vel_x = VELOCIDADE
vel_y = VELOCIDADE
while True:
    #regras
    x += vel_x
    y += vel_y
    if x + RAIO > 640:
        vel_x = -VELOCIDADE
    if x - RAIO < 0:
        vel_x = VELOCIDADE
    if y + RAIO > 480:
        vel_y = -VELOCIDADE
    if y - RAIO < 0:
        vel_y = VELOCIDADE
    #desenho
    tela.fill(PRETO)
    pygame.display.update()
    pygame.draw.circle(tela, AMARELO, (int(x), int(y)), RAIO, 0)
    pygame.display.update()
    #eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()


