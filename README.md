# the-nutritionist
Creatica 2020 Entry

# Useful Links
* [Board of Things](https://docs.qq.com/slide/DZFFmRlhjV0JnTUZY)
* [Creatica](https://www.creatica.io)
* [Creatica DevPost](https://creatica.devpost.com)
* [Pygame Documentation](https://www.pygame.org/docs/index.html)

# Technical Specifications (?)
If using Anaconda, run `conda create --name <name_of_env>` under this directory
to install packaged needed.

Under an existing environment, use `conda update --file env.yml`

To update `env.yml`, run `conda env export --file=env.yml`

For `pip`, run `pip install -r /path/to/requirements.txt`

To update `requirements.txt` in virtualenv: `pip freeze > requirements.txt`

If there's no virtualenv, use `pipreqs` as described 
[here](https://stackoverflow.com/questions/29938554/how-to-create-a-requirements-txt)
instead.

-----

Packages used:
* Python: `3.7`
* Pygame: `2.0.0`


# Resources Used
* [Linden Hill](https://www.theleagueofmoveabletype.com/linden-hill) from The League of Moveable Type
* [Recipes](https://www.choosemyplate.gov/myplatekitchen/recipes) from ChooseMyPlate: U.S. DEPARTMENT OF AGRICULTURE
* [Sprites](https://opengameart.org) from Open Game Art, raw or modified.
    * [Death (Assassin)](https://opengameart.org/content/assassin)
    * [Professor Ghost](https://opengameart.org/content/stendhal-ghost)
    * [Fire Cave BG](https://opengameart.org/content/fire-rpg-background)

# Scene Template
```python
import pygame
from pygame.locals import *
from util import *

def start(display_surf):
    scene_logger = get_public_logger('name_of_scene')
    scene_logger.info('Starting name_of_scene')
    while True:
        display_surf.fill(BG_PLACEHOLDER)
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
```
