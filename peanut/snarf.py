"""Player handler."""

from dataclasses import dataclass, field

import pygame

from sandwich import Sandwich, SandwichBar
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

    >>> Snarf(pos_x=9001).pos_x
    9001

    >>> Snarf(pos_x=9001).pos_y
    100

    >>> type(Snarf().img)
    <class 'pygame.Surface'>

    """
    pos_x: int = 100
    pos_y: int = 100
    size_x: int = 100
    size_y: int = 100
    move_amt: int = 5
    dying: int = 0
    falling: int = 0
    has_sandwich: bool = False

    ground_y: int = 0 # override this!
    images: SnarfImages = SnarfImages()
    img: pygame.Surface = pygame.image.load(Images.get_path(r'snarf.png'))

    def logic(self):
        """Do snarf game logic."""

        # Move in from the side.
        if self.pos_x < SandwichBar.pos_x:
            self._right()

        if self.pos_x > SandwichBar.pos_x:
            self._left()

        self.img = pygame.transform.scale(self.img, (int(self.size_x), int(self.size_y)))

        # TODO: Make Snarfs retreat after getting a sandwich.

        # Move down toward the sandwiches.
        if self.inline_with(SandwichBar):
            if self.pos_y < SandwichBar.pos_y:
                self._down()

        self.img = None

        #if self.dying:
        #    self.img = pygame.image.load(self.images.dying)
        #elif self.falling:
        #    self.img = pygame.image.load(self.images.falling)
        # else:
        #    self.img = pygame.image.load(self.images.default)
        # self.img = pygame.transform.scale(self.img, (int(self.size_x), int(self.size_y)))


    def collide(self, other):
        """Detect a collision."""
        return (
            self.pos_x-self.size_x < other.pos_x + other.size_x and
            self.pos_y - self.size_y < other.pos_y and
            self.pos_x+self.size_x > other.pos_x+other.size_x and
            self.pos_y + self.size_y > other.pos_y
        )


    def _down(self):
        """Start descending on a sandwich."""
        self.falling = 1

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

    def land_on(self, pad):
        """Detect if we landed on a launcher.

        >>> Snarf().land_on(SandwichBar())
        False

        >>> Snarf(pos_y=90, size_y=10).land_on(SandwichBar(pos_y=100, size_y=10))
        True
        """
        bottom_of_self = self.pos_y + self.size_y
        margin = 3
        return (
            self.inline_with(pad)
            and pad.pos_y - margin < bottom_of_self
            and bottom_of_self < pad.pos_y + margin
        )

    def inline_with(self, pad):
        """Return true if lined up in a vertical column with player.

        >>> Snarf().inline_with(Snarf())
        True

        >>> Snarf(pos_x=20, size_x=10).inline_with(Snarf(pos_x=15, size_x=10))
        True

        >>> Snarf(pos_x=200, size_x=10).inline_with(Snarf(pos_x=15, size_x=10))
        False

        >>> Snarf(pos_y=100,size_y=10).inline_with(Snarf(pos_y=90))
        True
        """
        return (
            pad.pos_x + pad.size_x > self.pos_x
            and pad.pos_x < self.pos_x + self.size_x
        )

if __name__ == "__main__":
    import doctest
    doctest.testmod()
