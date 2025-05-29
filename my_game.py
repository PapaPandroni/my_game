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

player = Player((ALL_SPRITES, HERO))


#enemey spawn event
enemy_spawn = pygame.event.custom_type()
pygame.time.set_timer(enemy_spawn, 500)

alien_spawn = pygame.event.custom_type()
pygame.time.set_timer(alien_spawn, 5000)

def collisions():
    player_death = pygame.sprite.spritecollide(player, ENEMY_SPRITES_GRP, False)
    if player_death:
        player.kill()

    for laser in LASER_SPRITES:
        laser_hits = pygame.sprite.spritecollide(laser, ENEMY_SPRITES_GRP, True)    
        if laser_hits:
            laser.kill()

    alien_saved = pygame.sprite.spritecollide(player, ALIEN_SPRITES_GRP, True)
    if alien_saved:
        print("POINT!")
        


points = 0

running = True
while running:
    
    dt = clock.tick() / 1000 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == enemy_spawn:
            Enemy((ALL_SPRITES, ENEMY_SPRITES_GRP))
        if event.type == alien_spawn:
            alien = Alien((ALL_SPRITES, ALIEN_SPRITES_GRP))


    #update
    ALL_SPRITES.update(dt)
    
    #GAME
    collisions()

    SCREEN.blit(background)
    ALL_SPRITES.draw(SCREEN)

    pygame.display.flip()

    

pygame.quit()


