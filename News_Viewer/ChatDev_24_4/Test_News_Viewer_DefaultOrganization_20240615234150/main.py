'''
This is the main file for the News Viewer application. It sets up the GUI and initializes the application.
'''
import tkinter as tk
from news_viewer import NewsViewer
def main():
    # Replace 'your-api-key' and 'your-sources' with your actual API key and news sources
    root = tk.Tk()
    app = NewsViewer(master=root, api_key='your-api-key', sources=['source1', 'source2', 'source3'])
    app.mainloop()
if __name__ == "__main__":
    main()