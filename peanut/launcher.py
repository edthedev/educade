"""Launch a Nutkin!"""
from dataclasses import dataclass, field
from typing import List, Set, Dict, Tuple, Optional

import pygame
from colors import Colors
from player import Player

@dataclass
class Launcher():
    """A Nutnik launcher"""
    size_x = 100
    size_y = 50
    pos_x: int = 50
    pos_y: int = 50
    size_x: int = 50
    size_y: int = 50
    players: List[Player]=field(default_factory=list)

    def __post_init__(self):
        """Start with an empty player list."""
        self._players = []

    def draw(self, screen):
        """Draw the launcher."""
        pygame.draw.rect(screen, Colors.RED,
                [self.pos_x, self.pos_y, self.size_x, self.size_y])

    def add_player(self, player):
        """Add a player to the launcher."""
        self._players += [player]

    def launch_players_who_are_not(self, no_launch_player):
        """Launch all players previously added."""
        for player in self._players:
            if player != no_launch_player:
                player.launched = 1
            self._players = []