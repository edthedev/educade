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
    variety: int = 0

    img: pygame.Surface = None
    draw_area: pygame.Rect = pygame.Rect(0, 0, 64, 64)

    def __post_init__(self):
        """Randomize self."""
        self.pos_x = random.choice(range(1,400)) # TODO: Place flora with more control?
        self.pos_y = random.choice(range(1,400))
        self.img = pygame.image.load(Images.get_path(r'flora.purple.png'))
        self.img = pygame.transform.scale(self.img, (int(self.size_x), int(self.size_y)))

        # Pick which variety we are.
        self.variety = random.choice(range(1,3))
        self.draw_area = pygame.Rect(self.variety * 32, 0, (self.variety + 1)* 32, 64)


    def draw(self, screen):
        """Draw self on the screen."""
        screen.blit(self.img, (self.pos_x, self.pos_y), area=self.draw_area)
    
    def logic(self):
        """Pass"""
        pass
