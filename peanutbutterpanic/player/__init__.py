"""Player handler."""

import pygame

from text import TextPrint
from controls import ControlSet

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

class Player():
    """A game player."""
    controls = [ControlSet()]
    pos_x = 100
    pos_y = 100
    size_x = 50
    size_y = 50
    move_amt = 5
    color = RED
    jumping = 0
    falling = 0
    jump_max = 300 # this will change during play
    ground_y = 0 # override this!

    def __init__(self, color, controls):
        """Make a new player.

        Assign unique color and controls."""
        self.controls = controls
        self.color = color
        self.text_print = TextPrint()
        self.debug = ""

    def logic(self):
        """Do player game logic."""

        # Can't jump forever.
        if self.jumping and self.pos_y < self.ground_y - self.jump_max:
            self.jumping = 0
            self.falling = 1

        if self.falling and self.pos_y > self.ground_y:
            self.falling = 0

        if self.jumping:
            self.pos_y -= self.move_amt

        if self.falling:
            self.jumping = 0 # Supports voluntary fall.
            self.pos_y += self.move_amt


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
            self.debug += "Joystick down"
            # self.text_print.print(self.screen, "Joystick DOWN: {}".format(joystick.get_axis(JOY_Y)))
            self._down()
        if joystick.get_axis(JOY_Y) <= -.8:
            # self.text_print.print(self.screen, "Joystick UP: {}".format(joystick.get_axis(JOY_Y)))
            self._up()
        if joystick.get_axis(JOY_X) >= .8:
            # self.text_print.print(self.screen, "Joystick RIGHT: {}".format(joystick.get_axis(JOY_X)))
            self._right()
        if joystick.get_axis(JOY_X) <= -.8:
            # self.text_print.print(self.screen, "Joystick LEFT: {}".format(joystick.get_axis(JOY_X)))
            self._left()
        if joystick.get_button(0):
            # self.text_print.print(self.screen, "Player fired!")
            fired = True
        return fired

    def collide(self, other):
        """Detect a collision."""
        return (
            self.pos_x-self.size_x < other.pos_x + other.size_x and
            self.pos_y - self.size_y < other.pos_y and
            self.pos_x+self.size_x > other.pos_x+other.size_x and
            self.pos_y + self.size_y > other.pos_y
        )

    def _up(self):
        """Start a jump."""
        if not self.falling:
            self.jumping = 1

    def _down(self):
        """Interrupt a jump. - New experimental feature...might remove this."""
        self.falling = 1

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
            self.debug += "BUTTON PRESS!"
            fired = True
        return fired

    def draw(self, screen):
        """Draw the player."""
        pygame.draw.rect(screen, WHITE,
                         [self.pos_x, self.pos_y, self.size_x, self.size_y])
        pygame.draw.rect(screen, self.color,
                         [self.pos_x + 10, self.pos_y + 10, self.size_x - 10, self.size_y - 10])

        self.text_print.indent()
        self.text_print.print(screen, "Player message: {}".format(self.debug))