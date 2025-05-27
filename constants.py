import pygame
import os

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

PLAYER_SPEED = 300
ENEMY_SPEED = 100

LASER = pygame.image.load(os.path.join("assets", "Charge_2.png"))