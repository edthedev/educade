import pygame
import random

from dataclasses import dataclass, field
from typing import List

from image import Images

@dataclass
class Flora():
    """Places to hide."""

    pos_x: int = 0
    pos_y: int = 0
    size_x: int = 600
    size_y: int = 600

    img: pygame.Surface = None

    def __post_init__(self):
        """Randomize self."""
        self.pos_x = random.choice(range(1,400)) # TODO: Place flora with more control?
        self.pos_y = random.choice(range(1,400))
        self.img = pygame.image.load(Images.get_path(r'flora.purple.png'))
        self.img = pygame.transform.scale(self.img, (int(self.size_x), int(self.size_y)))

    def draw(self, screen):
        """Draw self on the screen."""
        screen.blit(self.img, (self.pos_x, self.pos_y))
    
    def logic(self):
        """Pass"""
        pass
