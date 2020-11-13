import pygame
from constants import *
from classes.cube import Cube
import random
random.seed(RANDOM_SEED)


class Game:
    """
    Game class
    """

    def __init__(self, nb_players=1):

        self.nb_players = nb_players
        self.score = [0] * nb_players
        # apply randomly head positions of snakes for each player(s)
        if nb_players == 1:
            self.snakes_pos = [[
                [
                    random.randint(SNAKE_WIDTH*0.1, SNAKE_WIDTH*.9),
                    random.randint(SNAKE_HEIGHT*0.1, SNAKE_HEIGHT*.9)
                    ]] for id_player in range(nb_players)]
        else:
            self.snakes_pos = [
                [[random.randint(SNAKE_WIDTH*0.1/2, SNAKE_WIDTH*.9/2),
                random.randint(SNAKE_HEIGHT*0.1, SNAKE_HEIGHT*.9)]],
                [[random.randint(SNAKE_WIDTH*0.55, SNAKE_WIDTH*.95),
                random.randint(SNAKE_HEIGHT*0.1, SNAKE_HEIGHT*.9)]]
                ]

        # set clock for movements
        self.clock = pygame.time.Clock()
        self.time_playing = 0

        self.grid_list = GRID_INIT.tolist()
        self.grid = []
        x = y = MARGIN
        for line in self.grid_list:
            for cube in line:
                if cube == "w":
                    self.grid.append(Cube(x=x, y=y, type="wall"))
                elif cube == "e":
                    self.grid.append(Cube(x=x, y=y))
                x += CUBE_SIZE
            x = MARGIN
            y += CUBE_SIZE



    def update_game(self):
        pass
        

    def get_playing_time(self):
        return self.time_playing / 1000

    def update_time_playing(self):
        self.time_playing += self.clock.get_time()
        self.clock.tick()