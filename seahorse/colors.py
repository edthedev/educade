"""Helper for some colors."""

import pygame

class Colors():
    """Define some colors."""
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    DARK_BLUE = (70, 100, 200)
    SAND = (230, 200, 150)
    PURPLE = (128, 0, 128)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 128, 0)
    GROUND = (0, 128, 0)
    BROWN = (100, 100, 60)

    @staticmethod
    def fill(surface, color):
        """Fill all pixels of the surface with color, preserve transparency."""
        wide, high = surface.get_size()
        red, green, blue = color
        for xii in range(wide):
            for yii in range(high):
                area = surface.get_at((xii, yii))[3]
                surface.set_at((xii, yii), pygame.Color(red, green, blue, area))
