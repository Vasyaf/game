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
# коллекцию карт, либо перейти к прохождению уровней. При нажатии на коллекцию 
# появляется экран со всеми его картами. Там же показано какие карты у игрока
# сейчас есть и сколько штук, а каких нет.
# При нажатии на кнопку кампании открывается экран с уровнями. Покачто их
# будет три. Сначала пройти можно только первый уровень. После его прохождения 
# можно пройти 2-ой уровень, а после его прохождения 3-ый. Уровни можно 
# перепроходить.
#
#     Непесредственно об уровнях. В каждом уровне у вас будет разный противник.
# На каждом уровне у противника будет разная колода карт. Суть сражения:
# У игрока и противника есть их главный герой. У него есть здоровье. Если оно
# победит противник. Также у игрока и противника есть колода карт. Ходят по
# очереди. Перед игрой тот кто ходит первый берёт 3 карты. Тот кто ходит второй --
# 4 карты. Также в начале своего хода каждый игрок берёт 1 карту. Если игрок
# не может взять карту, то у него отнимается 3 единицы здоровья. Между игроками
# есть так называемое поле, куда призываются воины каждого ишрока или противника.
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


pygame.init()
size = width, height = 1280, 720
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
clock = pygame.time.Clock()
fps = 50
all_sprites = pygame.sprite.Group()


class Board:
    pass
    # класс для помещения квадратов на поле. Именно с помощью них
    # мы будем взаимодействовать с картами в игре.

    
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


class Enemy:
    pass
    # Это класс противника. Их будет трое. Здесь надо сделать их всех.

class zastavka:
    pass
    # Это вызов рисования экрана заставки.


class menu_igri:
    pass
    # Это вызов рисования меню игры.


class kollekchia:
    pass
    # Это вызов рисования коллекции.


class menu_yrovneu:
    pass
    # Это вызов рисования меню уровней.


class yrovni:
    pass
    # Это вызов рисования поля для боя. Он будет всегда одинаковый.
    # Но если будем всё успевать, то можно сделать и разные.
    
    
class pravila:
    pass
    # Это вызов рисования экрана с правилами.


def terminate():
    pygame.quit()
    sys.exit()
    
def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
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
# картинка, нажав на которую программа закончится. Она если что во весь экран.
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if event.pos[0] >= width - 50 and event.pos[1] <= 50:
                terminate()
        all_sprites.draw(screen)
    pygame.display.flip()
terminate()