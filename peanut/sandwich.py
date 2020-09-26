"""Sandwich bar for making sandwiches."""

import pygame

from dataclasses import dataclass

from colors import Colors

class Sandwich():
    """Helps draw sandwiches."""

    sandwich_colors = [Colors.BROWN, Colors.GREEN, Colors.YELLOW, Colors.RED, Colors.BROWN]
    sandwich_tall = 30

    @staticmethod
    def draw(screen, pos_x, pos_y):
        """Draw a sandwich at the selected location."""
        sandwich_tall = 30
        sandwich_colors = [Colors.BROWN, Colors.GREEN, Colors.YELLOW, Colors.RED, Colors.BROWN]
        layer_count = 5
        layer_wide = 60
        layer_tall = (sandwich_tall - 5) / layer_count

        for i in range(1, layer_count + 1):
            layer_color = sandwich_colors[i - 1]
            pygame.draw.rect(screen, layer_color,
                             [pos_x, pos_y + ((i - 1) * layer_tall), layer_wide, layer_tall])


@dataclass
class SandwichBar():
    """A place to make sandwiches."""
    pos_x: int = 100
    pos_y: int = 100
    size_x: int = 50
    size_y: int = 50

    slice_count = 0
    slice_size = 0
    slices_per_sandwich = 5

    sandwich_count = 3

    def logic(self):
        """Sandwich rules."""
        if self.slice_count >= self.slices_per_sandwich:
            self.slice_count -= self.slices_per_sandwich
            self.sandwich_count += 1

    def draw(self, screen):
        """Draw the sandwich bar, with sandwiches on it."""
        pygame.draw.rect(screen, Colors.BLUE,
                         [self.pos_x, self.pos_y, self.size_x, self.size_y])

        # -- Slices
        if self.slice_count > 0:
            for i in range(1, self.slice_count + 1):
                pygame.draw.rect(screen, Sandwich.sandwich_colors[i - 1],
                         [self.pos_x + 5, self.pos_y + 5 + (self.slice_size * (i-1)), self.size_x - 10, self.slice_size])

        # -- Stack of Sandwiches
        self.drawsandwiches(screen)

    def drawsandwiches(self, screen):
        """Draw a stack of sandwiches."""
        if self.sandwich_count > 0:
            for i in range(1, self.sandwich_count + 1):
                Sandwich.draw(screen, self.pos_x + 5, self.pos_y - (i * Sandwich.sandwich_tall)) # TODO: Make this a multiple of the layer_tall = 10 below...
