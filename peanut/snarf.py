"""Player handler."""

from dataclasses import dataclass

import pygame

from sandwich import Sandwich, SandwichBar

@dataclass
class SnarfImages():
    """Images of a Snarf"""
    default: str
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
    """
    pos_x: int = 100
    pos_y: int = 100
    size_x: int = 50
    size_y: int = 50
    move_amt: int = 5
    dying: int = 0
    falling: int = 0
    has_sandwich: bool = False
    move_x: int = 10
    move_y: int = 10

    ground_y: int = 0 # override this!
    images: SnarfImages = None

    def logic(self):
        """Do snarf game logic."""

        # Move in from the side.
        if(self.pos_x < SandwichBar.pox_x):
            self.pos_x += self.move_x

        if(self.pos_x > SandwichBar.pox_x):
            self.pos_x -= self.move_x

        # TODO: Make Snarfs retreat after getting a sandwich.

        # Move down toward the sandwiches.
        if(self.inline_with(SandwichBar)):
            if(self.pos_y < SandwichBar.pox_y):
                self.pos_y += self.move_y

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

        img = None

        if self.dying:
            img = pygame.image.load(self.images.dying)
        elif self.falling:
            img = pygame.image.load(self.images.falling)
        else:
            img = pygame.image.load(self.images.default)
        img = pygame.transform.scale(img, (int(self.size_x), int(self.size_y)))

        screen.blit(img, (self.pos_x, self.pos_y))

        if self.has_sandwich:
            Sandwich.draw(screen, self.pos_x,
                          pos_y=self.pos_y - Sandwich.sandwich_tall)

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
