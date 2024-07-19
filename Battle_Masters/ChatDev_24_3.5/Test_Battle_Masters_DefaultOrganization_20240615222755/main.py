'''
This is the main file of the Battle Masters game application.
'''
import tkinter as tk
from game import Game
class BattleMastersApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Battle Masters")
        self.geometry("800x600")
        self.game = Game()
        self.create_widgets()
    def create_widgets(self):
        # Create and configure GUI elements here
        start_button = tk.Button(self, text="Start Game", command=self.start_game)
        start_button.pack()
    def start_game(self):
        # Start the game here
        self.game.start_battle()
if __name__ == "__main__":
    app = BattleMastersApp()
    app.mainloop()