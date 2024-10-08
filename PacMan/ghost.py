""" Handles the ghost character """

import npc

class Ghost(npc.NPC):
    def __init__(self, rectangle_size, screen):
        super().__init__(rectangle_size, screen)

