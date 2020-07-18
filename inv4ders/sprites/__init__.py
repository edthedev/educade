#!/usr/bin/env python3
"""Four Player invaders clone."""

import pygame

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

class TextPrint(object):
    """
    This is a simple class that will help us print to the screen
    It has nothing to do with the joysticks, just outputting the
    information.
    """
    def __init__(self):
        """ Constructor """
        self.reset()
        self.x_pos = 10
        self.y_pos = 10
        self.font = pygame.font.Font(None, 20)

    def print(self, my_screen, text_string):
        """ Draw text onto the screen. """
        text_bitmap = self.font.render(text_string, True, BLACK)
        my_screen.blit(text_bitmap, [self.x_pos, self.y_pos])
        self.y_pos += self.line_height

    def reset(self):
        """ Reset text to the top of the screen. """
        self.x_pos = 10
        self.y_pos = 10
        self.line_height = 15

    def indent(self):
        """ Indent the next line of text """
        self.x_pos += 10

    def unindent(self):
        """ Unindent the next line of text """
        self.x_pos -= 10


class ControlSet():
    """A controller mapping."""

    def __init__(self, up=pygame.K_UP, down=pygame.K_DOWN,
                 left=pygame.K_LEFT, right=pygame.K_RIGHT):
        self.up_key = up
        self.down_key = down
        self.left_key = left
        self.right_key = right


class Player():
    """A game player."""
    controls = [ControlSet()]
    pos_x = 100
    pos_y = 100
    size_x = 50
    size_y = 50
    move_amt = 5
    color = RED

    def __init__(self, screen, color, controls):
        """Make a new player.

        Assign unique color and controls."""
        self.controls = controls
        self.color = color
        self.screen = screen
        self.text_print = TextPrint()

    def control(self, keys=None, joystick=None):
        """Look for signals accepted by this player, and apply them."""
        if keys:
            self._key_control(keys)
        if joystick:
            self._joy_control(joystick)

    def _joy_control(self, joystick):
        """Apply joystick controls.

        Only pass in the joystick you want to have accepted.
        """
        if joystick.get_axis(JOY_Y) >= .8:
            self.text_print.print(self.screen, "Joystick DOWN: {}".format(joystick.get_axis(JOY_Y)))
            self._down()
        if joystick.get_axis(JOY_Y) <= -.8:
            self.text_print.print(self.screen, "Joystick UP: {}".format(joystick.get_axis(JOY_Y)))
            self._up()
        if joystick.get_axis(JOY_X) >= .8:
            self.text_print.print(self.screen, "Joystick RIGHT: {}".format(joystick.get_axis(JOY_X)))
            self._right()
        if joystick.get_axis(JOY_X) <= -.8:
            self.text_print.print(self.screen, "Joystick LEFT: {}".format(joystick.get_axis(JOY_X)))
            self._left()

    def _up(self):
        """Move self up."""
        self.pos_y -= self.move_amt

    def _down(self):
        """Move self down."""
        self.pos_y += self.move_amt

    def _left(self):
        """Move self left."""
        self.pos_x -= self.move_amt

    def _right(self):
        """Move self right."""
        self.pos_x += self.move_amt

    def _key_control(self, keys):
        """Apply keyboard controls - as accepted by this player."""
        for control_set in self.controls:
            if keys[control_set.up_key]:
                self._up()
            if keys[control_set.down_key]:
                self._down()
            if keys[control_set.left_key]:
                self._left()
            if keys[control_set.right_key]:
                self._right()

    def draw(self):
        """Draw the player."""
        pygame.draw.rect(self.screen, WHITE,
                         [self.pos_x, self.pos_y, self.size_x, self.size_y])
        pygame.draw.rect(self.screen, self.color,
                         [self.pos_x + 10, self.pos_y + 10, self.size_x - 10, self.size_y - 10])

