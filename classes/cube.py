import pygame
from constants import CUBE_SIZE


class Cube(pygame.sprite.Sprite):

    def __init__(self, x, y, cube_type="bg", id_player=None, rotation="S"):
        super().__init__()

        if cube_type in ["head", "dark", "light"]:
            cube_type = "snake-player"+str(id_player)+"-"+cube_type

        self.image = pygame.image.load('img/cube/'+cube_type+'.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rotation = 0
        if rotation == "N":
            self.rotate_left()
        elif rotation == "O":
            self.rotate_left(nb=2)
        elif rotation == "E":
            pass
        elif rotation == "S":
            self.rotate_right()

    def move_down(self):
        self.rect.y += CUBE_SIZE

    def move_up(self):
        self.rect.y -= CUBE_SIZE

    def move_right(self):
        self.rect.x += CUBE_SIZE

    def move_left(self):
        self.rect.x -= CUBE_SIZE

    def rotate_left(self, nb=1):
        self.rotation += 90*nb
        self.image = pygame.transform.rotate(self.image, 90*nb)

    def rotate_right(self, nb=1):
        self.rotation -= 90*nb
        self.image = pygame.transform.rotate(self.image, -90*nb)
