from Product import Product

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

print(__name__)

target = Store("target")

wii = Product("wii", 100, "toy")

target.add_product(wii)

bestbuy = Store("bestbuy")

ps3 = Product("ps3", 200, "toy")

bestbuy.add_product(ps3).print_info()



if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)
  