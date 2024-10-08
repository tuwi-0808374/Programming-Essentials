""" Base class for assets """
import pygame

WIDTH = 0
HEIGHT = 1

class Asset:
    def __init__(self, rectangle_size, screen):
        self._rectangle_size = rectangle_size
        self._screen = screen
        self._x = 0
        self._y = 0
        self._images = []
        self._active_image = 0
        self._frame_counter = 0
        self._screen_size = pygame.display.get_surface().get_size()

    def load_images(self, paths_to_image):
        for path_to_image in paths_to_image:
            image = pygame.image.load(path_to_image).convert_alpha()
            image = pygame.transform.scale(image, self._rectangle_size)
            self._images.append(image)

    def draw(self, surface):
        if self._frame_counter % 10 == 0:
            self._active_image += 1
            if self._active_image == len(self._images):
                self._active_image = 0

        image = self._images[self._active_image]
        surface.blit(image, (self._x, self._y))

        self._frame_counter += 1