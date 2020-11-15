# Working Directory: the-nutrtionist/
# All dimensions are 3/2 of the dimension in the prototype
from .logger import *

import pygame
from os import getcwd
GLOBAL_LOGGER.debug(getcwd())

# Pygame-related
WIDTH, HEIGHT = (555, 645)
FPS = 60
CLOCK = pygame.time.Clock()


# State values
TO_PLAY = 'to_play'
TO_MAIN_MENU = 'to_main_menu'
TO_LOAD = 'to_load'
TO_HELL_OBESITY_COURSE = 'to_obesity_course'

END = 'end'
END_HEART_ATTACK = 1
END_VITAMINS = 2
END_OBESITY = 3
END_STARVATION = 4
END_ILLUSION = 5
END_NORMAL = 6


# UI-related
DEFAULT_FONT_FILE = './resources/Linden Hill.otf'
DEFAULT_ITALICS_FILE = './resources/Linden Hill Italic.otf'


# Colors
RED = (255, 0, 0)
GREED = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BG_PLACEHOLDER = (87, 87, 87)

# Dimensions
LEFT_DIALOG_WIDTH, LEFT_DIALOG_HEIGHT = (244.5, HEIGHT)
PHONE_WIDTH, PHONE_HEIGHT = (270, 600)
PHONE_LEFT, PHONE_TOP = (LEFT_DIALOG_WIDTH+20, 20)


# Functions
def get_gray(lightness):
    return tuple([lightness]*3)


def render_text(text: str, size=12, color=BLACK, font_file=DEFAULT_FONT_FILE, *args, **kwargs):
    """:returns font_surf, font_rect"""
    font = pygame.font.Font(font_file, size)
    font_surf = font.render(text, True, color, *args, **kwargs)
    font_rect = font_surf.get_rect()
    return font_surf, font_rect


def load_image(image_path: str, dimensions=()):
    """:returns image_surf, image_rect"""
    image_surf = pygame.image.load(image_path)
    if dimensions:
        image_surf = pygame.transform.scale(image_surf, dimensions)
    image_rect = image_surf.get_rect()
    return image_surf, image_rect
