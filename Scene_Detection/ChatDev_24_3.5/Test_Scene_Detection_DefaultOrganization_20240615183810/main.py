'''
This is the main file of the scene change detection application.
'''
import tkinter as tk
from tkinter import filedialog
from scene_detector import SceneDetector
class SceneChangeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scene Change Detection")
        self.root.geometry("400x200")
        self.file_path = tk.StringVar()
        self.label = tk.Label(root, text="Select a video file:")
        self.label.pack()
        self.browse_button = tk.Button(root, text="Browse", command=self.browse_file)
        self.browse_button.pack()
        self.detect_button = tk.Button(root, text="Detect Scene Changes", command=self.detect_scene_changes)
        self.detect_button.pack()
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
    def browse_file(self):
        self.file_path.set(filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mkv")]))
    def detect_scene_changes(self):
        video_file = self.file_path.get()
        if video_file:
            scene_detector = SceneDetector(video_file)
            scene_changes = scene_detector.detect()
            self.result_label.config(text="Scene changes detected at timestamps: " + ", ".join(map(str, scene_changes)))
        else:
            self.result_label.config(text="Please select a video file.")
if __name__ == "__main__":
    root = tk.Tk()
    app = SceneChangeApp(root)
    root.mainloop()