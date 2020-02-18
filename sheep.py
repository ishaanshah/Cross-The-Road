import pygame as pg

class Sheep():
    """Initialize the sheep and set it's starting position"""
    def __init__(self, screen, settings, id):
        self.screen = screen
        self.settings = settings
        self.id = id

        # Load the sheep image and get it's rectangle
        self.image = pg.image.load(f"assets/sheep_{id}.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start sheep at bottom/top center of the screen
        if self.id == 1:
            self.rect.bottom = self.screen_rect.bottom
        else:
            self.rect.top = 0
        self.rect.centerx = self.screen_rect.centerx

        # Store a decimal value for sheep's center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Used for movement of the sheep
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Upadate the ships postion based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.settings.sheep_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.settings.sheep_speed_factor
        
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.settings.sheep_speed_factor
        
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.settings.sheep_speed_factor

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def reset(self):
        self.__init__(self.screen, self.settings, self.id)

    def blitme(self):
        """Draw the sheep at it's current position"""
        self.screen.blit(self.image, self.rect)
