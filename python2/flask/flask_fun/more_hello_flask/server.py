from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/lists')
def lists():
	student_info = [
		{'name' : 'Ron', 'age': 29},
		{'name' : 'Cookie', 'age': 7},
		{'name' : 'Batman', 'age': 49}
	]
	return render_template('lists.html', rand_nums = [4,5,9], students = student_info)

if __name__ == '__main__':
	app.run(debug=True)