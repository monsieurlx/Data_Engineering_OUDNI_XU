from flask import Flask, render_template
from redis import Redis, RedisError, StrictRedis
from flask import request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
model = SentimentIntensityAnalyzer()


app = Flask(__name__)

def sentiment_analyzer_scores(sentence):
	score = model.polarity_scores(sentence)
	return "{:-<40} {}".format(sentence,score)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/', methods=['POST'])
def add_text():
	text = request.form['user_text']
	return sentiment_analyzer_scores(text)

if __name__ == '__main__':
	app.debug = True
	redis_client = StrictRedis(host='redis', port=5000)
	app.run(host='0.0.0.0')
	
