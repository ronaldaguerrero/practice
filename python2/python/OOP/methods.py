
class User:
	def __init__(self, username, email_address):
		self.name = username
		self.email = email_address
		self.account_balance = 0

	def make_deposit(self, amount):
		self.account_balance += amount

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50
