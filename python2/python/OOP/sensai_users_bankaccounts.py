# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

class BankAccount:
	def __init__(self, int_rate, balance, acct_type):
		self.interest_rate = int_rate
		self.account_type = acct_type
		if(acct_type == 'checking'):
			self.checking_bal = balance
		if(acct_type == 'saving'):
			self.saving_bal = balance

	def deposit(self, amount, acct_type): #- increases the account balance by the given amount
		if(acct_type == 'saving'):	
			self.saving_bal += amount
		if(acct_type == 'checking'):
			self.checking_bal += amount
		return self

	def withdraw(self, amount, acct_type): # - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
		if(acct_type == 'saving'):
			if (self.saving_bal - amount < 0):
				self.saving_bal -= 5
				print('Insufficient funds: Charging a $5 fee')
				return self
			else:
				self.saving_bal -= amount
				return self
		if(acct_type == 'checking'):
			if (self.checking_bal - amount < 0):
				self.checking_bal -= 5
				print('checking_bal funds: Charging a $5 fee')
				return self
			else:
				self.checking_bal -= amount
				return self

	def display_account_info(self, acct_type): # - print to the console: eg. "Balance: $100"
		if(acct_type == 'saving'):
			print(self.saving_bal, self.interest_rate)
		if(acct_type == 'checking'):
			print(self.checking_bal, self.interest_rate)
		return self

	def yield_interest(self, acct_type): #- increases the account balance by the current balance * the interest rate (as long as the balance is positive)
		if(acct_type == 'saving'):
			if (self.saving_bal > 0):
				self.saving_bal += (self.interest_rate * self.saving_bal)
				return self
			else:
				print('Insufficient funds: account balance is 0')
		if(acct_type == 'checking'):
			if (self.checking_bal > 0):
				self.checking_bal += (self.interest_rate * self.checking_bal)
				return self
			else:
				print('Insufficient funds: account balance is 0')

class User:
	def __init__(self, username, email_address, a_type):
		self.name = username
		self.email = email_address
		self.account = BankAccount(int_rate=0.02, balance=0, acct_type=a_type)	# added this line

	def make_deposit(self, amount, acct_type):
		self.account.deposit(amount, acct_type)
		return self

	def make_withdrawal(self, amount, acct_type):
		self.account.withdraw(amount, acct_type)
		return self

	def display_user_balance(self, acct_type):
		if(acct_type == 'saving'):
			print(self.name, self.account.saving_bal)
		if(acct_type == 'checking'):
			print(self.name, self.account.checking_bal)
		return self

	def transfer_money(self, other_user, amount, acct_type):
		self.account.withdraw(amount, acct_type)
		other_user.account.deposit(amount, acct_type)
		return self

guido = User("Guido van Rossum", "guido@python.com", 'checking')
monty = User("Monty Python", "monty@python.com", 'saving')

guido.make_deposit(100,'checking').make_deposit(200,'checking')

monty.make_deposit(50,'saving')

print('*************')
print('guido acct bal, below should be 300')
guido.display_user_balance('checking')	

print('*************')
print('monty acct bal, below should be 50 ')
monty.display_user_balance('saving')

print('*************')
print('output should be 100')
guido.make_withdrawal(200, 'checking').display_user_balance('checking')



