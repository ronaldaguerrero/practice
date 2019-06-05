class Store:
	def __init__(self, name):
		self.name = name
		self.list = []

	def add_product(self, new_product):
		self.list.append(new_product)
		return self

	def sell_product(self, id):
		self.list.pop(id)
		return self

	def inflation(self,percent_increase):
		for i in range(len(self.list)):
			eval(self.list[i]).update_price(percent_increase, True)
		return self

	def set_clearance(self, category, percent_discount):
		for i in range(len(self.list)):
			if(eval(self.list[i]).category == category):
				eval(self.list[i]).update_price(percent_discount, False)
		return self

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

Target = Store('Target')

Mac = Product('Mac', 1000, 'computer')

Target.add_product('Mac')

iPhone = Product('iPhone', 500, 'cell')

Target.add_product('iPhone')

# iPhone.update_price(0.10, True)

Target.set_clearance('cell', 0.10);

print('price is 450')
print(iPhone.price)

Target.print_info()
