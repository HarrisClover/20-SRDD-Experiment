'''
This is the main file that ties everything together. It uses the NewsArticle, CredibilityAnalyzer, and ModelTrainer classes to evaluate the credibility of news articles.
'''
from newsarticle import NewsArticle
from credibilityanalyzer import CredibilityAnalyzer
from modeltrainer import ModelTrainer
def main():
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
if __name__ == "__main__":
    main()