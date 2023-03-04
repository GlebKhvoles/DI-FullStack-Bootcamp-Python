class Person:
	def __init__(self, name, like: list, hate: list):
		self.name = name
		self.like = like
		self.hate = hate

	def taste(self, food: str):
		if food in self.like:
			food += ' and loves it!'
		if food in self.hate:
			food += ' and hates it!'
		else:
			food += '!'
		return f'{self.name} eats the {food}'

p1 = Person('Gleb', ['sushi'], ['holodets'])
print(p1.taste('sushi'))
print(p1.taste('holodets'))
print(p1.taste('pasta'))
