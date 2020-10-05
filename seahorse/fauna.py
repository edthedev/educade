"""Things in the ocean to hide from."""
from dataclasses import dataclass

import pygame

from image import Images
from player import Player

# TODO: Sweep to make all lib names plural.

@dataclass
class Fauna():
    """Something to hide from."""

    size: int
    pos_x: int = 0
    pos_y: int = 0
    size_x: int = 0
    size_y: int = 0
    variety: int = 0
    size_multiple: int = .5
    block_size: int = 0
    move_delay: int = 1
    move_clock: int = 0
    move_amt: int = 1

    img: pygame.Surface = None
    draw_area: pygame.Rect = None

    img_rows: int = 2
    img_cols: int = 3
    img_scale: int = 10
    img_color: pygame.Color = None
    chasing_player: Player = None

    def __post_init__(self):
        """Size self."""
        self.img = pygame.image.load(Images.get_path(r'fauna.white.png'))
        red = pygame.image.load(Images.get_path(r'red.png'))

        # Size
        self.block_size = int(self.size_multiple * 32)
        self.img_scale = int(self.size / self.block_size)

        self.size_x = self.block_size * self.img_scale
        self.size_y = self.block_size * self.img_scale

        self.img_color = True
        if self.img_color:
            self.img.blit(red, (0, 0), special_flags=pygame.BLEND_ADD)

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
        screen.blit(self.img, (self.pos_x, self.pos_y), area=self.draw_area)

    def logic(self):
        """Swim slowly against the current."""
        # TODO: Catch players and drag them off screen.
        self.move_clock = self.move_clock % self.move_delay
        self.move_clock += 1
        if self.move_clock >= self.move_delay:
            if self.chasing_player is None:
                self.pos_x -= self.move_amt
            else:
                if self.pos_y > self.chasing_player.pos_y:
                    self.pos_y -= self.move_amt
                else:
                    self.pos_y += self.move_amt

    def can_see(self, player):
        """Can we see this player?"""
        return player.hidden_in is None and player.inline_with(self)
