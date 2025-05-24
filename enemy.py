import pygame
import os
import random
from constants import *


path_to_enemies = os.path.join("assets", "enemies")

enemies = [enemy for enemy in os.listdir(path_to_enemies)]
enemy_spawn_x = random.randint(0, SCREEN_WIDTH)


class Enemy():
    def __init__(self):
        self.sprite_choice = os.path.join(path_to_enemies, random.choice(enemies))
        self.sprite = pygame.image.load(self.sprite_choice).convert_alpha()
        self.frect = self.sprite.get_frect(midtop = (enemy_spawn_x, 0))

    def draw(self, surface):
        surface.blit(self.sprite, self.frect)
        
    
    def update(self):
        
        if self.sprite_choice == os.path.join("assets", "enemies", "Ship1.png"):
            self.frect.y += 5
        if self.sprite_choice == os.path.join("assets", "enemies", "Ship2.png"):
            self.frect.y += 1
        if self.sprite_choice == os.path.join("assets", "enemies", "Ship3.png"):
            self.frect.y += 4
        if self.sprite_choice == os.path.join("assets", "enemies", "Ship4.png"):
            self.frect.y += 3
        if self.sprite_choice == os.path.join("assets", "enemies", "Ship5.png"):
            self.frect.y += 2
        if self.sprite_choice == os.path.join("assets", "enemies", "Ship6.png"):
            self.frect.y += 2.5