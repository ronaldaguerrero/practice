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

ron = BankAccount(0.05, 200, 'checking')
print('expectout output is 200')
ron.display_account_info('checking')
print('********')

print('expectout output is 1100+')
ron = BankAccount(0.10, 1000, 'saving')
ron.deposit(100, 'saving').yield_interest('saving').display_account_info('saving')






# devon = BankAccount(0.05, 0, 'checking')
# devon.withdraw(100)