import pygame
import os
from player import Player
from enemy import Enemy
from constants import *

pygame.init()




clock = pygame.time.Clock()

background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "orig_big.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player()
enemy = Enemy()

running = True
while running:
    
    dt = clock.tick() / 1000 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    SCREEN.blit(background)
    player.draw(SCREEN)
    enemy.draw(SCREEN)
    enemy.update(dt)
    player.update(dt)    

    #GAME


    pygame.display.flip()

    

pygame.quit()


