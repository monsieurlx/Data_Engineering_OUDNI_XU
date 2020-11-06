from flask import Flask, render_template
from redis import Redis, RedisError, StrictRedis

app = Flask(__name__)

	
@app.route('/')
def index():
	return render_template("index.html")

@app.route('/', methods=['POST'])
def add_text():
	text = request.form['user_text']
	return text

if __name__ == '__main__':
	redis_client = StrictRedis(host='redis', port=6379)
	app.run(host='0.0.0.0')
