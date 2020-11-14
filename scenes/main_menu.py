import pygame
from pygame.locals import *
from . import *


def start(display_surf):
    logger = get_public_logger('main_menu')
    while True:  # Game loop
        display_surf.fill(BG_PLACEHOLDER)
        title_surf_1, title_rect_1 = render_text('The', 36, color=WHITE)
        title_surf_2, title_rect_2 = render_text('Nutritionist', 64, color=WHITE)
        title_rect_1.center = (WIDTH/2, 100)
        title_rect_2.center = (WIDTH/2, 150)
        display_surf.blit(title_surf_1, title_rect_1)
        display_surf.blit(title_surf_2, title_rect_2)

        for event in pygame.event.get():  # Event loop
            if event.type == QUIT:
                logger.info('Quitting main_menu')
                return QUIT, 0

        pygame.display.flip()
        CLOCK.tick(FPS)

