'''
This is the main file of the application. It is responsible for running the application and managing the user interface.
'''
import tkinter as tk
from user import User
from matchmaker import MatchMaker
def main():
    # Create a new instance of the MatchMaker class
    match_maker = MatchMaker()
    # Create the main window
    window = tk.Tk()
    window.title("MatchMaker App")
    # Create the user interface
    username_label = tk.Label(window, text="Username")
    username_label.pack()
    username_entry = tk.Entry(window)
    username_entry.pack()
    interests_label = tk.Label(window, text="Interests (comma separated)")
    interests_label.pack()
    interests_entry = tk.Entry(window)
    interests_entry.pack()
    matches_label = tk.Label(window, text="Your matches will appear here")
    matches_label.pack()
    def update_matches():
        user = User(username_entry.get(), interests_entry.get().split(','))
        match_maker.add_user(user)
        matches = match_maker.get_matches_for(user)
        matches_label.config(text="Your matches: " + matches)
    submit_button = tk.Button(window, text="Submit", command=update_matches)
    submit_button.pack()
    # Start the main loop
    window.mainloop()
if __name__ == "__main__":
    main()