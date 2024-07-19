'''
This file contains the VectorProperty class which handles the properties of the vector graphics such as color and stroke width.
'''
import tkinter as tk
class VectorProperty:
    def __init__(self, window):
        self.color = tk.StringVar(window, "black")
        self.stroke_width = tk.StringVar(window, "1")
        self.color_entry = tk.Entry(window, textvariable=self.color)
        self.stroke_width_entry = tk.Entry(window, textvariable=self.stroke_width)
        self.color_entry.pack()
        self.stroke_width_entry.pack()
    def set_color(self, color):
        self.color.set(color)
    def set_stroke_width(self, width):
        self.stroke_width.set(width)