""" Main application for the control of the PacMan and Ghosts """
import pygame.time

import screen
import pacman
import ghost
import cherry


class Application:
    """ The main application
    PacMan and the ghost
    """
    def __init__(self):
        self._running = True
        self._screen = screen.Screen(600, 400, "PAC man")
        self._pacman = pacman.PacMan((50, 50), self._screen)
        self._pacman.load_images(["./Graphics/pacman1.png",
                                  "./Graphics/pacman2.png",
                                  "./Graphics/pacman3.png"])
        self._ghost = ghost.Ghost((50, 50), self._screen)
        self._ghost.load_images(["./Graphics/ghost1.png",
                                  "./Graphics/ghost2.png",
                                  "./Graphics/ghost3.png"])
        self._cherry = cherry.Cherry((50, 50), self._screen)
        self._cherry.load_images(["./Graphics/cherry.png"])
        self._screen.add_visual(self._pacman)
        self._screen.add_visual(self._ghost)
        self._screen.add_visual(self._cherry)

    def run(self) -> None:
        while self._running:
            result = self._screen.update()
            pygame.time.Clock().tick(60)

            self._running = result


if __name__ == "__main__":
    the_app = Application()
    the_app.run()
