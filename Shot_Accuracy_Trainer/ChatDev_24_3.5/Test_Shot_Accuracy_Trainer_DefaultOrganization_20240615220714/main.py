'''
This is the main file of the software application.
It provides the user interface and handles user inputs.
'''
from tkinter import Tk, Label, Button, Entry, OptionMenu, StringVar
from training import TrainingSession
class ShotAccuracyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shot Accuracy App")
        self.sport_label = Label(root, text="Select Sport:")
        self.sport_label.pack()
        self.sport_var = StringVar(root)
        self.sport_var.set("Basketball")  # default sport
        self.sport_menu = OptionMenu(root, self.sport_var, "Basketball", "Soccer", "Tennis")
        self.sport_menu.pack()
        self.distance_label = Label(root, text="Enter Distance (in meters):")
        self.distance_label.pack()
        self.distance_entry = Entry(root)
        self.distance_entry.pack()
        self.target_label = Label(root, text="Enter Target Size (in meters):")
        self.target_label.pack()
        self.target_entry = Entry(root)
        self.target_entry.pack()
        self.start_button = Button(root, text="Start Training", command=self.start_training)
        self.start_button.pack()
    def start_training(self):
        sport = self.sport_var.get()
        distance = float(self.distance_entry.get())
        target_size = float(self.target_entry.get())
        training_session = TrainingSession(sport, distance, target_size)
        training_session.start()
root = Tk()
app = ShotAccuracyApp(root)
root.mainloop()