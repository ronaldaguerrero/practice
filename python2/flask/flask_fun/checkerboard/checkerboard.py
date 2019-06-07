from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', times=4, col1='black', col2='red')

@app.route('/<int:x>')
def times(x):
	x = int(x/2)
	return render_template('index.html', times=x, y=4,col1='black', col2='red')

@app.route('/<int:x>/<int:y>')
def rows(x,y):
	x = int(x/2)
	y = int(y/2)
	return render_template('index.html', times=x, y=y, col1='black', col2='red')

@app.route('/<int:x>/<int:y>/<col1>/<col2>')
def colors(x,y,col1,col2):
	x = int(x/2)
	y = int(y/2)
	return render_template('index.html', times=x, y=y, col1=col1, col2=col2)

if __name__ == '__main__':
	app.run(debug=True)