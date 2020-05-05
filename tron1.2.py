import pygame, random
from pygame.locals import *
from time import sleep


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
pygame.init()#iniciando pygame
screen = pygame.display.set_mode((600, 600))#criando tamanho da tela
pygame.display.set_caption("Tron") #nome ta tela
screen.fill([8, 232, 235])

car = [(150, 150), (-10000, - 1000)]# lista da posição do carro
car_skin = pygame.Surface((10, 10)) #escolhendo o tamanho do carro(que no caso é um quadrado)
car_skin.fill((255, 0, 0)) #escolhendo a cor do carro

power_pos = ongrid_random() #poder possivelmente implementado futuramente
power = pygame.Surface((10, 10)) #tamanho dele
power.fill((255, 255, 255)) #sua cor


my_direction = 5 #direção que o carro começa a andar
clock = pygame.time.Clock() # isso serve para poder usar o clock ali em baixo
font = pygame.font.Font('freesansbold.ttf', 18)
font_start = pygame.font.Font('freesansbold.ttf', 30)
font_start2 = pygame.font.Font('freesansbold.ttf', 32)
fonte_coord = pygame.font.SysFont(pygame.font.get_default_font(), 100)
score = 0
game_over = False
start = False
time = False
while not game_over:
    clock.tick(10)#velociade do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        #direção onde o carro anda sem parar
        if event.type == KEYDOWN:
            if event.key == pygame.K_UP and my_direction != DOWN and move:
                my_direction = UP
                start = True
            if event.key == pygame.K_DOWN and my_direction != UP and move:
                my_direction = DOWN
                start = True
            if event.key == pygame.K_LEFT and my_direction != RIGHT and move:
                my_direction = LEFT
                start = True
            if event.key == pygame.K_RIGHT and my_direction != LEFT and move:
                my_direction = RIGHT
                start = True
            if event.key == pygame.K_KP_ENTER:
                time = True
                move = True


    if my_direction == UP:
        car[0] = (car[0][0], car[0][1] - 10)
    if my_direction == DOWN:
        car[0] = (car[0][0], car[0][1] + 10)

    if my_direction == RIGHT:
        car[0] = (car[0][0] + 10, car[0][1])
    if my_direction == LEFT:
        car[0] = (car[0][0] - 10, car[0][1])



    if collision(car[0], power_pos) and start:
        power_pos = ongrid_random()
        car.append((0, 0))
        score = score + 1

    # Check if snake collided with boundaries
    if car[0][0] == 600 or car[0][1] == 600 or car[0][0] < 0 or car[0][1] < 0:
        game_over = True
        break
    # Check if the snake has hit itself
    for i in range(1, len(car) - 1):
        if car[0][0] == car[i][0] and car[0][1] == car[i][1] and start:
            game_over = True
            break

    if game_over:
        break

    for c in range(len(car) - 1, 0, -1):
        car[c] = (car[c - 1][0], car[c - 1][1])


    screen.fill((7, 8, 14))#atualiza a tela pintando td de preto
    screen.blit(power, power_pos)
    '''for x in range(0, 600, 10):  # Draw vertical lines
        pygame.draw.line(screen, (8, 232, 235), (x, 0), (x, 600))
    for y in range(0, 600, 10):  # Draw vertical lines
        pygame.draw.line(screen, (8, 232, 235), (0, y), (600, y))'''
    if not start:
        screen.blit(font_start.render('APERTE ENTER PARA COMEÇAR', True, (255, 255, 255)), (50, 250))
    if time:
        pygame.draw.rect(screen, ([7, 8, 14]), [50, 240, 510, 50])
        for pos in car:
            screen.blit(car_skin, pos)
        pygame.display.update()
        sleep(1)
        screen.blit(fonte_coord.render('3', True, (255, 255, 255)), (290, 230))
        for pos in car:
            screen.blit(car_skin, pos)
        pygame.display.update()
        sleep(1)
        pygame.draw.rect(screen, ([7, 8, 14]), [240, 230, 120, 70])

        screen.blit(fonte_coord.render('2', True, (255, 255, 255)), (290, 230))
        for pos in car:
            screen.blit(car_skin, pos)
        pygame.display.update()
        sleep(1)
        pygame.draw.rect(screen, ([7, 8, 14]), [240, 230, 120, 70])

        screen.blit(fonte_coord.render('1', True, (255, 255, 255)), (290, 230))
        for pos in car:
            screen.blit(car_skin, pos)
        pygame.display.update()
        sleep(1)
        pygame.draw.rect(screen, ([7, 8, 14]), [240, 230, 120, 70])
        time = False
        start = True


    score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)

    for pos in car:
        screen.blit(car_skin, pos)


    pygame.display.update()
while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 44, 1))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (300, 220)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()





