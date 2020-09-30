"""Most of the game is managed by the play field."""

from dataclasses import dataclass, field
from typing import List

import random
import pygame

from player import Player, PlayerImages
from controls import ControlSet
from colors import Colors
from image import Images
from flora import Flora

# Set these to the two buttons you want to use for 'exit'. Count up starting from 0
SELECT = 3
START = 4



@dataclass
class PlayField():
    """Track the play field."""
    min_x: int = 0
    max_x: int = 1200
    min_y: int = 900
    max_y: int = 0
    debug: bool = False
    fish: List[ControlSet] = field(default_factory=list)
    flora: List[Flora] = field(default_factory=list)

    def __post_init__(self):
        """New play field."""

        self.ground_y = self.min_y - 100

        self.done = False
        self.sprites = []
        self.players = []
        self.stars = []
        self.add_players()
        self.screen = None
        self.add_flora()
        self.add_flora()
        self.add_flora()
        self.add_flora()

        if self.debug:
            pass

        # Initialize the joysticks
        pygame.init()
        pygame.joystick.init()
        size = [self.max_x, self.min_y]
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Undersea Hide and Seek")
        pygame.mouse.set_visible(False)

    def add_players(self):
        """Create the players.

        Return an array of the players as objects with .draw methods.
        """
        player1 = Player(color=Colors.YELLOW,
                         start_x=self.max_x / 5 * 2,
                         controls=[ControlSet()])
        player1.images = PlayerImages(
            default=Images.get_path(r'horse.purple.png')
        )
        player2 = Player(color=Colors.RED,
                         start_x=self.max_x / 5 * 4,
                         controls=[ControlSet(up=pygame.K_j, down=pygame.K_k,
                                              left=pygame.K_h, right=pygame.K_l),
                                   ControlSet(up=pygame.K_w, down=pygame.K_s,
                                              left=pygame.K_a, right=pygame.K_d)])
        player2.images = PlayerImages(
            default=Images.get_path(r'squid.purple.png')
        )
        player3 = Player(color=Colors.BLUE,
                         start_x=self.max_x / 5,
                         controls=[ControlSet(up=pygame.K_3, down=pygame.K_2,
                                              left=pygame.K_1, right=pygame.K_4)])
        player3.images = PlayerImages(
            default=Images.get_path(r'flounder.purple.png')
        )
        player4 = Player(color=Colors.PURPLE,
                         start_x=self.max_x / 5 * 3,
                         controls=[ControlSet(up=pygame.K_7, down=pygame.K_6,
                                              left=pygame.K_5, right=pygame.K_8)])
        player4.images = PlayerImages(
            default=Images.get_path(r'cuttlefish.purple.png')
        )


        self.players = [player1, player2, player3, player4]
        for player in self.players:
            player.pos_y = self.ground_y - player.size_y / 2
            player.ground_y = self.ground_y
            player.max_x = self.max_x

    def add_flora(self):
        """Add places to hide."""
        # self.fish += [ScaryFish()]
        self.flora += [Flora()]

    def add_fish(self):
        """Occassionally add a scary fish to the play field."""
        # self.fish += [ScaryFish()]

    def draw(self):
        """Re-Draw the play field."""
        self.screen.fill(Colors.DARK_BLUE)  # background

        for flora in self.flora:
            flora.draw(self.screen)

        for player in self.players:
            player.draw(self.screen)


        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    def controls(self):
        """Check for control inputs."""

        # Keyboard controls - for testing without joysticks

        # events = pygame.event.get()

        keys = pygame.key.get_pressed()
        for player in self.players:
            player.control(keys=keys)

        # Get count of joysticks
        joystick_count = pygame.joystick.get_count()

        # For each joystick:
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()

            # Exit like RetroArch - any joystick
            button7 = joystick.get_button(SELECT)
            button8 = joystick.get_button(START)
            if button7 == button8 == 1:
                self.done = True

            _ = self.players[i].control(joystick=joystick)
            # if jumped:
            #     self.jumped(self.players[i])

    def logic(self):
        """Calculate game logic."""
        self.sprites = self.players + self.flora

        # --- Arrange
        # The field adds things
        if random.randint(0, 10000) > (9990):  # New Snarf
            self.add_fish()

        # --- Act
        # Every sprite does it's thing.
        for sprite in self.sprites:
            sprite.logic()

        for star in self.stars:
            if star.pos_x < 0 or star.pos_x > self.max_x:
                self.stars.remove(star)  # It is off screen. Stop tracking it.

        # The field taketh away
        for player in self.players:
            # Grab a sandwich!
            for fish in self.fish:
                if player.collide(fish):  # Catch a snarf!
                    pass
                    # TODO: Rewind back to last hiding place.

        # --- Assert --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
