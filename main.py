import os
import pygame
from constants import *
#from ai_game import AIGame
from classes.game import Game
from functions.handdle_state import *
#from leaderboard import *


if __name__ == "__main__":

    # initialize pygame window
    #os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % WINDOWS_POSITION
    pygame.init()
    pygame.display.set_caption(TITLE)
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_icon(pygame.image.load(ICON))

    # initialize sound
    sound = pygame.mixer.Sound(MUSIC['Menu'])
    sound.play(loops=-1)
    sound.set_volume(VOLUME)

    
    # initialize bacjground menu
    # background = pygame.image.load("img/menu_bg.jpg")

    # initialize game
    game = Game()
    # ai_game = AIGame()

    running = True
    state = "playing"
    
    while running:

        # apply background
        screen.fill(BLACK)

        #print(state)

        
        if state == "playing":
            state, running = handle_state_playing(game=game, screen=screen, sound=sound)
        """
        elif state == "pause":
            state, running = handle_state_pause(game=game, screen=screen, sound=sound)
        elif state == "AI_pause":
            state, running = handle_state_pause(game=ai_game, screen=screen, sound=sound, state=state)
        elif state == "menu":
            state, running = handle_state_menu(game=game, ai_game=ai_game, screen=screen, bg=background, sound=sound)
        elif state == "game_over":
            state, running = handle_state_game_over(game=game, screen=screen, sound=sound)
        elif state == "AI_game_over":
            state, running = handle_state_game_over(game=ai_game, screen=screen, sound=sound, state=state)
        elif state == "leaderboard":
            state, running = handle_state_leaderboard(game=game, screen=screen, sound=sound)
        elif state == "AI_playing":
            state, running = handle_state_AI_playing(game=ai_game, screen=screen, sound=sound)

        # update screen
        pygame.display.flip()

        # check if ended and close game
        if state == "end" and not running:
            sound.stop()
            pygame.quit()
            print("\nGOOD BYE !")
        """

        # update screen
        pygame.display.flip()


    pygame.quit()
    print("\nGOOD BYE !")
