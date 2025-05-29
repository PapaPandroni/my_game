import pygame
from constants import ALIEN_SPRITE, SCREEN_WIDTH, SCREEN_HEIGHT
import random

class Alien(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.original_image = ALIEN_SPRITE
        self.image = ALIEN_SPRITE
        self.rect = self.image.get_frect(midbottom=(random.randint(50, SCREEN_WIDTH-50), random.randint(50, SCREEN_HEIGHT-50)))
        self.mask = pygame.mask.from_surface(self.image)
        self.duration = 3000

        self.spawntime = pygame.time.get_ticks()

        self.rotation = 0
        

    def spawn_duration(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.spawntime > self.duration:
            self.kill()
        
    def update(self, dt):
        self.spawn_duration()
        self.rotation += 120 * dt
        self.image = pygame.transform.rotate(self.original_image, self.rotation)
        self.rect = self.image.get_frect(center = self.rect.center)

        