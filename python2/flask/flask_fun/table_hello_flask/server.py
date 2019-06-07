# work in progress

from flask import Flask, render_template
import table
app = Flask(__name__)

@app.route('/')
def users():
	users = [
			User('Ron', 'Gue'),
			User('Cookie', 'Gue'),
			User('Super', 'Man')
		]

	table = UserTable(users)

	print(table.__html__())
	return render_template('index.html', table = table)

if __name__=='__main__':
	app.run(debug=True)