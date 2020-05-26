import pygame, random, pygame_menu
from pygame.locals import *
from time import sleep
from pygame_menu import sound
from pygame import mixer

score1 = 0
score2 = 0
num_players = 2
last_score = 0
def start_the_game1():
    global num_players
    num_players = 1
    start_the_game()
    return

def start_the_game():
        global num_players, last_score
        if num_players == 1:
            print(num_players)
        if num_players == 2:
            print(num_players)

        def ongrid_random():
            # Criando lugar aleatorio para o poder em um espaço na tela multiplo de 10
            x = random.randint(110, 690)
            y = random.randint(20, 670)
            return ((x // 10 * 10), (y // 10 * 10))

        def collision(c1, c2):
            # colisão
            return (c1[0] == c2[0] and (c1[1] == c2[1]))

        def surprise_box(player, surprise):
            #surprise = random.randint(1, 2)
            if surprise == 0:#moeda
                if player == 1:
                    car.append((-10, -10))
                if player == 2:
                    car2.append((-10, -10))
                moeda_sound = mixer.Sound('coin_mario.wav')
                moeda_sound.play()
                #engine.set_sound('coin_mario.wav')
            if surprise == 1:#sonic
                if num_players == 1:
                    if player == 1:
                        for c in range(1, 21):
                            car.append((-10, -10))
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



            return 20

        # criando variaveis para cada direção
        UP = 0
        RIGHT = 1
        DOWN = 2
        LEFT = 3
        pygame.init()  # iniciando pygame
        screen = pygame.display.set_mode((800, 700))  # criando tamanho da tela
        pygame.display.set_caption("Tron")  # nome ta tela
        screen.fill([8, 232, 235])

        car = [(550, 150), (550, 150), (550, 150)]  # lista da posição do carro
        if num_players == 1:
            car = [(400, 150), (400, 150), (400, 150)]
        car_skin = pygame.Surface((10, 10))  # escolhendo o tamanho do carro(que no caso é um quadrado)
        car_skin.fill((255, 0, 0))  # escolhendo a cor do carro
        pacman = pygame.image.load("seta.png")
        pacman_form = pygame.transform.scale(pacman, (8, 9))


        car2 = [(250, 150), (250, 150), (250, 150)]  # lista da posição do carro
        if num_players == 1:
            car2 = [(-25000, -15000), (-25000, -15000), (-25000, -15000)]
        car2_skin = pygame.Surface((10, 10))  # escolhendo o tamanho do carro(que no caso é um quadrado)
        car2_skin.fill((0, 0, 255))  # escolhendo a cor do carro
        carspeed = 17

        power_pos = ongrid_random()  # poder possivelmente implementado futuramente
        power_pos1 = power_pos + (-10, -10)
        power = pygame.Surface((10, 10))  # tamanho dele
        power.fill((255, 255, 255))  # sua cor
        explosion = pygame.image.load("explosion.png")
        explosion_form = pygame.transform.scale(explosion, (20, 20))
        explosion_sound = mixer.Sound('explosion.wav')


        rotate_up = pygame.transform.rotate(pacman_form, 90)
        rotate_R = pygame.transform.rotate(pacman_form, 0)
        rotate_L = pygame.transform.rotate(pacman_form, 180)
        rotate_D = pygame.transform.rotate(pacman_form, 270)

        my_direction = 5  # direção que o carro começa a andar
        direction_player1 = 5
        direction_player2 = 5
        clock = pygame.time.Clock()  # isso serve para poder usar o clock ali em baixo
        font = pygame.font.Font('freesansbold.ttf', 18)
        font_score = pygame.font.Font('freesansbold.ttf', 80)
        font_scor = pygame.font.Font('freesansbold.ttf', 22)
        font_scoretop = pygame.font.Font('freesansbold.ttf', 15)
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

                    if event.key == pygame.K_KP_ENTER or event.key == pygame.K_SPACE:
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
                    surprise_box(1, escolha)
                    score = score + 1
                if collision(car2[0], power_pos) and start:
                    power_pos = ongrid_random()
                    surprise_box(2, escolha)
                escolha = random.randint(0, 2)
                if num_players == 1:
                    escolha = 1
                    if escolha2 == 1:
                        carspeed = carspeed + 2
                if num_players == 2:
                    if escolha2 == 1:
                        carspeed = carspeed + 5


            if car[0][0] > 690 or car[0][1] >= 660 or car[0][0] < 100 or car[0][1] < 20:
                if car[0][0] > 690:
                    car[0] = (car[0][0] - 600, car[0][1])
                if car[0][1] >= 660:
                    car[0] = (car[0][0], car[0][1] - 660)
                if car[0][0] < 100:
                    car[0] = (car[0][0] + 600, car[0][1])
                if car[0][1] < 20:
                    car[0] = (car[0][0], car[0][1] + 660)
                #game_over = True
                #break
            if car2[0][0] > 690 or car2[0][1] >= 660 or car2[0][0] < 100 or car2[0][1] < 20:
                if car2[0][0] > 690:
                    car2[0] = (car2[0][0] - 600, car2[0][1])
                if car2[0][1] >= 660:
                    car2[0] = (car2[0][0], car2[0][1] - 660)
                if car2[0][0] < 100:
                    car2[0] = (car2[0][0] + 600, car2[0][1])
                if car2[0][1] < 20:
                    car2[0] = (car2[0][0], car2[0][1] + 660)
                #game_over = True
                #break
            # checando empate
            if num_players == 2:
                if collision(car[0], car2[0]):
                    explosion_sound.play()
                    screen.blit(explosion_form, (car[0][0] - 5, car[0][1] - 4))
                    pygame.display.update()
                    sleep(0.5)
                    empate = True
                    game_over = True
                    break

            for i in range(1, len(car) - 1):   #colisão entre player 1 em si mesmo
                if car[0][0] == car[i][0] and car[0][1] == car[i][1] and start:
                    explosion_sound.play()
                    screen.blit(explosion_form, (car[0][0] - 5, car[0][1] - 4))
                    pygame.display.update()
                    sleep(0.5)
                    game_over_player1 = True
                    game_over = True
                    break
            for i in range(1, len(car2) - 1):  # colisão entre player 2 em si mesmo
                if car2[0][0] == car2[i][0] and car2[0][1] == car2[i][1] and start:
                    explosion_sound.play()
                    screen.blit(explosion_form, (car2[0][0] - 5, car2[0][1] - 4))
                    pygame.display.update()
                    sleep(0.5)
                    game_over_player2 = True
                    game_over = True
                    break
            if num_players == 2:
                for i in range(1, len(car) - 1):    #colisão entre cabeça do player 2 com a player 1
                    if collision(car2[0], car[i]) and start:
                        explosion_sound.play()
                        screen.blit(explosion_form, (car2[0][0] - 5, car2[0][1] - 4))
                        pygame.display.update()
                        sleep(0.5)
                        game_over_player2 = True
                        game_over = True
                        break
            if num_players == 2:
                for i in range(1, len(car2) - 1):    #colisão entre cabeça do player 1 com o player 2
                    if collision(car[0], car2[i]) and start:
                        explosion_sound.play()
                        screen.blit(explosion_form, (car[0][0] - 5, car[0][1] - 4))
                        pygame.display.update()
                        sleep(0.5)
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


            if move == True:
                screen.blit(box_form, power_pos)

            '''pygame.draw.line(screen, (8, 232, 235), (599, 0), (599, 599))
            pygame.draw.line(screen, (8, 232, 235), (599, 1), (1, 1))
            pygame.draw.line(screen, (8, 232, 235), (1, 599), (1, 1))
            pygame.draw.line(screen, (8, 232, 235), (1, 599), (599, 599))'''

            pygame.draw.line(screen, (8, 232, 235), (99, 19), (700, 19))
            pygame.draw.line(screen, (8, 232, 235), (99, 19), (99, 680))
            pygame.draw.line(screen, (8, 232, 235), (99, 680), (700, 680))
            pygame.draw.line(screen, (8, 232, 235), (700, 680), (700, 19))

            pygame.draw.rect(screen, ([255, 0, 0]), [702, 0, 100, 700])
            pygame.draw.rect(screen, ([255, 0, 0]), [400, 0, 400, 18])
            pygame.draw.rect(screen, ([255, 0, 0]), [400, 681, 400, 20])
            pygame.draw.rect(screen, ([0, 0, 255]), [0, 0, 98, 700])
            pygame.draw.rect(screen, ([0, 0, 255]), [98, 0, 300, 18])
            pygame.draw.rect(screen, ([0, 0, 255]), [98, 681, 300, 20])
            global score1
            global score2
            if score2 - score1 == 1:
                pygame.draw.rect(screen, ([255, 0, 0]), [300, 681, 400, 20])
                pygame.draw.rect(screen, ([255, 0, 0]), [300, 0, 400, 18])
            if score2 - score1 == 2:
                pygame.draw.rect(screen, ([255, 0, 0]), [200, 681, 400, 20])
                pygame.draw.rect(screen, ([255, 0, 0]), [200, 0, 400, 18])
            if score2 - score1 == 3:
                pygame.draw.rect(screen, ([255, 0, 0]), [100, 681, 400, 20])
                pygame.draw.rect(screen, ([255, 0, 0]), [100, 0, 400, 18])
            if score2 - score1 == 4:
                pygame.draw.rect(screen, ([255, 0, 0]), [99, 681, 400, 20])
                pygame.draw.rect(screen, ([255, 0, 0]), [99, 0, 400, 18])
                pygame.draw.rect(screen, ([255, 0, 0]), [0, 500, 99, 200])
                pygame.draw.rect(screen, ([255, 0, 0]), [0, 0, 99, 200])
            if score2 - score1 > 4:
                pygame.draw.rect(screen, ([255, 0, 0]), [99, 681, 400, 20])
                pygame.draw.rect(screen, ([255, 0, 0]), [99, 0, 400, 18])
                pygame.draw.rect(screen, ([255, 0, 0]), [0, 0, 99, 700])


            if score1 - score2 == 1:
                pygame.draw.rect(screen, ([0, 0, 255]), [98, 0, 400, 18])
                pygame.draw.rect(screen, ([0, 0, 255]), [98, 681, 400, 20])
            if score1 - score2 == 2:
                pygame.draw.rect(screen, ([0, 0, 255]), [98, 0, 500, 18])
                pygame.draw.rect(screen, ([0, 0, 255]), [98, 681, 500, 20])
            if score1 - score2 == 3:
                pygame.draw.rect(screen, ([0, 0, 255]), [98, 0, 602, 18])
                pygame.draw.rect(screen, ([0, 0, 255]), [98, 681, 602, 20])
            if score1 - score2 == 4:
                pygame.draw.rect(screen, ([0, 0, 255]), [98, 0, 604, 18])
                pygame.draw.rect(screen, ([0, 0, 255]), [98, 681, 604, 20])
                pygame.draw.rect(screen, ([0, 0, 255]), [701, 0, 100, 200])
                pygame.draw.rect(screen, ([0, 0, 255]), [701, 500, 100, 200])
            if score1 - score2 > 4:
                pygame.draw.rect(screen, ([0, 0, 255]), [98, 0, 604, 18])
                pygame.draw.rect(screen, ([0, 0, 255]), [98, 681, 604, 20])
                pygame.draw.rect(screen, ([0, 0, 255]), [701, 0, 99, 700])

            score_font = font_score.render('%s' % (score1), True, (255, 255, 255))
            score_rect = score_font.get_rect()
            score_rect.topleft = (30, 300)
            score_font2 = font_score.render('%s' % (score2), True, (255, 255, 255))
            score_rect2 = score_font.get_rect()
            score_rect2.topleft = (730, 300)
            if num_players == 1:
                score_font = font_score.render('%s' % (score), True, (255, 255, 255))
                score_top = font_scor.render('SCORE', True, (255, 255, 255))
                score_rec = score_top.get_rect()
                score_rec.topleft = (12, 270)
                screen.blit(score_top, score_rec)

                score_top2 = font_scoretop.render('TOP SCORE', True, (255, 255, 255))
                score_rec2 = score_top.get_rect()
                score_rec2.topleft = (708, 270)
                screen.blit(score_top2, score_rec2)
                score_font2 = font_score.render('%s' % (last_score), True, (255, 255, 255))
            if score > 9:
                score_rect.topleft = (10, 300)
            if score1 > 9:
                score_rect.topleft = (10, 300)
            if score2 > 9:
                score_rect2.topleft = (710, 300)
            if last_score > 9:
                score_rect2.topleft = (710, 300)

            screen.blit(score_font, score_rect)
            screen.blit(score_font2, score_rect2)


            #screen.blit(power, power_pos - 10)
            '''for x in range(0, 600, 10):  # Draw vertical lines
                pygame.draw.line(screen, (8, 232, 235), (x, 0), (x, 600))
            for y in range(0, 600, 10):  # Draw vertical lines
                pygame.draw.line(screen, (8, 232, 235), (0, y), (600, y))'''
            if not start and not move:
                screen.blit(font_start.render('APERTE ENTER PARA COMEÇAR', True, (255, 255, 255)), (150, 300))

            if time:
                pygame.draw.rect(screen, ([7, 8, 14]), [150, 300, 510, 50])
                for pos in car:
                    screen.blit(car_skin, pos)
                    screen.blit(rotate_D, (pos))
                if num_players == 2:
                    for pos in car2:
                        screen.blit(car2_skin, pos)
                        screen.blit(rotate_D, (pos))
                pygame.display.update()
                sleep(0.5)
                screen.blit(fonte_coord.render('3', True, (255, 255, 255)), (390, 300))
                for pos in car:
                    screen.blit(car_skin, pos)
                    screen.blit(rotate_D, (pos))
                if num_players == 2:
                    for pos in car2:
                        screen.blit(car2_skin, pos)
                        screen.blit(rotate_D, (pos))
                pygame.display.update()
                moeda_sound = mixer.Sound('select_002.ogg')
                moeda_sound.play()
                sleep(0.5)
                pygame.draw.rect(screen, ([7, 8, 14]), [390, 300, 120, 70])

                screen.blit(fonte_coord.render('2', True, (255, 255, 255)), (390, 300))
                for pos in car:
                    screen.blit(car_skin, pos)
                    screen.blit(rotate_D, (pos))
                if num_players == 2:
                    for pos in car2:
                        screen.blit(car2_skin, pos)
                        screen.blit(rotate_D, (pos))
                pygame.display.update()
                moeda_sound = mixer.Sound('select_002.ogg')
                moeda_sound.play()
                sleep(0.5)
                pygame.draw.rect(screen, ([7, 8, 14]), [390, 300, 120, 70])

                screen.blit(fonte_coord.render('1', True, (255, 255, 255)), (390, 300))
                for pos in car:
                    screen.blit(car_skin, pos)
                    screen.blit(rotate_D, (pos))
                if num_players == 2:
                    for pos in car2:
                        screen.blit(car2_skin, pos)
                        screen.blit(rotate_D, (pos))
                pygame.display.update()
                moeda_sound = mixer.Sound('select_002.ogg')
                moeda_sound.play()
                sleep(0.5)
                pygame.draw.rect(screen, ([7, 8, 14]), [390, 300, 120, 70])
                direction_player1 = DOWN
                direction_player2 = K_s
                time = False
                move = True



            for pos in car:
                screen.blit(car_skin, pos)
                if car[0] and direction_player1 == UP:
                    screen.blit(rotate_up, (pos))
                if car[0] and direction_player1 == DOWN:
                    screen.blit(rotate_D, (pos))
                if car[0] and direction_player1 == LEFT:
                    screen.blit(rotate_L, (pos))
                if car[0] and direction_player1 == RIGHT:
                    screen.blit(rotate_R, (pos))
            if num_players == 2:
                for pos in car2:
                    screen.blit(car2_skin, pos)
                    if car2[0] and direction_player2 == K_w:
                        screen.blit(rotate_up, (pos))
                    if car2[0] and direction_player2 == K_s:
                        screen.blit(rotate_D, (pos))
                    if car2[0] and direction_player2 == K_a:
                        screen.blit(rotate_L, (pos))
                    if car2[0] and direction_player2 == K_d:
                        screen.blit(rotate_R, (pos))

            pygame.display.update()
        while True:
            if empate:
                screen.blit(fonte_coord.render('EMPATE', True, (255, 255, 255)), (280, 300))
                pygame.display.update()
                sleep(2)
                start_the_game()
            elif game_over_player1:
                game_over_font = pygame.font.Font('freesansbold.ttf', 35)
                game_over_screen = game_over_font.render('JOGADOR AZUL VENCEU', True, (20, 20, 255))
                if num_players == 1:
                    game_over_screen = game_over_font.render('YOU LOSE', True, (20, 20, 255))
                    if score > last_score:
                        last_score = score
                if num_players == 2:
                    score1 = score1 + 1
                game_over_rect = game_over_screen.get_rect()
                game_over_rect.midtop = (400, 300)
                screen.blit(game_over_screen, game_over_rect)
                pygame.display.update()
                moeda_sound = mixer.Sound('win_sound.wav')
                moeda_sound.play()
                sleep(3)
                start_the_game()
            elif game_over_player2:
                game_over_font = pygame.font.Font('freesansbold.ttf', 35)
                game_over_screen = game_over_font.render('JOGADOR VERMELHO VENCEU', True, (255, 30, 30))
                score2 = score2 + 1
                game_over_rect = game_over_screen.get_rect()
                game_over_rect.midtop = (400, 300)
                screen.blit(game_over_screen, game_over_rect)
                pygame.display.update()
                moeda_sound = mixer.Sound('win_sound.wav')
                moeda_sound.play()
                sleep(3)
                start_the_game()

            screen.blit(fonte_coord.render((score), True, (255, 255, 255)), (10, 300))
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()


def menu1():
    pygame.init()
    surface = pygame.display.set_mode((700, 700))

    engine = sound.Sound()
    engine.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, 'select_002.ogg')
    menu = pygame_menu.Menu(400, 600, 'Tron',
                            theme=pygame_menu.themes.THEME_DARK)

    menu.add_image('tronn.png', angle=0, scale=(0.4, 0.4))

    menu.set_sound(engine, recursive=True)

    menu.add_button('Começar', menu2)

    menu.mainloop(surface)


def menu2():
    pygame.init()

    surface = pygame.display.set_mode((700, 700))
    menu = pygame_menu.Menu(400, 600, 'Tron',
                            theme=pygame_menu.themes.THEME_DARK)

    engine = sound.Sound()
    engine.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, 'select_002.ogg')
    menu.set_sound(engine, recursive=True)


    menu.add_button('Jogar', menu3)
    menu.add_button('Sobre', menu4)
    menu.add_button('Sair', pygame_menu.events.EXIT)

    menu.mainloop(surface)


def menu3():
    pygame.init()

    surface = pygame.display.set_mode((700, 700))
    menu = pygame_menu.Menu(400, 600, 'Jogadores',
                            theme=pygame_menu.themes.THEME_DARK)

    engine = sound.Sound()
    engine.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, 'select_002.ogg')
    menu.set_sound(engine, recursive=True)

    menu.add_button('1 Jogador', player1)
    menu.add_button("2 Jogadores", player2)
    menu.add_button('Voltar', menu2)

    menu.mainloop(surface)

def menu4():
    pygame.init()

    surface = pygame.display.set_mode((700, 700))
    menu = pygame_menu.Menu(400, 600, 'Regras',
                            theme=pygame_menu.themes.THEME_DARK)
    engine = sound.Sound()
    engine.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, 'select_002.ogg')
    menu.set_sound(engine, recursive=True)

    regras= "O jogo é formado por duas pessoas que controlam os Trons, "\
            "usando as setinhas do teclado um jogador se move e o outro jogador "\
            "para se mover irá utilizar o famoso WASD."\
            "Durante a partida alguns poderes irão aparecer, deixando cada vez mais "\
            "o jogo dinâmico e competitivo. "\
            "Vença o seu adversário não encostando e nem esbarrando em nada e tente "\
            "pegar poderes para que você consiga ter certas vantagens. "\
            "Boa Sorte!!"

    font = pygame_menu.font.FONT_HELVETICA

    menu.add_label(regras, max_char=-1,font_size=20, font_name=font)

    menu.add_button("Poder",menu5)
    menu.add_button('Voltar', menu2)

    menu.mainloop(surface)

def player1():
    pygame.init()

    surface = pygame.display.set_mode((700, 700))
    menu = pygame_menu.Menu(400, 600, 'Jogador 1',
                            theme=pygame_menu.themes.THEME_DARK)
    engine = sound.Sound()
    engine.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, 'select_002.ogg')
    menu.set_sound(engine, recursive=True)

    menu.add_image('tron.png', angle=0, scale=(1, 1))
    menu.add_button("Vamos", start_the_game1)
    menu.add_button('Voltar', menu3)

    menu.mainloop(surface)

def player2():
    pygame.init()

    surface = pygame.display.set_mode((700, 800))
    menu = pygame_menu.Menu(500, 700, 'Jogador 2',
                            theme=pygame_menu.themes.THEME_DARK)
    engine = sound.Sound()
    engine.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, 'select_002.ogg')
    menu.set_sound(engine, recursive=True)

    menu.add_image('tron.png', angle=0, scale=(0.7, 0.7))
    menu.add_image('tron.png', angle=0, scale=(0.7, 0.7))
    menu.add_button("Vamos", start_the_game)
    menu.add_button('Voltar', menu3)

    menu.mainloop(surface)

def menu5():
    pygame.init()

    surface = pygame.display.set_mode((700, 800))
    menu = pygame_menu.Menu(500, 700, 'Poder',
                            theme=pygame_menu.themes.THEME_DARK)
    engine = sound.Sound()
    engine.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, 'select_002.ogg')
    menu.set_sound(engine, recursive=True)

    text1 = "Aumenta muito o tamanho."

    text2 = "Aumenta a velocidade."

    text3 = "Aumenta muito pouco o tamanho"

    menu.add_image('cogumelo.png', angle=0, scale=(0.5, 0.5))

    font = pygame_menu.font.FONT_HELVETICA

    menu.add_label(text1, max_char=-1,font_size=20, font_name=font)

    menu.add_image('sonic.png', angle=0, scale=(0.5, 0.5))

    menu.add_label(text2, max_char=-1,font_size=20, font_name=font)

    menu.add_image('moeda_mario.png', angle=0, scale=(0.5,0.5))

    menu.add_label(text3, max_char=-1,font_size=20, font_name=font)

    menu.add_button('Voltar', menu2)

    menu.mainloop(surface)

menu1()