import pygame
from time import sleep
from pygame.locals import *
from util import *


def start(display_surf):
    scene_logger = get_public_logger('hell_obesity_course')
    scene_logger.info('Starting hell_obesity_course')

    dialog_0_surf, dialog_0_rect = load_image('./resources/ghost_dialog_0.png')
    dialog_0_rect.midtop = (WIDTH/2, 50)
    display_surf.blit(dialog_0_surf, dialog_0_rect)
    pygame.display.flip()
    sleep(2)
    

    while True:
        display_surf.fill(BG_PLACEHOLDER)
        for event in pygame.event.get():
            if event.type == QUIT:
                scene_logger.info('Quitting hell_obesity_course')
                return QUIT, 0
        pygame.display.flip()  # Update screen
        CLOCK.tick(FPS)  # Balance loop time
