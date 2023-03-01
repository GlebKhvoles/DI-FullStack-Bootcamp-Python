
class Character:
	def __init__(self, name, life=20, attack=10):
		self.name = name
		self.life = life
		self.attack = attack
	def basic_attack(self, Other):
		Other.life -= self.attack

class Druid(Character):
	def __init__(self, name, life=20, attack=10):
		super().__init__(name, life, attack)
		print(f"Forest is calling for {name}!")
	def meditate(self):
		self.life += 10
		self.attack -= 2
	def animal_help(self):
		self.attack += 5
	def fight(self, Other):
		Other.life -= (0.75 * self.life + 0.75 * self.attack)
class Warrior(Character):
	def __init__(self, name, life=20, attack=10):
		super().__init__(name, life, attack)
		print(f"Taste my AXE!")
	def brawl(self, Other):
		Other.life -= (2 * self.attack)
		self.life += (0.5 * self.attack)
	def train(self):
		self.attack += 2
		self.life += 2
	def roar(self, Other):
		Other.attack -= 3
class Mage(Character):
	def __init__(self, name, life=20, attack=10):
		super().__init__(name, life, attack)
		print(f"Try to spell my name, if you dare!")
	def curse(self, Other):
		Other.attack -= 2
	def summon(self):
		self.attack += 3
	def cast_spell(self, Other):
		Other.life -= self.attack / self.life

silvan = Druid('Silvan', 200, 40)
sarmat = Warrior('Sarmat', 170, 70)
wizard = Mage('Wizard', 150, 30)

silvan.basic_attack(wizard)
silvan.animal_help()
silvan.fight(sarmat)
silvan.meditate()
sarmat.basic_attack(wizard)
sarmat.brawl(silvan)
sarmat.roar(wizard)
sarmat.train()
wizard.basic_attack(silvan)
wizard.cast_spell(silvan)
wizard.curse(sarmat)
wizard.summon()

print('silvan', silvan.life)
print('silvan', silvan.attack)
print('sarmat', sarmat.life)
print('sarmat', sarmat.attack)
print('wizard', wizard.life)
print('wizard', wizard.attack)
