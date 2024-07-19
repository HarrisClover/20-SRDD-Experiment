'''
Game module
Contains the Game class responsible for managing the game state and user interactions.
'''
import tkinter as tk
from story import Story
from game_screen import GameScreen
class Game(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.story = Story()
        self.current_screen = None
        self.start_game()
    def start_game(self):
        self.show_screen("intro")
    def show_screen(self, screen_name):
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = GameScreen(self, self.story.get_screen(screen_name))
        self.current_screen.pack()
    def make_choice(self, choice):
        self.story.make_choice(choice)
        self.show_screen(self.story.current_screen)
story.py