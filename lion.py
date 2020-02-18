import random
import pygame as pg
from pygame.sprite import Sprite


class Lion(Sprite):
    """A class to manage the lion's in the game which are fixed objects"""

    def __init__(self, screen, settings, position):
        """Create lion at random x positon on the each level"""
        super(Lion, self).__init__()
        self.screen = screen

        # Load the lion image and get it's rectangle
        self.image = pg.image.load("assets/lion.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Set position of lion
        self.rect.centerx = position[0]
        self.rect.centery = position[1]

        # Set direction of lion
        self.direction = bool(random.randint(0, 1))
        self.image = pg.transform.flip(self.image, self.direction, False)
