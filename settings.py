import pygame as pg

class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings
        self.screen_width = 960
        self.screen_height = 960 

        # Background image
        self.bg = pg.image.load("assets/background.png")

        # Sheep settings
        self.sheep_speed_factor = 5 

        # Car speed
        self.car_speed_factor = 10

        self.car_increase_factor = 1.25

        # Text settings
        self.font_face = "freesansbold.ttf"
        self.font_size = 30 