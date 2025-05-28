import pygame
import os

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

PLAYER_SPEED = 500
ENEMY_SPEED = 100

LASER = pygame.image.load(os.path.join("assets", "Charge_2.png"))

path_to_enemies = os.path.join("assets", "enemies")
ENEMY_SPRITES = [enemy for enemy in os.listdir(path_to_enemies)]


ALL_SPRITES = pygame.sprite.Group()

