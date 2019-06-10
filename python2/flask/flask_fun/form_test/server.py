from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'not so secret'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
	print(request.form)
	session['name'] = request.form['name']
	session['email'] = request.form['email']
	return redirect('/show')

@app.route('/show')
def show():
	return render_template('show.html', temp_name = session['name'], temp_email = session['email'])

if __name__== '__main__':
	app.run(debug=True)