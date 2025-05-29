import pygame
import os

pygame.mixer.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

PLAYER_SPEED = 500
ENEMY_SPEED = 50

LASER = pygame.transform.scale_by(pygame.image.load(os.path.join("assets", "Charge_2.png")), 5)

path_to_enemies = os.path.join("assets", "enemies")
ENEMY_SPRITES = [enemy for enemy in os.listdir(path_to_enemies)]


ALIEN_SPRITE = pygame.transform.scale_by(pygame.image.load(os.path.join("assets", "blue__0029_jump_3.png")).convert_alpha(), 0.15)
ALL_SPRITES = pygame.sprite.Group()
ENEMY_SPRITES_GRP = pygame.sprite.Group()
LASER_SPRITES = pygame.sprite.Group()
ALIEN_SPRITES_GRP = pygame.sprite.Group()
HERO = pygame.sprite.Group()


laser_sound = pygame.mixer.Sound(os.path.join("assets", "laser-312360.mp3"))
laser_sound.set_volume(0.1)