'''
Virus Protector - Main File
'''
import tkinter as tk
from scanner import Scanner
class VirusProtectorApp:
    def __init__(self, master):
        self.master = master
        master.title("Virus Protector")
        self.label = tk.Label(master, text="Welcome to Virus Protector!")
        self.label.pack()
        self.scan_button = tk.Button(master, text="Scan", command=self.scan)
        self.scan_button.pack()
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()
        self.threats_label = tk.Label(master, text="")
        self.threats_label.pack()
    def scan(self):
        scanner = Scanner()
        threats = scanner.scan()
        self.display_results(threats)
    def display_results(self, threats):
        if threats:
            self.threats_label.config(text="Threats found:\n" + "\n".join(threats))
        else:
            self.threats_label.config(text="No threats found.")
root = tk.Tk()
app = VirusProtectorApp(root)
root.mainloop()