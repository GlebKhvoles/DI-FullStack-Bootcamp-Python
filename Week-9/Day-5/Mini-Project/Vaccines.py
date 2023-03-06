class Human:
	def __init__(self, id_number:str, name:str, age:int, priority:bool, blood_type:str, family:list=[]):
		self.id_number = id_number
		self.name = name
		self.age = age
		self.priority = priority
		if blood_type not in ['A', 'B', 'AB', 'O']: # it's better to export this code to external function
			raise ValueError(f'There is no type of blood like that')
		self.blood_type = blood_type
		self.family = family
	def add_family_member(self, person): # there is a bug at this function, le'ts say that we have the following: member A, B, C for A his family member is B and we add C as family member to A then we need to add it also to B
		self.family.append(person)
		person.family.append(self)


class Queue:
	def __init__(self):
		self.humans = []
	def __str__(self):
		return " ".join([human.name for human in self.humans])
	def add_person(self, person):
		if person.age > 60 or person.priority:
			self.humans = [person] + self.humans
		else:
			self.humans.append(person)
	def find_in_queue(self, person):
		for idx, human in enumerate(self.humans):
			if human == person:
				return idx

	def swap(self, person1, person2):
		index1 = self.find_in_queue(person1)
		index2 = self.find_in_queue(person2)
		self.humans[index1], self.humans[index2] = self.humans[index2], self.humans[index1]
	def get_next(self):
		if not self.humans:
			return None
		person = self.humans[0]
		self.humans = self.humans[1:]
		return person
	def get_next_blood_type(self, blood_type):
		for human in self.humans:
			if human.blood_type == human.blood_type:
				self.humans.remove(human)
				return human
	def sort_by_age(self):
		priority_list = []
		older_list = []
		younger_list = []

		for human in self.humans:
			if human.priority:
				priority_list.append(human)
				continue
			if human.age >= 60:
				older_list.append(human)
				continue
			younger_list.append(human)

		return priority_list + older_list + younger_list
	def rearange_queue(self):
		for _ in range(len(self.humans)):
			for i in range(1, len(self.humans)):
				if self.humans[i - 1] in self.humans[i].family and i != len(self.humans) - 1:
					self.humans[i], self.humans[i + 1] = self.humans[i + 1], self.humans[i]

h1 = Human('H1', 'Nick', 14, True, 'B')
h2 = Human('H2', 'Coral', 44, False, 'O')
h3 = Human('H3', 'Maria', 23, False, 'AB')
h4 = Human('H4', 'Paul', 54, False, 'A')
h5 = Human('H5', 'Sonya', 41, True, 'B')
h6 = Human('H6', 'John', 22, False, 'AB')
h7 = Human('H7', 'Anna', 35, True, 'O')
h8 = Human('H8', 'Alex', 27, True, 'B')

queue = Queue()
queue.add_person(h1)
queue.add_person(h2)
queue.add_person(h3)
queue.add_person(h4)
queue.add_person(h5)
queue.add_person(h6)
queue.add_person(h7)
queue.add_person(h8)

print(queue)
queue.swap(h3, h5)
print(queue)
queue.get_next()
print(queue)
queue.add_person(h8)
queue.get_next_blood_type('O')
print(queue)
queue.add_person(h1)
print(queue)
queue.sort_by_age()
print(queue)

h1.add_family_member(h2)
h2.add_family_member(h3)
h3.add_family_member(h4)
h4.add_family_member(h5)
h5.add_family_member(h6)
h6.add_family_member(h7)
h7.add_family_member(h8)
h8.add_family_member(h1)
queue.rearange_queue()
print(queue)
