'''
SecureGuardGUI - Graphical User Interface
This file contains the SecureGuardGUI class, which is responsible for the graphical user interface of the SecureGuard application.
Author: Programmer
'''
import tkinter as tk
from tkinter import messagebox
class SecureGuardGUI:
    def __init__(self, scanner, firewall, password_manager):
        self.scanner = scanner
        self.firewall = firewall
        self.password_manager = password_manager
        # Create the main window
        self.root = tk.Tk()
        self.root.title("SecureGuard")
        self.root.geometry("800x600")
        # Create the menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        # Create the file menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        # Create the scan button
        self.scan_button = tk.Button(self.root, text="Scan", command=self.scan)
        self.scan_button.pack()
    def run(self):
        self.root.mainloop()
    def scan(self):
        threats_detected = self.scanner.scan()
        if threats_detected:
            messagebox.showinfo("Threats Detected", "Threats detected!")
        else:
            messagebox.showinfo("No Threats", "No threats detected.")