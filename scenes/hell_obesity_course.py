import pygame
from time import sleep
from pygame.locals import *
from util import *


def start(display_surf):
    scene_logger = get_public_logger('hell_obesity_course')
    scene_logger.info('Starting hell_obesity_course')

    display_surf.fill(BLACK)
    dialog_0_surf, dialog_0_rect = load_image('./resources/ghost_dialog_0.png', (300, 82))
    dialog_0_rect.midtop = (WIDTH/2, 480)
    display_surf.blit(dialog_0_surf, dialog_0_rect)
    pygame.display.flip()
    sleep(2)

    dialog_1_surf, dialog_1_rect = load_image('./resources/ghost_dialog_1.png', (300, 82))
    dialog_1_rect.midtop = (WIDTH/2, 480)
    classroom_surf, classroom_rect = load_image('./resources/ghost_classroom.png')
    classroom_rect.midbottom = (WIDTH/2, HEIGHT+20)
    background_surf, background_rect = load_image('./resources/com_fire_cave.png', (1167, 656))
    background_rect.center = (WIDTH/2, HEIGHT/2)

    while True:
        display_surf.blit(background_surf, background_rect)
        display_surf.blit(classroom_surf, classroom_rect)
        display_surf.blit(dialog_1_surf, dialog_1_rect)

        for event in pygame.event.get():
            if event.type == QUIT:
                scene_logger.info('Quitting hell_obesity_course')
                return QUIT, 0
        pygame.display.flip()  # Update screen
        CLOCK.tick(FPS)  # Balance loop time
