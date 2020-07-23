"""Most of the game is managed by the play field."""

import random
import pygame
from player import Player
# from text import TextPrint
from controls import ControlSet
from sandwich import SandwichBar
from colors import Colors
from launcher import Launcher
from star import Star

# Set these to the two buttons you want to use for 'exit'. Count up starting from 0
SELECT = 3
START = 4


class PlayField():
    """Track the play field."""
    MIN_X = 0
    MAX_Y = 0

    def __init__(self, max_x=1200, min_y=900):
        """New play field."""

        self.max_x = max_x
        self.min_y = min_y
        self.ground_y = self.min_y - 100

        self.done = False
        self.sprites = []
        self.players = []
        self.stars = []
        self.add_players()
        self.add_sandwich_bar()
        self.add_launchers()
        self.screen = None

        # Initialize the joysticks
        pygame.init()
        pygame.joystick.init()
        size = [self.max_x, self.min_y]
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Peanut Butter Panic")
        pygame.mouse.set_visible(False)

    def add_star(self):
        """Add a star."""
        self.stars += [Star(self.max_x)]

    def add_sandwich_bar(self):
        """Add the sandwich bar to the playing field."""
        self.sandwich_bar = SandwichBar(pos_x=self.max_x / 2,
                                        size_x=60,
                                        pos_y=self.ground_y - 20,
                                        size_y=self.MAX_Y + self.ground_y + 20)

    def add_launchers(self):
        """Add a couple of launchers."""
        LAUNCHER_SIZE_X = 60
        LAUNCHER_SIZE_Y = 20
        self.launchers = [
            Launcher(pos_x=self.max_x - LAUNCHER_SIZE_X, size_x=LAUNCHER_SIZE_X,
                     pos_y=self.ground_y - 20,
                     size_y=LAUNCHER_SIZE_Y),
            Launcher(pos_x=0, size_x=LAUNCHER_SIZE_X,
                     pos_y=self.ground_y - 20,
                     size_y=LAUNCHER_SIZE_Y)
        ]

    def add_players(self):
        """Create the players.

        Return an array of the players as objects with .draw methods.
        """
        player1 = Player(color=Colors.YELLOW,
                         controls=[ControlSet(), ControlSet(up=pygame.K_w, down=pygame.K_s,
                                                            left=pygame.K_a, right=pygame.K_d)])
        player2 = Player(color=Colors.RED,
                         controls=[ControlSet(up=pygame.K_j, down=pygame.K_k,
                                              left=pygame.K_h, right=pygame.K_l)])
        player3 = Player(color=Colors.BLUE,
                         controls=[ControlSet(up=pygame.K_3, down=pygame.K_2,
                                              left=pygame.K_1, right=pygame.K_4)])
        player4 = Player(color=Colors.PURPLE,
                         controls=[ControlSet(up=pygame.K_7, down=pygame.K_6,
                                              left=pygame.K_5, right=pygame.K_8)])
        self.players = [player1, player2, player3, player4]
        for player in self.players:
            player.pos_y = self.ground_y
            player.ground_y = self.ground_y

    def draw(self):
        """Re-Draw the play field."""
        self.screen.fill(Colors.BLACK)  # background
        pygame.draw.rect(self.screen, Colors.GROUND,
                         [self.MIN_X, self.ground_y, self.max_x, self.min_y])
        self.sandwich_bar.draw(self.screen)

        for launcher in self.launchers:
            launcher.draw(self.screen)

        for sprite in self.sprites:
            sprite.draw(self.screen)

        # textPrint.reset()
        # joystick_count = pygame.joystick.get_count()
        # textPrint.print(screen, "Number of joysticks: {}".format(joystick_count))
        # textPrint.print(screen, "Number of lasers: {}".format(len(self._lasers)))

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
        self.sprites = self.players + \
            self.stars  # Changes because stars get removed.

        # --- Arrange
        # The field adds things
        if random.randint(0, 1000) > 990:  # New star frequency
            self.add_star()

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
            if player.collide(self.sandwich_bar) \
                and (player.has_sandwich == 0) and self.sandwich_bar.sandwich_count > 0:
                player.has_sandwich = 1
                self.sandwich_bar.sandwich_count -= 1
            for star in self.stars:
                if player.collide(star):  # Catch a star!
                    self.stars.remove(star)
                    self.sandwich_bar.slice_count += 1
                    if player.color == star.color:
                        self.sandwich_bar.slice_count += 1
                    if star.pos_y == Star.STAR_TOP_LAYER:
                        self.sandwich_bar.slice_count += 2

            for launcher in self.launchers:
                if player.land_on(launcher):
                    player.falling = 0
                    launcher.launch_players_who_are_not(player)
                    launcher.add_player(player)

        # Slices add up to sandwiches.
        self.sandwich_bar.logic()

        # --- Assert --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
