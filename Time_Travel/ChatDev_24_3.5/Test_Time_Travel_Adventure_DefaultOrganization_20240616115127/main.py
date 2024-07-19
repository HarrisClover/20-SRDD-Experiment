'''
Time Travel Adventure
Software application that allows children to explore different time periods and learn about history through interactive storytelling and educational games.
'''
import tkinter as tk
from game import Game
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Time Travel Adventure")
        self.geometry("800x600")
        self.game = Game(self)
        self.game.pack()
if __name__ == "__main__":
    app = Application()
    app.mainloop()