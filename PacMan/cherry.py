""" Handles the cherry character """

import asset

class Cherry(asset.Asset):
    def __init__(self, rectangle_size, screen):
        super().__init__(rectangle_size, screen)
