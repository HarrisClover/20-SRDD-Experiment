'''
This file contains the NewsArticle class. This class is used to represent a news article. It has methods to clean the text and extract features.
'''
import nltk
from nltk.corpus import stopwords
import string
import os
class NewsArticle:
    def __init__(self, file_path):
        self.text = self.load_text(file_path)
    def load_text(self, file_path):
        # Load the text of the news article from the file
        with open(file_path, 'r') as file:
            text = file.read().replace('\n', '')
        return text
    def clean_text(self, text):
        # Remove punctuation
        text = "".join([word.lower() for word in text if word not in string.punctuation])
        # Tokenize the text
        tokens = nltk.word_tokenize(text)
        # Remove stopwords
        text = [word for word in tokens if word not in stopwords.words('english')]
        return text
    def extract_features(self):
        # Return the raw text
        return self.text