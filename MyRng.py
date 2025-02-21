import pygame,sys
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
RollResualt = pygame.font.SysFont('Comic Sans MS', 30)

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("My RNG")
clock = pygame.time.Clock()
running = True
dt = 0

while running:
    pity = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    def roll():
        global pity
        time.sleep(1)
        pity += 1 
        if pity == 10:
            rng = random.randint(1, int(higest_raritiy / 2))
            pity == 0
        else:
            rng = random.randint(1, int(higest_raritiy))
        if rng > common:
            RollResualt.render(screen, (960, 540), "common", (255, 255, 255))

        elif rng > uncommon:
            RollResualt.render(screen, (960, 540), "uncommon", (255, 255, 255))

        elif rng > good:
            RollResualt.render(screen, (960, 540), "good", (255, 255, 255))

        elif rng > great:
            RollResualt.render(screen, (960, 540), "great", (255, 255, 255))

        else:
            RollResualt.render_to(screen, (960, 540), "anazing", (255, 255, 255))
        
        screen.blit(text_surface, (960, 540))
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    roll()
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()


