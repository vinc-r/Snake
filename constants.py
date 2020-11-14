import numpy as np
import pygame

###################
# INTERFACE INFOS #
###################

TITLE = "Snake"
ICON = 'img/Snake-icon.ico'
MUSIC = {
    "Menu" : "sound/soundtrack-title-screen.wav"
}
VOLUME = .1

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# FONTS
FONT_ARCADE_IN = 'font/8-bit Arcade In.ttf'
FONT_ARCADE_OUT = 'font/8-bit Arcade OUT.ttf'

# Max name length for leaderboard
MAX_NAME_LENGTH = 6


##################
# GAMEPLAY INFOS #
##################

# Dimmensions of the board game arena
SNAKE_WIDTH = 10
SNAKE_HEIGHT = 10
MARGIN = 10

# SIze of snake cube (in pixels)
CUBE_SIZE = 20

GRID_INIT = np.array([["w"] * (SNAKE_WIDTH + 2)] * (SNAKE_HEIGHT + 2))
GRID_INIT[1:-1, 1:-1] = "e"

# SPEED MOVEMENT
FPS = 60.0988
SPEED_LEVEL = 20 / FPS

RANDOM_SEED = 1

##############################
# AZERTY KEYBORD TRANSLATION #
##############################

class AZERTY:
    """AZERTY TRANSLATION"""
    K_a = pygame.K_q
    K_p = pygame.K_p
    K_r = pygame.K_r
    K_q = pygame.K_a
    K_l = pygame.K_l
    K_m = pygame.K_SEMICOLON
    K_SPACE = pygame.K_SPACE
    K_LEFT = pygame.K_LEFT
    K_RIGHT = pygame.K_RIGHT
    K_UP = pygame.K_UP
    K_DOWN = pygame.K_DOWN


############################
# NEURAL NETWORK CONSTANTS #
############################

GAMMA_TRAINER = .996
EPSILON_TRAINER = 1.0
EPSILON_MIN_TRAINER = .01
EPSILON_DECAY_TRAINER = .9999
LEARNING_RATE_TRAINER = .01

# some possible actions aren't possible for all tetrimino or all spin
POSSIBLES_ACTIONS = {}
for i in range(11 * 4):
    POSSIBLES_ACTIONS[i] = {"col": (i // 4) - 5,
                            "spin": i % 4}


TIME_BETWEEN_MOVE_TRAINING = 0
