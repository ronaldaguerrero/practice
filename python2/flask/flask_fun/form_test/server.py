from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
	print(request.form)
	form_name = request.form['name']
	form_email = request.form['email']
	return render_template('show.html', temp_name = form_name, temp_email = form_email)

if __name__== '__main__':
	app.run(debug=True)