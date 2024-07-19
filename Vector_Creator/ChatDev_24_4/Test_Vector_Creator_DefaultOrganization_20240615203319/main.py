'''
This is the main file for the Vector Creator application. It initializes the application and handles user interaction.
'''
import tkinter as tk
from drawing_tool import DrawingTool
from vector_property import VectorProperty
from layer_manager import LayerManager
class VectorCreator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Vector Creator")
        self.vector_property = VectorProperty(self.window)
        self.drawing_tool = DrawingTool(self.window, self.vector_property)
        self.layer_manager = LayerManager(self.window)
    def run(self):
        self.window.mainloop()
if __name__ == "__main__":
    app = VectorCreator()
    app.run()