from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/')
def index():
	# call the function, passing in the name of our db
    mysql = connectToMySQL('pets_db')
     # call the query_db function, pass in the query as a string
    pets = mysql.query_db('SELECT * FROM pets;')
    return render_template('index.html', all_pets = pets)

@app.route('/add_pet', methods=['POST'])
def add():
	mysql = connectToMySQL('pets_db')
	query = 'INSERT INTO pets (name, type) VALUES (%(name)s, %(type)s);' 
	data = {
	 'name': request.form['name'],
	 'type': request.form['type']
	}
	mysql.query_db(query, data)
	return redirect('/')

if __name__ == '__main__':
	app.run(debug=True)