'''
Game Screen module
Contains the GameScreen class responsible for displaying the game screen and handling user choices.
'''
import tkinter as tk
class GameScreen(tk.Frame):
    def __init__(self, master, screen):
        super().__init__(master)
        self.screen = screen
        self.create_widgets()
    def create_widgets(self):
        text_label = tk.Label(self, text=self.screen.get("text"))
        text_label.pack()
        for choice in self.screen.get("choices"):
            choice_button = tk.Button(self, text=choice.get("text"), command=lambda choice=choice: self.master.make_choice(choice))
            choice_button.pack()