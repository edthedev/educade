"""Most of the game is managed by the play field."""

from dataclasses import dataclass, field
from typing import List

import random
import pygame

from players import Player, PlayerImages
from controls import ControlSet
from colors import Colors
from images import Images
from flora import Flora
from fauna import Fauna

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
    retreat_x: int = 400
    debug: bool = False
    fish: List[ControlSet] = field(default_factory=list)
    flora: List[Flora] = field(default_factory=list)
    fauna: List[Fauna] = field(default_factory=list)
    clock: int = 0
    flora_size: int = 80
    player_size: int = 40

    def __post_init__(self):
        """New play field."""

        self.ground_y = self.min_y - 100

        self.done = False
        self.sprites = []
        self.players = []
        self.stars = []
        self.add_players()
        self.screen = None

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
            default=Images.get_path(r'seahorse.png'),
            size_x=self.player_size,
            size_y=self.player_size
        )
        player2 = Player(color=Colors.RED,
                         start_x=self.max_x / 5 * 4,
                         controls=[ControlSet(up=pygame.K_j, down=pygame.K_k,
                                              left=pygame.K_h, right=pygame.K_l),
                                   ControlSet(up=pygame.K_w, down=pygame.K_s,
                                              left=pygame.K_a, right=pygame.K_d)])
        player2.images = PlayerImages(
            default=Images.get_path(r'squid.png'),
            size_x=self.player_size,
            size_y=self.player_size
        )
        player3 = Player(color=Colors.BLUE,
                         start_x=self.max_x / 5,
                         controls=[ControlSet(up=pygame.K_3, down=pygame.K_2,
                                              left=pygame.K_1, right=pygame.K_4)])
        player3.images = PlayerImages(
            default=Images.get_path(r'flounder.png'),
            size_x=self.player_size,
            size_y=self.player_size
        )
        player4 = Player(color=Colors.PURPLE,
                         start_x=self.max_x / 5 * 3,
                         controls=[ControlSet(up=pygame.K_7, down=pygame.K_6,
                                              left=pygame.K_5, right=pygame.K_8)])
        player4.images = PlayerImages(
            default=Images.get_path(r'cuttlefish.png'),
            size_x=self.player_size,
            size_y=self.player_size
        )


        self.players = [player1, player2, player3, player4]
        for player in self.players:
            player.pos_y = self.ground_y - player.size_y / 2
            player.ground_y = self.ground_y
            player.max_x = self.max_x

    def add_flora(self):
        """Add places to hide."""
        new_flora = Flora(variety=random.choice(range(0, 5)),
                          size=self.flora_size,
                          pos_x=self.max_x+self.flora_size,
                          pos_y=random.choice(range(0, self.min_y)))
        self.flora += [new_flora]
        # Let's draw from back to front...
        self.flora.sort(key=lambda x: x.pos_y, reverse=False)

    def add_fish(self):
        """Occassionally add a scary fish to the play field."""
        self.fauna += [Fauna(variety=random.choice(range(0, 5)),
                             size=self.flora_size,
                             pos_x=self.max_x+self.flora_size,
                             pos_y=random.choice(range(0, self.min_y)))]

    def draw(self):
        """Re-Draw the play field."""
        self.screen.fill(Colors.DARK_BLUE)  # background

        for fauna in self.fauna:
            fauna.draw(self.screen)

        # Only draw flora when they first appear.
        for flora in self.flora:
            flora.draw(self.screen)

        # Shift the background before drawing players.
        # self.screen.scroll(dx=-self.clock)
        # self.screen.scroll(dx=-1)

        for player in self.players:
            player.draw(self.screen)

        # Stupid hack to clean up
        # pygame.draw.rect(self.screen, Colors.DARK_BLUE,
        #                 [self.max_x-self.clock, 0, self.clock, self.min_y])

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

    def add_castle(self):
        """Add victory castle."""
        # TODO: Add a safe home to make it to for a victory celebration.
        new_flora = Flora(variety=0,
                          is_home=True,
                          size=self.flora_size*2,
                          pos_x=self.max_x+self.flora_size,
                          pos_y=self.flora_size)
        self.flora += [new_flora]
        # Let's draw from back to front...
        self.flora.sort(key=lambda x: x.pos_y, reverse=False)
        

    def logic(self):
        """Calculate game logic."""

        self.clock += 1
        round_length = 100

        # --- Arrange
        if self.clock == round_length:
            self.add_castle()
        
        if self.clock < round_length: # Add nothing at round end.
            # The field adds things
            if random.randint(0, 10000) > (9950 - int(self.clock/100)):  # New Fish
                self.add_fish()
            if random.randint(0, 10000) > (9900):  # New Flora
                self.add_flora()

        # --- Act
        # Every sprite does it's thing.
        for player in self.players:
            player.logic()
            player.hidden_in = None # Re-check hiding spots every loop.

        for flora in self.flora:
            # Be a place to hide.
            for player in self.players:
                if player.collide(flora):
                    if player.img_color == flora.img_color:
                        player.hidden_in = flora

            # Drift by in the current.
            flora.logic() # Drift to create the current.
            if flora.pos_x < 0 - self.flora_size:
                self.flora.remove(flora) # Past our maximum scrollback, so stop tracking.

        for fauna in self.fauna:
            # Chase!
            for player in self.players:
                if fauna.chasing_player is None:
                    if fauna.can_see(player):
                        fauna.chasing_player = player
                else:
                    if not fauna.can_see(fauna.chasing_player):
                        fauna.chasing_player = None

            # Just keep swimming!
            fauna.logic() # Swim
            if fauna.pos_x < 0 - self.flora_size:
                self.fauna.remove(fauna) # Swim away

        # --- Assert --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
