import pygame
import os
from constants import *
import time
from laser import Laser



class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join("assets", "Idle.png")).convert_alpha()
        self.rect = self.image.get_frect(midbottom=(SCREEN_WIDTH/2, SCREEN_HEIGHT))
        self.pos = pygame.math.Vector2(self.rect.x, self.rect.y)
        self.direction = pygame.math.Vector2(0,0)
        self.mask = pygame.mask.from_surface(self.image)

        #cooldown for weapon
        self.can_shoot = True
        self.laser_schoot = 0
        self.cooldown_duration = 350
            
    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if (current_time - self.laser_shoot_time) >= self.cooldown_duration:
                self.can_shoot = True

    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        self.direction.x = int(keys[pygame.K_RIGHT] - int(keys[pygame.K_LEFT]))
        self.direction.y = int(keys[pygame.K_DOWN] - int(keys[pygame.K_UP]))

        recent_pressed_key = pygame.key.get_just_pressed()
        if recent_pressed_key[pygame.K_SPACE] and self.can_shoot: 
            Laser(LASER, self.rect.midtop, (ALL_SPRITES, LASER_SPRITES))
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()
        
        if self.direction.length_squared() != 0:
            self.direction = self.direction.normalize()

        self.pos += self.direction * PLAYER_SPEED * dt
        self.rect.topleft = self.pos

        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        self.pos = pygame.math.Vector2(self.rect.topleft)

        self.laser_timer()



