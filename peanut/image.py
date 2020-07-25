"""Help load images."""

import os

class Images:
    """Static helper class for image stuff."""

    @staticmethod
    def get_path(image_name):
        """Return the full path."""
        my_path = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(my_path, 'img', image_name)