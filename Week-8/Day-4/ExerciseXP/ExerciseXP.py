#Exercise1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
class Siamese(Cat):
	def sing(self, sounds):
		return f'{sounds}'

all_cats = [Siamese("Bob", 3), Chartreux("Nick", 5), Bengal("Rubi", 7)]
sara_pets = Pets(all_cats)
sara_pets.walk()

#Exercise2
class Dog():
	def __init__(self, name, age, weight):
		self.name = name
		self.age = age
		self.weight = weight
		self.power = self.run_speed() * self.weight
	def bark(self):
		bark = print(f'{self.name} is barking')
		return bark # why you retuing the value of the print
	def run_speed(self):
		speed = (self.weight/self.age*10)
		return speed
	def fight(self, other_dog):
		if self.power > other_dog.power:
			return f'{self.name} is the winner'
		else: # this else is redundant because you are doing return line before
			return f'{other_dog} is the winner'

Dog1 = Dog('Jose', 6, 25)
Dog2 = Dog('Tyson', 4, 20)
Dog3 = Dog('Bruce', 8, 30)
print(Dog1.run_speed())
print(Dog3.fight(Dog2))

