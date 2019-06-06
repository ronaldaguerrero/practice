from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', times=4)

@app.route('/<int:x>')
def times(x):
	x = int(x/2)
	return render_template('index.html', times=x)

if __name__ == '__main__':
	app.run(debug=True)