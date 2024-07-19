'''
This file contains the ModelTrainer class. This class is used to train the ML model using a dataset of news articles and their credibility scores.
'''
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
class ModelTrainer:
    def __init__(self, dataset):
        self.dataset = pd.read_csv(dataset)
        self.scaler = StandardScaler()
        self.vectorizer = TfidfVectorizer()
    def train(self):
        # Split the dataset into features and labels
        X = self.dataset.iloc[:, :-1]
        y = self.dataset.iloc[:, -1]
        # Fit the vectorizer and transform the features
        X = self.vectorizer.fit_transform(X)
        # Scale the features
        X = self.scaler.fit_transform(X)
        # Split the dataset into training set and test set
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        # Train the model using the training set
        model = RandomForestClassifier(n_estimators=100)
        model.fit(X_train, y_train)
        # Evaluate the model using the test set
        accuracy = model.score(X_test, y_test)
        print(f'The accuracy of the model is: {accuracy*100}%')
        return model, self.vectorizer