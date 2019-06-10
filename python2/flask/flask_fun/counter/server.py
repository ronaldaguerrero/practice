from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'not so secret'

@app.route('/')
def index():
	if 'count' in session:
		session['count'] += 1
	else:
		session['count'] =1
	return render_template('index.html', count = session['count'])

@app.route('/plus2')
def plus2():
	session['count'] += 1
	return redirect('/')

@app.route('/destroy_session')
def destroy():
	session['count'] = 0;
	return redirect('/')

if __name__ == '__main__':
	app.run(debug=True)