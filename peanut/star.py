"""Stars that you can catch!"""
import random
import os
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
    STAR_LOW_LAYER = 350
    STAR_LOWEST_LAYER = 400
    LAYERS = [STAR_TOP_LAYER, STAR_MID_LAYER,
              STAR_MID_LAYER, STAR_LOW_LAYER, STAR_LOW_LAYER, 
              STAR_LOWEST_LAYER, STAR_LOWEST_LAYER, STAR_LOWEST_LAYER]
    STAR_COLORS = [Colors.RED, Colors.YELLOW, Colors.ORANGE, Colors.WHITE, Colors.BLUE, Colors.PURPLE]

    def __init__(self, max_x):
        """New random star."""
        self.pos_y = random.choice(self.LAYERS) # Randomly pick a layer
        self.pox_x = 40 + random.randint(10, 100)
        self.dir = random.choice([-1, 1]) # Move left or right.
        self.color = random.choice(self.STAR_COLORS)

        path = os.path.dirname(os.path.abspath(__file__))
        self.img = pygame.image.load(path + r'/img/star.png')

        if self.color == Colors.PURPLE:
            self.img = pygame.image.load(path + r'/img/star_purple.png')
        if self.color == Colors.RED:
            self.img = pygame.image.load(path + r'/img/star_red.png')
        if self.color == Colors.BLUE:
            self.img = pygame.image.load(path + r'/img/star_blue.png')

        if self.pos_y == self.STAR_MID_LAYER:
            self.img = pygame.image.load(path + r'/img/star_med.png')
        if self.pos_y == self.STAR_TOP_LAYER:
            self.img = pygame.image.load(path + r'/img/star_big.png')

        self.img = pygame.transform.scale(self.img, (int(30), int(30)))

        if self.dir == 1:
            self.pox_x = 1
        else:
            self.pos_x = max_x - 1

    def logic(self):
        """Star movement."""
        self.pos_x += self.dir

    def draw(self, screen):
        """Draw this star."""
        screen.blit(self.img, (self.pos_x, self.pos_y))

        # pygame.draw.rect(screen, self.color,
                         # [self.pos_x, self.pos_y, self.size_x, self.size_y])
