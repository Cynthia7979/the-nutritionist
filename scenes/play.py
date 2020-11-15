import pygame
from pygame.locals import *
from util import *
from util import json_parse
from logic import nutrition


@logged_class
class Texts(pygame.sprite.Sprite):

    def __init__(self, texts=()):
        super().__init__()
        self.logger.debug('Creating Texts.')

        margin = 20
        max_characters = 20
        line_height = 25

        self.image = pygame.Surface((LEFT_DIALOG_WIDTH, LEFT_DIALOG_HEIGHT/2))
        self.rect = self.image.get_rect(topleft=(0, LEFT_DIALOG_HEIGHT/2))
        self.logger.debug(f'{self.image}')

        to_blit = []
        current_bottom = LEFT_DIALOG_HEIGHT/2
        for text in texts:
            splited_text = [text[i:i+max_characters] for i in range(0, len(text), max_characters)]
            current_bottom -= line_height*len(splited_text)
            for segment in splited_text:
                self.logger.debug(f'{segment}: {current_bottom}')
                t_s, t_r = render_text(segment, 24, WHITE)
                t_r.bottomleft = (10, current_bottom)
                to_blit.append((t_s, t_r))
                current_bottom += line_height
            current_bottom -= line_height*len(splited_text)
            current_bottom -= margin
            if current_bottom < 0: break
        self.image.blits(to_blit)


class Phone(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((PHONE_WIDTH+2, PHONE_HEIGHT+2))
        self.rect = self.image.get_rect(topleft=(PHONE_LEFT, PHONE_TOP))
        pygame.draw.rect(self.image, BLACK, (0, 0, PHONE_WIDTH+2, PHONE_HEIGHT+2))  # Shadow
        pygame.draw.rect(self.image, WHITE, (0, 0, PHONE_WIDTH, PHONE_HEIGHT))  # Screen
        pygame.draw.rect(self.image, BLACK, (0, PHONE_HEIGHT-40, PHONE_WIDTH, 40))  # Bottom menu


class PhoneTopBar(pygame.sprite.Sprite):
    def __init__(self, text):
        super().__init__()

        self.image = pygame.Surface((PHONE_WIDTH, 41))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(topleft=(PHONE_LEFT, PHONE_TOP))

        text_surf, text_rect = render_text(text, size=24)
        text_rect.center = (PHONE_WIDTH/2, 20)
        self.image.blit(text_surf, text_rect)
        pygame.draw.line(self.image, BLACK, (0, 30), (PHONE_WIDTH, 30))

    def update_text(self, text):
        self.image.fill(WHITE)
        text_surf, text_rect = render_text(text)
        self.image.blit(text_surf, text_rect)


class BottomMenuButton(pygame.sprite.Sprite):
    def __init__(self, icon, centerx, centery=PHONE_HEIGHT, **kwargs):
        super().__init__()

        self.image, self.rect = load_image(icon, **kwargs)
        self.rect.center = (centerx, centery)


class AppIcon(pygame.sprite.Sprite):
    def __init__(self, top, left):
        super().__init__()

        self.image = pygame.Surface((101, 101), flags=SRCALPHA)
        self.rect = self.image.get_rect(topleft=(top, left))
        pygame.draw.rect(self.image, BLACK, (0, 0, 100, 100), width=1, border_radius=2)


def start(display_surf, load_from):
    global scene_logger
    scene_logger = get_public_logger('play')
    scene_logger.info('Start gaming!!')

    # Data/logic
    if not load_from:
        player = nutrition.Person()
    else:
        player = nutrition.Person(**json_parse.get_data(load_from))
    messages = ['This is a message', 'This is another message', 'This is a very long message as you start to feel tired',
                'message', 'message', 'message']

    # UI
    left_dialog_rect = pygame.Rect((0, 0,
                                    LEFT_DIALOG_WIDTH, LEFT_DIALOG_HEIGHT))
    general_screen = pygame.sprite.Group()
    general_screen_clickables = pygame.sprite.Group()
    back_icon = BottomMenuButton('resources/back_icon.png', PHONE_LEFT+90, dimensions=(20, 20))
    menu_icon = BottomMenuButton('resources/menu_icon.png', PHONE_LEFT+175, dimensions=(20, 20))
    text_box = Texts(messages)
    text_box.add(general_screen)
    Phone().add(general_screen)
    back_icon.add(general_screen, general_screen_clickables)
    menu_icon.add(general_screen, general_screen_clickables)

    main_screen = pygame.sprite.Group()
    main_screen_clickables = pygame.sprite.Group()
    recipe_app = AppIcon(PHONE_LEFT+25, PHONE_TOP+150)
    health_app = AppIcon(PHONE_LEFT + 145, PHONE_TOP + 150)
    setting_app = AppIcon(PHONE_LEFT + 25, PHONE_TOP + 270)
    recipe_app.add(main_screen, main_screen_clickables)
    health_app.add(main_screen, main_screen_clickables)
    setting_app.add(main_screen, main_screen_clickables)

    active_screen = main_screen

    while True:
        display_surf.fill(BG_PLACEHOLDER)
        pygame.draw.rect(display_surf, get_gray(60), left_dialog_rect)
        pygame.draw.line(display_surf, get_gray(200), (0, HEIGHT/2), (LEFT_DIALOG_WIDTH, HEIGHT/2))
        general_screen.draw(display_surf)
        main_screen.draw(display_surf)

        for event in pygame.event.get():
            if event.type == QUIT:
                scene_logger.info('Quitting game...')
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
