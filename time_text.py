import time
import pygame as pg


class Time_Text():
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        self.text = pg.font.Font(settings.font_face, settings.font_size)
        self.text_surf = self.text.render("Time: ", True, (0, 0, 0))
        self.text_rect = self.text_surf.get_rect()
        self.text_rect.centerx = settings.screen_width // 2
        self.text_rect.top = 0

    def update(self, time):
        # Update text
        self.text_surf = self.text.render(f"Time: {time}", True, (0, 0, 0))

    def blitme(self):
        self.screen.blit(self.text_surf, self.text_rect)
