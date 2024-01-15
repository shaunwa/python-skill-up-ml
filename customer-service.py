import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

while True:
    next_message = input('Message: ')
    scores = analyzer.polarity_scores(next_message)
    compound = scores['compound']
    if compound > 0.1:
        print('Positive comment!')
    elif compound < -0.1:
        print('Negative Commment!')
    else:
        print('Neutral Comment')