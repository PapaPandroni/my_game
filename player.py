import pygame
import os
from constants import *
import time



class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.transform.rotate(pygame.image.load(os.path.join("assets", "Idle.png")).convert_alpha(), 90)
        self.rect = self.image.get_frect(midbottom=(SCREEN_WIDTH/2, SCREEN_HEIGHT))
        self.pos = pygame.math.Vector2(self.rect.x, self.rect.y)
        self.direction = pygame.math.Vector2(0,0)
            
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        #if self.rect.right < SCREEN_WIDTH and self.rect.left > 0:
        self.direction.x = int(keys[pygame.K_RIGHT] - int(keys[pygame.K_LEFT]))
        #if self.rect.bottom < SCREEN_HEIGHT and self.rect.top > 0:
        self.direction.y = int(keys[pygame.K_DOWN] - int(keys[pygame.K_UP]))

        #if keys[pygame.K_UP] and self.rect.top > 0:
        #    self.direction.y = -1
        #if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
        #    self.direction.y = 1
        #if keys[pygame.K_LEFT] and self.rect.left > 0:
        #    self.direction.x = -1
        #if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
        #    self.direction.x = 1
        
        if pygame.key.get_just_pressed()[pygame.K_SPACE]:
            self.shoot()
            print("shoot")
        
        if self.direction.length_squared() != 0:
            self.direction = self.direction.normalize()

        self.pos += self.direction * PLAYER_SPEED * dt
        self.rect.topleft = self.pos


    def shoot(self):
        self.laser = pygame.image.load(os.path.join("assets", "Charge_2.png"))
        self.laser_frect = self.laser.get_frect(midbottom = (self.rect.centerx, self.rect.top))
        
        SCREEN.blit(self.laser, self.laser_frect)


    def draw(self, surface):
        surface.blit(self.image, self.rect)