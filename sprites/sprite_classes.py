import pygame




class Portal(pygame.sprite.Sprite):
    def __init__(self,image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.anime = False


    def animation(self,portal_image,FPS):
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.01:
                if self.frame ==len(portal_image) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0
    def update(self,step,player_image,scroll_group,player_group,player,stopenemy_group,coin_group,enemy_image1,FPS,portal_image,enemy_image2,enemy_image3):
        self.anime = True
        self.image = portal_image[self.frame]
        self.rect.x += step
        self.animation(portal_image,FPS)

class Coin(pygame.sprite.Sprite):
    def __init__(self,image, pos):
        super().__init__()
        self.image = image

        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self,step,player_image,scroll_group,player_group,player,stopenemy_group,coin_group,enemy_image1,FPS,portal_image,enemy_image2,enemy_image3):
        global schet
        self.rect.x += step
        if pygame.sprite.spritecollide(self, player_group, False):
            self.kill()
            #schet += 1


class Enemy(pygame.sprite.Sprite):
    def __init__(self,image, pos):
        super().__init__()
        self.images = image
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 1
        self.dir= 1
        self.frame = 0
        self.timer_anime = 0
        self.anime = False

    def animation(self,FPS):
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.1:
                if self.frame ==len(self.images) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0

    def update(self,step,player_image,scroll_group,player_group,player,stopenemy_group,coin_group,enemy_image1,FPS,portal_image,enemy_image2,enemy_image3):
        self.animation(FPS)
        self.rect.x += step
        if self.dir == 1:
            self.anime = True
            self.image = self.images[self.frame]
            self.rect.x += self.speed
        elif self.dir == -1:
            self.rect.x -= self.speed
            self.image = pygame.transform.flip(self.images[self.frame], True, False)
        if pygame.sprite.spritecollide(self,stopenemy_group,False):
            self.image = self.images[self.frame]
            self.dir *= -1




class StopEnemy(pygame.sprite.Sprite):
    def __init__(self,image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self,step,player_image,scroll_group,player_group,player,stopenemy_group,coin_group,enemy_image1,FPS,portal_image,enemy_image2,enemy_image3):
        self.rect.x += step
        if pygame.sprite.spritecollide(self, player_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
            if abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity_y = 0
            if abs(self.rect.left - player.rect.right) < 15 \
                    and abs(self.rect.centery - player.rect.centery) < 50:
                player.rect.right = self.rect.left
            if abs(self.rect.right - player.rect.left) < 15 \
                    and abs(self.rect.centery - player.rect.centery) < 50:
                player.rect.left = self.rect.right

class Box(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self,step,player_image,scroll_group,player_group,player,stopenemy_group,coin_group,enemy_image1,FPS,portal_image,enemy_image2,enemy_image3):
        self.rect.x += step
        if pygame.sprite.spritecollide(self,player_group,False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
            if abs(self.rect.bottom - player.rect.top) <15:
                player.rect.top = self.rect.bottom +5
                player.velocity_y = 0
            if abs(self.rect.left - player.rect.right) < 15 \
                    and abs(self.rect.centery - player.rect.centery) < 50:
                player.rect.right = self.rect.left
            if abs(self.rect.right - player.rect.left) < 15 \
                    and abs(self.rect.centery - player.rect.centery) < 50:
                player.rect.left = self.rect.right
class Ground(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self,step,player_image,scroll_group,player_group,player,stopenemy_group,coin_group,enemy_image1,FPS,portal_image,enemy_image2,enemy_image3):
        self.rect.x += step
        if pygame.sprite.spritecollide(self, player_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
            if abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity_y = 0
            if abs(self.rect.left - player.rect.right) < 15 \
                    and abs(self.rect.centery - player.rect.centery) < 50:
                player.rect.right = self.rect.left
            if abs(self.rect.right - player.rect.left) < 15 \
                    and abs(self.rect.centery - player.rect.centery) < 50:
                player.rect.left = self.rect.right
class Sand(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self,step,player_image,scroll_group,player_group,player,stopenemy_group,coin_group,enemy_image1,FPS,portal_image,enemy_image2,enemy_image3):
        self.rect.x += step
        if pygame.sprite.spritecollide(self, player_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
            if abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity_y = 0
            if abs(self.rect.left - player.rect.right) < 15 \
                    and abs(self.rect.centery - player.rect.centery) < 50:
                player.rect.right = self.rect.left
            if abs(self.rect.right - player.rect.left) < 15 \
                    and abs(self.rect.centery - player.rect.centery) < 50:
                player.rect.left = self.rect.right
class Water(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self,step,player_image,scroll_group,player_group,player,stopenemy_group,coin_group,enemy_image1,FPS,portal_image,enemy_image2,enemy_image3):
        self.rect.x += step
        if pygame.sprite.spritecollide(self, player_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
            if abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity_y = 0
            if abs(self.rect.left - player.rect.right) < 15 \
                    and abs(self.rect.centery - player.rect.centery) < 50:
                player.rect.right = self.rect.left
            if abs(self.rect.right - player.rect.left) < 15 \
                    and abs(self.rect.centery - player.rect.centery) < 50:
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
        self.frame = 0
        self.timer_anime = 0
        self.anime = False
    def animation(self,player_image,FPS):
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.05:
                if self.frame ==len(player_image) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0


    def update(self,player_image,scroll_group,player_group,player,stopenemy_group,coin_group,enemy_image1,FPS,portal_image,enemy_image2,enemy_image3):

        self.animation(player_image,FPS)
        key= pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.anime = True
            self.image = player_image[self.frame]
            self.rect.x += self.speed
            if self.rect.right > 750:
                self.rect.right= 750
                scroll_group.update(-self.speed,player_image,scroll_group,player_group,player,stopenemy_group,coin_group,enemy_image1,FPS,portal_image,enemy_image2,enemy_image3)


        elif key[pygame.K_a]:
            self.anime = True
            self.rect.x -= self.speed
            self.image = pygame.transform.flip(player_image[self.frame], True, False)

            if self.rect.left < 250:
                self.rect.left= 250
                scroll_group.update(self.speed,player_image,scroll_group,player_group,player,stopenemy_group,coin_group,enemy_image1,FPS,portal_image,enemy_image2,enemy_image3)
        else:
            self.anime=False

        if key[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = -17
            self.on_ground = False
        self.rect.y += self.velocity_y
        self.velocity_y += 1
        if self.velocity_y > 10:
            self.velocity_y = 10
        # self.anime = False

        #if key[pygame.K_d] and key[pygame.K_a] != True :
            #self.anime = False

