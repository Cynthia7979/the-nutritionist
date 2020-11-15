import pygame
from pygame.locals import *
from util import *
from util import json_parse
from logic import nutrition


RECIPE_ROW_HEIGHT = 70
TOP_BAR_HEIGHT = 40


class Screen(pygame.sprite.Group):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.name = name


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

    def update(self, texts):
        self.__init__(texts)


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


class Button(pygame.sprite.Sprite):
    def __init__(self, left, top, width, height, text):
        super().__init__()

        self.image = pygame.Surface((width+1, height+1))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(topleft=(left, top))
        pygame.draw.rect(self.image, BLACK, (0, 0, width, height), width=1, border_radius=2)
        text_surf, text_rect = render_text(text, 20)
        text_rect.center = (width/2, height/2)
        self.image.blit(text_surf, text_rect)


@logged_class
class RecipeRow(pygame.sprite.Sprite):
    def __init__(self, top, food_data, index):
        super().__init__()
        self.logger.debug(f'Creating RecipeRow for top={top}, index={index}, food={food_data}')
        self.index = index

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


@logged_class
class RecipePage(pygame.sprite.Sprite):
    def __init__(self, food, cart):
        super().__init__()
        self.logger.debug(f'Render Recipe Page for {food}')

        self.food = food
        self.image = pygame.Surface((PHONE_WIDTH, PHONE_HEIGHT), flags=SRCALPHA)
        self.rect = self.image.get_rect(topleft=(PHONE_LEFT, PHONE_TOP))

        title_surf, title_rect = render_text(food['name'], 30)
        title_rect.topleft = (10, TOP_BAR_HEIGHT+5)
        category_surf, category_rect = render_text(food['category'], 20)
        category_rect.topleft = (10, title_rect.bottom+5)
        description_surf, description_rect = render_text(food['description'].replace('\n',''), 20)
        description_rect.topleft = (10, category_rect.bottom+10)

        energy_surf, energy_rect = render_text(f'Energy         {food["Energy"]}kCal', 20, font_file=DEFAULT_ITALICS_FILE)
        energy_rect.topleft = (10, description_rect.bottom+30)
        sodium_surf, sodium_rect = render_text(f'Sodium         {food["Sodium"]}mg', 20, font_file=DEFAULT_ITALICS_FILE)
        sodium_rect.topleft = (10, energy_rect.bottom + 10)
        mineral_surf, mineral_rect = render_text(f'Mineral          {food["Mineral"]}mg', 20, font_file=DEFAULT_ITALICS_FILE)
        mineral_rect.topleft = (10, sodium_rect.bottom + 10)
        vitamin_surf, vitamin_rect = render_text(f'Vitamin          {food["Vitamin"]}mcg', 20, font_file=DEFAULT_ITALICS_FILE)
        vitamin_rect.topleft = (10, mineral_rect.bottom + 10)

        cart_surf, cart_rect = render_text('Cart:', 30)
        cart_rect.topleft = (10, mineral_rect.bottom+50)
        current_top = cart_rect.bottom+20
        for item in cart:
            item_surf, item_rect = render_text(item['name'], 20)
            item_rect.topleft = (60, current_top)
            self.image.blit(item_surf, item_rect)
            current_top = item_rect.bottom+10
        self.logger.debug(title_rect)
        self.logger.debug(category_rect)
        self.image.blits(((title_surf, title_rect), (category_surf, category_rect), (description_surf, description_rect),
                          (energy_surf, energy_rect), (sodium_surf, sodium_rect), (mineral_surf, mineral_rect),
                          (vitamin_surf, vitamin_rect), (cart_surf, cart_rect)))

    def update(self, cart):
        self.__init__(self.food, cart)


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
    messages = []
    cart = []

    # UI
    left_dialog_rect = pygame.Rect((0, 0,
                                    LEFT_DIALOG_WIDTH, LEFT_DIALOG_HEIGHT))
    general_screen = Screen('general')
    general_screen_clickables = pygame.sprite.Group()
    back_icon = BottomMenuButton('resources/back_icon.png', PHONE_LEFT+90, dimensions=(20, 20))
    menu_icon = BottomMenuButton('resources/menu_icon.png', PHONE_LEFT+175, dimensions=(20, 20))
    text_box = Texts(messages)
    text_box.add(general_screen)
    Phone().add(general_screen)
    back_icon.add(general_screen, general_screen_clickables)
    menu_icon.add(general_screen, general_screen_clickables)

    main_screen = Screen('main')
    main_screen_clickables = pygame.sprite.Group()
    recipe_app = Button(PHONE_LEFT + 25, PHONE_TOP + 150, 100, 100, 'Recipe')
    health_app = Button(PHONE_LEFT + 145, PHONE_TOP + 150, 100, 100, 'Health')
    setting_app = Button(PHONE_LEFT + 25, PHONE_TOP + 270, 100, 100, 'Settings')
    recipe_app.add(main_screen, main_screen_clickables)
    health_app.add(main_screen, main_screen_clickables)
    setting_app.add(main_screen, main_screen_clickables)

    recipe_screen = Screen('recipe')
    recipe_screen_clickables = pygame.sprite.Group()
    PhoneTopBar('Choose My Recipe').add(recipe_screen)
    current_top = PHONE_TOP+TOP_BAR_HEIGHT+5
    for i, food in enumerate(food_data):
        food_row = RecipeRow(current_top, food, i)
        food_row.add(recipe_screen, recipe_screen_clickables)
        current_top += RECIPE_ROW_HEIGHT+5
        if current_top + RECIPE_ROW_HEIGHT >= PHONE_TOP + PHONE_HEIGHT: break

    add_to_cart_btn = Button(PHONE_LEFT+40, PHONE_TOP+PHONE_HEIGHT-100, 80, 30, 'Buy')
    confirm_btn = Button(PHONE_LEFT + 160, PHONE_TOP + PHONE_HEIGHT - 100, 80, 30, 'Confirm')

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
                        food_page_screen = Screen('food_page')
                        food_page_screen.food = food_chosen
                        food_page_screen_clickables = pygame.sprite.Group()
                        page_base = RecipePage(food_chosen, cart)
                        page_base.add(food_page_screen)
                        PhoneTopBar(food_chosen['name']).add(food_page_screen)
                        add_to_cart_btn.add(food_page_screen, food_page_screen_clickables)
                        confirm_btn.add(food_page_screen, food_page_screen_clickables)

                        active_screen, last_screen = food_page_screen, recipe_screen
                elif active_screen.name == "food_page":
                    for collision in mouse_sprite.group_collide(food_page_screen_clickables):
                        if collision == add_to_cart_btn:
                            if len(cart) >= 3:
                                messages.append('You decided not to eat more than 3 courses. Too much.')
                                text_box.update(messages)
                            else:
                                cart.append(active_screen.food)
                                food_page_screen.update(cart)
                                scene_logger.info(f'Added {food["name"]} to cart')
                        elif collision == confirm_btn:
                            msgs_to_add, return_value = player.eat(cart)
                            messages += msgs_to_add
                            text_box.update(messages)
                            scene_logger.info(f'Eaten cart {cart}: {return_value}')
                            cart = []
                            food_page_screen.update(cart)
                            if return_value != 0: return return_value
                for collision in mouse_sprite.group_collide(general_screen_clickables):
                    if collision == back_icon:
                        active_screen, last_screen = last_screen, active_screen
                    elif collision == menu_icon:
                        active_screen, last_screen = main_screen, active_screen
        pygame.display.flip()  # Update screen
        CLOCK.tick(FPS)  # Balance loop time


