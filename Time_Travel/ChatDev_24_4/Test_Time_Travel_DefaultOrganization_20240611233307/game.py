'''
This file contains the Game class, which controls the game state and the game loop.
'''
import pygame
from scene_manager import SceneManager
class Game:
    def __init__(self):
        self.scene_manager = SceneManager()
    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))  # Create a screen object
        while True:
            self.scene_manager.scene.handle_events(pygame.event.get())
            self.scene_manager.scene.update()
            self.scene_manager.scene.render(screen)  # Pass the screen object to the render method
            pygame.display.flip()