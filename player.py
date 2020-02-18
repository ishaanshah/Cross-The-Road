from score import Score
from sheep import Sheep

class Player():
    """A class which handles all the information about the player"""

    def __init__(self, screen, settings, id, turn=False):
        # Initiate score to 0
        self.score = Score(screen, settings, id+1)

        self.settings = settings
        self.id = id
        
        # Used for scoring
        self.static_list = [[215, 0], [385, 0], [565, 0], [740, 0]]
        self.moving_list = [[125, 0], [300, 0], [475, 0], [650, 0], [830, 0]]

        # Convert to negative so as to make checking easy for player 2 
        if id == 1:
            self.static_list = list(map(lambda x: [-x[0], 0], 
                self.static_list))
            self.moving_list = list(map(lambda x: [-x[0], 0], 
                self.moving_list))
        
        # Make a sheep object
        self.sheep = Sheep(screen, settings, id+1)

        # Set if turn is true or false
        self.turn = turn

        self.alive = True

        # True if player has currently completed the level
        self.level_complete = False

        self.consider_time = True

    def update(self):
        """Update player score and position"""

        pos_y = self.sheep.centery
        if self.id == 0 and pos_y < 30:
            self.level_complete = True

        if self.id == 1 and pos_y > self.settings.screen_height - 30:
            self.level_complete = True

        if self.id == 1:
            pos_y = -pos_y

        for i in enumerate(self.static_list):
            if self.static_list[i[0]][1] == 0 and pos_y < self.static_list[i[0]][0]:
                self.static_list[i[0]][1] = 1
        
        for i in enumerate(self.static_list):
            if self.static_list[i[0]][1] == 1:
                self.score.update_score(5)
                self.static_list[i[0]][1] = 2
        
        for i in enumerate(self.moving_list):
            if self.moving_list[i[0]][1] == 0 and pos_y < self.moving_list[i[0]][0]:
                self.moving_list[i[0]][1] = 1
        
        for i in enumerate(self.moving_list):
            if self.moving_list[i[0]][1] == 1:
                self.score.update_score(10)
                self.moving_list[i[0]][1] = 2

        self.sheep.blitme()
        self.score.blitme()
    
    def kill(self):
        """Kill the player and remove it from the screen"""
        
        self.alive = False
        self.sheep.reset()

    def reset(self):
        """Reset player after each round if not dead"""
        if self.alive:
            self.sheep.reset()

            # Used for scoring
            self.static_list = [[215, 0], [385, 0], [565, 0], [740, 0]]
            self.moving_list = [[125, 0], [300, 0], [475, 0], [650, 0], [830, 0]]

            # Convert to negative so as to make checking easy for player 2 
            if self.id == 1:
                self.static_list = list(map(lambda x: [-x[0], 0], 
                    self.static_list))
                self.moving_list = list(map(lambda x: [-x[0], 0], 
                    self.moving_list))
        
        self.level_complete = False
