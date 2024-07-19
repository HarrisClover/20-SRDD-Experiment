'''
This is the main file for the VideoClipper application. It initializes the GUI and handles user interactions.
'''
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from video_editor import VideoEditor
class MainApplication:
    def __init__(self, window):
        self.window = window
        self.video_editor = VideoEditor()
        self.create_widgets()
    def create_widgets(self):
        self.open_button = tk.Button(self.window, text="Open Video", command=self.open_video)
        self.open_button.pack()
        self.clip_button = tk.Button(self.window, text="Set Clip Time", command=self.set_clip_time, state=tk.DISABLED)
        self.clip_button.pack()
        self.save_button = tk.Button(self.window, text="Save Video", command=self.save_video, state=tk.DISABLED)
        self.save_button.pack()
    def open_video(self):
        try:
            file_path = filedialog.askopenfilename()
            self.video_editor.load_video(file_path)
            self.clip_button.config(state=tk.NORMAL)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    def set_clip_time(self):
        try:
            start_time = simpledialog.askinteger("Input", "Enter start time")
            end_time = simpledialog.askinteger("Input", "Enter end time")
            self.video_editor.set_clip_time(start_time, end_time)
            self.save_button.config(state=tk.NORMAL)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    def save_video(self):
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".mp4")
            self.video_editor.save_video(file_path)
            self.clip_button.config(state=tk.DISABLED)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()