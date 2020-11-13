import pygame
from constants import *
from classes.cube import Cube
from classes.snake import Snake
import random
random.seed(RANDOM_SEED)


class Game:
    """
    Game class
    """

    def __init__(self, nb_players=1):

        self.nb_players = nb_players
        self.snakes = [Snake(id_player=i) for i in range(1,nb_players+1)]

        # set clock for movements
        self.clock = pygame.time.Clock()
        self.time_playing = 0

        self.grid_list = GRID_INIT.tolist()
        self.grid = []
        x = y = MARGIN
        for line in self.grid_list:
            for cube in line:
                if cube == "w":
                    self.grid.append(Cube(x=x, y=y, cube_type="wall"))
                elif cube == "e":
                    self.grid.append(Cube(x=x, y=y))
                x += CUBE_SIZE
            x = MARGIN
            y += CUBE_SIZE

    def update_game(self):
        for snake in self.snakes:
            snake.update_snake()
        
    def get_playing_time(self):
        return self.time_playing / 1000

    def update_time_playing(self):
        self.time_playing += self.clock.get_time()
        self.clock.tick()