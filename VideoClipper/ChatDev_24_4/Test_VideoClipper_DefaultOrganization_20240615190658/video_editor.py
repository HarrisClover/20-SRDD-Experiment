'''
This file contains the VideoEditor class, which is responsible for loading, clipping, and saving videos.
'''
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
class VideoEditor:
    def __init__(self):
        self.video_path = None
        self.start_time = 0
        self.end_time = None
    def load_video(self, video_path):
        _, ext = os.path.splitext(video_path)
        if ext.lower() not in ['.mp4', '.avi', '.mov']:  # add more video file extensions as needed
            raise ValueError("Invalid video file")
        self.video_path = video_path
    def set_clip_time(self, start_time, end_time):
        if start_time >= end_time or start_time < 0 or end_time > self.get_video_duration():
            raise ValueError("Invalid start or end time")
        self.start_time = start_time
        self.end_time = end_time
    def save_video(self, output_path):
        if self.end_time is None:
            self.end_time = self.get_video_duration()
        ffmpeg_extract_subclip(self.video_path, self.start_time, self.end_time, targetname=output_path)
    def get_video_duration(self):
        video = VideoFileClip(self.video_path)
        return video.duration