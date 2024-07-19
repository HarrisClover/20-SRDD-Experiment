'''
This file contains the game objects classes such as Player, TimeMachine, and HistoricalEvent.
'''
import pygame
class GameObject:
    def __init__(self):
        self.x = 0
        self.y = 0
    def handle_events(self, events):
        pass
    def update(self):
        pass
    def render(self, screen):
        pass
class Player(GameObject):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('player.png')
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x -= 5
                elif event.key == pygame.K_RIGHT:
                    self.x += 5
                elif event.key == pygame.K_UP:
                    self.y -= 5
                elif event.key == pygame.K_DOWN:
                    self.y += 5
    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))
class TimeMachine(GameObject):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('time_machine.png')
    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))
class HistoricalEvent(GameObject):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('historical_event.png')
        self.active = True
    def update(self):
        if self.active and self.is_colliding_with(self.player):
            self.active = False
            self.trigger_event()
    def is_colliding_with(self, other):
        # Simple bounding box collision detection
        return (self.x < other.x + other.image.get_width() and
                self.x + self.image.get_width() > other.x and
                self.y < other.y + other.image.get_height() and
                self.y + self.image.get_height() > other.y)
    def trigger_event(self):
        # Logic to trigger a historical event
        print("Historical event triggered!")
    def render(self, screen):
        if self.active:
            screen.blit(self.image, (self.x, self.y))