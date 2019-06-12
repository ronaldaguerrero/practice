from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/users')
def index():
	mysql = connectToMySQL('users')	        # call the function, passing in the name of our db
	users = mysql.query_db('SELECT * FROM users;')
	return render_template('users.html', all_users = users)

@app.route('/users/new')
def form():
	return render_template('add_user.html')

@app.route('/add_user', methods=['POST'])
def add():
	mysql = connectToMySQL('users')
	query = 'INSERT INTO users (name, email) VALUES (%(name)s, %(email)s);'
	data = {
		'name' : request.form['name'],
		'email' : request.form['email']
	}
	mysql.query_db(query, data)
	return redirect('/users')

@app.route('/user/<user_id>')
def show(user_id):
	mysql = connectToMySQL('users')
	query = 'SELECT * FROM users WHERE id = %(id)s;'
	data = {
	 'id': user_id
	}
	this_user = mysql.query_db(query, data)
	return render_template('show.html', user = this_user)

@app.route('/user/<user_id>/edit')
def show_edit(user_id):
	mysql = connectToMySQL('users')
	query = 'SELECT * FROM users WHERE id = %(id)s;'
	data = {
	 'id': user_id
	}
	this_user = mysql.query_db(query, data)
	return	render_template('edit.html', user = this_user)

@app.route('/edit/user/<user_id>', methods=['POST'])
def edit(user_id):
	mysql = connectToMySQL('users')
	query = 'UPDATE users SET name = %(name)s , email = %(email)s WHERE id = %(id)s;'
	data = {
	 'id' : user_id,
	 'name': request.form['name'],
	 'email': request.form['email']
	}
	this_user = mysql.query_db(query, data)
	return redirect('/user/'+str(user_id))

@app.route('/delete/<user_id>')
def delete(user_id):
	mysql = connectToMySQL('users')
	query = 'DELETE FROM users WHERE id = %(id)s;'
	data = {
	 'id': user_id
	}
	this_user = mysql.query_db(query, data)
	return redirect('/users')

if __name__ == '__main__':
	app.run(debug=True)