# Working Directory: the-nutrtionist/
from .logger import *

import pygame

# Pygame-related
WIDTH, HEIGHT = (555, 645)
FPS = 60
CLOCK = pygame.time.Clock()


# State values
TO_PLAY = 'to_play'
TO_MAIN_MENU = 'to_main_menu'
TO_LOAD = 'to_load'


# UI-related
DEFAULT_FONT_FILE = './resources/Linden Hill.otf'


# Syntax sugar
RED = (255, 0, 0)
GREED = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BG_PLACEHOLDER = (87, 87, 87)


# Functions
def get_gray(lightness):
    return tuple([lightness]*3)


def render_text(text: str, size=12, color=BLACK, font_file=DEFAULT_FONT_FILE, *args, **kwargs):
    """:returns font_surf, font_rect"""
    font = pygame.font.Font(font_file, size)
    font_surf = font.render(text, True, color, *args, **kwargs)
    font_rect = font_surf.get_rect()
    return font_surf, font_rect
