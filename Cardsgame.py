# -*- coding: utf-8 -*-
# 
#   Всем привет. Это наша программа. Она имеет жанр карточно-коллекционной игры.
# Её название -- Cardsgame.
#
# 
#   Суть такая: сначала перед игроком есть заставка. На ней он может ознакомиться
# с правилами, загрузить учётную запись или создать новую. При нажатии на кнопку
# правил будет высвечен новый экран с кнопкой возвращения в меню.
# При нажатии на кнопку новая игра, игрок создаёт свою учётную запись.
# Вводит свой никнейм(больше ничего не нужно). При нажатии на кнопку загрузки,
# игрок выбирает их всех имеющихся учётных записей свою.
#
#     После этого появляется экран меню. Там игрок может либо посмотреть свою
# коллекцию карт, либо перейти к прохождению уровней. Либо вернуться
# на заставку. При нажатии на коллекцию 
# появляется экран со всеми его картами. Там же показано какие карты у игрока
# сейчас есть и сколько штук, а каких нет.
# При нажатии на кнопку кампании открывается экран с уровнями. Пока что их
# будет три. Сначала пройти можно только первый уровень. После его прохождения 
# можно пройти 2-ой уровень, а после его прохождения 3-ый. Уровни можно 
# перепроходить.
#
#     Непесредственно об уровнях. В каждом уровне у вас будет разный противник.
# На каждом уровне у противника будет разная колода карт. Суть сражения:
# У игрока и противника есть их главный герой. У него есть здоровье. Если оно зако-
# нчится победит противник. Также у игрока и противника есть колода карт. Ходят по
# очереди. Перед игрой тот кто ходит первый берёт 3 карты. Тот кто ходит второй --
# 4 карты. Также в начале своего хода каждый игрок берёт 1 карту. Если игрок
# не может взять карту, то у него отнимается 3 единицы здоровья. Между игроками
# есть так называемое поле, куда призываются воины каждого игрока или противника.
#
#     Что делают карты. Пока что у нас будут только карты, которые являются
# какими-то существами. То есть игрок может в свой ход разыграть карту и у него
# на столе появится его воин. Карта имеет 4 показателя: имя существа, его урон,
# его здоровье и стоимость карты. 
#
#     У каждого игрока есть кристаллы маны. В начале
# игры у каждого по 0 и в начале своего хода у тебя становиться их на один больше.
# Максимум 8. В начале каждого своего хода кристаллы восстанавливаются и с их
# помощью можно разыгрывать карты.
# Когда вы разыграли карту вы получаете на стол своего воина у которого урон и 
# здоровье такие-же, какие были на карте которую вы разыграли. На следующий ход
# (разумеется свой) воин может атаковать один раз. Он может героя противника
# и нанести ему урон или ударить любого воина противника. При ударе вражеского
# воина оба получают урон, равный атаке другово воина.
#
#     У нас пока только три карты: курица(все показатели раны 1), робот(все
# показатели равны 3) и титан(все показатели равны 7). Потом можно будет добавить
# и более интересные карты, но пока надо сделать это. Вот наша программа.
# 
# Помимо неё нужно ещё сделать SQL таблицу. В ней будут храниться все учётные
# записи игроков. Она будет содержать такой вид. Её название -- cards_tab. И 
# название database тоже cards_tab.
# __________________________________________________
#  | Ima   | level | kolvo | Chicken | Robot | Titan |
# --------------------------------------------------
# 1| Igrok | 1   | 6     | 4       | 2     | 0     |
# __________________________________________________
#
# Имя это никнейм игрока. Уровень изначально 1-ый. Но за каждый пройденный уровень
# игрок увеличивает его на один(пока что максимум это 4). kolvo -- это количество
# карт. Остальные категории это все карты, которые есть в игре. У каждого игрока 
# написано сколько у него копий каждой карты.
#
# 
# Пока что всё. Если сделаем это, то впринципе будет достаточно. Но можно будет
# сделать и ещё что-нибудь.


import pygame
import sys
import os
import sqlite3


pygame.init()
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
# pygame.FULLSCREEN
clock = pygame.time.Clock()
fps = 50
all_sprites = pygame.sprite.Group()


class Board:
    def __init__(self):
        for i in range(365, 806, 110):
            for j in range(260, 361, 100):
                pygame.draw.rect(screen, (0, 0, 255), (i, j, 110, 100), 5)
        pygame.draw.rect(screen, (120, 0, 0), (565, 70, 150, 150), 5)
        pygame.draw.rect(screen, (120, 0, 0), (565, 500, 150, 150), 5)
        for i in range(20, 450, 100):
            for j in range(30, 620, 500):        
                pygame.draw.rect(screen, (205, 125, 125), (i, j, 75, 100), 5)
            
    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
   #     self.on_click(cell)
        
    def get_cell(self, m):
        x = 0
        qwe = 0
        for i in range(365, 806, 110):
            y = 0            
            for j in range(260, 361, 100):
                if m[0] >= i and m[0] <= i + 110:
                    if m[1] >= j and m[1] <= j + 100:
                        print(x, y)
                        qwe += 1
                y += 1
            x += 1
        if m[0] >= 565 and m[0] <= 715 and m[1] >= 70 and m[1] <= 220:
            print('враг')
            qwe += 1 
        if m[0] >= 565 and m[0] <= 715 and m[1] >= 500 and m[1] <= 650:
            print('ты')
            qwe += 1
        if qwe == 0:
            print('None')
        
                        

    
class Card:
    pass
    # Это класс любой карты.


class Igrok:
    pass
    # Это класс учётной записи каждого игрока. Именно здесь мы задействуем
    # базу данных.


class Allcards:
    pass
    # Это класс всех карт.


class Enemy_first:
    pass
    # Это класс противника. Их будет трое. Здесь надо сделать их всех.
    
class Enemy_second:
    pass


class Enemy_third:
    pass


def zastavka():
    fontObj = pygame.font.Font('freesansbold.ttf', 50)
    textSurfaceObj = fontObj.render('Новая игра', True, (255, 255, 255), (0, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (640, 200)
    screen.blit(textSurfaceObj, textRectObj)
    
    fontObj = pygame.font.Font('freesansbold.ttf', 50)
    textSurfaceObj = fontObj.render('Загрузить игру', True, (255, 255, 255), (0, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (640, 300)
    screen.blit(textSurfaceObj, textRectObj)
            
    fontObj = pygame.font.Font('freesansbold.ttf', 50)
    textSurfaceObj = fontObj.render('Правила игры', True, (255, 255, 255), (0, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (640, 400)
    screen.blit(textSurfaceObj, textRectObj)
    

def menu_igri():
    fontObj = pygame.font.Font('freesansbold.ttf', 30)
    textSurfaceObj = fontObj.render('Здесь должно быть название игры. Я просто не смог его придумать. Мдаа...', True, (255, 255, 255), (0, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (640, 100)
    screen.blit(textSurfaceObj, textRectObj)
    
    fontObj = pygame.font.Font('freesansbold.ttf', 50)
    textSurfaceObj = fontObj.render('Кампания', True, (255, 255, 255), (0, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (640, 400)
    screen.blit(textSurfaceObj, textRectObj)

    fontObj = pygame.font.Font('freesansbold.ttf', 50)
    textSurfaceObj = fontObj.render('Твоя коллекция', True, (255, 255, 255), (0, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (640, 500)
    screen.blit(textSurfaceObj, textRectObj)

    fontObj = pygame.font.Font('freesansbold.ttf', 25)
    textSurfaceObj = fontObj.render('Вернуться в главное меню', True, (255, 255, 255), (0, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (1100, 650)
    screen.blit(textSurfaceObj, textRectObj)

def kollekchia():
    fontObj = pygame.font.Font('freesansbold.ttf', 40)
    textSurfaceObj = fontObj.render('Здесь будет вся коллекция карт', True, (255, 255, 255), (0, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (600, 250)
    screen.blit(textSurfaceObj, textRectObj)   

def menu_yrovneu():
    fontObj = pygame.font.Font('freesansbold.ttf', 40)
    if level_igrok == 1:
        pygame.draw.circle(screen, (0, 0, 255), (401, 199), 35)
        textSurfaceObj = fontObj.render('1', True, (255, 255, 255), (0, 0, 255))
    else:
        textSurfaceObj = fontObj.render('1', True, (255, 255, 255), (0, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (400, 200)   
    screen.blit(textSurfaceObj, textRectObj)
    pygame.draw.circle(screen, (255, 255, 255), (400, 199), 35, 5)
    
    fontObj = pygame.font.Font('freesansbold.ttf', 40)
    if level_igrok == 2:
        pygame.draw.circle(screen, (0, 0, 255), (551, 299), 35)
        textSurfaceObj = fontObj.render('2', True, (255, 255, 255), (0, 0, 255))
    else:
        textSurfaceObj = fontObj.render('2', True, (255, 255, 255), (0, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (550, 300)
    screen.blit(textSurfaceObj, textRectObj)
    pygame.draw.circle(screen, (255, 255, 255), (550, 299), 35, 5)
    if level_igrok < 2:
        pygame.draw.rect(screen, (128, 128, 128), (510, 260, 80, 80), 5)
        pygame.draw.line(screen, (128, 128, 128), (510, 260), (590, 340), 5)
        pygame.draw.line(screen, (128, 128, 128), (590, 260), (510, 340), 5)
    
    fontObj = pygame.font.Font('freesansbold.ttf', 40)
    if level_igrok == 3:
        pygame.draw.circle(screen, (0, 0, 255), (701, 399), 35)
        textSurfaceObj = fontObj.render('3', True, (255, 255, 255), (0, 0, 255))
    else:
        textSurfaceObj = fontObj.render('3', True, (255, 255, 255), (0, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (700, 400)
    screen.blit(textSurfaceObj, textRectObj)
    pygame.draw.circle(screen, (255, 255, 255), (700, 399), 35, 5)
    if level_igrok < 3:
        pygame.draw.rect(screen, (128, 128, 128), (660, 360, 80, 80), 5)
        pygame.draw.line(screen, (128, 128, 128), (660, 360), (740, 440), 5)
        pygame.draw.line(screen, (128, 128, 128), (740, 360), (660, 440), 5)

def yrovni():
    pass
    # Это вызов рисования поля для боя. Он будет всегда одинаковый.
    # Но если будем всё успевать, то можно сделать и разные.
        
def pravila():
    pass
    # Это вызов рисования экрана с правилами.

def terminate():
    pygame.quit()
    sys.exit()
    
def load_image(name, color_key=None):
    fullname = os.path.join('game_sprites', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image
    # у вас должна быть папка под названием game_sprites. Все спрайты берутся из неё.

running = True
exit = pygame.sprite.Sprite(all_sprites)
exit.image = pygame.transform.scale(load_image('kres.jpg'), (50, 50))
exit.rect = exit.image.get_rect().move(width - 50, 0)
# картинка, нажав на которую программа закончится. Игра, если что, во весь экран.
ekran = 1
back_prov = True
level_play = 1
con = sqlite3.connect("cards_tab.db")
cur = con.cursor()
result = cur.execute("SELECT * FROM cards_tab").fetchall()
name = result[0][0]
kolvo = result[0][2]
cheaken = result[0][3]
robot = result[0][4]
titan = result[0][5]
level_igrok = result[0][1]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if event.pos[0] >= width - 50 and event.pos[1] <= 50:
                terminate()      
        if ekran == 1:
            zastavka()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.pos[0] >= 465 and event.pos[0] <= 815:
                    if event.pos[1] >= 375 and event.pos[1] <= 426:
                        ekran = 2
                        screen.fill((0, 0, 0))
                if event.pos[0] >= 500 and event.pos[0] <= 780:
                    if event.pos[1] >= 175 and event.pos[1] <= 226:
                        ekran = 3
                        screen.fill((0, 0, 0))
        elif ekran == 2:
            fontObj = pygame.font.Font('freesansbold.ttf', 50)
            textSurfaceObj = fontObj.render('Здесь должны быть правила', True, (255, 255, 255), (0, 0, 0))
             # textSurfaceObj = fontObj.render('''У игрока и противника есть их главный герой. У него есть здоровье. Если оно зако-
# нчится победит противник. Также у игрока и противника есть колода карт. Ходят по
# очереди. Перед игрой тот кто ходит первый берёт 3 карты. Тот кто ходит второй --
# 4 карты. Также в начале своего хода каждый игрок берёт 1 карту. Если игрок
# не может взять карту, то у него отнимается 3 единицы здоровья. Между игроками
# есть так называемое поле, куда призываются воины каждого игрока или противника.
#
#    Что делают карты. Пока что у нас будут только карты, которые являются
# какими-то существами. То есть игрок может в свой ход разыграть карту и у него
# на столе появится его воин. Карта имеет 4 показателя: имя существа, его урон,
# его здоровье и стоимость карты. 
#
#    У каждого игрока есть кристаллы маны. В начале
# игры у каждого по 0 и в начале своего хода у тебя становиться их на один больше.
# Максимум 8. В начале каждого своего хода кристаллы восстанавливаются и с их
# помощью можно разыгрывать карты.
# Когда вы разыграли карту вы получаете на стол своего воина у которого урон и 
# здоровье такие-же, какие были на карте которую вы разыграли. На следующий ход
# (разумеется свой) воин может атаковать один раз. Он может героя противника
# и нанести ему урон или ударить любого воина противника. При ударе вражеского
# воина оба получают урон, равный атаке другово воина.''', True, (255, 255, 255), (0, 0, 0))
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (640, 300)
            screen.blit(textSurfaceObj, textRectObj)
            
            if back_prov:
                back = pygame.sprite.Sprite(all_sprites)
                back.image = pygame.transform.scale(load_image('back.png'), (50, 50))
                back.rect = back.image.get_rect().move(0, 0)
                back_prov = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.pos[0] <= 50 and event.pos[1] <= 50:
                    ekran = 1
                    back.kill()
                    back_prov = True
                    screen.fill((0, 0, 0))
        elif ekran == 3:
            menu_igri()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.pos[0] >= 928 and event.pos[0] <= 1273:
                    if event.pos[1] >= 637 and event.pos[1] <= 663:
                        ekran = 1
                        screen.fill((0, 0, 0))
                if event.pos[0] >= 517 and event.pos[0] <= 763:
                    if event.pos[1] >= 375 and event.pos[1] <= 426:
                        ekran = 4
                        screen.fill((0, 0, 0))
                if event.pos[0] >= 438 and event.pos[0] <= 842:
                    if event.pos[1] >= 475 and event.pos[1] <= 526:
                        ekran = 5
                        screen.fill((0, 0, 0))
                
        elif ekran == 4:
            menu_yrovneu()
            if back_prov:
                back = pygame.sprite.Sprite(all_sprites)
                back.image = pygame.transform.scale(load_image('back.png'), (50, 50))
                back.rect = back.image.get_rect().move(0, 0)
                back_prov = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.pos[0] <= 50 and event.pos[1] <= 50:
                    ekran = 3
                    back.kill()
                    back_prov = True
                    screen.fill((0, 0, 0))
                if event.pos[0] >= 367 and event.pos[0] <= 433:
                    if event.pos[1] >= 166 and event.pos[1] <= 232:
                        ekran = 6
                        level_play = 1
                        back.kill()
                        back_prov = True                        
                        screen.fill((0, 0, 0))
                if level_igrok >= 2: 
                    if event.pos[0] >= 517 and event.pos[0] <= 583:
                        if event.pos[1] >= 266 and event.pos[1] <= 332:
                            ekran = 6
                            level_play = 2
                            back.kill()
                            back_prov = True                            
                            screen.fill((0, 0, 0))
                if level_igrok >= 3:
                    if event.pos[0] >= 667 and event.pos[0] <= 733:
                        if event.pos[1] >= 366 and event.pos[1] <= 432:
                            ekran = 6
                            level_play = 3
                            back.kill()
                            back_prov = True                            
                            screen.fill((0, 0, 0))
        elif ekran == 5:          
            kollekchia()
            if back_prov:
                back = pygame.sprite.Sprite(all_sprites)
                back.image = pygame.transform.scale(load_image('back.png'), (50, 50))
                back.rect = back.image.get_rect().move(0, 0)
                back_prov = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.pos[0] <= 50 and event.pos[1] <= 50:
                    ekran = 3
                    back.kill()
                    back_prov = True
                    screen.fill((0, 0, 0))            
        elif ekran == 6:
            if level_play == 1:
                fontObj = pygame.font.Font('freesansbold.ttf', 50)
                textSurfaceObj = fontObj.render('здесь будет 1-ый уровень', True, (255, 255, 255), (0, 0, 0))
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (640, 200)
                screen.blit(textSurfaceObj, textRectObj)
                name_e = 'Тролль'
                kolvo_e = 7
                cheaken_e = 6
                robot_e = 1
            elif level_play == 2:
                fontObj = pygame.font.Font('freesansbold.ttf', 50)
                textSurfaceObj = fontObj.render('здесь будет 2-ой уровень', True, (255, 255, 255), (0, 0, 0))
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (640, 200)
                screen.blit(textSurfaceObj, textRectObj)
            elif level_play == 3:
                fontObj = pygame.font.Font('freesansbold.ttf', 50)
                textSurfaceObj = fontObj.render('здесь будет 3-ий уровень', True, (255, 255, 255), (0, 0, 0))
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (640, 200)
                screen.blit(textSurfaceObj, textRectObj)
            fontObj = pygame.font.Font('freesansbold.ttf', 50)
            textSurfaceObj = fontObj.render(str(kolvo), True, (255, 255, 255), (0, 0, 0))
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (1050, 500)
            screen.blit(textSurfaceObj, textRectObj)
            pygame.draw.rect(screen, (0, 120, 0), (1015, 390, 70, 220), 3)
            
            fontObj = pygame.font.Font('freesansbold.ttf', 50)
            textSurfaceObj = fontObj.render(str(kolvo_e), True, (255, 255, 255), (0, 0, 0))
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (1050, 270)
            screen.blit(textSurfaceObj, textRectObj)
            pygame.draw.rect(screen, (0, 120, 0), (1015, 160, 70, 220), 3)
            
            board = Board()
            fontObj = pygame.font.Font('freesansbold.ttf', 50)
            textSurfaceObj = fontObj.render(name, True, (255, 255, 255), (0, 0, 0))
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (640, 540)
            screen.blit(textSurfaceObj, textRectObj)
            
            fontObj = pygame.font.Font('freesansbold.ttf', 40)
            textSurfaceObj = fontObj.render(name_e, True, (255, 255, 255), (0, 0, 0))
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (640, 100)
            screen.blit(textSurfaceObj, textRectObj)            
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        all_sprites.draw(screen)
    pygame.display.flip()
terminate() 