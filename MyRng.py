import pygame
import sys
import math
import random
import time

Draw = pygame.draw
RollPosition = (1920 / 2, 1080 / 2 - 300)

higest_raritiy = 32
common = int(higest_raritiy / 2)
uncommon = int(higest_raritiy / 4)
good = int(higest_raritiy / 8)
great = int(higest_raritiy / 16)
amazing = int(higest_raritiy / 32)

mouse = pygame.mouse
pygame.font.init()
RollResult = pygame.font.SysFont('Comic Sans MS', 50)
RarityUI = pygame.font.SysFont('comic sans ms', 40)
RollText =pygame.font.SysFont('comic sans ms', 40)


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
        Roll_Result = RollResult.render('common', True, (255, 255, 255))
        Rarity_UI = RarityUI.render('Rarity 1/2', True, (255, 255, 255))

    elif rng > uncommon:
        Roll_Result = RollResult.render('uncommon', True, (0, 255, 0))
        Rarity_UI = RarityUI.render('Rarity 1/4', True, (255, 255, 255))

    elif rng > good:
        Roll_Result = RollResult.render('good', True, (0, 0, 255))
        Rarity_UI = RarityUI.render('Rarity 1/8', True, (255, 255, 255))

    elif rng > great:
        Roll_Result = RollResult.render('great', True, (128, 0, 128))
        Rarity_UI = RarityUI.render('Rarity 1/16', True, (255, 255, 255))

    else:
        Roll_Result = RollResult.render('amazing', True, (255, 215, 0))
        Rarity_UI = RarityUI.render('Rarity 1/32', True, (255, 255, 255))
    
    # Calculate the position to center the text
    text_rect = Roll_Result.get_rect(center=(1920 / 2, 1080 / 2))
    text_rect2 = Rarity_UI.get_rect(center=(1920 / 2, 1080 / 2 + 100))
    screen.blit(Rarity_UI, text_rect2)
    screen.blit(Roll_Result, text_rect)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update mouse position
    mousePos = mouse.get_pos()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    roll()

    # Create an invisible rectangle at the mouse position
    CursorCollidePoint = pygame.Rect(mousePos[0] - 50, mousePos[1] - 50, 100, 100)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()