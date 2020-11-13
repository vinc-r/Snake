import pygame
from constants import *
import random
random.seed(2)
from classes.cube import Cube

class Snake():

    """
    Game class
    """

    def __init__(self, id_player=1):

        self.id_player = id_player
        self.size = 1
        self.score = 0
        self.orientation = random.choice(["E","N","O","S"])
        """
        # apply randomly head positions of snakes for each player(s)
        self.head_pos = [
                    random.randint(SNAKE_WIDTH*0.1, SNAKE_WIDTH*.9),
                    random.randint(SNAKE_HEIGHT*0.1, SNAKE_HEIGHT*.9)
                    ]

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
        """

        pos = [int(SNAKE_WIDTH/2), int(SNAKE_HEIGHT/2)]

        self.body = {
            'pos' : [pos],
            'cube' : [Cube(
                x=MARGIN+(1+pos[0])*(CUBE_SIZE),
                y=MARGIN+(1+pos[1])*(CUBE_SIZE),
                cube_type="head",
                id_player=self.id_player,
                rotation=self.orientation
                )]
        }

    def update_snake(self):
        pass

    def move_up(self):
        self.body['pos'].append([self.body['pos'][-1][0], self.body['pos'][-1][1]-1])
        self.body['pos'].pop(0)
        self.update_cube_pos()
        if self.orientation == "E":
            self.body['cube'][0].rotate_left()
        elif self.orientation == "O":
            self.body['cube'][0].rotate_right()
        self.orientation = "N"

    def move_down(self):
        self.body['pos'].append([self.body['pos'][-1][0], self.body['pos'][-1][1]+1])
        self.body['pos'].pop(0)
        self.update_cube_pos()
        if self.orientation == "E":
            self.body['cube'][0].rotate_right()
        elif self.orientation == "O":
            self.body['cube'][0].rotate_left()
        self.orientation = "S"

    def move_right(self):
        self.body['pos'].append([self.body['pos'][-1][0]+1, self.body['pos'][-1][1]])
        self.body['pos'].pop(0)
        self.update_cube_pos()
        if self.orientation == "S":
            self.body['cube'][0].rotate_left()
        elif self.orientation == "N":
            self.body['cube'][0].rotate_right()
        self.orientation = "E"

    def move_left(self):
        self.body['pos'].append([self.body['pos'][-1][0]-1, self.body['pos'][-1][1]])
        self.body['pos'].pop(0)
        self.update_cube_pos()
        if self.orientation == "N":
            self.body['cube'][0].rotate_left()
        elif self.orientation == "S":
            self.body['cube'][0].rotate_right()
        self.orientation = "O"

    def update_cube_pos(self):
        for i in range(self.size):
            self.body['cube'][i].rect.x = MARGIN+(1+self.body['pos'][i][0])*CUBE_SIZE
            self.body['cube'][i].rect.y = MARGIN+(1+self.body['pos'][i][1])*CUBE_SIZE
