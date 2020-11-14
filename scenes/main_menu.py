from pygame.locals import *
from . import *


def start(display_surf):
    while True:  # Game loop
        display_surf.fill(BLACK)
        for event in pygame.event.get():  # Event loop
            if event == QUIT:
                return QUIT, 0
        CLOCK.tick(FPS)

