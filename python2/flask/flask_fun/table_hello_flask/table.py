# import things
from flask_table import Table, Col

# Declare your table
class UserTable(Table):
	fn = Col('First Name')
	ln = Col('Last Name')

class User(object):
	def __init__(self, fn, ln):
		self.fn = fn
		self.ln = ln

