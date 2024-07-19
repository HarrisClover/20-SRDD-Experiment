'''
This is the main file of the virtual sports arena application.
'''
import tkinter as tk
from arena import Arena
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Virtual Sports Arena")
        self.geometry("800x600")
        self.arena = Arena(self)
if __name__ == "__main__":
    app = Application()
    app.mainloop()