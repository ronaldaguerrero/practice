from flask import Flask, render_template
from table import Table
app = Flask(__name__)

print(table.__html__())

@app.route('/')
def users():
	users = [
			User('Ron', 'Gue'),
			User('Cookie', 'Gue'),
			User('Super', 'Man')
		]
	table = UserTable(users)
	print(table.__html__())
	return render_template('users.html', table = table)

if __name__ == '__main__':
	app.run(debug=True)