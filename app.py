from flask import Flask, render_template
from redis import Redis, RedisError, StrictRedis
from flask import request
from model_s_analysis import check_sentence_sentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import test_app



app = Flask(__name__)

def sentiment_analyzer_scores(sentence):
	model = SentimentIntensityAnalyzer()
	score = model.polarity_scores(sentence)
	if check_sentence_sentiment(sentence) == 'Pos':
		print('The sentence is Positive')
	elif check_sentence_sentiment(sentence) == 'Neg':
		print('The sentence is Negative')
	else:
		print('The sentence is Neutral')

	score = model.polarity_scores(sentence)
	return "{:-<40} {}".format(sentence,score)
	




@app.route('/', methods=['GET', 'POST'])

def index():
	if request.method == 'POST':
		details = request.form	
		if details['form_type'] == 'submit_sentence':
			return sentiment_analyzer_scores(details['sentence'])
	return render_template('index.html')


def add_text():
	text = request.form['user_text']
	return sentiment_analyzer_scores(text)

if __name__ == '__main__':
	
	app.debug = True
	redis_client = StrictRedis(host='redis', port=5000)
	app.run(host='0.0.0.0')
	#exec(open('test_app.py').read())
	
