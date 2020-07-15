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

class ControlSet():
    """A controller mapping."""
    # TODO: Make this mappable on init
    up_key = pygame.K_UP
    down_key = pygame.K_DOWN
    left_key = pygame.K_LEFT
    right_key = pygame.K_RIGHT

class Player():
    """A game player."""
    # TODO: make controls a set
    controls = [ControlSet()]
    pos_x = 0
    pos_y = 0
    size_x = 50
    size_y = 50
    move_amt = 5
    color = RED

    def __init__(self, color, controls):
        """Make a new player.

        Assign unique color and controls."""
        self.controls = controls
        self.color = color

    def control(self, keys):
        """Look for signals accepted by this player, and apply them."""
        for controlSet in self.controls:
            if keys[controlSet.up_key]:
                self.pos_y -= self.move_amt
            if keys[controlSet.down_key]:
                self.pos_y += self.move_amt
            if keys[controlSet.left_key]:
                self.pos_x -= self.move_amt
            if keys[controlSet.right_key]:
                self.pos_x += self.move_amt

    def draw(self):
        # Draw the rectangle
        pygame.draw.rect(screen, WHITE, 
            [self.pos_x, self.pos_y, self.size_x, self.size_y])
        pygame.draw.rect(screen, self.color, 
            [self.pos_x + 10, self.pos_y + 10, self.size_x - 10, self.size_y - 10])

class invaders():
    """Game loggic goes here."""

    done = False
    # Starting position of the rectangle
    rect_x = 50
    rect_y = 50
    
    # Speed and direction of rectangle
    rect_change_x = 2
    rect_change_y = 2

    player1 = Player(color=RED,controls=[ControlSet()])

    def controls(self):
        """Check for control inputs."""

        ## Keyboard controls - for testing without joysticks
        keys=pygame.key.get_pressed()
        self.player1.control(keys)

        # Get count of joysticks
        joystick_count = pygame.joystick.get_count()
    
        # For each joystick:
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()

            # Exit like RetroArch - any joystick
            button7 = joystick.get_button(7)
            button8 = joystick.get_button(8)
            if button7 == button8 == 1:
                self.done = True

    def logic(self):
        """Calculate game logic."""
        self.rect_x += self.rect_change_x
        self.rect_y += self.rect_change_y
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

    def draw(self):
        """Update the screen."""
        # --- Drawing
        # Set the screen background
        screen.fill(BLACK)
    
        self.player1.draw()
    
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