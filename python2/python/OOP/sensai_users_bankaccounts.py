# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

class BankAccount:
	def __init__(self, int_rate, balance):
		self.interest_rate = int_rate
		self.account_balance = balance

	def deposit(self, amount): #- increases the account balance by the given amount
		self.account_balance += amount
		return self

	def withdraw(self, amount): # - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
		if (self.account_balance - amount < 0):
			self.account_balance -= 5
			print('Insufficient funds: Charging a $5 fee')
			return self
		else:
			self.account_balance -= amount
			return self

	def display_account_info(self): # - print to the console: eg. "Balance: $100"
		print(self.account_balance, self.interest_rate)
		return self

	def yield_interest(self): #- increases the account balance by the current balance * the interest rate (as long as the balance is positive)
		if (self.account_balance > 0):
			self.account_balance += (self.interest_rate * self.account_balance)
			return self
		else:
			print('Insufficient funds: account balance is 0')

ron = BankAccount(0.05, 100)
ron.deposit(100).withdraw(50).yield_interest().display_account_info()

devon = BankAccount(0.05, 0)
devon.withdraw(100)

class User:
	def __init__(self, username, email_address):
		self.name = username
		self.email = email_address
		self.account = BankAccount(int_rate=0.02, balance=0)	# added this line

	def make_deposit(self, amount):
		self.account.deposit(amount)
		return self

	def make_withdrawal(self, amount):
		self.account.withdraw(amount)
		return self

	def display_user_balance(self):
		print(self.name, self.account.account_balance)
		return self

	def transfer_money(self, other_user, amount):
		self.account.withdraw(amount)
		other_user.account.deposit(amount)
		return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

guido.make_deposit(100).make_deposit(200)

monty.make_deposit(50)

print('*************')
print('guido acct bal, below should be 300')
guido.display_user_balance()	

print('*************')
print('monty acct bal, below should be 50 ')
monty.display_user_balance()

print('*************')
print('output should be 100')
guido.make_withdrawal(200).display_user_balance()

print('*************')
print('output should be 25')
monty.transfer_money(guido, 25).display_user_balance()


