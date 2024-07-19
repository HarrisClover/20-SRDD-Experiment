'''
This file contains the NewsViewer class, which is responsible for fetching and displaying the news.
'''
import tkinter as tk
import requests
import tkinter.messagebox as messagebox
class NewsViewer(tk.Frame):
    def __init__(self, master=None, api_key=None, sources=None):
        super().__init__(master)
        self.master = master
        self.api_key = api_key
        self.sources = sources
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.news_listbox = tk.Listbox(self)
        self.news_listbox.pack(side="top", fill="both", expand=True)
        self.news_listbox.bind('<<ListboxSelect>>', self.on_select)
        self.refresh_button = tk.Button(self)
        self.refresh_button["text"] = "Refresh"
        self.refresh_button["command"] = self.update_news
        self.refresh_button.pack(side="bottom")
    def update_news(self):
        self.articles = []
        for source in self.sources:
            response = requests.get(f'https://newsapi.org/v2/top-headlines?sources={source}&apiKey={self.api_key}')
            data = response.json()
            self.articles.extend(data['articles'])
        self.news_listbox.delete(0, 'end')
        for article in self.articles:
            self.news_listbox.insert('end', article['title'])
    def on_select(self, event):
        selected_index = self.news_listbox.curselection()[0]
        selected_article = self.articles[selected_index]
        messagebox.showinfo("Article", selected_article['content'])