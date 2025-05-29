import pygame
import os
from player import Player
from enemy import Enemy
from constants import *
from laser import Laser
from alien import Alien
from explosion import Explosion

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()


pygame.display.set_caption("Alien Rescue")
background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "orig_big.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player((ALL_SPRITES, HERO))

font = pygame.font.Font(os.path.join("assets", "neo_scifi.ttf"), 50)



#enemey spawn event
enemy_spawn = pygame.event.custom_type()
pygame.time.set_timer(enemy_spawn, 500)

alien_spawn = pygame.event.custom_type()
pygame.time.set_timer(alien_spawn, 5000)


#Sounds
pygame.mixer.music.load(os.path.join("assets", "space-120280.mp3"))
pygame.mixer.music.play(loops=-1)



def collisions():
    global points
    player_death = pygame.sprite.spritecollide(player, ENEMY_SPRITES_GRP, False, pygame.sprite.collide_mask)
    if player_death:
        Explosion(EXPLOSION_SPRITES, player.rect.center, ALL_SPRITES)
        player.kill()

    for laser in LASER_SPRITES:
        laser_hits = pygame.sprite.spritecollide(laser, ENEMY_SPRITES_GRP, True, pygame.sprite.collide_mask)    
        if laser_hits:
            Explosion(EXPLOSION_SPRITES, laser.rect.midtop, ALL_SPRITES)
            laser.kill()

    alien_saved = pygame.sprite.spritecollide(player, ALIEN_SPRITES_GRP, True, pygame.sprite.collide_mask)
    if alien_saved:
        points += 1
        
def display_points(points):
    text_surface = font.render(f"{points}", True, "#ced3d4")
    text_rect = text_surface.get_frect(midtop = (SCREEN_WIDTH-100, 100))
    SCREEN.blit(text_surface, text_rect)
    pygame.draw.rect(SCREEN, "lightblue", text_rect.inflate((25, 25)).move(-2, -2), 1, 10)
    

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
    
    SCREEN.blit(background)
    collisions()
    display_points(points)
    ALL_SPRITES.draw(SCREEN)
    

    pygame.display.flip()

    

pygame.quit()


