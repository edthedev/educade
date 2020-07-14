#!/usr/bin/env python3
"""Four Player invaders clone."""

import math, re, time
import pygame
from random import randint

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Initialize the joysticks
pygame.joystick.init()
size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(False)

class invaders():

    done = False
    # Starting position of the rectangle
    rect_x = 50
    rect_y = 50
    
    # Speed and direction of rectangle
    rect_change_x = 2
    rect_change_y = 2

    def controls(self):
        # Get count of joysticks
        joystick_count = pygame.joystick.get_count()
    
        # For each joystick:
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()

            # Exit like RetroArch
            button7 = joystick.get_button(7)
            button8 = joystick.get_button(8)
            if button7 == button8 == 1:
                self.done = True

    def logic(self):
        self.rect_x += self.rect_change_x
        self.rect_y += self.rect_change_y
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

    def draw(self):
        # --- Drawing
        # Set the screen background
        screen.fill(BLACK)
    
        # Draw the rectangle
        pygame.draw.rect(screen, WHITE, [self.rect_x, self.rect_y, 50, 50])
        pygame.draw.rect(screen, RED, [self.rect_x + 10, self.rect_y + 10, 30, 30])
    
        # --- Wrap-up
        # Limit to 60 frames per second
        clock.tick(60)
    
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

# -------- Main Program Loop -----------
inv = invaders()
while not inv.done:
    inv.controls()
    inv.logic()
    inv.draw()
 
# Close everything down
pygame.quit()