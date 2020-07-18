#!/usr/bin/env python3
"""Four Player invaders clone."""

import pygame
from sprites import TextPrint, ControlSet, Player

# Set these to the two buttons you want to use for 'exit'. Count up starting from 0
SELECT = 3
START = 4

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)


# Used to manage how fast the screen updates
clock = pygame.time.Clock()

textPrint = TextPrint()

# Initialize the joysticks
pygame.init()
pygame.joystick.init()
size = [700, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Inv4ders")
pygame.mouse.set_visible(False)

class Laser():
    """Track the lasters."""
    pos_x = 0
    pos_y = 0
    dir = 1
    size_x = 3
    size_y = 10

    def draw(self, screen):
        """Draw this laser."""
        pygame.draw.rect(screen, RED,
                         [self.pos_x, self.pos_y, self.size_x, self.size_y])

class Invaders():
    """Game loggic goes here."""
    done = False

    player1 = Player(screen=screen, color=YELLOW,
                     controls=[ControlSet(), ControlSet(up=pygame.K_w, down=pygame.K_s,
                                                        left=pygame.K_a, right=pygame.K_d)])
    player2 = Player(screen=screen, color=RED,
                     controls=[ControlSet(up=pygame.K_j, down=pygame.K_k,
                                          left=pygame.K_h, right=pygame.K_l)])
    player3 = Player(screen=screen, color=BLUE,
                     controls=[ControlSet(up=pygame.K_3, down=pygame.K_2,
                                          left=pygame.K_1, right=pygame.K_4)])
    player4 = Player(screen=screen, color=PURPLE,
                     controls=[ControlSet(up=pygame.K_7, down=pygame.K_6,
                                          left=pygame.K_5, right=pygame.K_8)])
    def __init__(self):
        """Setup"""
        self._lasers = []

    def fired(self, player):
        """This player fired!"""
        new_laser = Laser()
        new_laser.pos_x = player.pos_x
        new_laser.pos_y = player.pos_y
        new_laser.dir = -1 # Going up!
        self._lasers.append(new_laser)

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
            button7 = joystick.get_button(SELECT)
            button8 = joystick.get_button(START)
            if button7 == button8 == 1:
                self.done = True

            if i == 0:
                fired = self.player1.control(joystick=joystick)
                if fired:
                    self.fired(player1)
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
        for laser in self._lasers:
            laser.pox_y += laser.dir

    def draw(self):
        """Update the screen."""
        # --- Drawing
        # Set the screen background

        for laser in self._lasers:
            laser.draw()

        self.player1.draw()
        self.player2.draw()
        self.player3.draw()
        self.player4.draw()

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        textPrint.reset()
        screen.fill(WHITE)
        joystick_count = pygame.joystick.get_count()
        textPrint.print(screen, "Number of joysticks: {}".format(joystick_count))

# -------- Main Program Loop -----------
inv = Invaders()
while not inv.done:
    inv.controls()
    inv.logic()
    inv.draw()
    # Limit to 60 frames per second
    clock.tick(60)

# Close everything down
pygame.quit()
