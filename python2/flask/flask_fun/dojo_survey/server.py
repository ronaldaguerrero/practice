from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
	form_name = request.form['name']
	form_loc = request.form['loc']
	form_lang = request.form['lang']
	form_com = request.form['comment']
	form_team = request.form['team']
	form_grad = request.form['grad']
	return render_template('result.html', name=form_name, loc=form_loc, lang=form_lang, com = form_com, team = form_team, grad = form_grad)


if __name__=='__main__':
	app.run(debug=True)