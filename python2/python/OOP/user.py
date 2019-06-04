# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance


class User:
	def __init__(self, username, email_address):
		self.name = username
		self.email = email_address
		self.account_balance = 0

	def make_deposit(self, amount):
		self.account_balance += amount
		return self

	def make_withdrawal(self, amount):
		self.account_balance -= amount
		return self

	def display_user_balance(self):
		print(self.name, self.account_balance)
		return self

	def transfer_money(self, other_user, amount):
		self.account_balance -= amount
		other_user.account_balance += amount
		return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

guido.make_deposit(100).make_deposit(200)

monty.make_deposit(50)
print('guido acct bal ', guido.account_balance)	# output: 300
print('monty acct bal ', monty.account_balance)	# output: 50

print('output should be 100')
guido.make_withdrawal(200).display_user_balance()

print('*************')
print('output should be 25')
monty.transfer_money(guido, 25).display_user_balance()


