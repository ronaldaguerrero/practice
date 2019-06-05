from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/dojo')
def dojo():
	return 'Dojo!'

@app.route('/say/flask')
def flask():
	return 'Hi Flask'

@app.route('/say/michael')
def michael():
	return 'Hi Michael!'

@app.route('/say/john')
def john():
	return 'Hi John!'

@app.route('/say/<int:n>')
def number(n):
	return 'My number is %d' % n

@app.route('/repeat/<int:n>/hello')
def re_hello(n):
	return 'hello ' * n

@app.route('/repeat/<int:n>/bye')
def re_bye(n):
	return 'bye ' * n

@app.route('/repeat/<int:n>/dogs')
def re_dogs(n):
	return 'dogs ' * n

if __name__=='__main__':
	app.run(debug=True)