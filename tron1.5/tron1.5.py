import pygame, random, pygame_menu
from pygame.locals import *
from time import sleep
from pygame_menu import sound
from pygame import mixer


def start_the_game():
        def ongrid_random():
            # Criando lugar aleatorio para o poder em um espaço na tela multiplo de 10
            x = random.randint(0, 590)
            y = random.randint(0, 590)
            return ((x // 10 * 10), (y // 10 * 10))

        def collision(c1, c2):
            # colisão
            return (c1[0] == c2[0] and (c1[1] == c2[1]))

        def surprise_box(player, surprise):
            #surprise = random.randint(1, 2)
            engine = sound.Sound()
            if surprise == 0:#moeda
                if player == 1:
                    car.append((-10, -10))
                if player == 2:
                    car2.append((-10, -10))
                moeda_sound = mixer.Sound('coin_mario.wav')
                moeda_sound.play()
                #engine.set_sound('coin_mario.wav')
            if surprise == 1:#sonic
                if player == 1:
                    for c in range(1, 11):
                        car.append((-10, -10))
                if player == 2:
                    for c in range(1, 11):
                        car2.append((-10, -10))
                moeda_sound = mixer.Sound('fast_sound.wav')
                moeda_sound.play()
            if surprise == 2:#Mario
                if player == 1:
                    for c in range(1, 31):
                        car.append((-10, -10))
                if player == 2:
                    for c in range(1, 31):
                        car2.append((-10, -10))
                moeda_sound = mixer.Sound('powerup_mario.wav')
                moeda_sound.play()
                #mixer.music.load('coin_mario.wav')
            print(surprise)
            return 20

        # criando variaveis para cada direção
        UP = 0
        RIGHT = 1
        DOWN = 2
        LEFT = 3
        pygame.init()  # iniciando pygame
        screen = pygame.display.set_mode((600, 600))  # criando tamanho da tela
        pygame.display.set_caption("Tron")  # nome ta tela
        screen.fill([8, 232, 235])

        car = [(450, 150), (450, 150), (450, 150)]  # lista da posição do carro
        car_skin = pygame.Surface((10, 10))  # escolhendo o tamanho do carro(que no caso é um quadrado)
        car_skin.fill((255, 0, 0))  # escolhendo a cor do carro

        car2 = [(150, 150), (150, 150), (150, 150)]  # lista da posição do carro
        car2_skin = pygame.Surface((10, 10))  # escolhendo o tamanho do carro(que no caso é um quadrado)
        car2_skin.fill((0, 0, 255))  # escolhendo a cor do carro
        carspeed = 17

        power_pos = ongrid_random()  # poder possivelmente implementado futuramente
        power_pos1 = power_pos + (-10, -10)
        power = pygame.Surface((10, 10))  # tamanho dele
        power.fill((255, 255, 255))  # sua cor

        my_direction = 5  # direção que o carro começa a andar
        direction_player1 = 5
        direction_player2 = 5
        clock = pygame.time.Clock()  # isso serve para poder usar o clock ali em baixo
        font = pygame.font.Font('freesansbold.ttf', 18)
        font_start = pygame.font.Font('freesansbold.ttf', 30)
        font_start2 = pygame.font.Font('freesansbold.ttf', 32)
        fonte_coord = pygame.font.SysFont(pygame.font.get_default_font(), 100)
        box = pygame.image.load("cogumelo.png")
        box_form = pygame.transform.scale(box, (13, 13))
        score = 0
        game_over = False
        start = False
        time = False
        move = False
        empate = False
        game_over_player1 = False
        game_over_player2 = False
        escolha = 0
        while not game_over:
            clock.tick(carspeed)  # velociade do jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                # direção onde o carro anda sem parar
                if event.type == KEYDOWN:
                    if event.key == pygame.K_UP and direction_player1 != DOWN and move:
                        direction_player1 = UP
                        start = True
                    if event.key == pygame.K_DOWN and direction_player1 != UP and move:
                        direction_player1 = DOWN
                        start = True
                    if event.key == pygame.K_LEFT and direction_player1 != RIGHT and move:
                        direction_player1 = LEFT
                        start = True
                    if event.key == pygame.K_RIGHT and direction_player1 != LEFT and move:
                        direction_player1 = RIGHT
                        start = True

                    if event.key == pygame.K_w and direction_player2 != K_s and move:
                        direction_player2 = K_w
                        start = True
                    if event.key == pygame.K_s and direction_player2 != K_w and move:
                        direction_player2 = K_s
                        start = True
                    if event.key == pygame.K_a and direction_player2 != K_d and move:
                        direction_player2 = K_a
                        start = True
                    if event.key == pygame.K_d and direction_player2 != K_a and move:
                        direction_player2 = K_d
                        start = True

                    if event.key == pygame.K_KP_ENTER:
                        moeda_sound = mixer.Sound('select_002.ogg')
                        moeda_sound.play()
                        time = True
                        move = True

            if direction_player1 == UP:
                car[0] = (car[0][0], car[0][1] - 10)
            if direction_player1 == DOWN:
                car[0] = (car[0][0], car[0][1] + 10)
            if direction_player1 == RIGHT:
                car[0] = (car[0][0] + 10, car[0][1])
            if direction_player1 == LEFT:
                car[0] = (car[0][0] - 10, car[0][1])

            if direction_player2 == K_w:
                car2[0] = (car2[0][0], car2[0][1] - 10)
            if direction_player2 == K_s:
                car2[0] = (car2[0][0], car2[0][1] + 10)
            if direction_player2 == K_d:
                car2[0] = (car2[0][0] + 10, car2[0][1])
            if direction_player2 == K_a:
                car2[0] = (car2[0][0] - 10, car2[0][1])

            if collision(car[0], power_pos) or collision(car2[0], power_pos) and start:

                if collision(car[0], power_pos) and start:
                    power_pos = ongrid_random()
                    score = score + 1
                    surprise_box(1, escolha)

                if collision(car2[0], power_pos) and start:
                    power_pos = ongrid_random()
                    score = score + 1
                    surprise_box(2, escolha)
                print(escolha,"test1")
                escolha = random.randint(0, 2)
                if escolha2 == 1:
                    print(carspeed)
                    carspeed = carspeed + 5
                    print(carspeed,",,")
                print(escolha,"test2")

            if car[0][0] == 600 or car[0][1] == 600 or car[0][0] < 0 or car[0][1] < 0:
                if car[0][0] == 600:
                    car[0] = (car[0][0] - 600, car[0][1])
                if car[0][1] == 600:
                    car[0] = (car[0][0], car[0][1] - 600)
                if car[0][0] < 0:
                    car[0] = (car[0][0] + 600, car[0][1])
                if car[0][1] < 0:
                    car[0] = (car[0][0], car[0][1] + 600)
                #game_over = True
                #break
            if car2[0][0] == 600 or car2[0][1] == 600 or car2[0][0] < 0 or car2[0][1] < 0:
                if car2[0][0] == 600:
                    car2[0] = (car2[0][0] - 600, car2[0][1])
                if car2[0][1] == 600:
                    car2[0] = (car2[0][0], car2[0][1] - 600)
                if car2[0][0] < 0:
                    car2[0] = (car2[0][0] + 600, car2[0][1])
                if car2[0][1] < 0:
                    car2[0] = (car2[0][0], car2[0][1] + 600)
                #game_over = True
                #break
            # checando empate
            if collision(car[0], car2[0]):
                print('empate')
                empate = True
                game_over = True
                break

            for i in range(1, len(car) - 1):   #colisão entre player 1 em si mesmo
                if car[0][0] == car[i][0] and car[0][1] == car[i][1] and start:
                    game_over_player1 = True
                    game_over = True
                    break
            for i in range(1, len(car2) - 1):  # colisão entre player 2 em si mesmo
                if car2[0][0] == car2[i][0] and car2[0][1] == car2[i][1] and start:
                    game_over_player2 = True
                    game_over = True
                    break
            for i in range(1, len(car) - 1):    #colisão entre cabeça do player 2 com a player 1
                if collision(car2[0], car[i]) and start:
                    game_over_player2 = True
                    game_over = True
                    break
            for i in range(1, len(car2) - 1):    #colisão entre cabeça do player 1 com o player 2
                if collision(car[0], car2[i]) and start:
                    game_over_player1 = True
                    game_over = True
                    break



            if game_over:
                break

            for c in range(len(car) - 1, 0, -1):
                car[c] = (car[c - 1][0], car[c - 1][1])

            for c in range(len(car2) - 1, 0, -1):
                car2[c] = (car2[c - 1][0], car2[c - 1][1])

            screen.fill((7, 8, 14))  # atualiza a tela pintando td de preto

            if escolha == 0:
                box = pygame.image.load("moeda_mario.png")
                box_form = pygame.transform.scale(box, (10, 10))
                escolha2 = escolha
            if escolha == 1:
                box = pygame.image.load("sonic.png")
                box_form = pygame.transform.scale(box, (13, 13))
                escolha2 = escolha
            if escolha == 2:
                box = pygame.image.load("cogumelo.png")
                box_form = pygame.transform.scale(box, (13, 13))
                escolha2 = escolha
            screen.blit(box_form, power_pos)

            pygame.draw.line(screen, (8, 232, 235), (599, 0), (599, 599))
            pygame.draw.line(screen, (8, 232, 235), (599, 1), (1, 1))
            pygame.draw.line(screen, (8, 232, 235), (1, 599), (1, 1))
            pygame.draw.line(screen, (8, 232, 235), (1, 599), (599, 599))
            #screen.blit(power, power_pos - 10)
            '''for x in range(0, 600, 10):  # Draw vertical lines
                pygame.draw.line(screen, (8, 232, 235), (x, 0), (x, 600))
            for y in range(0, 600, 10):  # Draw vertical lines
                pygame.draw.line(screen, (8, 232, 235), (0, y), (600, y))'''
            if not start and not move:
                screen.blit(font_start.render('APERTE ENTER PARA COMEÇAR', True, (255, 255, 255)), (50, 250))

            if time:
                pygame.draw.rect(screen, ([7, 8, 14]), [50, 240, 510, 50])
                for pos in car:
                    screen.blit(car_skin, pos)
                for pos in car2:
                    screen.blit(car2_skin, pos)
                pygame.display.update()
                sleep(0.5)
                screen.blit(fonte_coord.render('3', True, (255, 255, 255)), (290, 230))
                for pos in car:
                    screen.blit(car_skin, pos)
                for pos in car2:
                    screen.blit(car2_skin, pos)
                pygame.display.update()
                moeda_sound = mixer.Sound('select_002.ogg')
                moeda_sound.play()
                sleep(0.5)
                pygame.draw.rect(screen, ([7, 8, 14]), [240, 230, 120, 70])

                screen.blit(fonte_coord.render('2', True, (255, 255, 255)), (290, 230))
                for pos in car:
                    screen.blit(car_skin, pos)
                for pos in car2:
                    screen.blit(car2_skin, pos)
                pygame.display.update()
                moeda_sound = mixer.Sound('select_002.ogg')
                moeda_sound.play()
                sleep(0.5)
                pygame.draw.rect(screen, ([7, 8, 14]), [240, 230, 120, 70])

                screen.blit(fonte_coord.render('1', True, (255, 255, 255)), (290, 230))
                for pos in car:
                    screen.blit(car_skin, pos)
                for pos in car2:
                    screen.blit(car2_skin, pos)
                pygame.display.update()
                moeda_sound = mixer.Sound('select_002.ogg')
                moeda_sound.play()
                sleep(0.5)
                pygame.draw.rect(screen, ([7, 8, 14]), [240, 230, 120, 70])
                direction_player1 = DOWN
                direction_player2 = K_s
                time = False
                move = True


            for pos in car:
                screen.blit(car_skin, pos)
            for pos in car2:
                screen.blit(car2_skin, pos)

            pygame.display.update()
        while True:
            if empate:
                screen.blit(fonte_coord.render('EMPATE', True, (255, 255, 255)), (180, 230))
                pygame.display.update()
                sleep(2)
                start_the_game()
            elif game_over_player1:
                game_over_font = pygame.font.Font('freesansbold.ttf', 35)
                game_over_screen = game_over_font.render('JOGADOR AZUL VENCEU', True, (255, 255, 255))
                game_over_rect = game_over_screen.get_rect()
                game_over_rect.midtop = (300, 220)
                screen.blit(game_over_screen, game_over_rect)
                pygame.display.update()
                moeda_sound = mixer.Sound('win_sound.wav')
                moeda_sound.play()
                sleep(3)
                start_the_game()
            elif game_over_player2:
                game_over_font = pygame.font.Font('freesansbold.ttf', 35)
                game_over_screen = game_over_font.render('JOGADOR VERMELHO VENCEU', True, (255, 255, 255))
                game_over_rect = game_over_screen.get_rect()
                game_over_rect.midtop = (300, 220)
                screen.blit(game_over_screen, game_over_rect)
                pygame.display.update()
                moeda_sound = mixer.Sound('win_sound.wav')
                moeda_sound.play()
                sleep(3)
                start_the_game()
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()


def menu1():
    pygame.init()
    surface = pygame.display.set_mode((600, 400))

    engine = sound.Sound()
    engine.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, 'select_002.ogg')
    menu = pygame_menu.Menu(300, 400, 'Tron',
                            theme=pygame_menu.themes.THEME_BLUE)

    menu.add_image('character_robot_interact.png', angle=0, scale=(1, 1))

    menu.set_sound(engine, recursive=True)

    menu.add_button('Clique aqui para começar', menu2)

    menu.mainloop(surface)
def menu2():
    pygame.init()

    surface = pygame.display.set_mode((600, 400))
    menu = pygame_menu.Menu(300, 400, 'Tron',
                            theme=pygame_menu.themes.THEME_BLUE)

    engine = sound.Sound()
    engine.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, 'select_002.ogg')
    menu.set_sound(engine, recursive=True)


    menu.add_button('Play', start_the_game)
    menu.add_button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(surface)

menu1()