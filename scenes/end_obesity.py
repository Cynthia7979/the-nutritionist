import pygame
from pygame.locals import *
from time import sleep
from util import *
        
        
def start(display_surf):
    scene_logger = get_public_logger('end_obesity')
    scene_logger.info('Starting end_obesity')

    frames = 0
    death_speed = 2
    total_clicks = 0
    player_speed = 0

    death_sprites = [t[0] for t in (load_image('./resources/death_0.png', ),
                                    load_image('./resources/death_1.png', ),
                                    load_image('./resources/death_2.png', ),
                                    load_image('./resources/death_3.png', ),
                                    load_image('./resources/death_4.png', ))]
    death_image = death_sprites[0]
    death_rect = death_image.get_rect(midbottom=(100, HEIGHT / 2))
    # player_image, player_rect = load_image('./resources/death.png')
    player_image = pygame.Surface((35, 35))
    player_image.fill(WHITE)
    player_rect = player_image.get_rect(midbottom=(450, HEIGHT / 2 - 20))

    click_text_surf, click_text_rect = render_text('Click!!!', 54, WHITE)
    click_text_rect.midtop = (WIDTH/2, 30)

    # Texts
    display_surf.fill(BLACK)
    text_surf, text_rect = load_image('./resources/obesity_texts.png')
    text_rect.midleft = (0, HEIGHT/2)
    display_surf.blit(text_surf, text_rect)
    pygame.display.flip()
    sleep(5)

    # Talking...
    display_surf.fill(BG_PLACEHOLDER)
    pygame.draw.rect(display_surf, get_gray(20), (0, HEIGHT / 2, WIDTH, HEIGHT / 2))  # Ground
    display_surf.blit(death_image, death_rect)
    display_surf.blit(player_image, player_rect)

    dialog_0_surf, dialog_0_rect = load_image('./resources/death_dialog_0.png', (300, 82))
    dialog_0_rect.bottomleft = (death_rect.left, death_rect.top-20)
    display_surf.blit(dialog_0_surf, dialog_0_rect)
    pygame.display.flip()
    sleep(2)

    dialog_0_surf, dialog_0_rect = load_image('./resources/death_dialog_1.png', (300, 82))
    dialog_0_rect.bottomleft = (death_rect.left, death_rect.top-20)
    display_surf.blit(dialog_0_surf, dialog_0_rect)
    pygame.display.flip()
    sleep(2)

    while True:
        if frames % 3 == 0:  # Change every 3 frames
            death_image = death_sprites[(frames // 3) % 5]
        if frames//60 != 0:  # Prevent division by 0
            player_speed = total_clicks / (frames//60)  # Count clicks per second
        if frames % 120 == 0:  # Increase Death's speed every 2 seconds
            death_speed += 1
        if frames % 10 == 0:
            player_rect.left += (player_speed - death_speed)
        display_surf.fill(BG_PLACEHOLDER)
        pygame.draw.rect(display_surf, get_gray(20), (0, HEIGHT/2, WIDTH, HEIGHT/2))  # Ground
        display_surf.blit(death_image, death_rect)
        display_surf.blit(player_image, player_rect)
        display_surf.blit(click_text_surf, click_text_rect)
        for event in pygame.event.get():
            if event.type == QUIT:
                # scene_logger.info('Quitting name_of_scene')
                # return QUIT, 0
                pass
            elif event.type == MOUSEBUTTONUP:  # Click event
                total_clicks += 1
        if player_rect.colliderect(death_rect):
            return TO_HELL_OBESITY_COURSE
        frames += 1
        pygame.display.flip()  # Update screen
        CLOCK.tick(FPS)  # Balance loop time
