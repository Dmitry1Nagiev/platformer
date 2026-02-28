import pygame
import sys
import random

import pygwidgets
from pygwidgets import *
from sprites.sprite_classes import *



GREY = (210,210,210)
WIDTH = 1200
HEIGHT = 800
FPS = 60


LEVELS = {1:'game_lvl/level2.txt',
          2:'game_lvl/level3.txt'}

HP_BAR_WIDTH = 300
HP_BAR_HEIGHT = 30
HP_BAR_X = 200
HP_BAR_Y = 20




pygame.init()

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Platformer')
clock = pygame.time.Clock()
from load import *
hp = 100
hp_text = pygwidgets.DisplayText(window, (200,20), 'HP: 100',
                                         fontSize = 40, textColor = (0,0,0))

def restart():
    global box_group, player, ground_group,sand_group,water_group,player_group, scroll_group, portal_group, enemy_group, coin_group,stopenemy_group,hp,hp_text,npc_group,quest_text,quest_visible,coin_text,shet
    stopenemy_group = pygame.sprite.Group()
    scroll_group= pygame.sprite.Group()
    box_group = pygame.sprite.Group()
    ground_group = pygame.sprite.Group()
    sand_group = pygame.sprite.Group()
    water_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    portal_group = pygame.sprite.Group()
    coin_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    npc_group = pygame.sprite.Group()

    player = Player(player_image[0], (200, 460))
    player_group.add(player)
    hp = 100
    #hp_text = pygwidgets.DisplayText(window, (200, 20), 'HP: 100',
                                     #fontSize=40, textColor=(0, 0, 0))
    quest_text = DisplayText(window,(0,0), 'Collect 4 coins',
                                                     'Comic Sans',fontSize=20,
                                                     textColor=(0,0,0),
                                                    backgroundColor=(255,255,200))
    coin_text = pygwidgets.DisplayText(window, (0, 0), 'Coins: 0',
                                       fontSize=50, textColor=(255, 255, 255))
    quest_visible = False
    shet = 0






def lvlGame():
    global box_group, player,ground_group,sand_group,water_group,player_group, scroll_group, portal_group, enemy_group, coin_group,stopenemy_group,hp,hp_text,npc_group,quest_text,quest_visible,coin_text,shet,gameOver,level
    stopenemy_group.draw(window)
    box_group.draw(window)
    ground_group.draw(window)
    sand_group.draw(window)
    water_group.draw(window)
    player_group.draw(window)
    npc_group.draw(window)
    portal_group.draw(window)
    enemy_group.draw(window)
    coin_group.draw(window)

    gameOver =False


    step = 0

    ground_group.update(step,player_image,scroll_group,player_group,player,stopenemy_group,coin_group,enemy_image1,FPS,portal_image,enemy_image2,enemy_image3,npc_image)
    sand_group.update(step,player_image,scroll_group,player_group,player,stopenemy_group,coin_group,enemy_image1,FPS,portal_image,enemy_image2,enemy_image3,npc_image)
    water_group.update(step,player_image,scroll_group,player_group,player,stopenemy_group,coin_group,enemy_image1,FPS,portal_image,enemy_image2,enemy_image3,npc_image)
    portal_group.update(step,player_image,scroll_group,player_group,player,stopenemy_group,coin_group,enemy_image1,FPS,portal_image,enemy_image2,enemy_image3,npc_image)
    box_group.update(step,player_image,scroll_group,player_group,player,stopenemy_group,coin_group,enemy_image1,FPS,portal_image,enemy_image2,enemy_image3,npc_image)
    stopenemy_group.update(step,player_image,scroll_group,player_group,player,stopenemy_group,coin_group,enemy_image1,FPS,portal_image,enemy_image2,enemy_image3,npc_image)
    coin_group.update(step,player_image,scroll_group,player_group,player,stopenemy_group,coin_group,enemy_image1,FPS,portal_image,enemy_image2,enemy_image3,npc_image)
    enemy_group.update(step,player_image,scroll_group,player_group,player,stopenemy_group,coin_group,enemy_image1,FPS,portal_image,enemy_image2,enemy_image3,npc_image)
    player_group.update(player_image,scroll_group,player_group,player,stopenemy_group,coin_group,enemy_image1,FPS,portal_image,enemy_image2,enemy_image3,npc_image)
    npc_group.update(step,player_image,scroll_group,player_group,player,stopenemy_group,coin_group,enemy_image1,FPS,portal_image,enemy_image2,enemy_image3,npc_image)
    Color = 0

    quest_visible = False

    for npc in npc_group:
        distance = abs(player.rect.centerx - npc.rect.centerx)

        if distance < 100:
            quest_visible = True
            quest_text.setLoc((npc.rect.centerx - 80, npc.rect.top - 40))


    hit_coin = pygame.sprite.spritecollide(player, coin_group, False)
    hit_enemies = pygame.sprite.spritecollide(player,enemy_group,False)
    hit_water = pygame.sprite.spritecollide(player,water_group,False)

    if pygame.sprite.spritecollide(player,portal_group,False) and shet >= 4:
        level += 1


        if level in LEVELS:
            player.rect.topleft = (320,560)
            load_level()
        else:
            gameOver = True
    if gameOver:
        game_over_text = pygwidgets.DisplayText(window,(500,200),
                                                'COMPLETED', 'Conic Sans',
                                                fontSize=40,
                                                textColor=(0,220,0))
        game_over_text.draw()
        player_group.empty()
        enemy_group.empty()
        portal_group.empty()





    for coin in hit_coin:
        if hit_coin:
            coin.kill()
            shet += 1
            coin_text.setValue(f'Coins: {shet}')
            print(0)

    for water in hit_water:
        if hit_water:
            player.kill()
            restart()
            drawMap('game_lvl/level2.txt')


    for enemy in hit_enemies:
        if player.velocity_y > 0 and \
            player.rect.bottom - enemy.rect.top < 20:
            player.velocity_y -= 30
            enemy.kill()
        else:
            if not player.invulnerable:
                hp -= 10
                player.invulnerable = True
                player.velocity_y -= 20
                player.rect.x -= 10
                #hp_text.setValue(f'HP: {hp}')
            if hp <= 0:
                player.kill()
                restart()
                drawMap('game_lvl/level2.txt')
                return
    if hp >=60:
        Color = (0, 200, 0)
    if hp > 30 and hp < 60:
        Color = (255, 69, 0)
    if hp <= 30:
        Color = (139, 0, 0)

    pygame.draw.rect(window, (150, 150, 150), (HP_BAR_X, HP_BAR_Y, HP_BAR_WIDTH, HP_BAR_HEIGHT))

    current_width = (hp / 100) * HP_BAR_WIDTH

    pygame.draw.rect(window, (Color),
                     (HP_BAR_X, HP_BAR_Y, current_width, HP_BAR_HEIGHT))
    pygame.draw.rect(window, (0, 0, 0),
                     (HP_BAR_X, HP_BAR_Y, HP_BAR_WIDTH, HP_BAR_HEIGHT), 2)



    for enemy in enemy_group:
        enemy.move(FPS, stopenemy_group, enemy_image1, enemy_image2, enemy_image3)
    if quest_visible:
        quest_text.draw()
    coin_text.draw()
    pygame.display.update()

def load_level():
    global level

    box_group.empty()
    ground_group.empty()
    water_group.empty()
    sand_group.empty()
    enemy_group.empty()
    npc_group.empty()
    coin_group.empty()
    stopenemy_group.empty()
    portal_group.empty()
    restart()
    drawMap(LEVELS[level])




def drawMap (mapFile):
    global box_group, ground_group, sand_group, water_group, player_group, scroll_group, portal_group, enemy_group, coin_group,stopenemy_group,npc_group
    game_map = []

    with open(mapFile,'r') as file:
        for i in range(0,10):
            game_map.append(file.readline().replace('\n','').split(','))

    pos = [0,0]
    for i in range(0,10):
        pos[1] = i * 80
        for j in range(0,100):
            pos[0]= j * 80
            if game_map[i][j] == '1':
                box = Box(box_image,pos)
                box_group.add(box)
                scroll_group.add(box)
            elif game_map[i][j] == '2':
                ground = Ground(center_image,pos)
                ground_group.add(ground)
                scroll_group.add(ground)
            elif game_map[i][j] == '3':
                sand = Sand(earth_image,pos)
                sand_group.add(sand)
                scroll_group.add(sand)
            elif game_map[i][j] == '4':
                water = Water(water_image,pos)
                water_group.add(water)
                scroll_group.add(water)
            elif game_map[i][j] == '5':
                stopenemy = StopEnemy(stop_image,pos)
                stopenemy_group.add(stopenemy)
                scroll_group.add(stopenemy)
            elif game_map[i][j] == '6' :
                enemy1 = Enemy(enemy_image1,pos)
                enemy_group.add(enemy1)
                scroll_group.add(enemy1)
            elif game_map[i][j] == '7' :
                enemy2 = Enemy(enemy_image2, pos)
                enemy_group.add(enemy2)
                scroll_group.add(enemy2)
            elif game_map[i][j] == '8':
                enemy3 = Enemy(enemy_image3,pos)
                enemy_group.add(enemy3)
                scroll_group.add(enemy3)
            elif game_map[i][j] == '9':
                portal = Portal(portal_image[0], pos)
                portal_group.add(portal)
                scroll_group.add(portal)
            elif game_map[i][j] == '-1':
                coin = Coin(coin_image,pos)
                coin_group.add(coin)
                scroll_group.add(coin)
            elif game_map[i][j] == '-2':
                npc = Npc(npc_image[0],pos)
                npc_group.add(npc)
                scroll_group.add(npc)



schet = 0
level = 1

restart()
drawMap(LEVELS[level])







while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()





    window.fill(GREY)

    lvlGame()

