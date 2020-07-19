import pygame
import random

from colors import Colors

class SandwichBar():
    """A place to make sandwiches."""
    slice_count = 0
    slice_size = 5
    slices_per_sandwich = 6

    sandwich_count = 0

    def __init__(self, pos_x, pos_y, size_x, size_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y
    
    def logic(self):
        """Sandwich rules."""
        if self.slice_count >= self.slices_per_sandwich:
            self.slice_count -= self.slices_per_sandwich
            self.sandwich_count +=1

    def draw(self, screen):
        """Draw the sandwich bar, with sandwiches on it."""
        pygame.draw.rect(screen, Colors.BLUE,
                         [self.pos_x, self.pos_y, self.size_x, self.size_y])

        # -- Slices
        if self.slice_size > 0:
            for i in range(1, self.slice_count):
                pygame.draw.rect(screen, Colors.ORANGE,
                         [self.pos_x + 5, self.pos_y + 5 + (self.slice_size * (i-1)), self.size_x - 10, self.slice_size])

        # -- Stack of Sandwiches
        self.drawsandwiches(screen, self.pos_x, self.pos_y)

    def drawsandwiches(self, screen, pos_x, pos_y):
        """Draw a stack of sandwiches."""
        if self.sandwich_count > 0:
            for i in range(1, self.sandwich_count):
                self.drawsandwich(screen, self.pos_x + 5, self.pos_y + 30) # TODO: Make this a multiple of the layer_tall = 10 below...

    def drawsandwich(self, screen, pos_x, pos_y):
        """Draw a sandwich at x / y"""
        layer_count = 3

        sandwich_colors = [Colors.GREEN, Colors.BROWN, Colors.YELLOW, Colors.RED]

        layer_wide = self.size_x - 10
        layer_tall = 10

        for i in range(1, layer_count):
            if i == 1 or i == layer_count:
                layer_color = Colors.ORANGE
            else: 
                layer_color = random.choice(sandwich_colors)

            pygame.draw.rect(screen, layer_color,
                [pos_x, pos_y + (i- 1) * layer_tall, layer_wide, layer_tall])
