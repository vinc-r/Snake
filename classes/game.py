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

    def __init__(self, nb_players=2):

        self.nb_players = nb_players
        self.snakes = [Snake(id_player=i, nb_players=nb_players) for i in range(1,nb_players+1)]
        print("player position :", self.snakes[0].body['pos'])

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

        print("Grid before update :", self.grid_list)
        self.update_grid()
        print("Grid after update :", self.grid_list)
        apples_positions = [self.find_new_apple_position() for i in range(nb_players)]
        print("Apples positions :", apples_positions)
        self.apples = {
            'pos' : apples_positions,
            'cube' : [Cube(
                y=MARGIN+(apples_positions[i][0])*(CUBE_SIZE),
                x=MARGIN+(apples_positions[i][1])*(CUBE_SIZE),
                cube_type="apple"
                ) for i in range(nb_players)]
        }

    def update_grid(self):
        self.grid_list = GRID_INIT.tolist()
        for snake in self.snakes:
            for body_part_pos in snake.body['pos']:
                self.grid_list[body_part_pos[0]][body_part_pos[1]] = "p"
        try:
            for apple_pos in self.apples['pos']:
                print(apple_pos)
                self.grid_list[apple_pos[0]][apple_pos[1]]
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
        print(r)
        # return only one position available by finding max only on "empty" cases
        pos = [i[0] for i in np.where(r == max(r[np.array(self.grid_list)=="e"]))]
        self.grid_list[pos[0]][pos[1]] = "a"
        print("gird with apple", self.grid_list)
        return pos

    def new_apple(self, deleting_apple_pos, new_apple_pos=None):
        if new_apple_pos is None:
            self.update_grid()
            new_apple_pos = self.find_new_apple_position()

        for i in range(len(self.apples['pos'])):
            if self.apples['pos'][i] == deleting_apple_pos:
                self.apples['pos'][i] = new_apple_pos
                self.apples['cube'][i] = Cube(
                    y=MARGIN+(new_apple_pos[0])*(CUBE_SIZE),
                    x=MARGIN+(new_apple_pos[1])*(CUBE_SIZE),
                    cube_type="apple"
                )
        self.update_grid()

    def get_playing_time(self):
        return self.time_playing / 1000

    def update_time_playing(self):
        self.time_playing += self.clock.get_time()
        self.clock.tick()