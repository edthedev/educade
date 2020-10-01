"""Ocean floor things to hide behind."""

import pygame
import random

from dataclasses import dataclass, field
from typing import List
from colors import Colors

from image import Images

@dataclass
class Flora():
    """Places to hide."""

    pos_x: int = 0
    pos_y: int = 0
    size_x: int = 0
    size_y: int = 0
    variety: int = 0
    size_multiple: int = .5
    block_size: int = 0

    img: pygame.Surface = None
    draw_area: pygame.Rect = None

    img_rows: int = 2
    img_cols: int = 3
    img_scale: int = 3

    def __post_init__(self):
        """Randomize self."""
        self.img = pygame.image.load(Images.get_path(r'flora.purple.png'))

        # Size
        self.block_size = int(self.size_multiple * 32)
        self.size_x = self.block_size * self.img_scale
        self.size_y = self.block_size * self.img_scale
        self.img = pygame.transform.scale(self.img,
                                          (int(self.size_x * self.img_cols),
                                           int(self.size_y * self.img_rows)))

        # Pick which variety we are.
        self.draw_area = pygame.Rect(self.variety * self.block_size * self.img_scale,
                                     0,
                                     self.block_size * self.img_scale,
                                     self.block_size * self.img_scale)

    def draw(self, screen):
        """Draw self on the screen."""
        pygame.draw.rect(screen, Colors.WHITE,
                         [self.pos_x, self.pos_y, self.size_x, self.size_y])
        screen.blit(self.img, (self.pos_x, self.pos_y), area=self.draw_area)
    
    def logic(self):
        """Pass"""
        pass
