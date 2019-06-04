class User:
	def __init__(self):
		self.name = 'Ron G'
		self.email = 'ronald.a.guerrero@gmail.com'
		self.account_balance = 0

guido = User()
monty = User()

#access instance attributes

print(guido.name)
print(monty.email)

#set instance attributes

guido.name = "Guido"
monty.email = "Monty@email.com"

print(guido.name)
print(monty.email)

