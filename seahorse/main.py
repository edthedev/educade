#!/usr/bin/env python3
"""Undersea Hide and Seek"""

import argparse

import pygame

# from text import TextPrint
from field import PlayField

def main():
    """The main game loop."""

    parser = argparse.ArgumentParser(description='Peanut Butter Panic')
    parser.add_argument('-s', '--small', action='store_true')
    parser.add_argument('-d', '--debug', action='store_true')
    parser.add_argument('-f', '--five_to_four', action='store_true')
    args = parser.parse_args()

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    play_field = None
    if args.small:
        play_field = PlayField(max_x=800, min_y=600, debug=args.debug)
    else:
        play_field = PlayField(debug=args.debug)

    if args.five_to_four:
        play_field = PlayField(max_x=1280, min_y=1024, debug=args.debug)

    while not play_field.done:
        play_field.controls()
        play_field.logic()
        play_field.draw()
        # Limit to 60 frames per second
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
