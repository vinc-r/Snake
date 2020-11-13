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

        self.update_grid()
        apples_positions = [self.find_new_apple_position() for i in range(nb_players)]
        self.apples = {
            'pos' : apples_positions,
            'cube' : [Cube(
                x=MARGIN+(1+apples_positions[i][0])*(CUBE_SIZE),
                y=MARGIN+(1+apples_positions[i][1])*(CUBE_SIZE),
                cube_type="apple",
                ) for i in range(nb_players)]
        }

    def update_grid(self):
        self.grid_list = GRID_INIT.tolist()
        for snake in self.snakes:
            for body_part_pos in snake.body['pos']:
                self.grid_list[body_part_pos[0]][body_part_pos[1]] = "p"
        try:
            for apple in self.apples:
                print(apple["pos"])
                self.grid_list[apple["pos"][0]][apple["pos"][1]]
        except AttributeError:
            # if apple not created yet !
            pass 

        for snake in self.snakes:
            snake.update_snake()

    def update_game(self):
        pass

    def find_new_apple_position(self):
        # random matrix to draw
        r = np.random.rand(SNAKE_WIDTH+2, SNAKE_HEIGHT+2)
        # return only one position available by finding max only on "empty" cases
        pos = [i[0] for i in np.where(r == max(r[np.array(self.grid_list)=="e"]))]
        self.grid_list[pos[0]][pos[1]] = "a"
        return pos

    def get_playing_time(self):
        return self.time_playing / 1000

    def update_time_playing(self):
        self.time_playing += self.clock.get_time()
        self.clock.tick()