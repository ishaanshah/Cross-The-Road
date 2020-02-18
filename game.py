import sys, random, time
import pygame as pg

from settings import Settings
from player import Player
from lion import Lion
from score import Score
from time_text import Time_Text
import game_functions as gf
import helper as hp

def run_game():
    # Initialize random
    random.seed(time.time())
    
    # Initialize game and create the screen
    pg.init()
    settings = Settings()
    screen = pg.display.set_mode(
        (settings.screen_width, settings.screen_height))

    pg.display.set_caption("Cross the Road")

    # Create a clock for the game
    clock = pg.time.Clock()

    # Make lions
    lions = hp.create_lions(screen, settings)
    # Make cars
    cars = hp.create_cars(screen, settings)

    # Create players
    player_1 = Player(screen, settings, 0, True)
    player_2 = Player(screen, settings, 1)
    players = (player_1, player_2)

    # '0' represents player 1 and '1' represents player 2
    curr_player = 0

    start_time = time.time()
    time_text = Time_Text(screen, settings)

    complete_players = 0

    # Start the main loop for the game
    while players[0].alive or players[1].alive:
        # Subtract time score 
        if players[0].alive and players[1].alive:
            if players[0].level_complete:
                players[0].score.update_score(int(start_time - time.time()))
                start_time = time.time()
                players[0].reset()
                complete_players += 1
                
            if players[1].level_complete:
                players[1].score.update_score(int(start_time - time.time()))
                start_time = time.time()
                players[1].reset()
                complete_players += 1

        gf.check_events(players[curr_player])
        if gf.check_collisions(players[curr_player], lions, cars):
            players[curr_player].kill()
            curr_player = int(not curr_player)
            start_time = time.time()

        players[curr_player].sheep.update()
        cars.update()
        gf.update_screen(settings, screen, players[curr_player],
            lions, cars, time_text)
        
        if players[curr_player].alive and players[curr_player].level_complete:
            curr_player = not curr_player

        # Logic for level changing
        if players[0].alive and players[1].alive:
            if complete_players == 2:
                gf.change_level(settings)
                curr_player = 0
                complete_players = 0

        if players[0].alive ^ players[1].alive:
            if players[0].level_complete or players[1].level_complete:
                gf.change_level(settings)
                curr_player = not curr_player
                players[curr_player].reset()
                start_time = time.time()
        
        # Update time
        time_text.update(int(time.time()-start_time))

        clock.tick(30)

    white_bg = pg.Rect(0, 0, settings.screen_width, settings.screen_height)
    pg.draw.rect(screen, (255, 255, 255), white_bg)
    
    # Get the winner
    winner = gf.declare_winner(players)

    # Print the winner
    hp.print_winner(settings, screen, winner)

    pg.display.update()
    
    time.sleep(3)

run_game()
