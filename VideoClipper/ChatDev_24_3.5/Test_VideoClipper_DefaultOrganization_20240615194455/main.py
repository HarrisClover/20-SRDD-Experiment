'''
VideoClipper is a software application that allows users to easily clip and trim videos.
It provides an intuitive interface to select specific sections of the video, and saves the trimmed video as a new file.
'''
from video_clipper_gui import VideoClipperGUI
def main():
    # Create an instance of the VideoClipperGUI class
    video_clipper_gui = VideoClipperGUI()
    # Run the application
    video_clipper_gui.run()
if __name__ == "__main__":
    main()