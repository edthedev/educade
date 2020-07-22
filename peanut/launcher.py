import pygame
from colors import Colors

class Launcher():
    """A Nutnik launcher"""
    size_x = 100
    size_y = 50

    def __init__(self, pos_x, pos_y, size_x, size_y):
        """Make a launcher"""
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y
        self._players = [] # Players sitting on the launcher now.

    def draw(self, screen):
        """Draw the launcher."""
        pygame.draw.rect(screen, Colors.RED,
                [self.pos_x, self.pos_y, self.size_x, self.size_y])
    
    def add_player(self, player):
        """Add a player to the launcher."""
        self._players += [player]

    def launch_players(self):
        """Launch all players previously added."""
        for player in self._players:
            player.launched = 1
            self._players = []