"""Lasers!

Sssh. They are secret lasers.
"""

from dataclasses import dataclass

import pygame

from image import Images

@dataclass
class Laser():
    """A laser! Pew!"""

    img = pygame.image.load(Images.get_path(r'laser.png'))
    size_x: int = 50
    size_y: int = 500
    pos_x: int = 0
    pos_y: int = 0

    def __post_init__(self):
        """Size the laser."""
        self.img = pygame.transform.scale(self.img,
                                          (self.size_x, self.size_y))

    def draw(self, screen):
        """Draw a laser."""
        screen.blit(self.img, (self.pos_x, self.pos_y))
