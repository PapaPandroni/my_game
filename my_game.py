import pygame
import os
from player import Player
from enemy import Enemy
from constants import *
from laser import Laser
from alien import Alien

pygame.init()

clock = pygame.time.Clock()

background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "orig_big.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player(ALL_SPRITES)


#enemey spawn event
enemy_spawn = pygame.event.custom_type()
pygame.time.set_timer(enemy_spawn, 500)

alien_spawn = pygame.event.custom_type()
pygame.time.set_timer(alien_spawn, 5000)

running = True
while running:
    
    dt = clock.tick() / 1000 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == enemy_spawn:
            enemy = Enemy(ALL_SPRITES)
        if event.type == alien_spawn:
            alien = Alien(ALL_SPRITES)



    ALL_SPRITES.update(dt)
        
    SCREEN.blit(background)
    ALL_SPRITES.draw(SCREEN)

      

    #GAME


    pygame.display.flip()

    

pygame.quit()


