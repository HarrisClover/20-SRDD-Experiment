'''
This is the main file of the Business Analytics software application.
'''
import tkinter as tk
from dashboard import Dashboard
def main():
    # Create the main window
    root = tk.Tk()
    root.title("Business Analytics")
    # Create an instance of the Dashboard class
    dashboard = Dashboard(root)
    # Start the main event loop
    dashboard.start()
if __name__ == "__main__":
    main()