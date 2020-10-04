"""Help load images."""

import os

import pygame

class Images:
    """Static helper class for image stuff."""
    color_files = [r'red.png', r'orange.png', r'yellow.png', 
              r'green.png', r'blue.png', r'purple.png']

    @staticmethod
    def get_path(image_name):
        """Return the full path."""
        my_path = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(my_path, 'img', image_name)
    
    @staticmethod
    def color_image(base_image, color_image):
        """Color an image."""
        base_image.blit(color_image, (0, 0), special_flags=pygame.BLEND_ADD)
        return base_image
