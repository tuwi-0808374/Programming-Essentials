""" Handles the pac man character """

import npc

class PacMan(npc.NPC):
    def __init__(self, rectangle_size, screen):
        super().__init__(rectangle_size, screen)

