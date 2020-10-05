"""Ocean floor things to hide behind."""
from dataclasses import dataclass

import random
import pygame

from images import Images

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
    move_delay: int = 2
    move_clock: int = 0
    move_amt: int = 1

    img: pygame.Surface = None
    draw_area: pygame.Rect = None

    img_rows: int = 2
    img_cols: int = 3
    img_scale: int = 10
    img_color: int = 0

    is_home: bool = False

    def __post_init__(self):
        """Randomize self."""
        self.img = pygame.image.load(Images.get_path(r'flora.png'))

        if self.is_home:
            self.img = pygame.image.load(Images.get_path(r'home.png'))

        # Pick which color we are
        self.img_color = random.choice(range(0, 5))
        color_file = Images.color_files[self.img_color]
        color_img = pygame.image.load(Images.get_path(color_file))

        # Apply chosen color
        if not self.is_home:
            Images.color_image(self.img, color_img)

        # Size
        self.block_size = int(self.size_multiple * 32)
        self.img_scale = int(self.size / self.block_size)

        self.size_x = self.block_size * self.img_scale
        self.size_y = self.block_size * self.img_scale
        self.img = pygame.transform.scale(self.img,
                                          (int(self.size_x * self.img_cols),
                                           int(self.size_y * self.img_rows)))

        # Pick which variety we are.
        var_x = self.variety % self.img_cols
        var_y = self.variety % self.img_rows
        self.draw_area = pygame.Rect(var_x * self.block_size * self.img_scale,
                                     var_y * self.block_size * self.img_scale,
                                     self.block_size * self.img_scale,
                                     self.block_size * self.img_scale)


    def draw(self, screen):
        """Draw self on the screen."""
        #pygame.draw.rect(screen, Colors.DARK_BLUE,
        #                 [self.pos_x, self.pos_y, self.size_x, self.size_y])
        if self.is_home:
            screen.blit(self.img, (self.pos_x, self.pos_y))
        else:
            screen.blit(self.img, (self.pos_x, self.pos_y), area=self.draw_area)

    def logic(self):
        """Drift slowly to create the current."""
        self.move_clock = self.move_clock % self.move_delay
        self.move_clock += 1
        if self.move_clock >= self.move_delay:
            self.pos_x -= self.move_amt
