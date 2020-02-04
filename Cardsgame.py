# -*- coding: utf-8 -*-
# 
# Всем привет. Это наша программа. Она имеет жанр карточно-коллекционной игры.
# Её название -- Cardsgame.
#
# 
# Суть такая: сначала перед игроком есть заставка. На ней он может ознакомиться
# с правилами, загрузить учётную запись или создать новую. При нажатии на кнопку
# правил будет высвечен новый экран с кнопкой возвращения в меню.
# При нажатии на кнопку новая игра, игрок создаёт свою учётную запись.
# Вводит свой никнейм(больше ничего не нужно). При нажатии на кнопку загрузки,
# игрок выбирает их всех имеющихся учётных записей свою.
#
# После этого появляется экран меню. Там игрок может либо посмотреть свою
# коллекцию карт, либо перейти к прохождению уровней. Либо вернуться
# на заставку. При нажатии на коллекцию 
# появляется экран со всеми его картами. Там же показано какие карты у игрока
# сейчас есть и сколько штук, а каких нет.
# При нажатии на кнопку кампании открывается экран с уровнями. Пока что их
# будет три. Сначала пройти можно только первый уровень. После его прохождения 
# можно пройти 2-ой уровень, а после его прохождения 3-ый. Уровни можно 
# перепроходить.
#
# Непесредственно об уровнях. В каждом уровне у вас будет разный противник.
# На каждом уровне у противника будет разная колода карт. Суть сражения:
# У игрока и противника есть их главный герой. У него есть здоровье. Если оно зако-
# нчится победит противник. Также у игрока и противника есть колода карт. Ходят по
# очереди. Перед игрой тот кто ходит первый берёт 3 карты. Тот кто ходит второй --
# 4 карты. Также в начале своего хода каждый игрок берёт 1 карту. Если игрок
# не может взять карту, то у него отнимается 3 единицы здоровья. Между игроками
# есть так называемое поле, куда призываются воины каждого игрока или противника.
#
# Что делают карты. Пока что у нас будут только карты, которые являются
# какими-то существами. То есть игрок может в свой ход разыграть карту и у него
# на столе появится его воин. Карта имеет 4 показателя: имя существа, его урон,
# его здоровье и стоимость карты. 
#
# У каждого игрока есть кристаллы маны. В начале
# игры у каждого по 0 и в начале своего хода у тебя становиться их на один больше.
# Максимум 8. В начале каждого своего хода кристаллы восстанавливаются и с их
# помощью можно разыгрывать карты.
# Когда вы разыграли карту вы получаете на стол своего воина у которого урон и 
# здоровье такие-же, какие были на карте которую вы разыграли. На следующий ход
# (разумеется свой) воин может атаковать один раз. Он может героя противника
# и нанести ему урон или ударить любого воина противника. При ударе вражеского
# воина оба получают урон, равный атаке другово воина.
#
# У нас пока только три карты: курица(все показатели раны 1), робот(все
# показатели равны 3) и титан(все показатели равны 7). Потом можно будет добавить
# и более интересные карты, но пока надо сделать это. Вот наша программа.
# 
# Помимо неё нужно ещё сделать SQL таблицу. В ней будут храниться все учётные
# записи игроков. Она будет содержать такой вид. Её название -- cards_tab. И 
# название database тоже cards_tab.
# __________________________________________________
# | Ima | level | kolvo | Chicken | Robot | Titan |
# --------------------------------------------------
# 1| Igrok | 1 | 6 | 4 | 2 | 0 |
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
import random


pygame.init()
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
# pygame.FULLSCREEN
clock = pygame.time.Clock()
fps = 50
all_sprites = pygame.sprite.Group()


class Board:
    def __init__(self):
        self.pole = []
        self.prov_click = None
        self.rect_yellow = None
        self.prov_yellow = True
        
        self.imag30 = pygame.sprite.Sprite(all_sprites)
        self.imag30.image = pygame.transform.scale(load_image('egg.png'), (0, 0))
        self.imag30.rect = self.imag30.image.get_rect().move(0, 0)
        self.imag31 = pygame.sprite.Sprite(all_sprites)
        self.imag31.image = pygame.transform.scale(load_image('egg.png'), (0, 0))
        self.imag31.rect = self.imag31.image.get_rect().move(0, 0)
        self.imag32 = pygame.sprite.Sprite(all_sprites)
        self.imag32.image = pygame.transform.scale(load_image('egg.png'), (0, 0))
        self.imag32.rect = self.imag32.image.get_rect().move(0, 0)
        self.imag33 = pygame.sprite.Sprite(all_sprites)
        self.imag33.image = pygame.transform.scale(load_image('egg.png'), (0, 0))
        self.imag33.rect = self.imag33.image.get_rect().move(0, 0)
        self.imag34 = pygame.sprite.Sprite(all_sprites)
        self.imag34.image = pygame.transform.scale(load_image('egg.png'), (0, 0))
        self.imag34.rect = self.imag34.image.get_rect().move(0, 0)
        
        self.imag20 = pygame.sprite.Sprite(all_sprites)
        self.imag20.image = pygame.transform.scale(load_image('egg.png'), (0, 0))
        self.imag20.rect = self.imag20.image.get_rect().move(0, 0)
        self.imag21 = pygame.sprite.Sprite(all_sprites)
        self.imag21.image = pygame.transform.scale(load_image('egg.png'), (0, 0))
        self.imag21.rect = self.imag21.image.get_rect().move(0, 0)
        self.imag22 = pygame.sprite.Sprite(all_sprites)
        self.imag22.image = pygame.transform.scale(load_image('egg.png'), (0, 0))
        self.imag22.rect = self.imag22.image.get_rect().move(0, 0)
        self.imag23 = pygame.sprite.Sprite(all_sprites)
        self.imag23.image = pygame.transform.scale(load_image('egg.png'), (0, 0))
        self.imag23.rect = self.imag23.image.get_rect().move(0, 0)
        self.imag24 = pygame.sprite.Sprite(all_sprites)
        self.imag24.image = pygame.transform.scale(load_image('egg.png'), (0, 0))
        self.imag24.rect = self.imag24.image.get_rect().move(0, 0)
        
        self.imag10 = pygame.sprite.Sprite(all_sprites)
        self.imag10.image = pygame.transform.scale(load_image('egg.png'), (0, 0))
        self.imag10.rect = self.imag10.image.get_rect().move(0, 0)
        self.imag11 = pygame.sprite.Sprite(all_sprites)
        self.imag11.image = pygame.transform.scale(load_image('egg.png'), (0, 0))
        self.imag11.rect = self.imag11.image.get_rect().move(0, 0)
        self.imag12 = pygame.sprite.Sprite(all_sprites)
        self.imag12.image = pygame.transform.scale(load_image('egg.png'), (0, 0))
        self.imag12.rect = self.imag12.image.get_rect().move(0, 0)
        self.imag13 = pygame.sprite.Sprite(all_sprites)
        self.imag13.image = pygame.transform.scale(load_image('egg.png'), (0, 0))
        self.imag13.rect = self.imag13.image.get_rect().move(0, 0)
        self.imag14 = pygame.sprite.Sprite(all_sprites)
        self.imag14.image = pygame.transform.scale(load_image('egg.png'), (0, 0))
        self.imag14.rect = self.imag14.image.get_rect().move(0, 0)
        
        self.imag00 = pygame.sprite.Sprite(all_sprites)
        self.imag00.image = pygame.transform.scale(load_image('egg.png'), (0, 0))
        self.imag00.rect = self.imag00.image.get_rect().move(0, 0)
        self.imag01 = pygame.sprite.Sprite(all_sprites)
        self.imag01.image = pygame.transform.scale(load_image('egg.png'), (0, 0))
        self.imag01.rect = self.imag01.image.get_rect().move(0, 0)
        self.imag02 = pygame.sprite.Sprite(all_sprites)
        self.imag02.image = pygame.transform.scale(load_image('egg.png'), (0, 0))
        self.imag02.rect = self.imag02.image.get_rect().move(0, 0)
        self.imag03 = pygame.sprite.Sprite(all_sprites)
        self.imag03.image = pygame.transform.scale(load_image('egg.png'), (0, 0))
        self.imag03.rect = self.imag03.image.get_rect().move(0, 0)
        self.imag04 = pygame.sprite.Sprite(all_sprites)
        self.imag04.image = pygame.transform.scale(load_image('egg.png'), (0, 0))
        self.imag04.rect = self.imag04.image.get_rect().move(0, 0)        
        for i in range(4):
            qwe = []
            for j in range(5):
                qwe.append(0)
            self.pole.append(qwe)
            
    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)
        
    def get_cell(self, m):
        x = 0
        for i in range(365, 806, 110):
            y = 0            
            for j in range(260, 361, 100):
                if m[0] >= i and m[0] <= i + 110:
                    if m[1] >= j and m[1] <= j + 100:
                        if self.prov_yellow:
                            pygame.draw.rect(screen, (255, 255, 0), (i, j, 110, 100), 5)
                            self.rect_yellow = (i, j, 110, 100)
                            self.prov_yellow = False
                        else:
                            pygame.draw.rect(screen, (120, 120, 120), self.rect_yellow, 5)
                            self.prov_yellow = True
                        return x, y
                y += 1
            x += 1
        x = 0
        y = 2
        for i in range(20, 450, 100):
            y = 2        
            for j in range(30, 620, 500):
                if m[0] >= i and m[0] <= i + 75:
                    if m[1] >= j and m[1] <= j + 100:
                        if j > 200:
                            if self.prov_yellow:
                                pygame.draw.rect(screen, (255 , 255, 0), (i, j, 75, 100), 5)
                                self.rect_yellow = (i, j, 75, 100)
                                self.prov_yellow = False
                            else:
                                pygame.draw.rect(screen, (120, 120, 120), self.rect_yellow, 5)
                                self.prov_yellow = True                        
                        return x, y
                y += 1
            x += 1 
        if m[0] >= 565 and m[0] <= 715 and m[1] >= 70 and m[1] <= 220:
            if self.prov_yellow:
                pygame.draw.rect(screen, (255 , 255, 0), (565, 70, 150, 150), 5)
                self.rect_yellow = (565, 70, 150, 150)
                self.prov_yellow = False
            else:
                pygame.draw.rect(screen, (120, 120, 120), self.rect_yellow, 5)
                self.prov_yellow = True            
            return 'Enemy'
     # if m[0] >= 565 and m[0] <= 715 and m[1] >= 500 and m[1] <= 650: 
     # return 'You'
        if m[0] >= 949 and m[0] <= 985 and m[1] >= 342 and m[1] <= 378:
            global turn
            turn = False
            return None
        return None
    
    def prov(self, x, y):
        if self.pole[x][y] == 0:
            return True
        else:
            return False
    
    def izm(self, x, y, zn, kartinka=0, go=True):
        self.pole[x][y] = zn
        global ris_pole
        if x == 3 and zn != 0:
            qwe = kartinka + '.png'
            if y == 0:
                if go:
                    for i in range(920, 19, -45):
                        self.imag30.kill()
                        self.imag30 = pygame.sprite.Sprite(all_sprites)
                        self.imag30.image = pygame.transform.scale(load_image(qwe), (75, 100))
                        self.imag30.rect = self.imag30.image.get_rect().move(i, 534 - i // 5)
                        all_sprites.draw(screen)
                        pygame.display.flip()
                        ris_fon()                       
                else:
                    self.imag30.kill()
                    self.imag30 = pygame.sprite.Sprite(all_sprites)
                    self.imag30.image = pygame.transform.scale(load_image(qwe), (75, 100))
                    self.imag30.rect = self.imag30.image.get_rect().move(20, 530)                    
            elif y == 1:
                if go:
                    for i in range(930, 119, -45):
                        self.imag31.kill()
                        self.imag31 = pygame.sprite.Sprite(all_sprites)
                        self.imag31.image = pygame.transform.scale(load_image(qwe), (75, 100))
                        self.imag31.rect = self.imag31.image.get_rect().move(i, 554 - i // 5)
                        all_sprites.draw(screen)
                        pygame.display.flip()
                        ris_fon() 
                else:
                    self.imag31.kill()
                    self.imag31 = pygame.sprite.Sprite(all_sprites)
                    self.imag31.image = pygame.transform.scale(load_image(qwe), (75, 100))
                    self.imag31.rect = self.imag31.image.get_rect().move(120, 530) 
            elif y == 2:
                if go:
                    for i in range(920, 219, -35):
                        self.imag32.kill()
                        self.imag32 = pygame.sprite.Sprite(all_sprites)
                        self.imag32.image = pygame.transform.scale(load_image(qwe), (75, 100))
                        self.imag32.rect = self.imag32.image.get_rect().move(i, 574 - i // 5)
                        all_sprites.draw(screen)
                        pygame.display.flip()
                        ris_fon()  
                else:
                    self.imag32.kill()
                    self.imag32 = pygame.sprite.Sprite(all_sprites)
                    self.imag32.image = pygame.transform.scale(load_image(qwe), (75, 100))
                    self.imag32.rect = self.imag32.image.get_rect().move(220, 530) 
            elif y == 3:
                if go:
                    for i in range(920, 319, -60):
                        self.imag33.kill()
                        self.imag33 = pygame.sprite.Sprite(all_sprites)
                        self.imag33.image = pygame.transform.scale(load_image(qwe), (75, 100))
                        self.imag33.rect = self.imag33.image.get_rect().move(i, 594 - i // 5)
                        all_sprites.draw(screen)
                        pygame.display.flip()
                        ris_fon()  
                else:
                    self.imag33.kill()
                    self.imag33 = pygame.sprite.Sprite(all_sprites)
                    self.imag33.image = pygame.transform.scale(load_image(qwe), (75, 100))
                    self.imag33.rect = self.imag33.image.get_rect().move(320, 530) 
            elif y == 4:
                if go:
                    for i in range(920, 419, -50):
                        self.imag34.kill()
                        self.imag34 = pygame.sprite.Sprite(all_sprites)
                        self.imag34.image = pygame.transform.scale(load_image(qwe), (75, 100))
                        self.imag34.rect = self.imag34.image.get_rect().move(i, 614 - i // 5)
                        all_sprites.draw(screen)
                        pygame.display.flip()
                        ris_fon() 
                else:
                    self.imag34.kill()
                    self.imag34 = pygame.sprite.Sprite(all_sprites)
                    self.imag34.image = pygame.transform.scale(load_image(qwe), (75, 100))
                    self.imag34.rect = self.imag34.image.get_rect().move(420, 530) 
        elif x == 2 and zn != 0:
            if y == 0:
                if go:
                    for i in range(920, 19, -25):
                        self.imag20.kill()
                        self.imag20 = pygame.sprite.Sprite(all_sprites)
                        self.imag20.image = pygame.transform.scale(load_image(kartinka), (75, 100))
                        self.imag20.rect = self.imag20.image.get_rect().move(i, 26 + i // 5)
                        all_sprites.draw(screen)
                        pygame.display.flip()
                        ris_fon()  
                else:
                    self.imag20.kill()
                    self.imag20 = pygame.sprite.Sprite(all_sprites)
                    self.imag20.image = pygame.transform.scale(load_image(kartinka), (75, 100))
                    self.imag20.rect = self.imag20.image.get_rect().move(20, 30) 
            elif y == 1:
                if go:
                    for i in range(920, 119, -25):
                        self.imag21.kill()
                        self.imag21 = pygame.sprite.Sprite(all_sprites)
                        self.imag21.image = pygame.transform.scale(load_image(kartinka), (75, 100))
                        self.imag21.rect = self.imag21.image.get_rect().move(i, 6 + i // 5)
                        all_sprites.draw(screen)
                        pygame.display.flip()
                        ris_fon() 
                else:
                    self.imag21.kill()
                    self.imag21 = pygame.sprite.Sprite(all_sprites)
                    self.imag21.image = pygame.transform.scale(load_image(kartinka), (75, 100))
                    self.imag21.rect = self.imag21.image.get_rect().move(120, 30) 
            elif y == 2:
                if go:
                    for i in range(920, 219, -25):
                        self.imag22.kill()
                        self.imag22 = pygame.sprite.Sprite(all_sprites)
                        self.imag22.image = pygame.transform.scale(load_image(kartinka), (75, 100))
                        self.imag22.rect = self.imag22.image.get_rect().move(i, -14 + i // 5)
                        all_sprites.draw(screen)
                        pygame.display.flip()
                        ris_fon()  
                else:
                    self.imag22.kill()
                    self.imag22 = pygame.sprite.Sprite(all_sprites)
                    self.imag22.image = pygame.transform.scale(load_image(kartinka), (75, 100))
                    self.imag22.rect = self.imag22.image.get_rect().move(220, 30) 
            elif y == 3:
                if go:
                    for i in range(920, 319, -25):
                        self.imag23.kill()
                        self.imag23 = pygame.sprite.Sprite(all_sprites)
                        self.imag23.image = pygame.transform.scale(load_image(kartinka), (75, 100))
                        self.imag23.rect = self.imag23.image.get_rect().move(i, -34 + i // 5)
                        all_sprites.draw(screen)
                        pygame.display.flip()
                        ris_fon()  
                else:
                    self.imag23.kill()
                    self.imag23 = pygame.sprite.Sprite(all_sprites)
                    self.imag23.image = pygame.transform.scale(load_image(kartinka), (75, 100))
                    self.imag23.rect = self.imag23.image.get_rect().move(320, 30) 
            elif y == 4:
                if go:
                    for i in range(920, 419, -25):
                        self.imag24.kill()
                        self.imag24 = pygame.sprite.Sprite(all_sprites)
                        self.imag24.image = pygame.transform.scale(load_image(kartinka), (75, 100))
                        self.imag24.rect = self.imag24.image.get_rect().move(i, -54 + i // 5)
                        all_sprites.draw(screen)
                        pygame.display.flip()
                        ris_fon() 
                else:
                    self.imag24.kill()
                    self.imag24 = pygame.sprite.Sprite(all_sprites)
                    self.imag24.image = pygame.transform.scale(load_image(kartinka), (75, 100))
                    self.imag24.rect = self.imag24.image.get_rect().move(420, 30) 
        elif x == 1 and zn != 0:
            qwe = zn + '.png'
            if y == 0:
                self.imag10.kill()
                self.imag10 = pygame.sprite.Sprite(all_sprites)
                self.imag10.image = pygame.transform.scale(load_image(qwe), (110, 100))
                self.imag10.rect = self.imag10.image.get_rect().move(y * 110  + 365, 360)
            elif y == 1:
                self.imag11.kill()
                self.imag11 = pygame.sprite.Sprite(all_sprites)
                self.imag11.image = pygame.transform.scale(load_image(qwe), (110, 100))
                self.imag11.rect = self.imag11.image.get_rect().move(y * 110  + 365, 360)
            elif y == 2:
                self.imag12.kill()
                self.imag12 = pygame.sprite.Sprite(all_sprites)
                self.imag12.image = pygame.transform.scale(load_image(qwe), (110, 100))
                self.imag12.rect = self.imag12.image.get_rect().move(y * 110  + 365, 360)
            elif y == 3:
                self.imag13.kill()
                self.imag13 = pygame.sprite.Sprite(all_sprites)
                self.imag13.image = pygame.transform.scale(load_image(qwe), (110, 100))
                self.imag13.rect = self.imag13.image.get_rect().move(y * 110  + 365, 360)
            elif y == 4:
                self.imag14.kill()
                self.imag14 = pygame.sprite.Sprite(all_sprites)
                self.imag14.image = pygame.transform.scale(load_image(qwe), (110, 100))
                self.imag14.rect = self.imag14.image.get_rect().move(y * 110  + 365, 360)
        elif x == 0 and zn != 0:
            qwe = zn + '.png'
            if y == 0:
                self.imag00.kill()
                self.imag00 = pygame.sprite.Sprite(all_sprites)
                self.imag00.image = pygame.transform.scale(load_image(qwe), (110, 100))
                self.imag00.rect = self.imag00.image.get_rect().move(y * 110  + 365, 260)
            elif y == 1:
                self.imag01.kill()
                self.imag01 = pygame.sprite.Sprite(all_sprites)
                self.imag01.image = pygame.transform.scale(load_image(qwe), (110, 100))
                self.imag01.rect = self.imag01.image.get_rect().move(y * 110  + 365, 260)
            elif y == 2:
                self.imag02.kill()
                self.imag02 = pygame.sprite.Sprite(all_sprites)
                self.imag02.image = pygame.transform.scale(load_image(qwe), (110, 100))
                self.imag02.rect = self.imag02.image.get_rect().move(y * 110  + 365, 260)
            elif y == 3:
                self.imag03.kill()
                self.imag03 = pygame.sprite.Sprite(all_sprites)
                self.imag03.image = pygame.transform.scale(load_image(qwe), (110, 100))
                self.imag03.rect = self.imag03.image.get_rect().move(y * 110  + 365, 260)
            elif y == 4:
                self.imag04.kill()
                self.imag04 = pygame.sprite.Sprite(all_sprites)
                self.imag04.image = pygame.transform.scale(load_image(qwe), (110, 100))
                self.imag04.rect = self.imag04.image.get_rect().move(y * 110  + 365, 260)            
        elif x == 3 and zn == 0:          
            if y == 0:
                self.imag30.kill()
            elif y == 1:
                self.imag31.kill()
            elif y == 2:
                self.imag32.kill()
            elif y == 3:
                self.imag33.kill()
            elif y == 4:
                self.imag34.kill()
        elif x == 2 and zn == 0:
            if y == 0:
                self.imag20.kill()
            elif y == 1:
                self.imag21.kill()
            elif y == 2:
                self.imag22.kill()
            elif y == 3:
                self.imag23.kill()
            elif y == 4:
                self.imag24.kill()
        elif x == 1 and zn == 0:
            pass
        elif x == 0 and zn == 0:
            pass        
            
    def on_click(self, infa):
        if infa != None:
            if self.prov_click is None:
                self.prov_click = infa
            else:
                ban = 0
                global ris_pole
                if self.prov_click != 'Enemy':
                    if self.prov_click[1] == 3:
                        if infa[1] == 1:
                            g = self.pole[self.prov_click[1]][self.prov_click[0]]
                            global now_mana
                            if g == 'cheaken':
                                if now_mana - 1 < 0:
                                    ban = 1
                                else:
                                    now_mana -= 1
                            elif g == 'robot':
                                if now_mana - 3 < 0:
                                    ban = 1
                                else:
                                    now_mana -= 3                            
                            if ban == 0:
                                a = 25
                                if infa[0] == 0:
                                    gg = g + '.png'
                                    if self.prov_click[0] == 0:
                                        self.imag30.kill()
                                    elif self.prov_click[0] == 1:
                                        self.imag31.kill()
                                    elif self.prov_click[0] == 2:
                                        self.imag32.kill()
                                    elif self.prov_click[0] == 3:
                                        self.imag33.kill()
                                    elif self.prov_click[0] == 4:
                                        self.imag34.kill()                                 
                                    if 20 + self.prov_click[0] * 100 > 365:
                                        a *= -1
                                    for i in range(20 + self.prov_click[0] * 100, 366, a):
                                        self.imag10.kill()
                                        self.imag10 = pygame.sprite.Sprite(all_sprites)
                                        self.imag10.image = pygame.transform.scale(load_image(gg), (75, 100))
                                        if self.prov_click[0] == 0:
                                            self.imag10.rect = self.imag10.image.get_rect().move(i, 453 - i // 5)
                                        else:
                                            self.imag10.rect = self.imag10.image.get_rect().move(i, 453 - i // (self.prov_click[0] * 5))
                                        all_sprites.draw(screen)
                                        pygame.display.flip()
                                        ris_fon()
                                elif infa[0] == 1:
                                    gg = g + '.png'
                                    if self.prov_click[0] == 0:
                                        self.imag30.kill()
                                    elif self.prov_click[0] == 1:
                                        self.imag31.kill()
                                    elif self.prov_click[0] == 2:
                                        self.imag32.kill()
                                    elif self.prov_click[0] == 3:
                                        self.imag33.kill()
                                    elif self.prov_click[0] == 4:
                                        self.imag34.kill()                                                                      
                                    if 20 + self.prov_click[0] * 100 > 465:
                                        a *= -1
                                    for i in range(20 + self.prov_click[0] * 100, 466, a):
                                        self.imag11.kill()
                                        self.imag11 = pygame.sprite.Sprite(all_sprites)
                                        self.imag11.image = pygame.transform.scale(load_image(gg), (75, 100))
                                        if self.prov_click[0] == 0:
                                            self.imag11.rect = self.imag11.image.get_rect().move(i, 453 - i // 5)
                                        else:
                                            self.imag11.rect = self.imag11.image.get_rect().move(i, 453 - i // (self.prov_click[0] * 5))
                                        all_sprites.draw(screen)
                                        pygame.display.flip()
                                        ris_fon()
                                elif infa[0] == 2:
                                    gg = g + '.png'
                                    if self.prov_click[0] == 0:
                                        self.imag30.kill()
                                    elif self.prov_click[0] == 1:
                                        self.imag31.kill()
                                    elif self.prov_click[0] == 2:
                                        self.imag32.kill()
                                    elif self.prov_click[0] == 3:
                                        self.imag33.kill()
                                    elif self.prov_click[0] == 4:
                                        self.imag34.kill()                                    
                                    for i in range(20 + self.prov_click[0] * 100, 566, a):
                                        self.imag12.kill()
                                        self.imag12 = pygame.sprite.Sprite(all_sprites)
                                        self.imag12.image = pygame.transform.scale(load_image(gg), (75, 100))
                                        if self.prov_click[0] == 0:
                                            self.imag12.rect = self.imag12.image.get_rect().move(i, 453 - i // 5)
                                        else:
                                            self.imag12.rect = self.imag12.image.get_rect().move(i, 453 - i // (self.prov_click[0] * 5))
                                        all_sprites.draw(screen)
                                        pygame.display.flip()
                                        ris_fon() 
                                elif infa[0] == 3:
                                    gg = g + '.png'
                                    if self.prov_click[0] == 0:
                                        self.imag30.kill()
                                    elif self.prov_click[0] == 1:
                                        self.imag31.kill()
                                    elif self.prov_click[0] == 2:
                                        self.imag32.kill()
                                    elif self.prov_click[0] == 3:
                                        self.imag33.kill()
                                    elif self.prov_click[0] == 4:
                                        self.imag34.kill()                                                                   
                                    for i in range(20 + self.prov_click[0] * 100, 667, a):
                                        self.imag13.kill()
                                        self.imag13 = pygame.sprite.Sprite(all_sprites)
                                        self.imag13.image = pygame.transform.scale(load_image(gg), (75, 100))
                                        if self.prov_click[0] == 0:
                                            self.imag13.rect = self.imag13.image.get_rect().move(i, 463 - i // 5)
                                        else:
                                            self.imag13.rect = self.imag13.image.get_rect().move(i, 463 - i // (self.prov_click[0] * 5))
                                        all_sprites.draw(screen)
                                        pygame.display.flip()
                                        ris_fon() 
                                elif infa[0] == 4:
                                    gg = g + '.png'
                                    if self.prov_click[0] == 0:
                                        self.imag30.kill()
                                    elif self.prov_click[0] == 1:
                                        self.imag31.kill()
                                    elif self.prov_click[0] == 2:
                                        self.imag32.kill()
                                    elif self.prov_click[0] == 3:
                                        self.imag33.kill()
                                    elif self.prov_click[0] == 4:
                                        self.imag34.kill()                                                                
                                    if 20 + self.prov_click[0] * 100 > 465:
                                        a *= -1
                                    for i in range(20 + self.prov_click[0] * 100, 766, a):
                                        self.imag14.kill()
                                        self.imag14 = pygame.sprite.Sprite(all_sprites)
                                        self.imag14.image = pygame.transform.scale(load_image(gg), (75, 100))
                                        if self.prov_click[0] == 0:
                                            self.imag14.rect = self.imag14.image.get_rect().move(i, 473 - i // 5)
                                        else:
                                            self.imag14.rect = self.imag14.image.get_rect().move(i, 473 - i // (self.prov_click[0] * 5))
                                        all_sprites.draw(screen)
                                        pygame.display.flip()
                                        ris_fon() 
                                self.izm(infa[1], infa[0], g)
                                self.izm(self.prov_click[1], self.prov_click[0], 0)
                    elif self.prov_click[1] == 1:
                        if infa == 'Enemy':
                            global xp_e
                            g = self.pole[self.prov_click[1]][self.prov_click[0]]
                            if g == 'cheaken':
                                ataka = pygame.sprite.Sprite(all_sprites)
                                ataka.image = pygame.transform.scale(load_image('egg.png'), (50, 40))
                                ataka.rect = ataka.image.get_rect().move(640, 125)
                                all_sprites.draw(screen)
                                clock.tick(2.5)
                                pygame.display.flip()
                                clock.tick(2.5)
                                ataka.kill()
                                ris_fon()                                
                                xp_e -= 1
                            elif g == 'robot':
                                qwe = 'lighting' + str(self.prov_click[0]) + '.png'                           
                                ataka = pygame.sprite.Sprite(all_sprites)
                                ataka.image = pygame.transform.scale(load_image(qwe), (150, 140))
                                ataka.rect = ataka.image.get_rect().move(self.prov_click[0] * 55 + 475, 220)
                                all_sprites.draw(screen)
                                clock.tick(2.5)
                                pygame.display.flip()
                                clock.tick(2.5)
                                ataka.kill()
                                ris_fon() 
                                xp_e -= 3
                            
                    if self.prov_click[1] == 2:
                        if infa[1] == 0:
                            g = self.pole[self.prov_click[1]][self.prov_click[0]]
                            global now_mana_e
                            if g == 'cheaken':
                                if now_mana_e - 1 < 0:
                                    ban = 1
                                else:
                                    now_mana_e -= 1
                            elif g == 'robot':
                                if now_mana_e - 3 < 0:
                                    ban = 1
                                else:
                                    now_mana_e -= 3                            
                            if ban == 0:
                                a = 25
                                if infa[0] == 0:
                                    gg = g + '.png'
                                    if self.prov_click[0] == 0:
                                        self.imag20.kill()
                                    elif self.prov_click[0] == 1:
                                        self.imag21.kill()
                                    elif self.prov_click[0] == 2:
                                        self.imag22.kill()
                                    elif self.prov_click[0] == 3:
                                        self.imag23.kill()
                                    elif self.prov_click[0] == 4:
                                        self.imag24.kill()                                   
                                    if 20 + self.prov_click[0] * 100 > 365:
                                        a *= -1
                                    for i in range(20 + self.prov_click[0] * 100, 366, a):
                                        self.imag00.kill()
                                        self.imag00 = pygame.sprite.Sprite(all_sprites)
                                        self.imag00.image = pygame.transform.scale(load_image(gg), (75, 100))
                                        if self.prov_click[0] == 0:
                                            self.imag00.rect = self.imag00.image.get_rect().move(i, 183 + i // 5)
                                        else:
                                            self.imag00.rect = self.imag00.image.get_rect().move(i, 183 + i // (self.prov_click[0] * 5))
                                        all_sprites.draw(screen)
                                        pygame.display.flip()
                                        ris_fon()
                                elif infa[0] == 1:
                                    gg = g + '.png'
                                    if self.prov_click[0] == 0:
                                        self.imag20.kill()
                                    elif self.prov_click[0] == 1:
                                        self.imag21.kill()
                                    elif self.prov_click[0] == 2:
                                        self.imag22.kill()
                                    elif self.prov_click[0] == 3:
                                        self.imag23.kill()
                                    elif self.prov_click[0] == 4:
                                        self.imag24.kill()                                                                      
                                    if 20 + self.prov_click[0] * 100 > 465:
                                        a *= -1
                                    for i in range(20 + self.prov_click[0] * 100, 466, a):
                                        self.imag01.kill()
                                        self.imag01 = pygame.sprite.Sprite(all_sprites)
                                        self.imag01.image = pygame.transform.scale(load_image(gg), (75, 100))
                                        if self.prov_click[0] == 0:
                                            self.imag01.rect = self.imag01.image.get_rect().move(i, 173 + i // 5)
                                        else:
                                            self.imag01.rect = self.imag01.image.get_rect().move(i, 173 + i // (self.prov_click[0] * 5))
                                        all_sprites.draw(screen)
                                        pygame.display.flip()
                                        ris_fon() 
                                elif infa[0] == 2:
                                    gg = g + '.png'
                                    if self.prov_click[0] == 0:
                                        self.imag20.kill()
                                    elif self.prov_click[0] == 1:
                                        self.imag21.kill()
                                    elif self.prov_click[0] == 2:
                                        self.imag22.kill()
                                    elif self.prov_click[0] == 3:
                                        self.imag23.kill()
                                    elif self.prov_click[0] == 4:
                                        self.imag24.kill()                                    
                                    for i in range(20 + self.prov_click[0] * 100, 566, a):
                                        self.imag02.kill()
                                        self.imag02 = pygame.sprite.Sprite(all_sprites)
                                        self.imag02.image = pygame.transform.scale(load_image(gg), (75, 100))
                                        if self.prov_click[0] == 0:
                                            self.imag02.rect = self.imag02.image.get_rect().move(i, 163 + i // 5)
                                        else:
                                            self.imag02.rect = self.imag02.image.get_rect().move(i, 163 + i // (self.prov_click[0] * 5))
                                        all_sprites.draw(screen)
                                        pygame.display.flip()
                                        ris_fon() 
                                elif infa[0] == 3:
                                    gg = g + '.png'
                                    if self.prov_click[0] == 0:
                                        self.imag20.kill()
                                    elif self.prov_click[0] == 1:
                                        self.imag21.kill()
                                    elif self.prov_click[0] == 2:
                                        self.imag22.kill()
                                    elif self.prov_click[0] == 3:
                                        self.imag23.kill()
                                    elif self.prov_click[0] == 4:
                                        self.imag24.kill()                                                                      
                                    for i in range(20 + self.prov_click[0] * 100, 667, a):
                                        self.imag03.kill()
                                        self.imag03 = pygame.sprite.Sprite(all_sprites)
                                        self.imag03.image = pygame.transform.scale(load_image(gg), (75, 100))
                                        if self.prov_click[0] == 0:
                                            self.imag03.rect = self.imag03.image.get_rect().move(i, 153 + i // 5)
                                        else:
                                            self.imag03.rect = self.imag03.image.get_rect().move(i, 153 + i // (self.prov_click[0] * 5))
                                        all_sprites.draw(screen)
                                        pygame.display.flip()
                                        ris_fon() 
                                elif infa[0] == 4:
                                    gg = g + '.png'
                                    if self.prov_click[0] == 0:
                                        self.imag20.kill()
                                    elif self.prov_click[0] == 1:
                                        self.imag21.kill()
                                    elif self.prov_click[0] == 2:
                                        self.imag22.kill()
                                    elif self.prov_click[0] == 3:
                                        self.imag23.kill()
                                    elif self.prov_click[0] == 4:
                                        self.imag24.kill()                                                                     
                                    if 20 + self.prov_click[0] * 100 > 465:
                                        a *= -1
                                    for i in range(20 + self.prov_click[0] * 100, 766, a):
                                        self.imag04.kill()
                                        self.imag04 = pygame.sprite.Sprite(all_sprites)
                                        self.imag04.image = pygame.transform.scale(load_image(gg), (75, 100))
                                        if self.prov_click[0] == 0:
                                            self.imag04.rect = self.imag04.image.get_rect().move(i, 143 + i // 5)
                                        else:
                                            self.imag04.rect = self.imag04.image.get_rect().move(i, 143 + i // (self.prov_click[0] * 5))
                                        all_sprites.draw(screen)
                                        pygame.display.flip()
                                        ris_fon() 
                                self.izm(infa[1], infa[0], g)
                                self.izm(self.prov_click[1], self.prov_click[0], 0)
                    if self.prov_click[1] == 0:
                        if infa == 'you':
                            global xp_you
                        g = self.pole[self.prov_click[1]][self.prov_click[0]]
                        if g == 'cheaken':
                            ataka = pygame.sprite.Sprite(all_sprites)
                            ataka.image = pygame.transform.scale(load_image('egg.png'), (50, 40))
                            ataka.rect = ataka.image.get_rect().move(640, 550)
                            all_sprites.draw(screen)
                            clock.tick(2.5)
                            pygame.display.flip()
                            clock.tick(2.5)
                            ataka.kill()
                            ris_fon()                               
                            xp_you -= 1
                        elif g == 'robot':
                            qwe = 'lighting' + str(self.prov_click[0]) + '.png'                           
                            ataka = pygame.sprite.Sprite(all_sprites)
                            ataka.image = pygame.transform.scale(load_image(qwe), (150, 140))
                            ataka.rect = ataka.image.get_rect().move(self.prov_click[0] * 55 + 475, 420)
                            all_sprites.draw(screen)
                            clock.tick(2.5)
                            pygame.display.flip()
                            clock.tick(2.5)
                            ataka.kill()
                            ris_fon() 
                            xp_you -= 3
                        ris_pole = True
                self.prov_click = None
                        

    
class Card:
    def __init__(self, mana, yron, xp, kartinka=None):
        self.mana = mana
        self.yron = yron
        self.xp = xp
        self.kartinka = kartinka
        
    def ranen(self, yron):
        self.xp -= yron
        if xp <= 0:
            pass


class Cheaken(Card):
    def __init__(self):
        self.mana = 1
        self.yron = 1
        self.xp = 1
        self.kartinka = 'cheaken.png'


class Robot(Card):
    def __init__(self):
        self.mana = 3
        self.yron = 3
        self.xp = 3
        self.kartinka = 'robot.png'


class Titan(Card):
    def __init__(self):
        self.mana = 7
        self.yron = 7
        self.xp = 7
      #  self.kartinka = 


class Igrok:
    pass
    # Это класс учётной записи каждого игрока. Именно здесь мы задействуем
    # базу данных.


class Allcards:
    pass
    # Это класс всех карт.
    

def kollekchia():
    fontObj = pygame.font.Font('freesansbold.ttf', 40)
    textSurfaceObj = fontObj.render('Здесь будет вся коллекция карт', True, (255, 255, 255), (0, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (600, 250)
    screen.blit(textSurfaceObj, textRectObj)
    pygame.draw.rect(screen, (0, 120, 0), (100, 50, 100, 150), 3)
    pygame.draw.rect(screen, (0, 120, 0), (230, 50, 100, 150), 3)
    pygame.draw.rect(screen, (0, 120, 0), (360, 50, 100, 150), 3)    

def menu_yrovneu():
    fontObj = pygame.font.Font('freesansbold.ttf', 40)
    if level_igrok == 1:
        pygame.draw.circle(screen, (0, 0, 255), (401, 199), 35)
        textSurfaceObj = fontObj.render('1', True, (255, 255, 255), (0, 0, 255))
    else:
        pygame.draw.circle(screen, (0, 255, 0), (401, 199), 35)
        textSurfaceObj = fontObj.render('1', True, (255, 255, 255), (0, 255, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (400, 200)   
    screen.blit(textSurfaceObj, textRectObj)
    pygame.draw.circle(screen, (210, 105, 30), (400, 199), 35, 5)
    
    fontObj = pygame.font.Font('freesansbold.ttf', 40)
    if level_igrok == 2:
        pygame.draw.circle(screen, (0, 0, 255), (551, 299), 35)
        textSurfaceObj = fontObj.render('2', True, (255, 255, 255), (0, 0, 255))
    else:
        pygame.draw.circle(screen, (0, 255, 0), (551, 299), 35)
        textSurfaceObj = fontObj.render('2', True, (255, 255, 255), (0, 255, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (550, 300)
    screen.blit(textSurfaceObj, textRectObj)
    pygame.draw.circle(screen, (210, 105, 30), (550, 299), 35, 5)
    if level_igrok < 2:
        pygame.draw.rect(screen, (128, 128, 128), (510, 260, 80, 80), 5)
        pygame.draw.line(screen, (128, 128, 128), (510, 260), (590, 340), 5)
        pygame.draw.line(screen, (128, 128, 128), (590, 260), (510, 340), 5)
    
    fontObj = pygame.font.Font('freesansbold.ttf', 40)
    if level_igrok == 3:
        pygame.draw.circle(screen, (0, 0, 255), (701, 399), 35)
        textSurfaceObj = fontObj.render('3', True, (255, 255, 255), (0, 0, 255))
    else:
        pygame.draw.circle(screen, (0, 255, 0), (701, 399), 35)
        textSurfaceObj = fontObj.render('3', True, (255, 255, 255), (0, 255, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (700, 400)
    screen.blit(textSurfaceObj, textRectObj)
    pygame.draw.circle(screen, (210, 105, 30), (700, 399), 35, 5)
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
    
def vzat_carty(who, go=True):
    if who == 'you':
        global kolvo
        if kolvo <= 0:
            global xp_you
            global net_kart
            xp_you -= net_kart
            net_kart += 1
        else:
            kolvo -= 1
            if kolvo == 9:
                pygame.draw.rect(screen, (0, 0, 0), (1020, 380, 75, 210))
            for i in range(5):
                if board.prov(3, i):
                    qw = True
                    qwer = []
                    global cheaken
                    global robot
                    global titan
                    if cheaken > 0:
                        qwer.append('cheaken')
                    if robot > 0:
                        qwer.append('robot')
                    if titan > 0:
                        qwer.append('titan')
                    asd = random.choice(qwer)
                    if asd == 'cheaken':
                        cheaken -= 1
                    elif asd == 'robot':
                        robot -= 1
                    elif asd == 'titan':
                        titan -= 1
                    board.izm(3, i, asd, asd, go)
                    break
    else:
        global kolvo_e
        if kolvo_e <= 0:
            global xp_e
            global net_kart_e
            xp_e -= net_kart_e
            net_kart_e += 1
        else:
            kolvo_e -= 1
            if kolvo_e == 9:
                pygame.draw.rect(screen, (0, 0, 0), (1020, 150, 75, 210))
            for i in range(5):
                if board.prov(2, i):
                    qw = True
                    qwer = []
                    global cheaken_e
                    global robot_e
                    global titan_e
                    if cheaken_e > 0:
                        qwer.append('cheaken')
                    if robot_e > 0:
                        qwer.append('robot')
                    if titan_e > 0:
                        qwer.append('titan')
                    asd = random.choice(qwer)
                    if asd == 'cheaken':
                        cheaken_e -= 1
                    elif asd == 'robot':
                        robot_e -= 1
                    elif asd == 'titan':
                        titan_e -= 1
                    board.izm(2, i, asd, 'card.png', go)
                    break
                
def ris_fon():
    fon = pygame.sprite.Sprite(all_sprites)
    fon.image = pygame.transform.scale(load_image('fon.jpg'), (1280, 720))
    fon.rect = fon.image.get_rect().move(0, 0)
    screen.blit(fon.image, fon.rect)
    fon.kill()
    for i in range(365, 806, 110):
        for j in range(260, 361, 100):
            pygame.draw.rect(screen, (120, 120, 120), (i, j, 110, 100), 5)
    pygame.draw.rect(screen, (120, 120, 120), (565, 70, 150, 150), 5)
    pygame.draw.rect(screen, (120, 0, 0), (565, 500, 150, 150), 5)
    for i in range(20, 450, 100):
        for j in range(30, 620, 500):
            if j > 200:
                pygame.draw.rect(screen, (120, 120, 120), (i, j, 75, 100), 5)
            else:
                pygame.draw.rect(screen, (120, 0, 0), (i, j, 75, 100), 5)
    pygame.draw.rect(screen, (255, 153, 0), (930, 300, 74, 120))
    pygame.draw.circle(screen, (149, 80, 12), (967, 360), 20)
    fontObj = pygame.font.Font('freesansbold.ttf', 50)
    textSurfaceObj = fontObj.render(name, True, (0, 85, 255))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (640, 540)
    screen.blit(textSurfaceObj, textRectObj)
    
    fontObj = pygame.font.Font('freesansbold.ttf', 40)
    textSurfaceObj = fontObj.render(name_e, True, (0, 85, 255))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (640, 100)
    screen.blit(textSurfaceObj, textRectObj)
    
    fontObj = pygame.font.Font('freesansbold.ttf', 50)
    textSurfaceObj = fontObj.render(str(kolvo), True, (0, 85, 255))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (1050, 500)
    screen.blit(textSurfaceObj, textRectObj)
    pygame.draw.rect(screen, (0, 120, 0), (1015, 390, 70, 220), 3)
    
    fontObj = pygame.font.Font('freesansbold.ttf', 50)
    textSurfaceObj = fontObj.render(str(kolvo_e), True, (0, 85, 255))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (1050, 270)
    screen.blit(textSurfaceObj, textRectObj)
    pygame.draw.rect(screen, (0, 120, 0), (1015, 160, 70, 220), 3)
    
    pygame.draw.circle(screen, (200, 0, 0), (715, 650), 36)
    fontObj = pygame.font.Font('freesansbold.ttf', 45)
    textSurfaceObj = fontObj.render(str(xp_you), True, (255, 255, 255))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (715, 653)
    screen.blit(textSurfaceObj, textRectObj)
    
    pygame.draw.circle(screen, (200, 0, 0), (715, 220), 36) 
    fontObj = pygame.font.Font('freesansbold.ttf', 45)
    textSurfaceObj = fontObj.render(str(xp_e), True, (255, 255, 255))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (715, 223)
    screen.blit(textSurfaceObj, textRectObj)
    
    for i in range(7):
        n = 50 * i
        qw = [(770 + n, 40), (790 + n, 40), (800 + n, 58)]
        qw.append((790 + n, 76))
        qw.append((770 + n, 76))
        qw.append((760 + n, 58))
        if i < now_mana_e:
            pygame.draw.polygon(screen, (0, 191, 255), (qw))
        else:
            pygame.draw.polygon(screen, (0, 0, 255), (qw))
    for i in range(7):
        n = 50 * i
        qw = [(770 + n, 640), (790 + n, 640), (800 + n, 658)]
        qw.append((790 + n, 676))
        qw.append((770 + n, 676))
        qw.append((760 + n, 658))
        if i < now_mana:
            pygame.draw.polygon(screen, (0, 191, 255), (qw))
        else:
            pygame.draw.polygon(screen, (0, 0, 255), (qw))    
    
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
end_game = False
board = Board()
back_prov = True
kar_nachalo_prov = True
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
turn = True
prov_vzat_carty = True
start = True
kolvo_mana = 0
start_game = True
net_kart = 1
net_kart_e = 1
now_mana = 0
now_mana_e = 1
end_game_prov = True
enemy_turn = 0
ris_pole = True
fon6_prov = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if event.pos[0] >= width - 50 and event.pos[1] <= 50:
                terminate()      
        if ekran == 1:           
            fon1 = pygame.sprite.Sprite(all_sprites)
            fon1.image = pygame.transform.scale(load_image('fon1.jpg'), (1280, 720))
            fon1.rect = fon1.image.get_rect().move(0, 0)
            screen.blit(fon1.image, fon1.rect)
            fon1.kill()
            exit.kill()
            exit = pygame.sprite.Sprite(all_sprites)
            exit.image = pygame.transform.scale(load_image('kres.jpg'), (50, 50))
            exit.rect = exit.image.get_rect().move(width - 50, 0)            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.pos[0] >= 360 and event.pos[0] <= 920:
                    if event.pos[1] >= 500 and event.pos[1] <= 565:
                        ekran = 2                      
                        screen.fill((0, 0, 0))
                if event.pos[0] >= 290 and event.pos[0] <= 990:
                    if event.pos[1] >= 145 and event.pos[1] <= 210:
                        ekran = 3                       
                        screen.fill((0, 0, 0))
        elif ekran == 2:
            fon2 = pygame.sprite.Sprite(all_sprites)
            fon2.image = pygame.transform.scale(load_image('fon2.jpg'), (1280, 720))
            fon2.rect = fon1.image.get_rect().move(0, 0)
            screen.blit(fon2.image, fon2.rect)
            fon2.kill()
            exit.kill()
            exit = pygame.sprite.Sprite(all_sprites)
            exit.image = pygame.transform.scale(load_image('kres.jpg'), (50, 50))
            exit.rect = exit.image.get_rect().move(width - 50, 0)
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
            fon3 = pygame.sprite.Sprite(all_sprites)
            fon3.image = pygame.transform.scale(load_image('fon3.jpg'), (1280, 720))
            fon3.rect = fon3.image.get_rect().move(0, 0)
            screen.blit(fon3.image, fon3.rect)
            fon3.kill()
            exit.kill()
            exit = pygame.sprite.Sprite(all_sprites)
            exit.image = pygame.transform.scale(load_image('kres.jpg'), (50, 50))
            exit.rect = exit.image.get_rect().move(width - 50, 0)            
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
                if event.pos[0] >= 345 and event.pos[0] <= 935:
                    if event.pos[1] >= 355 and event.pos[1] <= 420:
                        ekran = 4
                        screen.fill((0, 0, 0))
                if event.pos[0] >= 190 and event.pos[0] <= 1090:
                    if event.pos[1] >= 515 and event.pos[1] <= 580:
                        ekran = 5
                        screen.fill((0, 0, 0))
                
        elif ekran == 4:
            fon = pygame.sprite.Sprite(all_sprites)
            fon.image = pygame.transform.scale(load_image('fon.jpg'), (1280, 720))
            fon.rect = fon.image.get_rect().move(0, 0)
            screen.blit(fon.image, fon.rect)
            exit.kill()
            exit = pygame.sprite.Sprite(all_sprites)
            exit.image = pygame.transform.scale(load_image('kres.jpg'), (50, 50))
            exit.rect = exit.image.get_rect().move(width - 50, 0)            
            fon.kill()            
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
            fon = pygame.sprite.Sprite(all_sprites)
            fon.image = pygame.transform.scale(load_image('fon.jpg'), (1280, 720))
            fon.rect = fon.image.get_rect().move(0, 0)
            screen.blit(fon.image, fon.rect)
            fon.kill()
            exit.kill()
            exit = pygame.sprite.Sprite(all_sprites)
            exit.image = pygame.transform.scale(load_image('kres.jpg'), (50, 50))
            exit.rect = exit.image.get_rect().move(width - 50, 0)            
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
            if ris_pole:
                fon = pygame.sprite.Sprite(all_sprites)
                fon.image = pygame.transform.scale(load_image('fon.jpg'), (1280, 720))
                fon.rect = fon.image.get_rect().move(0, 0)
                screen.blit(fon.image, fon.rect)
                fon.kill()
                exit.kill()
                exit = pygame.sprite.Sprite(all_sprites)
                exit.image = pygame.transform.scale(load_image('kres.jpg'), (50, 50))
                exit.rect = exit.image.get_rect().move(width - 50, 0)                
                for i in range(365, 806, 110):
                    for j in range(260, 361, 100):
                        pygame.draw.rect(screen, (120, 120, 120), (i, j, 110, 100), 5)
                pygame.draw.rect(screen, (120, 120, 120), (565, 70, 150, 150), 5)
                pygame.draw.rect(screen, (120, 0, 0), (565, 500, 150, 150), 5)
                for i in range(20, 450, 100):
                    for j in range(30, 620, 500):
                        if j > 200:
                            pygame.draw.rect(screen, (120, 120, 120), (i, j, 75, 100), 5)
                        else:
                            pygame.draw.rect(screen, (120, 0, 0), (i, j, 75, 100), 5)
                pygame.draw.rect(screen, (255, 153, 0), (930, 300, 74, 120))
                pygame.draw.circle(screen, (149, 80, 12), (967, 360), 20)
                ris_pole = False
            if level_play == 1 and start:
                name_e = 'Тролль'
                kolvo_e = 7
                cheaken_e = 6
                robot_e = 1
                titan_e = 0
                start = False
                xp_you = 45
                xp_e = 15
            elif level_play == 2 and start:
                name_e = 'Тролль'
                kolvo_e = 8
                cheaken_e = 3
                robot_e = 4
                titan_e = 1
                start = False
                xp_you = 35
                xp_e = 20
            elif level_play == 3 and start:
                name_e = 'Тролль'
                kolvo_e = 13
                cheaken_e = 4
                robot_e = 6
                titan_e = 3
                start = False
                xp_you = 25
                xp_e = 30
            fontObj = pygame.font.Font('freesansbold.ttf', 50)
            textSurfaceObj = fontObj.render(str(kolvo), True, (0, 85, 255))
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (1050, 500)
            screen.blit(textSurfaceObj, textRectObj)
            pygame.draw.rect(screen, (0, 120, 0), (1015, 390, 70, 220), 3)
            
            fontObj = pygame.font.Font('freesansbold.ttf', 50)
            textSurfaceObj = fontObj.render(str(kolvo_e), True, (0, 85, 255))
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (1050, 270)
            screen.blit(textSurfaceObj, textRectObj)
            pygame.draw.rect(screen, (0, 120, 0), (1015, 160, 70, 220), 3)
            
            pygame.draw.circle(screen, (200, 0, 0), (715, 650), 36)
            fontObj = pygame.font.Font('freesansbold.ttf', 45)
            textSurfaceObj = fontObj.render(str(xp_you), True, (255, 255, 255))
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (715, 653)
            screen.blit(textSurfaceObj, textRectObj)
            
            pygame.draw.circle(screen, (200, 0, 0), (715, 220), 36) 
            fontObj = pygame.font.Font('freesansbold.ttf', 45)
            textSurfaceObj = fontObj.render(str(xp_e), True, (255, 255, 255))
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (715, 223)
            screen.blit(textSurfaceObj, textRectObj)
            
            fontObj = pygame.font.Font('freesansbold.ttf', 50)
            textSurfaceObj = fontObj.render(name, True, (0, 85, 255))
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (640, 540)
            screen.blit(textSurfaceObj, textRectObj)
            
            fontObj = pygame.font.Font('freesansbold.ttf', 40)
            textSurfaceObj = fontObj.render(name_e, True, (0, 85, 255))
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (640, 100)
            screen.blit(textSurfaceObj, textRectObj)
            for i in range(7):
                n = 50 * i
                qw = [(770 + n, 40), (790 + n, 40), (800 + n, 58)]
                qw.append((790 + n, 76))
                qw.append((770 + n, 76))
                qw.append((760 + n, 58))
                if i < now_mana_e:
                    pygame.draw.polygon(screen, (0, 191, 255), (qw))
                else:
                    pygame.draw.polygon(screen, (0, 0, 255), (qw))
            for i in range(7):
                n = 50 * i
                qw = [(770 + n, 640), (790 + n, 640), (800 + n, 658)]
                qw.append((790 + n, 676))
                qw.append((770 + n, 676))
                qw.append((760 + n, 658))
                if i < now_mana:
                    pygame.draw.polygon(screen, (0, 191, 255), (qw))
                else:
                    pygame.draw.polygon(screen, (0, 0, 255), (qw))
            if start_game:
                for i in range(3):
                    vzat_carty('you', False)                
                    vzat_carty('enemy', False)
                vzat_carty('enemy', False)
                start_game = False
            if turn:
                if prov_vzat_carty:
                    vzat_carty('you')
                    if kolvo_mana < 7:
                        kolvo_mana += 1
                    now_mana = kolvo_mana
                    prov_vzat_carty = False
                    enemy_turn = 0
            else:
                if enemy_turn == 0:
                    vzat_carty('enemy')
                    now_mana_e = kolvo_mana
                    if xp_e > 0:  
                        for i in range(3):
                            sp_rand = []
                            rand = random.randrange(0, 5)
                            while board.prov(2, rand):
                                sp_rand.append(rand)
                                if len(sp_rand) == 5:
                                    rand = None
                                    break
                                rand = random.randrange(0, 5)
                                while rand in sp_rand:
                                    rand = random.randrange(0, 5)
                            sp_rand = []
                            rand_2 = random.randrange(0, 5)
                            while board.prov(0, rand_2) is False:
                                sp_rand.append(rand_2)
                                if len(sp_rand) == 5:
                                    rand_2 = None
                                    break
                                rand_2 = random.randrange(0, 5)
                                while rand_2 in sp_rand:
                                    rand_2 = random.randrange(0, 5)
                            if rand != None and rand_2 != None:
                                board.on_click((rand, 2))
                                board.on_click((rand_2, 0))
                if xp_e > 0:
                    if board.prov(0, enemy_turn) is False:
                        board.on_click((enemy_turn, 0))
                        board.on_click('you')
                prov_vzat_carty = True
                if enemy_turn == 4:
                    turn = True
                enemy_turn += 1
            if xp_you <= 0 and end_game_prov:
                boom = pygame.sprite.Sprite(all_sprites)
                boom.image = pygame.transform.scale(load_image('boom.png'), (150, 150))
                boom.rect = boom.image.get_rect().move(565, 500)
                
                fontObj = pygame.font.Font('freesansbold.ttf', 45)
                textSurfaceObj = fontObj.render('You lose!', True, (0, 85, 255))
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (200, 200)
                screen.blit(textSurfaceObj, textRectObj)
                
                fontObj = pygame.font.Font('freesansbold.ttf', 45)
                textSurfaceObj = fontObj.render('Вернуться в меню', True, (0, 85, 255))
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (200, 300)
                screen.blit(textSurfaceObj, textRectObj)                
                end_game_prov = False
                end_game = True
            elif xp_e <= 0 and end_game_prov:
                boom = pygame.sprite.Sprite(all_sprites)
                boom.image = pygame.transform.scale(load_image('boom.png'), (150, 150))
                boom.rect = boom.image.get_rect().move(565, 70) 

                fontObj = pygame.font.Font('freesansbold.ttf', 55)
                textSurfaceObj = fontObj.render('You win!', True, (0, 85, 255))
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (200, 200)
                screen.blit(textSurfaceObj, textRectObj)
                
                fontObj = pygame.font.Font('freesansbold.ttf', 30)
                textSurfaceObj = fontObj.render('Вернуться в меню', True, (0, 85, 255))
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (200, 300)
                screen.blit(textSurfaceObj, textRectObj)
                end_game = True
                end_game_prov = False
            if end_game is False:
                if event.type ==  pygame.MOUSEBUTTONDOWN:
                    board.get_click(event.pos)
            else:
                if event.type ==  pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] >= 63 and event.pos[0] <= 337:
                        if event.pos[1] >= 285 and event.pos[1] <= 316:
                            screen.fill((0, 0, 0))
                            all_sprites.empty()
                            end_game = False
                            board = Board()
                            back_prov = True
                            enemy_turn = 0
                            kar_nachalo_prov = True
                            con = sqlite3.connect("cards_tab.db")
                            cur = con.cursor()
                            result = cur.execute("SELECT * FROM cards_tab").fetchall()
                            name = result[0][0]
                            kolvo = result[0][2]
                            cheaken = result[0][3]
                            robot = result[0][4]
                            titan = result[0][5]
                            cheaken += 2
                            robot += 1
                            titan += 1
                            kolvo += 4
                            turn = True
                            prov_vzat_carty = True
                            start = True
                            kolvo_mana = 0
                            net_kart = 1
                            net_kart_e = 1
                            now_mana = 0
                            now_mana_e = 1
                            end_game_prov = True
                            ris_pole = True
                            start_game = True
                            if xp_you > 0:
                                if level_play >= level_igrok:
                                    level_igrok += 1
                            ekran = 3
        all_sprites.draw(screen)
    pygame.display.flip()
terminate()