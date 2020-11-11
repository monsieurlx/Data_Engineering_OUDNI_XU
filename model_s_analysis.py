from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def create_model():
	return SentimentIntensityAnalyzer()

def check_sentence_sentiment(text):
	# This function will check if a text is Positive, Negative or Neutral
	if model.polarity_scores(text)['pos'] > 0.5:
		return 'Pos'

	elif model.polarity_scores(text)['neg'] > 0.5:
		return 'Neg'

	else:
		return 'Neutral'


if __name__ == "__main__":
    text = input("Write a sentence:\n")
    score(text)

