import pygame
from pygame.locals import *
from util import *


class PhoneUI(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


def start(display_surf, load_from):
    scene_logger = get_public_logger('name_of_scene')
    scene_logger.info('Starting name_of_scene')

    left_dialog_rect = pygame.Rect((0, 0,
                                    LEFT_DIALOG_WIDTH, LEFT_DIALOG_HEIGHT))
    text_box_rect = pygame.Rect((0, LEFT_DIALOG_HEIGHT/2,
                                 LEFT_DIALOG_WIDTH, LEFT_DIALOG_HEIGHT/2))
    phone_surf = pygame.Surface((PHONE_WIDTH, PHONE_HEIGHT))
    phone_rect = phone_surf.get_rect(topleft=(LEFT_DIALOG_WIDTH+20, 20))

    while True:
        display_surf.fill(BG_PLACEHOLDER)
        pygame.draw.rect(display_surf, get_gray(60), left_dialog_rect)
        pygame.draw.rect(display_surf, get_gray(60), text_box_rect)
        pygame.draw.line(display_surf, get_gray(200), (0, HEIGHT/2), (LEFT_DIALOG_WIDTH, HEIGHT/2))
        pygame.draw.rect(display_surf, WHITE, phone_rect)

        for event in pygame.event.get():
            if event.type == QUIT:
                scene_logger.info('Quitting name_of_scene')
                return QUIT, 0
            elif event.type == MOUSEBUTTONUP:  # Click event
                mouse_pos = event.pos
                # if some_rect.collidepoint(mouse_pos):  # Clicked on something
                #     scene_logger.info('Clicked some_rect')
                #     # Do something
                # if another_rect.collidepoint(mouse_pos):
                #     scene_logger.info('Clicked another_rect')
                #     # Do something
        pygame.display.flip()  # Update screen
        CLOCK.tick(FPS)  # Balance loop time
