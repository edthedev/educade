import pygame
from colors import Colors

def Launcher():
    """A Nutnik launcher"""
    size_x = 100
    size_y = 50

    def __init__(self, pos_x, pos_y):
        """Make a launcher"""
        self.pos_x = pos_x
        self.pos_y = pos_y

    def draw(self, screen):
        """Draw the sandwich bar, with sandwiches on it."""
        pygame.draw.rect(screen, Colors.RED,
                [self.pos_x, self.pos_y, size_x, size_y])