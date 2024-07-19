'''
This file contains the SceneManager class, which controls the current scene (or screen) of the game.
'''
from scenes import MenuScene
class SceneManager:
    def __init__(self):
        self.scene = MenuScene(self)
    def go_to_scene(self, scene):
        self.scene = scene