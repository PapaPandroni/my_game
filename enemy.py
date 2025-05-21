import pygame
import os
import random

path_to_enemies = os.path.join("assets", "enemies")

enemies = [enemy for enemy in os.listdir(path_to_enemies)]


class Enemy():
    def __init__(self):
        sprite_choice = os.path.join(path_to_enemies, random.choice(enemies))
        self.sprite = pygame.image.load(sprite_choice).convert_alpha()
    
    def draw(self, surface):
        surface.blit(self.sprite)
