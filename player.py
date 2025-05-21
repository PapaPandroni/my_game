import pygame
import os

class Player():
    def __init__(self):
        self.sprite = pygame.image.load(os.path.join("assets", "Idle.png")).convert_alpha()
    
    def draw(self, surface):
        surface.blit(self.sprite)