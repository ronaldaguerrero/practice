
# add additional parameters
class User:
	def __init__(self, username, email_address):
		self.name = username
		self.email = email_address
		self.account_balance = 0

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python
