import sys
from pygame.locals import *
from scenes import main_menu
from another_dir import test
from scenes import *

DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    # state = (scenes.state_value, *args)
    # Example: (TO_PLAY, './saves/load_file.txt')
    # Can also use pygame vars like (QUIT, 0)
    pygame.init()
    pygame.display.set_caption('The Nutritionist')

    test.start()
    state = main_menu.start(DISPLAY)
    if QUIT in state:
        GLOBAL_LOGGER.info('Bye ヾ(·u· )))')
        sys.exit(state[1])
    elif TO_PLAY in state:
        # game.start()
        pass


if __name__ == '__main__':
    main()
