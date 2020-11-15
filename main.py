import sys
import pygame
from pygame.locals import *
from scenes import main_menu, play
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
        GLOBAL_LOGGER.info('Bye ヾ(·u· )))')
        logger_exit()
        sys.exit(state[1])
    elif TO_PLAY in state:
        state = play.start(DISPLAY, state[1])
        if END in state:
            if END_NORMAL in state:
                # end_normal.play()
                pass
            elif END_HEART_ATTACK in state:
                pass
            elif END_OBESITY in state:
                pass
            elif END_STARVATION in state:
                pass
            elif END_ILLUSION in state:
                pass
    elif TO_LOAD in state:
        # load_screen.start()
        pass


if __name__ == '__main__':
    main()
