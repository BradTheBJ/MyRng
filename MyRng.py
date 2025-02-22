import pygame
import sys
import math
import random
import time

Draw = pygame.draw
RollPosition = (1920 / 2, 1080 / 2 + 300)

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
RollText = pygame.font.SysFont('comic sans ms', 40)
PityIndicator = pygame.font.SysFont('comic sans ms', 40)
CloseGameText = pygame.font.SysFont('comic sans ms', 20)  # Smaller font for "Close Game" text

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("My RNG")
clock = pygame.time.Clock()
running = True
dt = 0
pity = 0  # Initialize pity outside the loop
mouse_pressed = False  # Flag to track mouse button state
show_pity_text = False  # Flag to indicate when to show the pity text

# Variables to store the current roll result and rarity UI
current_roll_result = None
current_rarity_ui = None

def roll():
    global pity, current_roll_result, current_rarity_ui, show_pity_text
    pity += 1 
    if pity == 10:
        rng = random.randint(1, int(higest_raritiy / 2))
        pity = 0  # Correct assignment
        show_pity_text = True  # Set the flag to show the pity text
    else:
        rng = random.randint(1, int(higest_raritiy))
        show_pity_text = False  # Reset the flag after displaying the text
    
    if rng > common:
        current_roll_result = RollResult.render('common', True, (255, 255, 255))
        current_rarity_ui = RarityUI.render('Rarity 1/2', True, (255, 255, 255))

    elif rng > uncommon:
        current_roll_result = RollResult.render('uncommon', True, (0, 255, 0))
        current_rarity_ui = RarityUI.render('Rarity 1/4', True, (255, 255, 255))

    elif rng > good:
        current_roll_result = RollResult.render('good', True, (0, 0, 255))
        current_rarity_ui = RarityUI.render('Rarity 1/8', True, (255, 255, 255))

    elif rng > great:
        current_roll_result = RollResult.render('great', True, (128, 0, 128))
        current_rarity_ui = RarityUI.render('Rarity 1/16', True, (255, 255, 255))

    else:
        current_roll_result = RollResult.render('amazing', True, (255, 215, 0))
        current_rarity_ui = RarityUI.render('Rarity 1/32', True, (255, 255, 255))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update mouse position
    mousePos = mouse.get_pos()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # Create an invisible rectangle at the mouse position
    CursorCollidePoint = pygame.Rect(mousePos[0] - 50, mousePos[1] - 50, 100, 100)
    
    # Draw a wider rectangle at RollPosition
    RollObject = Draw.rect(screen, (255, 255, 255), (RollPosition[0] - 150, RollPosition[1] - 25, 300, 50))

    RollTextSurface = RollText.render('Roll', True, (0, 0, 0))

    # Calculate the position to center the RollText in the RollObject
    roll_text_rect = RollTextSurface.get_rect(center=(RollPosition[0], RollPosition[1]))
    screen.blit(RollTextSurface, roll_text_rect)

    # RENDER YOUR GAME HERE
    if CursorCollidePoint.colliderect(RollObject):
        if mouse.get_pressed()[0] and not mouse_pressed:
            roll()
            mouse_pressed = True
        elif not mouse.get_pressed()[0]:
            mouse_pressed = False

    # Blit the current roll result and rarity UI to the screen
    if current_roll_result and current_rarity_ui:
        text_rect = current_roll_result.get_rect(center=(1920 / 2, 1080 / 2))
        text_rect2 = current_rarity_ui.get_rect(center=(1920 / 2, 1080 / 2 + 100))
        screen.blit(current_rarity_ui, text_rect2)
        screen.blit(current_roll_result, text_rect)

    # Show the pity text if the flag is set
    if show_pity_text:
        PityText = PityIndicator.render('2x luck', True, (255, 255, 255))
        screen.blit(PityText, (1920 / 2 - PityText.get_width() / 2, 1080 / 2 - 150))

    # Blit the "Close Game" text in the top left corner
    CloseGameSurface = CloseGameText.render('Close Game', True, (255, 255, 255))
    screen.blit(CloseGameSurface, (10, 10))

    # Check if the mouse is over the "Close Game" text and close the game if clicked
    if CursorCollidePoint.colliderect(CloseGameSurface.get_rect(topleft=(10, 10))):
        if mouse.get_pressed()[0] and not mouse_pressed:
            running = False

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()