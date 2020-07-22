#!/usr/bin/env python3
"""Peanut Butter Panic!

Lovingly updated for four players.

Peanut Butter Panic! was easily one of my favorite games for the good old Commordore 64.
It was a part of my inspiration to become a programmer.
This four player tribute is presented along with full open source code in the hopes of inspiring at least a few smiles and maybe a few careers.

TODO:
- [x] Make sandwiches!
- [x] Press down to eat sandwiches to get fat.
- [ ] Fix collision detection for fat players.
- [ ] Fix off-by-one in sandwich display.
- [ ] Launch eachother for the higher stars!
- [ ] Snarfs!
- [ ] Show total sandwiches eaten as score.
- [ ] Show elapsed time.
- [ ] Display welcome message at start.

# Per https://www.mobygames.com/game/peanut-butter-panic

Commodore 64 Credits (10 people)

CTW Software Group was a US software development group, part of Children's Computer Workshop, Inc., 
mainly involved with developing educational games and software based on the Sesame Street license.

CTW Software Group Development Team for Peanut Butter Panic:
Harold Byrd, Dick Codor, Sandy Damashek, Bernie De Koven, Lisa Feder, Laura Kurland, Dan Oehlsen, Mary Schenck Balcer, Alan Shapiro, Debra Weinberger
"""

import pygame
# from text import TextPrint
from controls import ControlSet
from sandwich import SandwichBar
from colors import Colors
from launcher import Launcher
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
    args = parser.parse_args()

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    field = None
    if args.small:
        field = PlayField(max_x=600, min_y=400)
    else:
        field = PlayField()

    while not field.done:
        field.controls()
        field.logic()
        field.draw()
        # Limit to 60 frames per second
        clock.tick(60)

    pygame.quit()