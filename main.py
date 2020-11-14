import sys
from pygame.locals import *
from scenes import main_menu
from scenes import *

DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    # state = (scene_specific_global_var, *args)
    # Example: (TO_PLAY, './saves/load_file.txt')
    # Can also use pygame vars like (QUIT, 0)
    pygame.init()
    pygame.display.set_caption('The Nutritionist')

    state = main_menu.start(DISPLAY)
    if QUIT in state:
        sys.exit(state[1])
    elif TO_PLAY in state:
        # game.start()
        pass


if __name__ == '__main__':
    main()
