import random

from ExerciseXP import Dog
from random import randint

class PetDog(Dog):
	def __init__(self, name, age, weight):
		super().__init__(name, age, weight)
		self.trained = False
	def train(self):
		self.bark()
		self.trained =True
	def play(self, *dogs):
		dog_names = self.name
		for dog in dogs:
			dog_names += ' ' + dog.name
		print(f'{dog_names} all play together')
	def do_a_trick(self):
		tricks = [f'{self.name} does a barrel roll', f'{self.name} stands on his back legs', f'{self.name} shakes your hand', f'{self.name} plays dead']
		if self.trained:
			print(tricks[random.randint(0,3)])

Dog1 = PetDog('Jose', 6, 25)
Dog2 = PetDog('Tyson', 4, 20)
Dog3 = PetDog('Bruce', 8, 30)

Dog1.train()
Dog2.play(Dog1, Dog3)
Dog1.do_a_trick()
