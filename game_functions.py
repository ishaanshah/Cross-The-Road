import sys
import pygame as pg
from pygame.sprite import spritecollideany


def check_events(player):
    """Respond to keypresses and mouse events"""

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event, player)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, player)


def check_keydown_events(event, player):
    """Respond to key presses"""

    keys = (
        (pg.K_RIGHT, pg.K_LEFT, pg.K_UP, pg.K_DOWN),
        (pg.K_d, pg.K_a, pg.K_w, pg.K_s)
    )

    if event.key == keys[player.id][0]:
        player.sheep.moving_right = True

    if event.key == keys[player.id][1]:
        player.sheep.moving_left = True

    if event.key == keys[player.id][2]:
        player.sheep.moving_up = True

    if event.key == keys[player.id][3]:
        player.sheep.moving_down = True


def check_keyup_events(event, player):
    """Respond to key releases"""

    keys = (
        (pg.K_RIGHT, pg.K_LEFT, pg.K_UP, pg.K_DOWN),
        (pg.K_d, pg.K_a, pg.K_w, pg.K_s)
    )

    if event.key == keys[player.id][0]:
        player.sheep.moving_right = False

    if event.key == keys[player.id][1]:
        player.sheep.moving_left = False

    if event.key == keys[player.id][2]:
        player.sheep.moving_up = False

    if event.key == keys[player.id][3]:
        player.sheep.moving_down = False


def update_screen(settings, screen, player, lions, cars, time_text):
    """Update the screen"""

    # Redraw the screen during each pass through the loop
    screen.blit(settings.bg, (0, 0))
    player.update()
    lions.draw(screen)
    cars.draw(screen)
    time_text.blitme()

    # Make the most recently drawn screen visible
    pg.display.flip()


def check_collisions(player, lions, cars):
    """Returns true if there is a collision """

    if (spritecollideany(player.sheep, lions) or
            spritecollideany(player.sheep, cars)):
        player.sheep.reset()
        return True
    return False


def declare_winner(players):
    """Return the winner"""

    if players[0].score.score < players[1].score.score:
        return 2
    elif players[0].score.score == players[1].score.score:
        return 0
    else:
        return 1


def change_level(settings):
    settings.car_speed_factor *= settings.car_increase_factor
