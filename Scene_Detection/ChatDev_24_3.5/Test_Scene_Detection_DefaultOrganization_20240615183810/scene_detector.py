'''
This file contains the SceneDetector class responsible for detecting scene changes in a video.
'''
import cv2
class SceneDetector:
    def __init__(self, video_file):
        self.video_file = video_file
    def detect(self):
        scene_changes = []
        cap = cv2.VideoCapture(self.video_file)
        if not cap.isOpened():
            raise Exception("Error opening video file.")
        prev_frame = None
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            if prev_frame is not None:
                frame_diff = cv2.absdiff(gray_frame, prev_frame)
                _, threshold = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)
                contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                if len(contours) > 0:
                    scene_changes.append(cap.get(cv2.CAP_PROP_POS_MSEC) / 1000)
            prev_frame = gray_frame
        cap.release()
        return scene_changes