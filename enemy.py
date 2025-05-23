import pygame
import os
import random
from constants import *


path_to_enemies = os.path.join("assets", "enemies")

enemies = [enemy for enemy in os.listdir(path_to_enemies)]
enemy_spawn_x = random.randint(0, SCREEN_WIDTH)


class Enemy():
    def __init__(self):
        sprite_choice = os.path.join(path_to_enemies, random.choice(enemies))
        self.sprite = pygame.image.load(sprite_choice).convert_alpha()
        self.frect = self.sprite.get_frect(midtop = (enemy_spawn_x, 0))
    
    def draw(self, surface):
        surface.blit(self.sprite, self.frect)
        
    
    def movement(self):
        self.frect.y += 0.5