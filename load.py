import pygame
from script import load_image
player_image = load_image('assets/images/player')
stop_image = pygame.image.load('assets/images/blocks/stop.png').convert_alpha()
fireball_image = load_image('assets/images/Fireball')
enemy_image1 = load_image('assets/images/enemy/1')
enemy_image2 = load_image('assets/images/enemy/2')
enemy_image3 = load_image('assets/images/enemy/3')
#pygame.image.load('assets/images/enemy/2/1.png').convert_alpha(),

#pygame.image.load('assets/images/enemy/3/1.png').convert_alpha()]
portal_image = load_image('assets/images/portal')

portal_image1 = pygame.image.load('assets/images/portal/Portal_100x100px1.png').convert_alpha()

coin_image = pygame.image.load('assets/images/item/monetka.png').convert_alpha()

player_image1 = [pygame.image.load('assets/images/player/1.png').convert_alpha(),
                pygame.image.load('assets/images/player/2.png').convert_alpha(),
                pygame.image.load('assets/images/player/3.png').convert_alpha()]
box_image = pygame.image.load('assets/images/blocks/box.png').convert_alpha()
water_image = pygame.image.load('assets/images/blocks/water.png').convert_alpha()
center_image = pygame.image.load('assets/images/blocks/center.png').convert_alpha()
earth_image = pygame.image.load('assets/images/blocks/earth.png').convert_alpha()
