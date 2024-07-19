'''
canvas.py
This file contains the Canvas class that represents the shared canvas.
Usage:
    from canvas import Canvas
    canvas = Canvas(master)
'''
import tkinter as tk
import socket
import threading
class Canvas(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, bg="white")
        self.bind("<Button-1>", self.on_mouse_down)
        self.bind("<B1-Motion>", self.on_mouse_drag)
        self.client_sockets = []
        self.lock = threading.Lock()
    def on_mouse_down(self, event):
        # Handle mouse down event
        self.send_data(f"DOWN {event.x} {event.y}")
    def on_mouse_drag(self, event):
        # Handle mouse drag event
        self.send_data(f"DRAG {event.x} {event.y}")
    def send_data(self, data):
        with self.lock:
            for client_socket in self.client_sockets:
                client_socket.send(data.encode())
    def process_data(self, data):
        # Process received data and update the canvas
        parts = data.split()
        if len(parts) == 3:
            action, x, y = parts
            if action == "DOWN":
                self.create_oval(int(x) - 2, int(y) - 2, int(x) + 2, int(y) + 2, fill="black")
            elif action == "DRAG":
                self.create_oval(int(x) - 2, int(y) - 2, int(x) + 2, int(y) + 2, fill="black")