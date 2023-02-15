# Exercise1
def display_message():
	print('I am learning coding in this course.')


display_message()


# Exercise2
def favorite_book(title):
	print(f'One of my favorite books is {title}')


favorite_book('"The Night in Lisbon"')


# Exercise3
def describe_city(city, country='Belgium'):
	print(f'{city} is in {country}')


describe_city('Bruges')

# Exercise4
from random import randint


def numbers(num):
	rm_num = randint(1, 100)
	if num == rm_num:
		print('Correct number!')
	else:
		print(f"Incorrect number. Numbers are {num} and {rm_num}")


num = int(input('Enter a number: '))
numbers(num)


# Exercise5
def make_shirt(size, text):
	if size == 'large' or size == 'medium':
		text = 'I love Python'
	else:
		text = 'I love life'
	print(f'The size of the shirt is "{size}" and the text is "{text}"')


make_shirt(size='small', text='...')

# Exercise6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']


def show_magicians():
	for magician in magician_names:
		print(magician)


def make_great():
	for x in range(0, len(magician_names)):
		magician_names[x] += ' the Great'


make_great()
show_magicians()
