import pygame
import os
from constants import *
import time


class Player():
    def __init__(self):
        self.sprite = pygame.transform.rotate(pygame.image.load(os.path.join("assets", "Idle.png")).convert_alpha(), 90)
        self.frect = self.sprite.get_frect(midbottom=(SCREEN_WIDTH/2, SCREEN_HEIGHT))
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.frect.top > 0:
            self.frect.y -= 6
        if keys[pygame.K_DOWN] and self.frect.bottom < SCREEN_HEIGHT:
            self.frect.y += 6
        if keys[pygame.K_LEFT] and self.frect.left > 0:
            self.frect.x -= 6
        if keys[pygame.K_RIGHT] and self.frect.right < SCREEN_WIDTH:
            self.frect.x += 6
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        self.laser = pygame.image.load(os.path.join("assets", "Charge_2.png"))
        self.laser_frect = self.laser.get_frect(midbottom = (self.frect.centerx, self.frect.top))
        
        SCREEN.blit(self.laser, self.laser_frect)


    def draw(self, surface):
        surface.blit(self.sprite, self.frect)