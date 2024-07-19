'''
News API
A class that interacts with the news API to fetch news articles.
'''
import requests
import configparser
class NewsAPI:
    def __init__(self):
        try:
            config = configparser.ConfigParser()
            config.read('config.ini')
            self.api_key = config.get('API', 'api_key')
            self.base_url = "https://newsapi.org/v2"
        except Exception as e:
            print("Error loading configuration file:", str(e))
            # Handle the error gracefully, e.g., show an error message to the user
    def get_sources(self):
        try:
            url = f"{self.base_url}/sources?apiKey={self.api_key}"
            response = requests.get(url)
            sources = []
            if response.status_code == 200:
                data = response.json()
                sources = [source['name'] for source in data['sources']]
            return sources
        except Exception as e:
            print("Error fetching news sources:", str(e))
            # Handle the error gracefully, e.g., show an error message to the user
    def get_news(self, source):
        try:
            url = f"{self.base_url}/top-headlines?sources={source}&apiKey={self.api_key}"
            response = requests.get(url)
            news = ""
            if response.status_code == 200:
                data = response.json()
                articles = data['articles']
                for article in articles:
                    title = article['title']
                    description = article['description']
                    news += f"{title}\n{description}\n\n"
            return news
        except Exception as e:
            print("Error fetching news:", str(e))
            # Handle the error gracefully, e.g., show an error message to the user