from flask import Flask, render_template, request
import requests

from horoscope.crawler.crawler_horoscope import get_horoscope

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
	sign = request.form['query']
	horoscope = get_horoscope(sign)
	if not horoscope:
		return '404'

	return horoscope


if __name__ == '__main__':
	app.run()	


#o flask eh como se fosse uma ponte que conecta duas coisas diferentes: o html e
#a linguagem python

