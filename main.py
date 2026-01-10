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
    global box_group, ground_group,sand_group,water_group,player_group, scroll_group
    scroll_group= pygame.sprite.Group
    box_group = pygame.sprite.Group()
    ground_group = pygame.sprite.Group()
    sand_group = pygame.sprite.Group()
    water_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()




def lvlGame():
    global box_group, ground_group,sand_group,water_group,player_group

    box_group.draw(window)
    ground_group.draw(window)
    sand_group.draw(window)
    water_group.draw(window)
    box_group.update()
    ground_group.update()
    sand_group.update()
    water_group.update()

    player = Player(player_image, (160,240))
    player_group.add(player)
    pygame.display.update()



def drawMap (mapFile):
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

