"""Ocean floor things to hide behind."""
from dataclasses import dataclass

import pygame

from image import Images
from colors import Colors

@dataclass
class Flora():
    """Places to hide."""

    size: int
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
    img_scale: int = 5
    img_color: pygame.Color = None

    def __post_init__(self):
        """Randomize self."""
        self.img = pygame.image.load(Images.get_path(r'flora.purple.png'))

        # Size
        self.block_size = int(self.size_multiple * 32)
        self.img_scale = int(self.size / self.block_size)

        self.size_x = self.block_size * self.img_scale
        self.size_y = self.block_size * self.img_scale
        self.img = pygame.transform.scale(self.img,
                                          (int(self.size_x * self.img_cols),
                                           int(self.size_y * self.img_rows)))
        if self.img_color:
            pass
        # TODO: Blit blend in the desired color.

        # Pick which variety we are.
        var_x = self.variety % self.img_cols
        var_y = self.variety % self.img_rows
        self.draw_area = pygame.Rect(var_x * self.block_size * self.img_scale,
                                     var_y * self.block_size * self.img_scale,
                                     self.block_size * self.img_scale,
                                     self.block_size * self.img_scale)

    def draw(self, screen):
        """Draw self on the screen."""
        pygame.draw.rect(screen, Colors.DARK_BLUE,
                         [self.pos_x, self.pos_y, self.size_x, self.size_y])
        screen.blit(self.img, (self.pos_x, self.pos_y), area=self.draw_area)