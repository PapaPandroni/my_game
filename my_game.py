import pygame
import os
from player import Player
from enemy import Enemy
from constants import *
from laser import Laser

pygame.init()

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "orig_big.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player(all_sprites)
enemy = Enemy()

running = True
while running:
    
    dt = clock.tick() / 1000 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    all_sprites.update(dt)
        
    SCREEN.blit(background)
    all_sprites.draw(SCREEN)
    enemy.draw(SCREEN)
    enemy.update(dt)
      

    #GAME


    pygame.display.flip()

    

pygame.quit()


