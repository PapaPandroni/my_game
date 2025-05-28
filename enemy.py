import pygame
import os
import random
from constants import *


path_to_enemies = os.path.join("assets", "enemies")

enemies = [enemy for enemy in os.listdir(path_to_enemies)]



class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.sprite_choice = os.path.join(path_to_enemies, random.choice(enemies))
        self.spawn_x = random.randint(0, SCREEN_WIDTH)
        self.image = pygame.image.load(self.sprite_choice).convert_alpha()
        self.rect = self.image.get_frect(midtop = (self.spawn_x, 0))
        self.direction = pygame.math.Vector2(random.uniform(-0.6, 0.6), 1)
        
    
    def update(self, dt):
        
        if self.sprite_choice == os.path.join("assets", "enemies", "Ship1.png"):
            self.rect.center += ENEMY_SPEED * dt * 1 * self.direction
        if self.sprite_choice == os.path.join("assets", "enemies", "Ship2.png"):
            self.rect.center += ENEMY_SPEED * dt * 2 * self.direction
        if self.sprite_choice == os.path.join("assets", "enemies", "Ship3.png"):
            self.rect.center += ENEMY_SPEED * dt * 1.5 * self.direction
        if self.sprite_choice == os.path.join("assets", "enemies", "Ship4.png"):
            self.rect.center += ENEMY_SPEED * dt * 2.5 * self.direction
        if self.sprite_choice == os.path.join("assets", "enemies", "Ship5.png"):
            self.rect.center += ENEMY_SPEED * dt * 5 * self.direction
        if self.sprite_choice == os.path.join("assets", "enemies", "Ship6.png"):
            self.rect.center += ENEMY_SPEED * dt * 1.75 * self.direction
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()