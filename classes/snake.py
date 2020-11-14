import pygame
from constants import *
import random
random.seed(RANDOM_SEED)
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

        pos = [int(SNAKE_WIDTH/2)-1, int(SNAKE_HEIGHT/2)+1]

        self.body = {
            'pos' : [pos],
            'cube' : [Cube(
                x=MARGIN+(pos[0])*(CUBE_SIZE),
                y=MARGIN+(pos[1])*(CUBE_SIZE),
                cube_type="head",
                id_player=self.id_player,
                rotation=self.orientation
                )]
        }

    def update_snake(self):
        pass

    def move_up(self, game):
        if self.orientation == "S":
            return
        if self.body['pos'][-1][1]-1 <= 0:
            return 'game over'
        self.body['pos'].append([self.body['pos'][-1][0], self.body['pos'][-1][1]-1])
        self.body['pos'].pop(0)
        self.update_cube_pos()
        if self.orientation == "E":
            self.body['cube'][0].rotate_left()
        elif self.orientation == "O":
            self.body['cube'][0].rotate_right()
        self.orientation = "N"
        if self.body['pos'][-1] in game.apples['pos']:
            print("apple to eat")
        print("player position :", self.body['pos'], "\torientiation :",self.orientation)

    def move_down(self, game):
        if self.orientation == "N":
            return
        if self.body['pos'][-1][1]+1 > SNAKE_HEIGHT:
            return 'game over'
        self.body['pos'].append([self.body['pos'][-1][0], self.body['pos'][-1][1]+1])
        self.body['pos'].pop(0)
        self.update_cube_pos()
        if self.orientation == "E":
            self.body['cube'][0].rotate_right()
        elif self.orientation == "O":
            self.body['cube'][0].rotate_left()
        self.orientation = "S"
        if self.body['pos'][-1] in game.apples['pos']:
            print("apple to eat")
        print("player position :", self.body['pos'], "\torientiation :",self.orientation)

    def move_right(self, game):
        if self.orientation == "O":
            return
        if self.body['pos'][-1][0]+1 > SNAKE_WIDTH:
            return 'game over'
        self.body['pos'].append([self.body['pos'][-1][0]+1, self.body['pos'][-1][1]])
        self.body['pos'].pop(0)
        self.update_cube_pos()
        if self.orientation == "S":
            self.body['cube'][0].rotate_left()
        elif self.orientation == "N":
            self.body['cube'][0].rotate_right()
        self.orientation = "E"
        if self.body['pos'][-1] in game.apples['pos']:
            print("apple to eat")
        print("player position :", self.body['pos'], "\torientiation :",self.orientation)

    def move_left(self, game):
        if self.orientation == "E":
            return
        if self.body['pos'][-1][0]-1 <= 0:
            return 'game over'
        self.body['pos'].append([self.body['pos'][-1][0]-1, self.body['pos'][-1][1]])
        self.body['pos'].pop(0)
        self.update_cube_pos()
        if self.orientation == "N":
            self.body['cube'][0].rotate_left()
        elif self.orientation == "S":
            self.body['cube'][0].rotate_right()
        self.orientation = "O"
        if self.body['pos'][-1] in game.apples['pos']:
            print("apple to eat")
        print("player position :", self.body['pos'], "\torientiation :",self.orientation)

    def update_cube_pos(self):
        for i in range(self.size):
            self.body['cube'][i].rect.x = MARGIN+(self.body['pos'][i][0])*CUBE_SIZE
            self.body['cube'][i].rect.y = MARGIN+(self.body['pos'][i][1])*CUBE_SIZE

