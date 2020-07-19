#!/usr/bin/env python3
"""Peanut Butter Panic!

Lovingly updated for four players.

Peanut Butter Panic! was easily one of my favorite games for the good old Commordore 64.
It was a part of my inspiration to become a programmer.
This four player tribute is presented along with full open source code in the hopes of inspiring at least a few smiles and maybe a few careers.

TODO:
- [ ] Make sandwiches!
- [ ] Track player scores.
- [ ] Eat sandwiches to get fat.
- [ ] Launch eachother for the higher stars!


# Per https://www.mobygames.com/game/peanut-butter-panic

Commodore 64 Credits (10 people)

CTW Software Group was a US software development group, part of Children's Computer Workshop, Inc., 
mainly involved with developing educational games and software based on the Sesame Street license.

CTW Software Group Development Team for Peanut Butter Panic:
Harold Byrd, Dick Codor, Sandy Damashek, Bernie De Koven, Lisa Feder, Laura Kurland, Dan Oehlsen, Mary Schenck Balcer, Alan Shapiro, Debra Weinberger
"""

import random
import pygame
from player import Player
from text import TextPrint
from controls import ControlSet

# Set these to the two buttons you want to use for 'exit'. Count up starting from 0
SELECT = 3
START = 4

class Colors():
    """Define some colors."""
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    PURPLE = (128, 0, 128)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 128, 0)
    GROUND = (0, 128, 0)

# GAME FIELD
STAR_TOP_LAYER = 40

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

textPrint = TextPrint()

class SandwichBar():
    """A place to make sandwiches."""
    sandwich_count = 0
    sandwich_size = 40

    def __init__(self, pos_x, pos_y, size_x, size_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y

    def draw(self, screen):
        """Draw the sandwich bar, with sandwiches on it."""
        pygame.draw.rect(screen, Colors.BLUE,
                         [self.pos_x, self.pos_y, self.size_x, self.size_y])
        for i in range(0, self.sandwich_count):
            pygame.draw.rect(screen, Colors.GREEN,
                         [self.pos_x + 10, self.pos_y + 10 + (self.sandwich_size * i), self.size_x - 10, self.pos_y + 10 + ((self.sandwich_size + 1) * i)])


class PlayField():
    """Track the play field."""
    MIN_X = 0
    MAX_X = 1200
    MIN_Y = 900
    GROUND_Y = MIN_Y - 100
    MAX_Y = 0

    def __init__(self):
        """New play field."""
        self.done = False
        self.sprites = []
        self.players = []
        self.stars = []
        self.add_players()
        self.screen = None
        self.sandwich_bar = SandwichBar(pos_x = self.MAX_X / 2, size_x = 60, 
            pos_y = self.GROUND_Y - 20, size_y = self.MAX_Y - self.GROUND_Y + 20)

        # Initialize the joysticks
        pygame.init()
        pygame.joystick.init()
        size = [self.MAX_X, self.MIN_Y]
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Peanut Butter Panic")
        pygame.mouse.set_visible(False)

    def add_star(self):
        """Add a star."""
        self.stars += [Star(self.MAX_X)]

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
            player.pos_y = self.GROUND_Y
            player.ground_y = self.GROUND_Y

    def draw(self):
        """Re-Draw the play field."""
        self.screen.fill(Colors.BLACK)  # background
        pygame.draw.rect(self.screen, Colors.GROUND,
                         [self.MIN_X, self.GROUND_Y, self.MAX_X, self.MIN_Y])

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
        self.sprites = self.players + self.stars # Changes because stars get removed.

        # --- Arrange
        # The field adds things
        if random.randint(0, 1000) > 990:  # New star frequency
            self.add_star()

        # --- Act
        # Every sprite does it's thing.
        for sprite in self.sprites:
            sprite.logic()

        # The field taketh away
        for star in self.stars:
            if star.pos_x < 0 or star.pos_x > self.MAX_X:
                self.stars.remove(star) # It is off screen. Stop tracking it.
            for player in self.players:
                if player.collide(star):
                    self.stars.remove(star)
                    self.sandwich_bar.sandwich_count += 1

        # --- Assert --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True



class Star():
    """Track the stars."""
    pos_x = 0
    pos_y = 0
    dir = 1
    size_x = 5
    size_y = 5
    STAR_TOP_LAYER = 20
    STAR_MID_LAYER = 150
    STAR_LOW_LAYER = 200
    LAYERS = [STAR_TOP_LAYER, STAR_MID_LAYER,
              STAR_MID_LAYER, STAR_LOW_LAYER, STAR_LOW_LAYER]
    STAR_COLORS = [Colors.RED, Colors.YELLOW, Colors.ORANGE, Colors.WHITE, Colors.BLUE]

    def __init__(self, max_x):
        """New random star."""
        self.pos_y = random.choice(self.LAYERS) # Randomly pick a layer
        self.pox_x = 40 + random.randint(10, 100)
        self.dir = random.choice([-1, 1]) # Move left or right.
        self.color = random.choice(self.STAR_COLORS)
        if self.dir == 1:
            self.pox_x = 1
        else:
            self.pos_x = max_x - 1

    def logic(self):
        """Star movement."""
        self.pos_x += self.dir

    def draw(self, screen):
        """Draw this star."""
        pygame.draw.rect(screen, self.color,
                         [self.pos_x, self.pos_y, self.size_x, self.size_y])


# -------- Main Program Loop -----------
field = PlayField()

while not field.done:
    field.controls()
    field.logic()
    field.draw()
    # Limit to 60 frames per second
    clock.tick(60)

# Close everything down
pygame.quit()
