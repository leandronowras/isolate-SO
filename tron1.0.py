import pygame, random
from pygame.locals import *


def ongrid_random():
    #Criando lugar aleatorio para o poder em um espaço na tela multiplo de 10
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    #colisão
    return (c1[0] == c2[0] and (c1[1] == c2[1]))

#criando variaveis para cada direção
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
test = 0
pygame.init()#iniciando pygame
screen = pygame.display.set_mode((600, 600))#criando tamanho da tela
pygame.display.set_caption("Tron") #nome ta tela

car = [(200, 200), (210, 200), (220, 200)]# lista da posição do carro
car_skin = pygame.Surface((9, 9)) #escolhendo o tamanho do carro(que no caso é um quadrado)
car_skin.fill((255, 0, 0)) #escolhendo a cor do carro

power_pos = ongrid_random() #poder possivelmente implementado futuramente
power = pygame.Surface((10, 10)) #tamanho dele
power.fill((255, 255, 255)) #sua cor


my_direction = 5 #direção que o carro começa a andar
clock = pygame.time.Clock() # isso serve para poder usar o clock ali em baixo

while True:
    clock.tick(15)#velociade do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        #direção onde o carro anda sem parar
        if event.type == KEYDOWN:
            if event.key == pygame.K_UP:
                my_direction = UP
            if event.key == pygame.K_DOWN:
                my_direction = DOWN
            if event.key == pygame.K_LEFT:
                my_direction = LEFT
            if event.key == pygame.K_RIGHT:
                my_direction = RIGHT
            if event.key == pygame.K_KP_ENTER:
                my_direction = LEFT


    if my_direction == UP:
        car[0] = (car[0][0], car[0][1] - 10)
        car.append((-20, -20))
        #print(car)  #ative esse printe caso queira saber exatamente os valores que estão indo na lista de posição para desenhar o carro
    if my_direction == DOWN:
        car[0] = (car[0][0], car[0][1] + 10)
        car.append((-20, -20))
    if my_direction == RIGHT:
        car[0] = (car[0][0] + 10, car[0][1])
        car.append((-20, -20))
    if my_direction == LEFT:
        car[0] = (car[0][0] - 10, car[0][1])
        car.append((-20, -20))


    if collision(car[0], power_pos):
        power_pos = ongrid_random()
        car.append((0, 0))
    for c in range(len(car) - 1, 0, -1):
        car[c] = (car[c - 1][0], car[c - 1][1])








    screen.fill((0, 0, 0))#atualiza a tela pintando td de preto
    screen.blit(power, power_pos)#desenha o poder
    for pos in car:
        screen.blit(car_skin, pos)#desenha o carro




    pygame.display.update()





