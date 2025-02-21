import pygame
import sys
import math
import random
import time

higest_raritiy = 32

common = int(higest_raritiy / 2)
uncommon = int(higest_raritiy / 4)
good = int(higest_raritiy / 8)
great = int(higest_raritiy / 16)
amazing = int(higest_raritiy / 32)

pygame.font.init()
RollResualt = pygame.font.SysFont('Comic Sans MS', 50)

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("My RNG")
clock = pygame.time.Clock()
running = True
dt = 0
pity = 0  # Initialize pity outside the loop

def roll():
    global pity
    time.sleep(1)
    pity += 1 
    if pity == 10:
        rng = random.randint(1, int(higest_raritiy / 2))
        pity = 0  # Correct assignment
    else:
        rng = random.randint(1, int(higest_raritiy))
    
    if rng > common:
        text_surface = RollResualt.render('common', True, (255, 255, 255))
    elif rng > uncommon:
        text_surface = RollResualt.render('uncommon', True, (0, 255, 0))
    elif rng > good:
        text_surface = RollResualt.render('good', True, (0, 0, 255))
    elif rng > great:
        text_surface = RollResualt.render('great', True, (128, 0, 128))
    else:
        text_surface = RollResualt.render('amazing', True, (255, 215, 0))
    
    screen.blit(text_surface, (960, 540))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    roll()
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()