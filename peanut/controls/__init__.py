import pygame

class ControlSet():
    """A controller mapping."""

    def __init__(self, up=pygame.K_UP, down=pygame.K_DOWN,
                 left=pygame.K_LEFT, right=pygame.K_RIGHT):
        self.up_key = up
        self.down_key = down
        self.left_key = left
        self.right_key = right