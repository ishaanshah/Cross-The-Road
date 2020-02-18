import pygame as pg


class Score():
    """A class which is used to display and update the score"""
    def __init__(self, screen, settings, id):
        self.score = 0
        self.id = id
        self.screen = screen

        # Display text
        self.text = pg.font.Font(settings.font_face, settings.font_size)
        self.text_surf = self.text.render(
            f"Player {self.id}: {self.score}", True, (0, 0, 0)
        )
        self.text_rect = self.text_surf.get_rect()

        # Set postition of text
        if id == 1:
            self.text_rect.left, self.text_rect.top = (0, 1)
        else:
            self.text_rect.left, self.text_rect.top = (
                settings.screen_width-200, 0)

    def update_score(self, score):
        self.score += score

    def blitme(self):
        # Update text
        self.text_surf = self.text.render(
            f"Player {self.id}: {self.score}", True, (0, 0, 0)
        )
        self.screen.blit(self.text_surf, self.text_rect)
