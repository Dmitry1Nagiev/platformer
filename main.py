import pygame
import sys
import random
from sprites.sprite_classes import *



GREY = (210,210,210)
WIDTH = 1200
HEIGHT = 800
FPS = 60
pygame.init()

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Platformer')
clock = pygame.time.Clock()
from load import *

def restart():
    global box_group, player, ground_group,sand_group,water_group,player_group, scroll_group, portal_group, enemy_group, coin_group,stopenemy_group
    scroll_group= pygame.sprite.Group()
    box_group = pygame.sprite.Group()
    ground_group = pygame.sprite.Group()
    sand_group = pygame.sprite.Group()
    water_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    portal_group = pygame.sprite.Group()
    coin_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    stopenemy_group = pygame.sprite.Group()
    player = Player(player_image, (100, 560))
    player_group.add(player)




def lvlGame():
    global box_group, player,ground_group,sand_group,water_group,player_group, scroll_group, portal_group, enemy_group, coin_group,stopenemy_group

    box_group.draw(window)
    ground_group.draw(window)
    sand_group.draw(window)
    water_group.draw(window)
    player_group.draw(window)
    stopenemy_group.draw(window)
    portal_group.draw(window)
    enemy_group.draw(window)
    coin_group.draw(window)

    step = 0

    ground_group.update(step,player_group,player,stopenemy_group)
    sand_group.update(step,player_group,player,stopenemy_group)
    water_group.update(step,player_group,player,stopenemy_group)
    portal_group.update(step,player_group,player,stopenemy_group)
    box_group.update(step,player_group,player,stopenemy_group)
    stopenemy_group.update(step,player_group,player,stopenemy_group)
    coin_group.update(step,player_group,player,stopenemy_group)
    enemy_group.update(step,player_group,player,stopenemy_group)
    player_group.update(player_image,scroll_group,player_group,player,stopenemy_group)



    pygame.display.update()



def drawMap (mapFile):
    global box_group, ground_group, sand_group, water_group, player_group, scroll_group, portal_group, enemy_group, coin_group,stopenemy_group
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
                enemy1 = Enemy(enemy1_image,pos)
                enemy_group.add(enemy1)
                scroll_group.add(enemy1)
            elif game_map[i][j] == '7' :
                enemy2 = Enemy(enemy2_image, pos)
                enemy_group.add(enemy2)
                scroll_group.add(enemy2)
            elif game_map[i][j] == '8':
                enemy3 = Enemy(enemy3_image,pos)
                enemy_group.add(enemy3)
                scroll_group.add(enemy3)
            elif game_map[i][j] == '9':
                portal = Portal(portal_image, pos)
                portal_group.add(portal)
                scroll_group.add(portal)
            elif game_map[i][j] == '-1':
                coin = Coin(coin_image,pos)
                coin_group.add(coin)
                scroll_group.add(coin)






restart()
drawMap('game_lvl/level2.txt')






while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()




    window.fill(GREY)

    lvlGame()

