import random
import pygame as pg
from pygame.sprite import Group

from lion import Lion
from car import Car

def create_lions(screen, settings):
    """Make lions"""

    lions = Group()
    y_coorinates_lion = [215, 385, 565, 740]
    for y in y_coorinates_lion:
        x = random.randint(60, settings.screen_width/3)
        lion = Lion(screen, settings, (x, y))
        lions.add(lion)
        x = random.randint(settings.screen_width/3 + 60, 
            2*settings.screen_width/3)
        lion = Lion(screen, settings, (x, y))
        lions.add(lion)
        x = random.randint(2*settings.screen_width/3 + 60, 
            settings.screen_width-60)
        lion = Lion(screen, settings, (x, y))
        lions.add(lion)

    return lions

def create_cars(screen, settings):
    """Make cars"""

    cars = Group()
    y_coorinates_car = [125, 300, 475, 650, 830]
    for y in y_coorinates_car:
        x = random.randint(100, settings.screen_width-100)
        car = Car(screen, settings, (x, y))
        cars.add(car)
    
    return cars

def print_winner(settings, screen, winner):
    # Display winner
    text_winner = pg.font.Font(settings.font_face, 2*settings.font_size)
    if winner != 0:
        text_surf = text_winner.render(f"Player {winner} won!",
            True, (0, 0, 0))
    else:
        text_surf = text_winner.render(f"It is a draw", True, (0, 0, 0))
        
    text_rect = text_surf.get_rect()
    text_rect.centerx = settings.screen_width // 2
    text_rect.centery = settings.screen_height // 2

    screen.blit(text_surf, text_rect)
