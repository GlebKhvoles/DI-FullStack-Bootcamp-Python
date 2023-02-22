#Exercise1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cats = [Cat('Kim', 9), Cat('John', 5), Cat('Boris', 11)]
def oldest_cat(cats):
    oldestcat = ['', 0]
    for cat in cats:
        if cat.age > oldestcat[1]:
            oldestcat = [cat.name, cat.age]
    return oldestcat

print(f"The oldest cat is {oldest_cat(cats)[0]}, and is {oldest_cat(cats)[1]} years old.")

#Exercise2
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def bark(self):
        print(f"{self.name} goes woof!")
    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

davids_dog = Dog("Rex", 50)
print(f"David's dog name is {davids_dog.name} and its height is {davids_dog.height}cm")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(f"Sarah's dog name is {sarahs_dog.name} and its height is {sarahs_dog.height}cm")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is a bigger than {sarahs_dog.name}")
elif davids_dog.height < sarahs_dog.height:
    print(f"{sarahs_dog.name} is a bigger than {davids_dog.name}")

#Exercise3
class Song:
    def __init__(self, lyrics: list):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

#Exercise4
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
    def get_animals(self):
        print(f"All the animals of the zoo are {self.animals}")
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    def sort_animals(self):
        animals_temp = []
        for i in range(len(self.animals)):
            if type(self.animals[i]) is list:
                for x in self.animals[i]:
                    animals_temp.append(x)
            else:
                animals_temp.append(self.animals[i])
        animals_temp.sort()

        self.animals.clear()
        first_letter = ''
        for i in range(len(animals_temp)):
            if i + 1 == len(animals_temp):
                if first_letter == animals_temp[i][0]:
                    self.animals[-1].append(animals_temp[i])
                else:
                    self.animals.append(animals_temp[i])
            else:
                if first_letter == animals_temp[i][0]:
                    if type(self.animals[-1]) is list:
                        self.animals[-1].append(animals_temp[i])
                    else:
                        last_val = self.animals.pop()
                        self.animals.append([last_val, animals_temp[i]])
                else:
                    self.animals.append(animals_temp[i])
                first_letter = animals_temp[i][0]

    def get_groups(self):
        num_group = 0
        for str_animal in self.animals:
            if type(str_animal) is list:
                num_group += 1
                list_animal = []
                for animal in str_animal:
                    list_animal.append(animal)
                print(f'Group {num_group} - {",".join(list_animal)}')

ramat_gan_safari = Zoo('Ramat-gan')
ramat_gan_safari.add_animal('Ape')
ramat_gan_safari.add_animal('Baboon')
ramat_gan_safari.add_animal('Bear')
ramat_gan_safari.add_animal('Bird')
ramat_gan_safari.add_animal('Cat')
ramat_gan_safari.add_animal('Cougar')
ramat_gan_safari.add_animal('Racoon')
ramat_gan_safari.add_animal('Eel')
ramat_gan_safari.add_animal('Emu')

ramat_gan_safari.sort_animals()
ramat_gan_safari.add_animal('Emu')
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal('Bird')
ramat_gan_safari.sell_animal('Something')
ramat_gan_safari.get_animals()
ramat_gan_safari.get_groups()