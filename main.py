import sys
import pygame
from pygame.locals import *
from scenes import main_menu
from util import *

DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    GLOBAL_LOGGER.info('Hello hello, starting!')
    # state = (scenes.state_value, *args)
    # Example: (TO_PLAY, './saves/load_file.txt')
    # Can also use pygame vars like (QUIT, 0)
    pygame.init()
    pygame.display.set_caption('The Nutritionist')

    state = main_menu.start(DISPLAY)
    if QUIT in state:
        logger_exit()
        GLOBAL_LOGGER.info('Bye ヾ(·u· )))')
        sys.exit(state[1])
    elif TO_PLAY in state:
        # game.start(state[1])
        pass
    elif TO_LOAD in state:
        # load_screen.start()
        pass


if __name__ == '__main__':
    main()
