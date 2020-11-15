import pygame
from pygame.locals import *
from util import *


def start(display_surf):
    scene_logger = get_public_logger('name_of_scene')
    scene_logger.info('Starting name_of_scene')
    left_rect = pygame.Rect((0, 0, WIDTH / 2, HEIGHT))
    while True:
        display_surf.fill(BG_PLACEHOLDER)
        pygame.draw.rect(display_surf, BLACK, left_rect)
        for event in pygame.event.get():
            if event.type == QUIT:
                scene_logger.info('Quitting name_of_scene')
                return QUIT, 0
            elif event.type == MOUSEBUTTONUP:  # Click event
                mouse_pos = event.pos
                if some_rect.collidepoint(mouse_pos):  # Clicked on something
                    scene_logger.info('Clicked some_rect')
                    # Do something
                if another_rect.collidepoint(mouse_pos):
                    scene_logger.info('Clicked another_rect')
                    # Do something
        pygame.display.flip()  # Update screen
        CLOCK.tick(FPS)  # Balance loop time
