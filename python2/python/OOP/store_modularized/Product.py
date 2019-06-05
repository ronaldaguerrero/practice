class Product:
	def __init__(self, name, price, category):
		self.name = name
		self.price = price
		self.category = category
		self.store = Store(name)

	def update_price(self, percent_change, is_increased):
		if(is_increased == True):
			self.price += (self.price * percent_change) 
		else:
			self.price -= (self.price * percent_change)
		return self

if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)
  