from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/success')
def success():
	return 'success'

@app.route('/hello/<name>')
def hello(name):
	print(name)
	return 'Hello, ' + name

@app.route('/users/<sn>/<id>')
def show(sn, id):
	print(sn)
	print(id)
	return 'username: ' + sn + ', id: ' + id

if __name__=='__main__':
	app.run(debug=True)