import pygame
from pygame.locals import *
from util import *
from util import json_parse
from logic import nutrition


RECIPE_ROW_HEIGHT = 70
TOP_BAR_HEIGHT = 40

class MouseSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect((x, y, 1, 1))

    def group_collide(self, group):
        return pygame.sprite.spritecollide(self, group, False)

@logged_class
class Texts(pygame.sprite.Sprite):

    def __init__(self, texts=()):
        super().__init__()
        self.logger.debug('Creating Texts.')

        margin = 20
        max_characters = 20
        line_height = 25

        self.image = pygame.Surface((LEFT_DIALOG_WIDTH, LEFT_DIALOG_HEIGHT/2))
        self.image.fill(get_gray(60))
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

        self.image = pygame.Surface((PHONE_WIDTH, PHONE_HEIGHT))
        self.rect = self.image.get_rect(topleft=(PHONE_LEFT, PHONE_TOP))
        self.image.fill(get_gray(200))
        pygame.draw.rect(self.image, BLACK, (0, PHONE_HEIGHT-40, PHONE_WIDTH, 40))  # Bottom menu


class PhoneTopBar(pygame.sprite.Sprite):
    def __init__(self, text):
        super().__init__()

        self.image = pygame.Surface((PHONE_WIDTH, TOP_BAR_HEIGHT+1))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(topleft=(PHONE_LEFT, PHONE_TOP))

        text_surf, text_rect = render_text(text, size=24)
        text_rect.center = (PHONE_WIDTH/2, TOP_BAR_HEIGHT/2)
        self.image.blit(text_surf, text_rect)
        pygame.draw.line(self.image, BLACK, (0, TOP_BAR_HEIGHT), (PHONE_WIDTH, 40))

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
    def __init__(self, left, top):
        super().__init__()

        self.image = pygame.Surface((101, 101))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(topleft=(left, top))
        pygame.draw.rect(self.image, BLACK, (0, 0, 100, 100), width=1, border_radius=2)


class RecipeRow(pygame.sprite.Sprite):
    def __init__(self, top, food_data, index):
        super().__init__()

        self.image = pygame.Surface((PHONE_WIDTH, RECIPE_ROW_HEIGHT))
        self.rect = self.image.get_rect(topleft=(PHONE_LEFT, top))
        self.image.fill(WHITE)
        pygame.draw.line(self.image, BLACK, (0, RECIPE_ROW_HEIGHT-1), (PHONE_WIDTH, RECIPE_ROW_HEIGHT-1))  # Bottom line
        pygame.draw.line(self.image, BLACK, (0, 1), (PHONE_WIDTH, 1))  # Top line
        name_surf, name_rect = render_text(food_data['name'], 20)
        name_rect.topleft = (10, 10)
        category_surf, category_rect = render_text(food_data['category'])
        category_rect.topleft = (10, 40)
        self.image.blits(((name_surf, name_rect), (category_surf, category_rect)))

        self.index = index


class RecipePage(pygame.sprite.Sprite):
    def __init__(self, food):
        super().__init__()

        self.image = pygame.Surface((PHONE_WIDTH, PHONE_HEIGHT), flags=SRCALPHA)
        self.rect = self.image.get_rect(topleft=(PHONE_LEFT, PHONE_TOP))

        title_surf, title_rect = render_text(food['name'], 30)
        title_rect.topleft = (PHONE_LEFT+20, TOP_BAR_HEIGHT+10)
        category_surf, category_rect = render_text(food['category'], 20)
        category_rect.topleft = (PHONE_LEFT+20, title_rect.bottom+10)
        self.image.blits(((title_surf, title_rect), (category_surf, category_rect)))


def start(display_surf, load_from):
    global scene_logger
    scene_logger = get_public_logger('play')
    scene_logger.info('Start gaming!!')

    # Data/logic
    if not load_from:
        player = nutrition.Person()
    else:
        player = nutrition.Person(**json_parse.get_data(load_from))
    food_data = json_parse.get_data('food_data.json')
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

    recipe_screen = pygame.sprite.Group()
    recipe_screen_clickables = pygame.sprite.Group()
    PhoneTopBar('Choose My Recipe').add(recipe_screen)
    current_top = PHONE_TOP+TOP_BAR_HEIGHT+5
    for i, food in enumerate(food_data):
        food_row = RecipeRow(current_top, food, i)
        food_row.add(recipe_screen, recipe_screen_clickables)
        current_top += RECIPE_ROW_HEIGHT+5
        if current_top + RECIPE_ROW_HEIGHT >= PHONE_TOP + PHONE_HEIGHT: break

    active_screen = main_screen
    last_screen = main_screen

    while True:
        display_surf.fill(BG_PLACEHOLDER)
        pygame.draw.rect(display_surf, get_gray(60), left_dialog_rect)
        pygame.draw.line(display_surf, get_gray(200), (0, HEIGHT/2-1), (LEFT_DIALOG_WIDTH, HEIGHT/2-1))
        general_screen.draw(display_surf)
        active_screen.draw(display_surf)

        for event in pygame.event.get():
            if event.type == QUIT:
                scene_logger.info('Quitting game...')
                return QUIT, 0
            elif event.type == MOUSEBUTTONUP:  # Click event
                mouse_pos = event.pos
                mouse_sprite = MouseSprite(*mouse_pos)
                if active_screen == main_screen:
                    for collision in mouse_sprite.group_collide(main_screen_clickables):
                        if collision == recipe_app:
                            active_screen, last_screen = recipe_screen, active_screen
                elif active_screen == recipe_screen:
                    collisions = mouse_sprite.group_collide(recipe_screen_clickables)
                    if collisions:
                        collision = collisions[0]  # Should only be one
                        food_chosen = food_data[collision.index]
                        food_page_screen = pygame.sprite.Group()
                        page_base = RecipePage(food_chosen)
                        page_base.add(food_page_screen)
                        active_screen = food_page_screen
                for collision in mouse_sprite.group_collide(general_screen_clickables):
                    if collision == back_icon:
                        active_screen, last_screen = last_screen, active_screen
                    elif collision == menu_icon:
                        active_screen, last_screen = main_screen, active_screen
        pygame.display.flip()  # Update screen
        CLOCK.tick(FPS)  # Balance loop time


