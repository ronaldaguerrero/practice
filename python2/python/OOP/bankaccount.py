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