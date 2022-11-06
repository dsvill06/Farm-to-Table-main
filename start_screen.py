import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from ui_element import UIElement, GameState
from states import title_screen, korn, milk, eggs, question_mark
import constants
import images


def main():
    pygame.init()
    
    screen = pygame.display.set_mode((constants.X,constants.Y))
    pygame.display.set_caption('Farm-to-Table')
    game_state = GameState.TITLE
    pygame.mixer.music.load('../pygame_test/start_screen.py')
    pygame.mixer.music.play(-1)
    

    # main loop
    while True:
        
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)

        if game_state == GameState.KORN:
            game_state = korn(screen)
            
        if game_state == GameState.MILK:
            game_state = milk(screen)
        
        if game_state == GameState.EGGS:
            game_state = eggs(screen)
            
        if game_state == GameState.QUESTION:
            game_state = question_mark(screen)

        if game_state == GameState.QUIT:
            pygame.quit()
            return

# call main when the script is run
if __name__ == "__main__":
    main()