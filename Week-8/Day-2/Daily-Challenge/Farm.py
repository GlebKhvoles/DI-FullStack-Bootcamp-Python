class Farm:
	def __init__(self, name):
		self.name = name
		self.animals = {}
		print(f"{name}'s farm")

	def add_animal(self, animal, quantity=1):
		if animal in self.animals:
			self.animals[animal] += 1 if quantity == 0 else quantity
		else:
			self.animals[animal] = quantity if quantity == 0 else quantity
		print(f"{animal}: {quantity}")

	def get_info(self):
		sentence = "     E-I-E-I-0!"
		print(sentence)

	def get_animal_types(self):
		animal_list = []
		[animal_list.append(type) for type in sorted(self.animals)]
		return animal_list
	def get_short_info(self, name):
		animals = self.get_animal_types()
		return f"McDonald’s farm has {animals[0]}s, {animals[1]}s and {animals[2]}."


macdonald = Farm('McDonald')
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
