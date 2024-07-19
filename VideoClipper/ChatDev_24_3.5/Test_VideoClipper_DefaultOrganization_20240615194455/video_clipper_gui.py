'''
This file contains the VideoClipperGUI class which provides the graphical user interface for the VideoClipper application.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip
class VideoClipperGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("VideoClipper")
        self.video_path = None
        self.start_time = None
        self.end_time = None
        # Create the GUI elements
        self.create_widgets()
    def create_widgets(self):
        # Create a label for video selection
        self.video_label = tk.Label(self.root, text="Select a video:")
        self.video_label.pack()
        # Create a button to browse and select a video file
        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_video)
        self.browse_button.pack()
        # Create a label for start time selection
        self.start_label = tk.Label(self.root, text="Start time (in seconds):")
        self.start_label.pack()
        # Create an entry field for start time input
        self.start_entry = tk.Entry(self.root)
        self.start_entry.pack()
        # Create a label for end time selection
        self.end_label = tk.Label(self.root, text="End time (in seconds):")
        self.end_label.pack()
        # Create an entry field for end time input
        self.end_entry = tk.Entry(self.root)
        self.end_entry.pack()
        # Create a button to clip and save the video
        self.clip_button = tk.Button(self.root, text="Clip Video", command=self.clip_video)
        self.clip_button.pack()
    def browse_video(self):
        # Open a file dialog to select a video file
        self.video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mov")])
    def clip_video(self):
        # Get the start and end times from the entry fields
        self.start_time = float(self.start_entry.get())
        self.end_time = float(self.end_entry.get())
        # Clip the video using moviepy
        video = VideoFileClip(self.video_path)
        clipped_video = video.subclip(self.start_time, self.end_time)
        # Save the clipped video as a new file
        save_path = filedialog.asksaveasfilename(defaultextension=".mp4")
        clipped_video.write_videofile(save_path)
        # Display a success message
        messagebox.showinfo("Success", "Video clipped and saved successfully!")
    def run(self):
        # Run the main event loop
        self.root.mainloop()