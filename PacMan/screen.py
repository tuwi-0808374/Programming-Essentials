""" Handles the control of the PyGame screen """

import pygame

# Constants
BLACK = (0, 0, 0)
WIDTH = 0
HEIGHT = 1

class Screen:
    def __init__(self, width, height, title):
        """ __init__
        :param width: The width of the graphical screen
        :param height: The height of the graphical screen
        """
        self._display_surface = None
        self._screen_size = None
        self._size = width, height
        self._initialized = False
        self._title = title
        self._on_init()
        self._drawable_objects = []

    def _on_init(self):
        pygame.init()
        self._display_surface = pygame.display.set_mode(self._size)
        self._screen_size = pygame.display.get_surface().get_size()
        pygame.display.set_caption(self._title)
        self._initialized = True

    def get_width(self):
        return self._screen_size[WIDTH]

    def get_height(self):
        return self._screen_size[HEIGHT]

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._initialized = False

    def on_cleanup(self):
        pygame.quit()

    def add_visual(self, drawable_object):
        self._drawable_objects.append(drawable_object)

    def _on_render(self, surface):
        for drawable_object in self._drawable_objects:
            drawable_object.draw(self._display_surface)
        pygame.display.flip()

    def update(self):
        if self._initialized:
            for event in pygame.event.get():
                self.on_event(event)

            self._display_surface.fill(BLACK)
            self._on_render(self._display_surface)
        else:
            self.on_cleanup()

        return self._initialized
