import pygame
import os

pygame.init()

WIDTH, HEIGHT = 1280, 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "orig_big.png")).convert(), (WIDTH, HEIGHT))


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.blit(background)


    #GAME


    pygame.display.flip()

    clock.tick(60)

pygame.quit()