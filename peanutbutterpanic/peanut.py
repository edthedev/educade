#!/usr/bin/env python3
"""Four Player invaders clone."""

import random
import pygame
from player import Player
from text import TextPrint
from controls import ControlSet

# Set these to the two buttons you want to use for 'exit'. Count up starting from 0
SELECT = 3
START = 4

class colors():
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    PURPLE = (128, 0, 128)
    YELLOW = (255, 255, 0)
    GROUND = (0, 128, 0)

# GAME FIELD
STAR_TOP_LAYER = 40

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

textPrint = TextPrint()

class PlayField():
    """Track the play field."""
    MIN_X = 0
    MAX_X = 800
    MIN_Y = 600
    GROUND_Y = MIN_Y - 100
    MAX_Y = 0

    def __init__(self):
        """New play field."""
        self.done = False
        self.sprites = []
        self.players = []
        self.add_players()
        self.screen = None

        # Initialize the joysticks
        pygame.init()
        pygame.joystick.init()
        size = [self.MAX_X, self.MIN_Y]
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Peanut Butter Panic")
        pygame.mouse.set_visible(False)

    def add_players(self):
        """Create the players.

        Return an array of the players as objects with .draw methods.
        """
        player1 = Player(color=colors.YELLOW,
                         controls=[ControlSet(), ControlSet(up=pygame.K_w, down=pygame.K_s,
                                                            left=pygame.K_a, right=pygame.K_d)])
        player2 = Player(color=colors.RED,
                         controls=[ControlSet(up=pygame.K_j, down=pygame.K_k,
                                              left=pygame.K_h, right=pygame.K_l)])
        player3 = Player(color=colors.BLUE,
                         controls=[ControlSet(up=pygame.K_3, down=pygame.K_2,
                                              left=pygame.K_1, right=pygame.K_4)])
        player4 = Player(color=colors.PURPLE,
                         controls=[ControlSet(up=pygame.K_7, down=pygame.K_6,
                                              left=pygame.K_5, right=pygame.K_8)])
        self.players = [player1, player2, player3, player4]
        for player in self.players:
            player.pos_y = self.GROUND_Y
            player.ground_y = self.GROUND_Y
        self.sprites += self.players

    def draw(self):
        """Re-Draw the play field."""
        self.screen.fill(colors.BLACK)  # background
        pygame.draw.rect(self.screen, colors.GROUND,
                         [self.MIN_X, self.GROUND_Y, self.MAX_X, self.MIN_Y])

        for sprite in self.sprites:
            sprite.draw(self.screen)

        # textPrint.reset()
        # joystick_count = pygame.joystick.get_count()
        # textPrint.print(screen, "Number of joysticks: {}".format(joystick_count))
        # textPrint.print(screen, "Number of lasers: {}".format(len(self._lasers)))

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    def controls(self):
        """Check for control inputs."""

        # Keyboard controls - for testing without joysticks

        # events = pygame.event.get()

        keys = pygame.key.get_pressed()
        for player in self.players:
            player.control(keys=keys)

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

            _ = self.players[i].control(joystick=joystick)
            # if jumped:
            #     self.jumped(self.players[i])

    def logic(self):
        """Calculate game logic."""

        # --- Every sprite does it's thing.
        for sprite in self.sprites:
            sprite.logic()

        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True


class Star():
    """Track the stars."""
    pos_x = 0
    pos_y = 0
    dir = 1
    size_x = 3
    size_y = 10

    def __init__(self):
        """New random star."""
        self.pos_y = STAR_TOP_LAYER
        self.pox_x = 40 + random.randint(10, 100)

    def logic(self):
        """Star movement."""
        self.pos_x += self.dir

    def draw(self, screen):
        """Draw this star."""
        pygame.draw.rect(screen, RED,
                         [self.pos_x, self.pos_y, self.size_x, self.size_y])


# -------- Main Program Loop -----------
field = PlayField()

while not field.done:
    field.controls()
    field.logic()
    field.draw()
    # Limit to 60 frames per second
    clock.tick(60)

# Close everything down
pygame.quit()
