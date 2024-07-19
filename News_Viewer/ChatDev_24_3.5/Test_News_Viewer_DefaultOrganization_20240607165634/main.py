'''
News Viewer
A simple and user-friendly software application that allows users to view and read news articles from various sources.
'''
import tkinter as tk
from news_api import NewsAPI
class NewsViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("News Viewer")
        self.news_api = NewsAPI()
        self.create_widgets()
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Welcome to News Viewer!")
        self.label.pack()
        self.source_label = tk.Label(self.root, text="Select news source:")
        self.source_label.pack()
        self.source_var = tk.StringVar()
        self.source_dropdown = tk.OptionMenu(self.root, self.source_var, *self.news_api.get_sources())
        self.source_dropdown.pack()
        self.button = tk.Button(self.root, text="Get News", command=self.get_news)
        self.button.pack()
        self.news_text = tk.Text(self.root, height=20, width=80)
        self.news_text.pack()
    def get_news(self):
        source = self.source_var.get()
        news = self.news_api.get_news(source)
        self.news_text.delete(1.0, tk.END)
        self.news_text.insert(tk.END, news)
if __name__ == "__main__":
    root = tk.Tk()
    app = NewsViewerApp(root)
    root.mainloop()