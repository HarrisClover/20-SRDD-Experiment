'''
This file contains the LayerManager class which handles the arrangement of elements in layers.
'''
import tkinter as tk
class LayerManager:
    def __init__(self, window):
        self.layers = []
        self.layer_listbox = tk.Listbox(window)
        self.layer_listbox.pack()
    def add_layer(self, layer):
        self.layers.append(layer)
        self.layer_listbox.insert(tk.END, layer)
    def remove_layer(self, layer):
        self.layers.remove(layer)
        self.layer_listbox.delete(self.layers.index(layer))
    def arrange_layers(self):
        for i, layer in enumerate(self.layers):
            layer.lower(i)