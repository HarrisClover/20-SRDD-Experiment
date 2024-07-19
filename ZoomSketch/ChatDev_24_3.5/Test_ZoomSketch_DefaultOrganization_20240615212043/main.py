'''
main.py
This is the main file that initializes the application and handles the communication between clients.
Usage:
    python main.py
'''
import tkinter as tk
from canvas import Canvas
import socket
import threading
class App:
    def __init__(self, root):
        self.root = root
        self.canvas = Canvas(root)
        self.canvas.pack()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(("localhost", 5000))
        self.server_socket.listen(5)  # Allow up to 5 client connections
        self.client_sockets = []
        self.lock = threading.Lock()
        self.receive_thread = threading.Thread(target=self.receive_data)
        self.receive_thread.start()
    def receive_data(self):
        while True:
            with self.lock:
                for client_socket in self.client_sockets:
                    data = client_socket.recv(1024).decode()
                    if not data:
                        client_socket.close()
                        self.client_sockets.remove(client_socket)
                        break
                    self.canvas.process_data(data)
    def accept_connections(self):
        while True:
            client_socket, _ = self.server_socket.accept()
            self.client_sockets.append(client_socket)
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    accept_thread = threading.Thread(target=app.accept_connections)
    accept_thread.start()
    root.mainloop()