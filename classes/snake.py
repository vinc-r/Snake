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

        pos = [int(SNAKE_WIDTH/2), int(SNAKE_HEIGHT/2)]

        self.body = {
            'pos' : [pos],
            'cube' : [Cube(
                y=MARGIN+(pos[0])*(CUBE_SIZE),
                x=MARGIN+(pos[1])*(CUBE_SIZE),
                cube_type="head",
                id_player=self.id_player,
                rotation=self.orientation
                )]
        }

    def update_snake(self):
        pass

    def move_up(self, game):
        # if impossible orientation => do nothing and ignore move
        if self.orientation == "S":
            return
        # if goes outside arena limits => game over
        if self.body['pos'][-1][0]-1 <= 0:
            return 'game over'
        # and new position for head (tail will be remove if no apple is eaten)
        self.body['pos'].append([self.body['pos'][-1][0]-1, self.body['pos'][-1][1]])
        # cheack if eat an apple and eat it if possible
        self.eat_apple(game)
        # change orientation
        if self.orientation == "E":
            self.body['cube'][-1].rotate_left()
        elif self.orientation == "O":
            self.body['cube'][-1].rotate_right()
        self.orientation = "N"
        self.update_cube_pos()
        print("player position :", self.body['pos'], "\torientiation :",self.orientation)

    def move_down(self, game):
        # if impossible orientation => do nothing and ignore move
        if self.orientation == "N":
            return
        # if goes outside arena limits => game over
        if self.body['pos'][-1][0]+1 > SNAKE_HEIGHT:
            return 'game over'
        # and new position for head (tail will be remove if no apple is eaten)
        self.body['pos'].append([self.body['pos'][-1][0]+1, self.body['pos'][-1][1]])
        # cheack if eat an apple and eat it if possible
        self.eat_apple(game)
        # change orientation
        if self.orientation == "E":
            self.body['cube'][-1].rotate_right()
        elif self.orientation == "O":
            self.body['cube'][-1].rotate_left()
        self.orientation = "S"
        self.update_cube_pos()
        print("player position :", self.body['pos'], "\torientiation :",self.orientation)

    def move_right(self, game):
        # if impossible orientation => do nothing and ignore move
        if self.orientation == "O":
            return
        # if goes outside arena limits => game over
        if self.body['pos'][-1][1]+1 > SNAKE_WIDTH:
            return 'game over'
        # and new position for head (tail will be remove if no apple is eaten)
        self.body['pos'].append([self.body['pos'][-1][0], self.body['pos'][-1][1]+1])
        # cheack if eat an apple and eat it if possible
        self.eat_apple(game)
        # change orientation
        if self.orientation == "S":
            self.body['cube'][-1].rotate_left()
        elif self.orientation == "N":
            self.body['cube'][-1].rotate_right()
        self.orientation = "E"
        self.update_cube_pos()
        print("player position :", self.body['pos'], "\torientiation :",self.orientation)

    def move_left(self, game):
        if self.orientation == "E":
            return
        if self.body['pos'][-1][1]-1 <= 0:
            return 'game over'
        self.body['pos'].append([self.body['pos'][-1][0], self.body['pos'][-1][1]-1])
        self.eat_apple(game)
        self.update_cube_pos()
        if self.orientation == "N":
            self.body['cube'][-1].rotate_left()
        elif self.orientation == "S":
            self.body['cube'][-1].rotate_right()
        self.orientation = "O"
        self.update_cube_pos()
        print("player position :", self.body['pos'], "\torientiation :",self.orientation)

    def eat_apple(self, game):
        # cheack if eat an apple
        if self.body['pos'][-1] in game.apples['pos']:
            self.size+=1
            # insert cube
            self.body['cube'].insert(0, 
                Cube(x=MARGIN+self.body['pos'][0][1]*CUBE_SIZE,
                        y=MARGIN+self.body['pos'][0][0]*CUBE_SIZE,
                        cube_type=["dark","light"][self.size%2],
                        id_player=self.id_player))
            game.new_apple(deleting_apple_pos=self.body['pos'][-1])
        else:
            # remove tail if noting eaten
            self.body['pos'].pop(0)




    def update_cube_pos(self):
        for i in range(self.size):
            self.body['cube'][i].rect.y = MARGIN+(self.body['pos'][i][0])*CUBE_SIZE
            self.body['cube'][i].rect.x = MARGIN+(self.body['pos'][i][1])*CUBE_SIZE

