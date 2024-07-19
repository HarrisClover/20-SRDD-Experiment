# Scene Change Detection Application User Manual

## Introduction

The Scene Change Detection Application is a software that automatically detects scene changes in a video and provides a timestamp or marker indicating when the change occurred. This user manual provides detailed instructions on how to install the application and how to use it effectively.

## Installation

To install the Scene Change Detection Application, follow the steps below:

1. Ensure that you have Python installed on your system. If not, download and install Python from the official website (https://www.python.org).

2. Clone or download the application code from the GitHub repository: [link to repository].

3. Open a terminal or command prompt and navigate to the directory where you downloaded the application code.

4. Create a virtual environment (optional but recommended) by running the following command:

   ```
   python -m venv venv
   ```

5. Activate the virtual environment by running the appropriate command based on your operating system:

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

7. Once the installation is complete, you are ready to use the Scene Change Detection Application.

## Usage

To use the Scene Change Detection Application, follow the steps below:

1. Open a terminal or command prompt and navigate to the directory where you downloaded the application code.

2. Activate the virtual environment (if you created one) by running the appropriate command as mentioned in the installation steps.

3. Run the following command to start the application:

   ```
   python main.py
   ```

4. The application window will open, displaying the title "Scene Change Detection" and two buttons: "Browse" and "Detect Scene Changes".

5. Click the "Browse" button to select a video file (.mp4, .avi, or .mkv) from your local system.

6. After selecting the video file, click the "Detect Scene Changes" button to start the scene change detection process.

7. The application will analyze the video and display the detected scene changes as timestamps below the buttons.

8. You can repeat the process by clicking the "Browse" button again and selecting a different video file.

9. To exit the application, close the application window or press Ctrl+C in the terminal or command prompt.

## Troubleshooting

If you encounter any issues while installing or using the Scene Change Detection Application, please try the following troubleshooting steps:

1. Make sure you have installed all the required dependencies mentioned in the requirements.txt file.

2. Ensure that the video file you are trying to analyze is in a supported format (.mp4, .avi, or .mkv).

3. Check if the video file is accessible and not corrupted.

4. If the application crashes or freezes during the scene change detection process, try using a different video file or contact our support team for assistance.

## Conclusion

Congratulations! You have successfully installed and learned how to use the Scene Change Detection Application. This software will help you automatically detect scene changes in videos and provide timestamps or markers indicating when the changes occurred. If you have any further questions or need assistance, please don't hesitate to contact our support team.