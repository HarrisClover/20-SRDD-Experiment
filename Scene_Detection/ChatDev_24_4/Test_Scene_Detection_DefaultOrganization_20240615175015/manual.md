manual.md

```
# Scene Change Detector

Automatically detects scene changes in a video and provides a timestamp or marker indicating when the change occurred.

## Quick Install

This application requires Python and OpenCV. If you don't have Python installed, you can download it from the official website: https://www.python.org/downloads/

To install OpenCV, you can use pip, which is a package manager for Python. Open your terminal and type the following command:

`pip install opencv-python`

## 🤔 What is this?

Scene Change Detector is a Python application that uses OpenCV to analyze a video and detect scene changes. It calculates the Bhattacharyya distance between the histograms of a group of frames and its subsequent group. If the distance exceeds a certain threshold, it considers that a scene change has occurred and records the timestamp.

## 📖 Documentation

### How to use it?

1. Run the main.py file in your Python environment. You can do this by navigating to the directory where the file is located using the terminal and typing `python main.py`.

2. The application will ask you to enter the path of the video. Type the full path of the video file you want to analyze and press Enter.

3. The application will start analyzing the video. This process may take a while depending on the length of the video.

4. Once the analysis is complete, the application will print the timestamps of the detected scene changes.

### Customizing the detection

You can customize the scene detection by modifying the `threshold` and `window_size` parameters in the `detect_scene_change` function:

- `threshold`: This is the Bhattacharyya distance threshold above which a scene change is considered to have occurred. The default value is 0.3. Increase this value to make the detection less sensitive, or decrease it to make it more sensitive.

- `window_size`: This is the number of frames that are compared at a time. The default value is 10. Increase this value to consider a larger group of frames, which may result in more accurate detection but slower processing.

```