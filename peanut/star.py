"""Stars that you can catch!"""
import random

import pygame

from colors import Colors

class Star():
    """Track the stars."""
    pos_x = 0
    pos_y = 0
    dir = 1
    size_x = 5
    size_y = 5
    STAR_TOP_LAYER = 20
    STAR_MID_LAYER = 200
    STAR_LOW_LAYER = 400
    LAYERS = [STAR_TOP_LAYER, STAR_MID_LAYER,
              STAR_MID_LAYER, STAR_LOW_LAYER, STAR_LOW_LAYER, STAR_LOW_LAYER]
    STAR_COLORS = [Colors.RED, Colors.YELLOW, Colors.ORANGE, Colors.WHITE, Colors.BLUE]

    def __init__(self, max_x):
        """New random star."""
        self.pos_y = random.choice(self.LAYERS) # Randomly pick a layer
        self.pox_x = 40 + random.randint(10, 100)
        self.dir = random.choice([-1, 1]) # Move left or right.
        self.color = random.choice(self.STAR_COLORS)
        if self.dir == 1:
            self.pox_x = 1
        else:
            self.pos_x = max_x - 1

    def logic(self):
        """Star movement."""
        self.pos_x += self.dir

    def draw(self, screen):
        """Draw this star."""
        pygame.draw.rect(screen, self.color,
                         [self.pos_x, self.pos_y, self.size_x, self.size_y])
