from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def square():
	return render_template('index.html', times=3, color='blue')

@app.route('/play/<int:x>')
def times(x):
	return render_template('index.html', times=x, color='blue')

@app.route('/play/<int:x>/<color>')
def color(x, color):
	return render_template('index.html', times=x, color=color)

if __name__ == '__main__':
	app.run(debug=True)