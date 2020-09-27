"""Launch a Nutkin!"""
from dataclasses import dataclass, field
from typing import List

import pygame
from colors import Colors
from player import Player
from image import Images

@dataclass
class Launcher():
    """A Nutnik launcher"""
    size_x = 100
    size_y = 50
    pos_x: int = 50
    pos_y: int = 50
    size_x: int = 50
    size_y: int = 80
    players: List[Player] = field(default_factory=list)
    img_launcher = pygame.image.load(Images.get_path(r'launcher.png'))
    img_launched = pygame.image.load(Images.get_path(r'launched.png'))
    img = img_launcher
    launching: int = 0
    size_change = 20

    def __post_init__(self):
        """Start with an empty player list."""
        self._players = []
        self.img_launched = pygame.transform.scale(self.img_launched,
                                                   (self.size_x, self.size_y + self.size_change))
        self.img_launcher = pygame.transform.scale(self.img_launcher, (self.size_x, self.size_y))
        self.img = self.img_launcher

    def draw(self, screen):
        """Draw the launcher."""
        if self.launching > 0:
            self.img = self.img_launched
            self.launching -= 1
            screen.blit(self.img, (self.pos_x, self.pos_y - self.size_change))
        else:
            self.img = self.img_launcher
            screen.blit(self.img, (self.pos_x, self.pos_y))

        #pygame.draw.rect(screen, Colors.RED,
        #                 [self.pos_x, self.pos_y, self.size_x, self.size_y])

    def add_player(self, player):
        """Add a player to the launcher."""
        self._players += [player]

    def launch_players_who_are_not(self, no_launch_player):
        """Launch all players previously added."""
        for player in self._players:
            if player != no_launch_player:
                player.launched = 1
                self.launching = 8
            self._players = []
