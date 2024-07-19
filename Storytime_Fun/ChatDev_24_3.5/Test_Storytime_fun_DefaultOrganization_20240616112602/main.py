'''
This is the main file of the interactive storybook application.
'''
import tkinter as tk
from storybook import Storybook
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interactive Storybook")
        self.storybook = Storybook(self)
        self.storybook.pack()
if __name__ == "__main__":
    app = Application()
    app.mainloop()