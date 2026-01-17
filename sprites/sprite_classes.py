import pygame




class Portal(pygame.sprite.Sprite):
    def __init__(self,image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self,step,player_group,player):
        self.rect.x += step
class Coin(pygame.sprite.Sprite):
    def __init__(self,image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self,step,player_group,player):
        self.rect.x += step
class Enemy(pygame.sprite.Sprite):
    def __init__(self,image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 1
        self.dir= 1
    def update(self,step,player_group,player,stopenemy_group):
        self.rect.x += step
        if self.dir == 1:
            self.rect.x += self.speed
        elif self.dir == -1:
            self.rect.x -= self.speed
        if pygame.sprite.spritecollide(self,stopenemy_group,False):
            self.speed * -1
class StopEnemy(pygame.sprite.Sprite):
    def __init__(self,image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self,step,player_group,player,stopenemy_group):
        self.rect.x += step
        if pygame.sprite.spritecollide(self,player_group,False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
            if abs(self.rect.left - player.rect.right) < 15 \
                    and abs(self.rect.centery - player.rect.centery) < 50:
                player.rect.right = self.rect.left
            if abs(self.rect.right - player.rect.left) > 15 \
                    and abs(self.rect.centery + player.rect.centery) > 50:
                player.rect.left = self.rect.right

class Box(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self,step,player_group,player,stopenemy_group):
        self.rect.x += step
        if pygame.sprite.spritecollide(self,player_group,False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
            if abs(self.rect.left - player.rect.right) < 15 \
                    and abs(self.rect.centery - player.rect.centery) < 50:
                player.rect.right = self.rect.left
            if abs(self.rect.right - player.rect.left) > 15 \
                    and abs(self.rect.centery + player.rect.centery) > 50:
                player.rect.left = self.rect.right
class Ground(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self,step,player_group,player,stopenemy_group):
        self.rect.x += step
        if pygame.sprite.spritecollide(self,player_group,False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
            if abs(self.rect.left - player.rect.right) < 15 \
                    and abs(self.rect.centery - player.rect.centery) < 50:
                player.rect.right = self.rect.left
            if abs(self.rect.right - player.rect.left) > 15 \
                    and abs(self.rect.centery + player.rect.centery) > 50:
                player.rect.left = self.rect.right
class Sand(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self,step,player_group,player,stopenemy_group):
        self.rect.x += step
        if pygame.sprite.spritecollide(self,player_group,False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
            if abs(self.rect.left - player.rect.right) < 15 \
                    and abs(self.rect.centery - player.rect.centery) < 50:
                player.rect.right = self.rect.left
            if abs(self.rect.right - player.rect.left) > 15 \
                    and abs(self.rect.centery + player.rect.centery) > 50:
                player.rect.left = self.rect.right
class Water(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self,step,player_group, player, stopenemy_group):
        self.rect.x += step

        if pygame.sprite.spritecollide(self,player_group,False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
            if abs(self.rect.left - player.rect.right) < 15 \
                    and abs(self.rect.centery - player.rect.centery) < 50:
                player.rect.right = self.rect.left
            if abs(self.rect.right - player.rect.left) > 15 \
                    and abs(self.rect.centery + player.rect.centery) > 50:
                player.rect.left = self.rect.right
class Player(pygame.sprite.Sprite):

    def __init__(self,image,pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 5
        self.velocity_y = 0
        self.on_ground = True

    def update(self,scroll_group,player_image):



        key= pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.image = pygame.transform.flip(player_image, False, False)
            self.rect.x += self.speed
            if self.rect.right > 750:
                self.rect.right= 750
                scroll_group.update(-self.speed)

        if key[pygame.K_a]:
            self.image= pygame.transform.flip(player_image, True, False)
            self.rect.x -= self.speed
            if self.rect.left < 250:
                self.rect.left= 250
                scroll_group.update(-self.speed)

        if key[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = -15
            self.on_ground = False
            self.rect.y += self.velocity_y
            self.velocity_y += 1
        if self.velocity_y > 10:
            self.velocity_y = 10

