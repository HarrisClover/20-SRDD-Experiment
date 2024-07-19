# ChatDev News Credibility Analyzer

## Introduction

The ChatDev News Credibility Analyzer is a software tool designed to evaluate the credibility of news articles by analyzing multiple factors and generating trustworthiness scores with explanations and evidence. This user manual will guide you through the installation process, explain the main functions of the software, and provide instructions on how to use it effectively.

## Installation

To install the ChatDev News Credibility Analyzer, please follow these steps:

1. Ensure that you have Python installed on your system. If not, you can download it from the official Python website (https://www.python.org/downloads/).

2. Clone the ChatDev News Credibility Analyzer repository from GitHub using the following command:

   ```
   git clone https://github.com/ChatDev/News-Credibility-Analyzer.git
   ```

3. Navigate to the project directory:

   ```
   cd News-Credibility-Analyzer
   ```

4. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

5. Once the installation is complete, you are ready to use the ChatDev News Credibility Analyzer.

## Main Functions

The ChatDev News Credibility Analyzer provides the following main functions:

1. Evaluate Credibility: This function allows you to evaluate the credibility of a news article. To use this function, follow these steps:

   - Create an instance of the `Article` class by providing the file path of the news article as a parameter.

     ```python
     from article import Article

     article = Article("path/to/article.txt")
     ```

   - Call the `evaluate_credibility` method of the `Article` instance to get the credibility score, explanation, and evidence.

     ```python
     credibility_score, explanation, evidence = article.evaluate_credibility()
     ```

2. Calculate Credibility Score: This function calculates the credibility score of a news article based on various factors. To use this function, follow these steps:

   - Create an instance of the `Article` class by providing the file path of the news article as a parameter.

     ```python
     from article import Article

     article = Article("path/to/article.txt")
     ```

   - Call the `calculate_credibility_score` method of the `Article` instance to get the credibility score.

     ```python
     credibility_score = article.calculate_credibility_score()
     ```

3. Generate Explanation: This function generates an explanation for the credibility score of a news article. To use this function, follow these steps:

   - Create an instance of the `Article` class by providing the file path of the news article as a parameter.

     ```python
     from article import Article

     article = Article("path/to/article.txt")
     ```

   - Call the `generate_explanation` method of the `Article` instance to get the explanation.

     ```python
     explanation = article.generate_explanation()
     ```

4. Generate Evidence: This function generates evidence to support the credibility score of a news article. To use this function, follow these steps:

   - Create an instance of the `Article` class by providing the file path of the news article as a parameter.

     ```python
     from article import Article

     article = Article("path/to/article.txt")
     ```

   - Call the `generate_evidence` method of the `Article` instance to get the evidence.

     ```python
     evidence = article.generate_evidence()
     ```

## Conclusion

The ChatDev News Credibility Analyzer is a powerful tool for evaluating the credibility of news articles. By analyzing multiple factors and generating trustworthiness scores with explanations and evidence, it helps users make informed decisions about the reliability of the information they consume. Follow the installation instructions and explore the main functions to start using the software effectively. If you have any questions or need further assistance, please don't hesitate to reach out to our support team.