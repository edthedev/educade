#!/usr/bin/env python3
"""Four Player invaders clone."""

import math
import re
import time
import pygame
from random import randint

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Joystick X / Y Axis
JOY_Y = 0
JOY_X = 1

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()
size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(False)


class ControlSet():
    """A controller mapping."""

    def __init__(self, up=pygame.K_UP, down=pygame.K_DOWN,
                 left=pygame.K_LEFT, right=pygame.K_RIGHT):
        self.up_key = up
        self.down_key = down
        self.left_key = left
        self.right_key = right


class Player():
    """A game player."""
    controls = [ControlSet()]
    pos_x = 100
    pos_y = 100
    size_x = 50
    size_y = 50
    move_amt = 5
    color = RED

    def __init__(self, color, controls):
        """Make a new player.

        Assign unique color and controls."""
        self.controls = controls
        self.color = color

    def control(self, keys=None, joystick=None):
        """Look for signals accepted by this player, and apply them."""
        if keys:
            self._key_control(keys)
        if joystick:
            self._joy_control(joystick)

    def _joy_control(self, joystick):
        """Apply joystick controls.

        Only pass in the joystick you want to have accepted.
        """
        if joystick.get_axis(JOY_Y) >= 1:
            self._up()
        if joystick.get_axis(JOY_Y) <= 1:
            self._down()
        if joystick.get_axis(JOY_X) >= 1:
            self._right()
        if joystick.get_axis(JOY_X) <= 1:
            self._left()

    def _up(self):
        """Move self up."""
        self.pos_y -= self.move_amt

    def _down(self):
        """Move self down."""
        self.pos_y += self.move_amt

    def _left(self):
        """Move self left."""
        self.pos_x -= self.move_amt

    def _right(self):
        """Move self right."""
        self.pos_x += self.move_amt

    def _key_control(self, keys):
        """Apply keyboard controls - as accepted by this player."""
        for controlSet in self.controls:
            if keys[controlSet.up_key]:
                self._up()
            if keys[controlSet.down_key]:
                self._down()
            if keys[controlSet.left_key]:
                self._left()
            if keys[controlSet.right_key]:
                self._right()

    def draw(self):
        # Draw the rectangle
        pygame.draw.rect(screen, WHITE,
                         [self.pos_x, self.pos_y, self.size_x, self.size_y])
        pygame.draw.rect(screen, self.color,
                         [self.pos_x + 10, self.pos_y + 10, self.size_x - 10, self.size_y - 10])


class invaders():
    """Game loggic goes here."""
    done = False

    player1 = Player(color=RED,
                     controls=[ControlSet(), ControlSet(up=pygame.K_w, down=pygame.K_s,
                                                        left=pygame.K_a, right=pygame.K_d)])
    player2 = Player(color=WHITE,
                     controls=[ControlSet(up=pygame.K_j, down=pygame.K_k,
                                          left=pygame.K_h, right=pygame.K_l)])
    player3 = Player(color=GREEN,
                     controls=[ControlSet(up=pygame.K_3, down=pygame.K_2,
                                          left=pygame.K_1, right=pygame.K_4)])
    player4 = Player(color=GREEN,
                     controls=[ControlSet(up=pygame.K_7, down=pygame.K_6,
                                          left=pygame.K_5, right=pygame.K_8)])

    def controls(self):
        """Check for control inputs."""

        # Keyboard controls - for testing without joysticks

        # events = pygame.event.get()

        keys = pygame.key.get_pressed()
        self.player1.control(keys=keys)
        self.player2.control(keys=keys)
        self.player3.control(keys=keys)
        self.player4.control(keys=keys)

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

            if i == 0:
                self.player1.control(joystick=joystick)
            if i == 1:
                self.player2.control(joystick=joystick)
            if i == 2:
                self.player3.control(joystick=joystick)
            if i == 3:
                self.player4.control(joystick=joystick)

    def logic(self):
        """Calculate game logic."""
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
        self.player2.draw()
        self.player3.draw()
        self.player4.draw()

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
