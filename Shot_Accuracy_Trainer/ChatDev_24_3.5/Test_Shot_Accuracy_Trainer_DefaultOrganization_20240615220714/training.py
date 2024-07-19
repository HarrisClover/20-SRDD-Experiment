'''
This file contains the TrainingSession class that handles the training session.
It tracks shot accuracy, provides real-time feedback, and generates reports.
'''
import random
from tkinter import Tk
class TrainingSession:
    def __init__(self, sport, distance, target_size):
        self.sport = sport
        self.distance = distance
        self.target_size = target_size
        self.shots_taken = 0
        self.shots_scored = 0
    def start(self):
        print(f"Starting {self.sport} training session...")
        print(f"Distance: {self.distance} meters")
        print(f"Target Size: {self.target_size} meters")
        print("Let's begin!")
        while True:
            shot_result = self.take_shot()
            self.shots_taken += 1
            if shot_result:
                self.shots_scored += 1
                print("Goal!")
            else:
                print("Missed!")
            accuracy = self.calculate_accuracy()
            print(f"Accuracy: {accuracy}%")
            choice = input("Press 'q' to quit or any other key to continue: ")
            if choice == 'q':
                break
        self.generate_report()
    def take_shot(self):
        # Simulate shot accuracy based on target size
        success_threshold = self.target_size / self.distance
        return random.random() < success_threshold
    def calculate_accuracy(self):
        return (self.shots_scored / self.shots_taken) * 100
    def generate_report(self):
        print("Training session report:")
        print(f"Sport: {self.sport}")
        print(f"Distance: {self.distance} meters")
        print(f"Target Size: {self.target_size} meters")
        print(f"Shots Taken: {self.shots_taken}")
        print(f"Shots Scored: {self.shots_scored}")
        print(f"Accuracy: {self.calculate_accuracy()}%")