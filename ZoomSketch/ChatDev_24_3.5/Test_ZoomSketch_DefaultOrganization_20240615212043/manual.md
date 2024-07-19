# Real-time Collaborative Sketching Software User Manual

## Introduction

The Real-time Collaborative Sketching Software is a Python-based application that allows multiple users to draw together on a shared canvas in real-time. This user manual provides detailed instructions on how to install the necessary dependencies and how to use the software effectively.

## Installation

To install the Real-time Collaborative Sketching Software, follow these steps:

1. Make sure you have Python installed on your system. If not, download and install Python from the official website (https://www.python.org).

2. Clone or download the project files from the repository.

3. Open a terminal or command prompt and navigate to the project directory.

4. Create a virtual environment (optional but recommended) by running the following command:

   ```
   python -m venv venv
   ```

5. Activate the virtual environment by running the appropriate command for your operating system:

   - For Windows:

     ```
     venv\Scripts\activate
     ```

   - For macOS/Linux:

     ```
     source venv/bin/activate
     ```

6. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

7. Once the installation is complete, you are ready to use the Real-time Collaborative Sketching Software.

## Usage

To use the Real-time Collaborative Sketching Software, follow these steps:

1. Open a terminal or command prompt and navigate to the project directory.

2. Activate the virtual environment (if you created one) by running the appropriate command as mentioned in the installation steps.

3. Run the main.py file using the following command:

   ```
   python main.py
   ```

4. The application window will open, displaying the shared canvas.

5. Share the IP address and port number (e.g., localhost:5000) with other users who want to join the collaborative session.

6. Other users can run the main.py file on their systems and enter the shared IP address and port number when prompted.

7. Once connected, all users can start drawing on the canvas simultaneously. The changes made by one user will be reflected in real-time on the canvas of all connected users.

8. To exit the application, simply close the application window.

## Features

The Real-time Collaborative Sketching Software offers the following features:

- Real-time collaboration: Multiple users can draw together on a shared canvas in real-time.

- Simultaneous drawing: Changes made by one user are immediately reflected on the canvas of all connected users.

- Basic drawing tools: The software provides basic drawing tools such as mouse down and mouse drag events to create ovals on the canvas.

## Troubleshooting

If you encounter any issues while installing or using the Real-time Collaborative Sketching Software, try the following troubleshooting steps:

1. Make sure you have installed all the required dependencies mentioned in the requirements.txt file.

2. Check your internet connection to ensure that you can establish a connection with other users.

3. Verify that the IP address and port number used for connection are correct and accessible by all users.

4. If you are using a firewall or antivirus software, make sure it is not blocking the application's network communication.

5. If the application crashes or freezes, try restarting it and check for any error messages in the terminal or command prompt.

If the issue persists, please contact our support team for further assistance.

## Conclusion

The Real-time Collaborative Sketching Software provides a seamless and interactive platform for multiple users to draw together in real-time. By following the installation and usage instructions provided in this user manual, you can easily set up and use the software to collaborate with others on creative projects. Enjoy sketching together!