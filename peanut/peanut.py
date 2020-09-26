#!/usr/bin/env python3
"""Sandwich Panic

A clone of Peanut Butter Panic, lovingly updated for four players.

Peanut Butter Panic! was easily one of my favorite games for the good old Commordore 64.
It was a part of my inspiration to become a programmer.
This four player tribute is presented along with
full open source code in the hopes of inspiring at least a few smiles and maybe a few careers.
"""

import pygame
# from text import TextPrint
from star import Star
from field import PlayField


WELCOME_MESSAGE = """
* * * * * * * * * * * * * 
    Welcome Nutniks!
* * * * * * * * * * * * * 

Your gaol is to make 
as many sandwiches as 
you can by catching
stars to power your
sandwich machine.

"""

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Peanut Butter Panic')
    parser.add_argument('-s', '--small', action='store_true')
    parser.add_argument('-d', '--debug', action='store_true')
    args = parser.parse_args()

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    field = None
    if args.small:
        field = PlayField(max_x=800, min_y=600,debug=args.debug)
    else:
        field = PlayField(debug=args.debug)

    while not field.done:
        field.controls()
        field.logic()
        field.draw()
        # Limit to 60 frames per second
        clock.tick(60)

    pygame.quit()
