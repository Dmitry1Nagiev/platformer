import pygame
from script import load_image
player_image = load_image('assets/images/player')
stop_image = pygame.image.load('assets/images/blocks/stop.png').convert_alpha()
fireball_image = load_image('assets/images/Fireball')
enemy_image1 = load_image('assets/images/enemy/1')
enemy_image2 = load_image('assets/images/enemy/2')
enemy_image3 = load_image('assets/images/enemy/3')
#pygame.image.load('assets/images/enemy/2/1.png').convert_alpha(),
#npc_image = load_image('assets/images/NPC')
npc_image = load_image('assets/images/NPC/npc')
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
button_image = pygame.image.load('assets/images/button/button.png')
collect_sound = pygame.mixer.Sound('assets/sounds/sounds/collect.mp3')
exit_sound = pygame.mixer.Sound('assets/sounds/sounds/exit.mp3')
fall_down_sound = pygame.mixer.Sound('assets/sounds/sounds/fall_down.mp3')
jump_sound = pygame.mixer.Sound('assets/sounds/sounds/jump.mp3')
level_up_sound = pygame.mixer.Sound('assets/sounds/sounds/level_up.mp3')
victory_sound = pygame.mixer.Sound('assets/sounds/sounds/the-sound-of-victory-in-the-game-level.wav')