'''
This file contains the DrawingTool class which handles the drawing tools that the user can use to create shapes, lines, and curves.
'''
import tkinter as tk
class DrawingTool:
    def __init__(self, window, vector_property):
        self.canvas = tk.Canvas(window)
        self.canvas.pack()
        self.line_button = tk.Button(window, text="Draw Line", command=self.prepare_draw_line)
        self.line_button.pack()
        self.start = None
        self.end = None
        self.vector_property = vector_property
    def prepare_draw_line(self):
        self.canvas.bind("<ButtonPress-1>", self.start_line)
        self.canvas.bind("<ButtonRelease-1>", self.end_line)
    def start_line(self, event):
        self.start = (event.x, event.y)
    def end_line(self, event):
        self.end = (event.x, event.y)
        self.draw_line()
    def draw_line(self):
        if self.start and self.end:
            self.canvas.create_line(self.start, self.end, fill=self.vector_property.color.get(), width=self.vector_property.stroke_width.get())
            self.start = None
            self.end = None
    def draw_shape(self, points):
        self.canvas.create_polygon(points, fill=self.vector_property.color.get(), width=self.vector_property.stroke_width.get())
    def draw_curve(self, points):
        self.canvas.create_line(points, smooth=True, fill=self.vector_property.color.get(), width=self.vector_property.stroke_width.get())