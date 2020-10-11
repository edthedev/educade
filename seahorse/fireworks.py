"""Kaboom! Celebration!"""
from dataclasses import dataclass

import random
import pygame

from images import Images

@dataclass
class Firework():
    """Something to hide from."""

    size: int
    pos_x: int = 0
    pos_y: int = 0
    variety: int = 0
    size_multiple: int = 1

    move_delay: int = 1
    move_clock: int = 0
    move_amt: int = 1

    img: pygame.Surface = None
    draw_area: pygame.Rect = None

    img_rows: int = 2
    img_cols: int = 3
    img_scale: int = 10
    img_color: pygame.Color = None

    def __post_init__(self):
        """Size self."""
        self.img = pygame.image.load(Images.get_path(r'firework.png'))

        # Size
        self.block_size = int(self.size_multiple * 32)
        self.img_scale = int(self.size / self.block_size)

        self.size_x = self.block_size * self.img_scale
        self.size_y = self.block_size * self.img_scale

        self.img_color = True

        color = random.choice(Images.color_files)
        color_img = pygame.image.load(Images.get_path(color))
        self.img = Images.color_image(base_image=self.img, color_image=color_img)

        self.img = pygame.transform.scale(self.img,
                                          (int(self.size_x * self.img_cols),
                                           int(self.size_y * self.img_rows)))

    def draw(self, screen):
        """Draw self on the screen."""
        #pygame.draw.rect(screen, Colors.DARK_BLUE,
        #                 [self.pos_x, self.pos_y, self.size_x, self.size_y])
        screen.blit(self.img, (self.pos_x, self.pos_y), area=self.draw_area)

    def logic(self):
        """Move slowly upward and then go boom."""

        if self.move_clock < 20:
            self.pos_y -= self.move_amt
        else:
            if self.variety < 6:
                self.variety += 1

            # Pick which variety we are.
            var_x = self.variety % self.img_cols
            var_y = self.variety % self.img_rows
            self.draw_area = pygame.Rect(var_x * self.block_size * self.img_scale,
                                        var_y * self.block_size * self.img_scale,
                                        self.block_size * self.img_scale,
                                        self.block_size * self.img_scale)

