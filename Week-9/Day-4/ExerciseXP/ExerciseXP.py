class Human():
	def __init__(self, name: str, age: int, living_place=None):
		self.name = name
		self.age = age
		self.living_place = living_place
	def move(self, building):
		self.living_place = building
		building.inhabitants.append(self)

class Building():
	def __init__(self, address: str, inhabitants: list = []):
		self.address = address
		self.inhabitants = inhabitants
class City():
	def __init__(self, name: str, buildings: list = []):
		self.name = name
		self.buildings = buildings
	def construct(self, address):
		new_building = Building(address)
		self.buildings.append(new_building)
		return new_building

	def info(self):
		age_sum = 0
		population = 0
		for building in self.buildings:
			for citizen in building.inhabitants:
				population += 1
				age_sum += citizen.age
				avg_age = age_sum / population
		return f'There are {len(self.buildings)} buildings in {self.name} with the average age of inhabitants - {avg_age}'

city = City('New England')

h1 = Human('Cale', 21)
h2 = Human('Alex', 22)
h3 = Human('Rudy', 43)
h4 = Human('Anna', 34)
h5 = Human('Bruce', 56)
h6 = Human('Olga', 13)
h7 = Human('Maria', 26)
h8 = Human('Daria', 28)

b1 = city.construct('Ratnaya street 2')
b2 = city.construct('Ratnaya street 7')
b3 = city.construct('Ratnaya street 9')

h7.move(b3)
h5.move(b2)
h1.move(b1)
h3.move(b3)
h4.move(b1)
h2.move(b2)
h6.move(b3)
h8.move(b1)

print(city.info())