"""Player handler."""

from dataclasses import dataclass, field
from typing import List

import pygame

# from text import TextPrint
from controls import ControlSet
from colors import Colors
from images import Images

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)

# Joystick X / Y Axis
JOY_X = 0
JOY_Y = 1

@dataclass
class PlayerImages():
    """Images of a NutNik"""
    default: str
    size_x: int
    size_y: int
    images: List[pygame.Surface] = None

    def __post_init__(self):
        """Load some images."""
        self.images = []
        for color in [r'red.png', r'orange.png', r'yellow.png',
                      r'green.png', r'blue.png', r'purple.png']:
            color_img = pygame.image.load(Images.get_path(color))
            horse = pygame.image.load(self.default)
            Images.color_image(base_image=horse, color_image=color_img)
            red_horse = pygame.transform.scale(horse, (int(self.size_x), int(self.size_y)))
            self.images += [red_horse]

        pygame.display.set_icon(self.images[0])

    def __getitem__(self, key):
        """Return the image surface.

        This prevent us from having to call player.images.images[0] later.
        """
        return self.images[key]

@dataclass
class Player():
    """A game player.

    >>> Player(start_x=9001).pos_x
    9001

    >>> Player(start_x=9001).pos_y
    100
    """
    controls: List[ControlSet] = field(default_factory=list)
    pos_x: int = 100
    pos_y: int = 100
    size_x: int = 50
    size_y: int = 50
    color: tuple = Colors.RED
    falling: int = 0
    ground_y: int = 0 # override this!
    max_x: int = 100
    start_x: int = 100
    secret_keys: int = 1
    move_delay: int = 2
    move_clock: int = 0
    img_color: int = 0
    color_cooldown: int = 0
    images: PlayerImages = None
    move_amt: int = 4
    drift_amt: int = 1

    def __post_init__(self):
        """Set pos_x to start_x"""
        self.pos_x = self.start_x


    def logic(self):
        """Drift slowly to create the current."""
        self.move_clock = self.move_clock % self.move_delay
        self.move_clock += 1
        if self.move_clock >= self.move_delay:
            if self.pos_x > 0 - self.size_x:
                self.pos_x -= self.drift_amt

        if self.color_cooldown > 0:
            self.color_cooldown -= 1

    def control(self, keys=None, joystick=None):
        """Look for signals accepted by this player, and apply them.

        Return True if the player fired.
        """
        if keys:
            return self._key_control(keys)
        if joystick:
            return self._joy_control(joystick)

    def _joy_control(self, joystick):
        """Apply joystick controls.

        Only pass in the joystick you want to have accepted.
        Return True if the player fired.
        """
        fired = False
        if joystick.get_axis(JOY_Y) >= .8:
            # self.text_print.print(self.screen,
            # "Joystick DOWN: {}".format(joystick.get_axis(JOY_Y)))
            self._down()
        if joystick.get_axis(JOY_Y) <= -.8:
            # self.text_print.print(self.screen,
            # "Joystick UP: {}".format(joystick.get_axis(JOY_Y)))
            self._up()
        if joystick.get_axis(JOY_X) >= .8:
            # self.text_print.print(self.screen,
            # "Joystick RIGHT: {}".format(joystick.get_axis(JOY_X)))
            self._right()
        if joystick.get_axis(JOY_X) <= -.8:
            # self.text_print.print(self.screen,
            # "Joystick LEFT: {}".format(joystick.get_axis(JOY_X)))
            self._left()
        if joystick.get_button(0):
            # self.text_print.print(self.screen, "Player fired!")
            self.change_color()
            fired = True
        return fired

    def collide(self, other):
        """Detect a collision.

        >>> Player(start_x=500,pos_y=500).collide(Player(start_x=500,pos_y=500))
        True

        >>> Player(start_x=500,pos_y=500).collide(Player(start_x=500,pos_y=0))
        False

        >>> Player(start_x=500,pos_y=500).collide(Player(start_x=0,pos_y=500))
        False

        >>> Player(start_x=510,pos_y=500).collide(Player(start_x=500,pos_y=500))
        True

        >>> Player(start_x=510,pos_y=500,lasering=0).collide(Player(start_x=500,pos_y=30))
        False

        >>> Player(start_x=510,pos_y=500,lasering=30).collide(Player(start_x=500,pos_y=30))
        True

        """
        return (
            self.pos_x-self.size_x <= other.pos_x + other.size_x and
            self.pos_y - self.size_y <= other.pos_y and
            self.pos_x+self.size_x >= other.pos_x+other.size_x and
            self.pos_y + self.size_y >= other.pos_y
        )
        # TODO: Add a test that ensures the castle celebration is easy enough to trigger.
        # But first setup a very visible celebration when a player gets home. Bubbles!

    def _up(self):
        """Move up."""
        self.pos_y -= (self.move_amt)

    def _down(self):
        """Interrupt a jump. - New experimental feature...might remove this."""
        self.pos_y += (self.move_amt)

    def _left(self):
        """Move self left."""
        self.pos_x -= self.move_amt

    def _right(self):
        """Move self right."""
        self.pos_x += self.move_amt

    def _key_control(self, keys):
        """Apply keyboard controls - as accepted by this player.
        Return True if the player fired.
        """
        fired = False
        for control_set in self.controls:
            if keys[control_set.up_key]:
                self._up()
            if keys[control_set.down_key]:
                self._down()
            if keys[control_set.left_key]:
                self._left()
            if keys[control_set.right_key]:
                self._right()
        if keys[pygame.K_SPACE]:
            self.change_color()
            fired = True
        return fired

    def change_color(self):
        """Change colors.

        Note that Spacebar is routed to all players, so will chnage all their colors.
        This will not happen when joysticks are connected.
        """
        if self.color_cooldown <= 0:
            self.img_color += 1
            self.img_color = self.img_color % 6
            self.color_cooldown = 10

    def draw(self, screen):
        """Draw the player."""
        img = self.images[self.img_color]

        screen.blit(img, (self.pos_x, self.pos_y))

    def land_on(self, pad):
        """Detect if we landed on a launcher.

        >>> Player().land_on(Player())
        False

        >>> Player(pos_y=90, size_y=10).land_on(Player(pos_y=100, size_y=10))
        True
        """
        bottom_of_self = self.pos_y + self.size_y
        margin = 3
        return (
            self.inline_with(pad)
            and pad.pos_y - margin < bottom_of_self
            and bottom_of_self < pad.pos_y + margin
        )

    def inline_with(self, other):
        """Return true if lined up in a vertical column with player.

        >>> Player().inline_with(Player())
        True

        >>> Player(start_x=20, size_x=10).inline_with(Player(start_x=15, size_x=10))
        True

        >>> Player(start_x=200, size_x=10).inline_with(Player(start_x=15, size_x=10))
        False

        >>> Player(pos_y=100,size_y=10).inline_with(Player(pos_y=90))
        True
        """
        # return (
        #     pad.pos_x + pad.size_x > self.pos_x
        #    and pad.pos_x < self.pos_x + self.size_x
        #)
        return (
            # Left Edge of Other within self
            other.pos_x >= self.pos_x
            and other.pos_x <= self.pos_x + self.size_x
            or
            # Right Edge of Other within self
            other.pos_x + other.size_x >= self.pos_x
            and other.pos_x + other.size_x <= self.pos_x + self.size_x
        )

if __name__ == "__main__":
    import doctest
    doctest.testmod()
