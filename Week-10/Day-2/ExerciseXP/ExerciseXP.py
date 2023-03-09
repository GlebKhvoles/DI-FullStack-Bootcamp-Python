#Exercise2
import random

def random_guess(x):
	if x == random.randrange(100):
		print("Success")
	else:
		print("Fail")

#Exercise3
import string
def random_str():
	alphabet = string.ascii_letters
	return ''.join(random.choice(alphabet) for i in range(5))
print(random_str())

#Exercise4
import datetime
def current_time():
	date = datetime.datetime.today().strftime('%D')
	return date
print(current_time())

#Exercise5
def until_jan():
	current_year = datetime.datetime.now().year
	day_x = datetime.date(current_year + 1, 1, 1)
	actual_time = datetime.datetime.today().date()
	days = day_x - actual_time
	print(f'the 1st of January is in {days.days} days')
until_jan()

#Exercise6
def until_bd(bd):
	actual_time = datetime.datetime.today().date()
	delta_time = actual_time - bd
	return delta_time.days * 24 * 60
print(f'You have spent {until_bd(datetime.date(1995, 9, 4))} minutes in your life')

#Exercise7
def now():
	current_year = datetime.datetime.now().year
	actual_time = datetime.datetime.today().date()
	pesah = datetime.date(current_year, 4, 5)
	until_pesah = pesah - actual_time
	print(f'The next holiday(Pesah) is in {until_pesah.days} days')
now()

#Exercise8
bd = datetime.datetime(1995, 9, 4)
difference = datetime.datetime.now() - bd
age_someone_seconds = difference.days * 86400 + difference.seconds
earth_year = 31557600
print(f"Age on Earth: {round(age_someone_seconds / earth_year, 2)}")
print(f"Age on Mercury: {round(age_someone_seconds / (earth_year * 0.2408467), 2)}")
print(f"Age on Venus: {round(age_someone_seconds / (earth_year * 0.61519726), 2)}")
print(f"Age on Mars: {round(age_someone_seconds / (earth_year * 1.8808158), 2)}")
print(f"Age on Jupiter: {round(age_someone_seconds / (earth_year * 11.862615), 2)}")
print(f"Age on Saturn: {round(age_someone_seconds / (earth_year * 29.447498), 2)}")
print(f"Age on Uranus: {round(age_someone_seconds / (earth_year * 84.016846), 2)}")
print(f"Age on Neptune: {round(age_someone_seconds / (earth_year * 164.79132), 2)}")

#Exercise9
import faker
users = []

def add():
	fake = faker.Faker()
	for i in range(3):
		users.append(
			{'name': fake.name(),
			 'address': fake.address(),
			 'language_code': fake.language_code()})
	print(users)
add()