'''
This is the main file of the social networking software application.
'''
from tkinter import Tk, Label, Button
from database import Database
from user import User
class SocialNetworkApp:
    def __init__(self, master):
        self.master = master
        master.title("Social Network App")
        self.label = Label(master, text="Welcome to the Social Network App!")
        self.label.pack()
        self.button = Button(master, text="Find Potential Partners", command=self.find_partners)
        self.button.pack()
        self.database = Database()  # Create an instance of the Database class
    def find_partners(self):
        # Logic to find and display potential partners based on shared interests and compatibility
        user_id = 1  # Assuming the user ID is 1 for simplicity
        potential_partners = self.database.get_potential_partners(user_id)
        if len(potential_partners) > 0:
            print("Potential Partners:")
            for partner in potential_partners:
                print(partner)
        else:
            print("No potential partners found.")
root = Tk()
app = SocialNetworkApp(root)
root.mainloop()