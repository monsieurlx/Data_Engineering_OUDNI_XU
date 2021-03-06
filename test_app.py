import unittest
import os
import requests
from model_s_analysis import check_sentence_sentiment


class FlaskTests(unittest.TestCase):

	def setUp(self):
		os.environ['NO_PROXY'] = '0.0.0.0'
		
		
	def tearDown(self):
		pass


	#test if the site respond 
	def test_a_interface(self):
		response = requests.get('http://localhost:5000')
		self.assertEqual(response.status_code,200)

	#test a positive text
	def test_b_sentiment_positive(self):
		text = 'Leo is so GOOD !!!'
		
		
		self.assertEqual(check_sentence_sentiment(text),'Pos')

	#test a negative text
	def test_c_sentiment_negative(self):
		text = 'Leo is so BAD !!!'
		self.assertEqual(check_sentence_sentiment(text),'Neg')

	#test a neutral text
	def test_d_sentiment_neutral(self):
		text = 'My name is Leo'
		self.assertEqual(check_sentence_sentiment(text),'Neutral')


if __name__ == '__main__':
	unittest.main()		
