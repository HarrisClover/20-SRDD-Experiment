'''
This is the main file of our Time Travel Adventure application. 
It initializes the game and controls the main game loop.
'''
import pygame
from game import Game
def main():
    pygame.init()
    game = Game()
    game.run()
if __name__ == "__main__":
    main()