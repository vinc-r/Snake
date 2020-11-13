import pygame
from classes.cube import Cube
from constants import *


def handle_state_playing(game, screen, sound, state="playing", running=True):

    # update clock
    game.update_time_playing()

    # update board game
    if game.update_game() == "game_over":
        return "game_over", True

    # apply background
    screen.fill(BLACK)

    # apply grid
    for cube in game.grid:
        screen.blit(cube.image, cube.rect)

    # apply actual tetrimino
    """
    for cube in game.tetrimino.cubes:
        screen.blit(cube.image, cube.rect)
    """

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == AZERTY.K_p:
                return "pause", True

            elif event.key == pygame.K_ESCAPE:
                return "menu", False

    return state, running