import pygame
import os
from constants import *
import time



class Player():
    def __init__(self):
        self.sprite = pygame.transform.rotate(pygame.image.load(os.path.join("assets", "Idle.png")).convert_alpha(), 90)
        self.frect = self.sprite.get_frect(midbottom=(SCREEN_WIDTH/2, SCREEN_HEIGHT))
        self.pos = pygame.math.Vector2(self.frect.x, self.frect.y)
        self.direction = pygame.math.Vector2(0,0)
        
    
    def update(self, dt):
        self.direction = pygame.math.Vector2(0,0)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.frect.top > 0:
            self.direction.y = -1
        if keys[pygame.K_DOWN] and self.frect.bottom < SCREEN_HEIGHT:
            self.direction.y = 1
        if keys[pygame.K_LEFT] and self.frect.left > 0:
            self.direction.x = -1
        if keys[pygame.K_RIGHT] and self.frect.right < SCREEN_WIDTH:
            self.direction.x = 1
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        if self.direction.length_squared() != 0:
            self.direction = self.direction.normalize()

        self.pos += self.direction * PLAYER_SPEED * dt
        self.frect.topleft = self.pos


    def shoot(self):
        self.laser = pygame.image.load(os.path.join("assets", "Charge_2.png"))
        self.laser_frect = self.laser.get_frect(midbottom = (self.frect.centerx, self.frect.top))
        
        SCREEN.blit(self.laser, self.laser_frect)


    def draw(self, surface):
        surface.blit(self.sprite, self.frect)