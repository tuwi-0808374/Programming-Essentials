""" Base class for the playable characters and the non-playable characters """
import pygame
import random


# Constants
RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3

WIDTH = 0
HEIGHT = 1

class NPC:
    def __init__(self, rectangle_size, screen):
        self._rectangle_size = rectangle_size
        self._screen = screen
        self._energized = False
        self._x = 0
        self._y = 0
        self._speed = 2
        self._direction = RIGHT
        self._images = []
        self._active_image = 0
        self._frame_counter = 0
        self._screen_size = pygame.display.get_surface().get_size()

    def load_images(self, paths_to_image):
        for path_to_image in paths_to_image:
            image = pygame.image.load(path_to_image).convert_alpha()
            image = pygame.transform.scale(image, self._rectangle_size)
            self._images.append(image)

    def up(self):
        if self._y > 0:
            self._direction = UP

    def down(self):
        if self._y < self._screen.get_height():
            self._direction = DOWN

    def left(self):
        if self._x > 0:
            self._direction = LEFT

    def right(self):
        if self._x < self._screen.get_width():
            self._direction = RIGHT

    def move(self):
        new_x = self._x
        new_y = self._y

        if self._direction == RIGHT:
            new_x = self._x + self._speed

        if self._direction == LEFT:
            new_x = self._x - self._speed

        if self._direction == UP:
            new_y = self._y - self._speed

        if self._direction == DOWN:
            new_y = self._y + self._speed

        if new_x < 0:
            new_x = 0

        maximum_x = self._screen_size[0] - self._rectangle_size[WIDTH]
        if new_x > maximum_x:
            new_x = maximum_x
            new_x = maximum_x

        if new_y < 0:
            new_y = 0

        maximum_y = self._screen.get_height() - self._rectangle_size[HEIGHT]
        if new_y > maximum_y:
            new_y = maximum_y

        self._x = new_x
        self._y = new_y

    def draw(self, surface):
        if self._frame_counter % 10 == 0:
            self._active_image += 1
            if self._active_image == len(self._images):
                self._active_image = 0

        image = self._images[self._active_image]
        if self._direction == RIGHT:
            # Pacman default faces right
            pass
        elif self._direction == LEFT:
            image = pygame.transform.rotate(image, 180)
            image = pygame.transform.flip(image, False, True)
        elif self._direction == UP:
            image = pygame.transform.rotate(image, 90)
        elif self._direction == DOWN:
            image = pygame.transform.rotate(image, -90)

        surface.blit(image, (self._x, self._y))

        self._frame_counter += 1

        if self._frame_counter % 30 == 0:
            new_direction = random.choice([RIGHT, LEFT, UP, DOWN])
            if new_direction == RIGHT:
                self.right()

            if new_direction == LEFT:
                self.left()

            if new_direction == UP:
                self.up()

            if new_direction == DOWN:
                self.down()

            self._frame_counter = 0

        self.move()