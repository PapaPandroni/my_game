import pygame
from constants import LASER, ENEMY_SPRITES_GRP


class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = pos)
        
    def update(self, dt):
        self.rect.centery -= 750 *dt
        if self.rect.bottom < 0:
            self.kill()
        