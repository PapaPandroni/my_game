import pygame
from constants import LASER


class Laser(pygame.sprite.Sprite):
    def __init__(self, groups, player):
        super().__init__(groups)
        self.image = LASER
        self.rect = self.image.get_frect(midbottom = (player.rect.centerx, player.rect.top))
        
    def update(self):
        if pygame.key.get_just_pressed()[pygame.K_SPACE]:
            pass