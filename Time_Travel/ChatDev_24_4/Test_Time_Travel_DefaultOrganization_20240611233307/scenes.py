'''
This file contains different Scene classes for different screens of the game, such as the menu screen, the game screen, etc.
'''
import pygame
from game_objects import Player, TimeMachine, HistoricalEvent
class Scene:
    def __init__(self, scene_manager):
        self.scene_manager = scene_manager
    def handle_events(self, events):
        raise NotImplementedError
    def update(self):
        raise NotImplementedError
    def render(self, screen):
        raise NotImplementedError
class MenuScene(Scene):
    def __init__(self, scene_manager):
        super().__init__(scene_manager)
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render("Press any key to start", True, (255, 255, 255))
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                self.scene_manager.go_to_scene(GameScene(self.scene_manager))
    def update(self):
        pass
    def render(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.text, (100, 100))
class GameScene(Scene):
    def __init__(self, scene_manager):
        super().__init__(scene_manager)
        self.player = Player()
        self.time_machine = TimeMachine()
        self.historical_event = HistoricalEvent()
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        self.player.handle_events(events)
    def update(self):
        self.player.update()
        self.time_machine.update()
        self.historical_event.update()
    def render(self, screen):
        screen.fill((0, 0, 0))
        self.player.render(screen)
        self.time_machine.render(screen)
        self.historical_event.render(screen)