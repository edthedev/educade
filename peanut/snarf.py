"""Player handler."""

from dataclasses import dataclass

import pygame

from sandwich import SandwichBar
from image import Images

@dataclass
class SnarfImages():
    """Images of a Snarf"""
    default: str = Images.get_path(r'snarf.png')
    alt: str = Images.get_path(r'snarf2.png')
    falling: str = ''
    eating: str = ''
    dying: str = ''

@dataclass
class Snarf():
    """A snarf tries to eat the sandwiches.

    Players can catch them in the air to stop them.

    >>> Snarf(SandwichBar(), pos_x=9001).pos_x
    9001

    >>> Snarf(SandwichBar(), pos_x=9001).pos_y
    100

    >>> type(Snarf(SandwichBar()).img)
    <class 'pygame.Surface'>

    """
    sandwich_bar: SandwichBar
    pos_x: int = -100
    pos_y: int = -100
    size_x: int = 100
    size_y: int = 100
    move_amt: int = 1
    dying: int = 0
    falling: int = 0
    has_sandwich: bool = False
    full: int = 0
    img_number: int = 0

    ground_y: int = 0 # override this!
    images: SnarfImages = SnarfImages()
    img: pygame.Surface = pygame.image.load(Images.get_path(r'snarf.png'))
    img1: pygame.Surface = pygame.image.load(Images.get_path(r'snarf.png'))
    img2: pygame.Surface = pygame.image.load(Images.get_path(r'snarf2.png'))

    def __post_init__(self):
        self.img = pygame.transform.scale(self.img, (int(self.size_x), int(self.size_y)))

    def logic(self):
        """Do snarf game logic.

        Generally, move toward the sandwich bar.
        """

        self.img_number += 1
        if self.img_number == 20:
            self.img = self.img1
        if self.img_number > 40:
            self.img_number = 0
            self.img = self.img2

        # Move in from the side.

        if self.full:
            self.reset()

        ## Float in from off screen.
        if self.pos_y < 0:
            self.pos_y += self.move_amt
        if self.pos_x < 0:
            self._right()

        # Move down toward the sandwiches.
        if self.inline_with_sandwich_bar():
            if self.pos_y < self.sandwich_bar.pos_y:
                self.pos_y += self.move_amt
        else:
            if self.pos_x < self.sandwich_bar.pos_x:
                self._right()

            if self.pos_x >= self.sandwich_bar.pos_x:
                self._left()

        #if self.dying:
        #    self.img = pygame.image.load(self.images.dying)
        #elif self.falling:
        #    self.img = pygame.image.load(self.images.falling)
        # else:
        #    self.img = pygame.image.load(self.images.default)


    def collide(self, other):
        """Detect a collision."""
        return (
            self.pos_x-self.size_x < other.pos_x + other.size_x and
            self.pos_y - self.size_y < other.pos_y and
            self.pos_x+self.size_x > other.pos_x+other.size_x and
            self.pos_y + self.size_y > other.pos_y
        )

    def reset(self):
        """Move soemwhere random."""
        self.pos_y = -100
        self.pos_x = -100

    def _left(self):
        """Move self left."""
        self.pos_x -= self.move_amt

    def _right(self):
        """Move self right."""
        self.pos_x += self.move_amt

    def draw(self, screen):
        """Draw the snarf."""
        screen.blit(self.img, (self.pos_x, self.pos_y))

        # if self.has_sandwich:
        #    Sandwich.draw(screen, self.pos_x,
        #                  pos_y=self.pos_y - Sandwich.sandwich_tall)

    def inline_with_sandwich_bar(self):
        """Return true if lined up in a vertical column with player.

        >>> Snarf(SandwichBar(pos_x=500), pox_x = 500).inline_with_sandwich_bar()
        True

        >>> Snarf(SandwichBar(pos_x=0), pox_x = 500).inline_with_sandwich_bar()
        False

        >>> Snarf(SandwichBar(pos_x=450), pox_x = 500).inline_with_sandwich_bar()
        True

        """
        return (
            self.sandwich_bar.pos_x - 30 < self.pos_x
            and
            self.sandwich_bar.pos_x + 30 > self.pos_x
            # or
            # pad.pos_x + pad.size_x > self.pos_x
            # and pad.pos_x < self.pos_x + self.size_x
        )

if __name__ == "__main__":
    import doctest
    doctest.testmod()
