import random
import pygame as pg
from pygame.sprite import Sprite

class Car(Sprite):
    """A class to manage the car's in the game which are moving objects"""

    def __init__(self, screen, settings, position):
        """Create car at random x positon on the each level"""
        super(Car, self).__init__()
        self.screen = screen
        self.settings = settings

        # Set type of car
        self.type = random.randint(1, 3)

        # Load the car image and get it's rectangle
        self.image = pg.image.load(f"assets/car_{self.type}.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Set position of car
        self.rect.centerx = position[0]
        self.rect.centery = position[1]

        # Store a decimal value for car's center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Set direction of car, 0 is left and 1 is right
        self.direction = random.randint(0, 1)
        self.image = pg.transform.flip(self.image, bool(self.direction), False)
        
    def update(self):
        """Update the cars postion based on the movement flag"""
        if self.rect.right > self.screen_rect.right:
            self.direction = 0
            self.image = pg.transform.flip(self.image, True, False)
        
        if self.rect.left < 0:
            self.direction = 1
            self.image = pg.transform.flip(self.image, True, False)
        
        if self.direction == 0:
            self.centerx -= self.settings.car_speed_factor
      
        if self.direction == 1:
            self.centerx += self.settings.car_speed_factor

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery