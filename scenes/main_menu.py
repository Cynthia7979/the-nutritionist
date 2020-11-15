import pygame
from pygame.locals import *
from util import *


def start(display_surf):
    main_menu_logger = get_public_logger('main_menu')
    main_menu_logger.info('Starting main_menu')

    # Titles
    title_surf_1, title_rect_1 = render_text('The', 36, color=WHITE)
    title_surf_2, title_rect_2 = render_text('Nutritionist', 64, color=WHITE)
    title_rect_1.center = (WIDTH / 2, 80)
    title_rect_2.center = (WIDTH / 2, 130)
    # Buttons
    play_btn, play_rect = render_text('Play', 36, color=WHITE)
    load_btn, load_rect = render_text('Load', 36, color=WHITE)
    quit_btn, quit_rect = render_text('Quit', 36, color=WHITE)
    play_rect.center = (WIDTH / 2, 300)
    load_rect.center = (WIDTH / 2, 350)
    quit_rect.center = (WIDTH / 2, 400)
    while True:  # Game loop
        display_surf.fill(BG_PLACEHOLDER)

        # Draw titles
        display_surf.blits(blit_sequence=(
            (title_surf_1, title_rect_1),
            (title_surf_2, title_rect_2)
        ))

        # Draw buttons
        display_surf.blits(blit_sequence=(
            (play_btn, play_rect),
            (load_btn, load_rect),
            (quit_btn, quit_rect)
        ))

        for event in pygame.event.get():  # Event loop
            if event.type == QUIT:
                main_menu_logger.info('Quitting main_menu')
                return QUIT, 0
            if event.type == MOUSEBUTTONUP:
                mouse_pos = event.pos
                if play_rect.collidepoint(*mouse_pos):
                    main_menu_logger.info('Clicked Play button')
                    return TO_PLAY, 0
                elif load_rect.collidepoint(*mouse_pos):
                    main_menu_logger.info('Clicked Load button')
                    return TO_LOAD, 0
                elif quit_rect.collidepoint(*mouse_pos):
                    main_menu_logger.info('Quitting main_menu')
                    return QUIT, 0

        pygame.display.flip()
        CLOCK.tick(FPS)

