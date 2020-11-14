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

    
    # apply actual positions snake(s)
    for snake in game.snakes:
        for cube in snake.body['cube']:
            screen.blit(cube.image, cube.rect)

    # apply actual positions apple(s)
    for cube in game.apples['cube']:
        screen.blit(cube.image, cube.rect)

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == AZERTY.K_p:
                return "pause", True

            elif event.key == pygame.K_ESCAPE:
                return "menu", False

            elif event.key == AZERTY.K_UP:
                if game.snakes[0].move_up(game) == "game over":
                    return "game over", False

            elif event.key == AZERTY.K_LEFT:
                if game.snakes[0].move_left(game) == "game over":
                    return "game over", False

            elif event.key == AZERTY.K_RIGHT:
                if game.snakes[0].move_right(game) == "game over":
                    return "game over", False

            elif event.key == AZERTY.K_DOWN:
                if game.snakes[0].move_down(game) == "game over":
                    return "game over", False

    return state, running