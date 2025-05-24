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
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    SCREEN.blit(background)
    player.draw(SCREEN)
    enemy.draw(SCREEN)
    enemy.update()
    player.update()    

    #GAME


    pygame.display.flip()

    clock.tick(60)

pygame.quit()


