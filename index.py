import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title and icon
pygame.display.set_caption("Simple Game Screen")
icon = pygame.image.load('icon.png')  # Replace with your icon file path
pygame.display.set_icon(icon)

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Game loop
running = True
while running:
    # Fill the screen with a color
    screen.fill(white)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()