'''
This is the main file for the scene detection application. It uses OpenCV to read video frames and calculate the Bhattacharyya distance between the histograms of a group of frames and its subsequent group. If the distance exceeds a certain threshold, it considers that a scene change has occurred and records the timestamp.
'''
try:
    import cv2
except ModuleNotFoundError:
    import os
    os.system('pip install opencv-python')
import numpy as np
from datetime import timedelta
def calculate_difference(frame1, frame2):
    '''
    Calculate the Bhattacharyya distance between the histograms of two frames
    '''
    channels = cv2.split(frame1)
    channels2 = cv2.split(frame2)
    bhatta_dist = 0
    for chan1, chan2 in zip(channels, channels2):
        hist1 = cv2.calcHist([chan1],[0],None,[256],[0,256])
        hist2 = cv2.calcHist([chan2],[0],None,[256],[0,256])
        bhatta_dist += cv2.compareHist(hist1, hist2, cv2.HISTCMP_BHATTACHARYYA)
    return bhatta_dist / 3
def detect_scene_change(video_path, threshold=0.3, window_size=10):
    '''
    Detect scene changes in a video using a sliding window approach
    '''
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    ret, frame1 = cap.read()
    scene_changes = []
    frame_count = 0
    frame_buffer = [frame1]
    while cap.isOpened():
        ret, frame2 = cap.read()
        if not ret:
            break
        frame_buffer.append(frame2)
        if len(frame_buffer) > window_size:
            frame_buffer.pop(0)
        diff = calculate_difference(frame_buffer[0], frame_buffer[-1])
        if diff > threshold:
            timestamp = timedelta(seconds=(frame_count / fps))
            scene_changes.append(str(timestamp))
        frame_count += 1
    cap.release()
    return scene_changes
if __name__ == "__main__":
    video_path = input("Enter the path of the video: ")
    scene_changes = detect_scene_change(video_path)
    print("Scene changes occurred at the following timestamps:")
    for timestamp in scene_changes:
        print(timestamp)