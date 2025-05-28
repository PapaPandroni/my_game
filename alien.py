import pygame
from constants import ALIEN_SPRITE, SCREEN_WIDTH, SCREEN_HEIGHT
import random

class Alien(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = ALIEN_SPRITE
        self.rect = self.image.get_frect(midbottom=(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)))
        self.duration = 3000

        self.spawntime = pygame.time.get_ticks()

    def spawn_duration(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.spawntime > self.duration:
            self.kill()
        
    def update(self, dt):
        self.spawn_duration()

        