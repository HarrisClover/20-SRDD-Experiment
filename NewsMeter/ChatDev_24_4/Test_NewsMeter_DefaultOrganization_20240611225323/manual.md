manual.md

```
# News Credibility Analyzer

A Python application for evaluating the credibility of news articles by analyzing multiple factors and generating trustworthiness scores with explanations and evidence.

## Quick Install

Before running the application, you need to install the required Python packages. You can do this by running the following command in your terminal:

`pip install -r requirements.txt`

This will install the following packages:

- nltk==3.5
- numpy==1.21.2
- pandas==1.3.3
- scikit-learn==0.24.2

## What is this?

This application uses machine learning to evaluate the credibility of news articles. It uses a dataset of news articles and their credibility scores to train a model, which is then used to predict the credibility of new articles.

The application consists of four main components:

- NewsArticle: This class is used to represent a news article. It has methods to clean the text and extract features.
- CredibilityAnalyzer: This class takes a NewsArticle object and uses a trained model to predict the credibility score.
- ModelTrainer: This class is used to train the ML model using a dataset of news articles and their credibility scores.
- main.py: This is the main file that ties everything together. It uses the NewsArticle, CredibilityAnalyzer, and ModelTrainer classes to evaluate the credibility of news articles.

## How to use it?

1. Prepare your dataset: The application requires a dataset of news articles and their credibility scores in a CSV format. The last column should contain the credibility scores.

2. Train the model: Run the `main.py` file to train the model. This will print the accuracy of the model on the console.

3. Evaluate the credibility of a news article: To evaluate the credibility of a news article, you need to create a text file containing the text of the article. Then, you can modify the `main.py` file to load this text file and print the credibility score.

Here is an example of how to use the application:

```python
# Load the dataset
dataset = load_dataset('dataset.csv')
# Train the model
trainer = ModelTrainer(dataset)
model, vectorizer = trainer.train()
# Load the news article
article = NewsArticle('article.txt')
# Get the text of the article
text = article.text
# Convert it into a matrix of TF-IDF features
features = vectorizer.transform([text])
# Analyze the credibility
analyzer = CredibilityAnalyzer(model)
score = analyzer.analyze(features)
print(f'The credibility score of the article is: {score}')
```

Please note that the application is still in development and may not always provide accurate results. Always use your judgment when evaluating the credibility of news articles.
```