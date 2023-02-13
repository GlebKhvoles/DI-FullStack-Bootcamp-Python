# Exercise1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

print(dict(zip(keys, values)))

# Exercise2
ticket_cost = 0
total_cost = 0
family = {}

while True:
	family_member_name = input("Enter the family member name or exit: ")
	if family_member_name == 'exit':
		break

	family_member_age = int(input("Enter the family member age: "))
	family[family_member_name] = family_member_age

for name in family:
	if 12 >= family[name] >= 3:
		ticket_cost = 10
	elif family[name] > 12:
		ticket_cost = 15
	elif family[name] < 3:
		ticket_cost = 0

	print(f"{name}'s price is: {ticket_cost}")
	total_cost += ticket_cost

print(f"Total price of tickets is: {total_cost}")

# Exercise3
brand = {
   'name': 'Zara',
   'creation_date': '1975',
   'creator_name': 'Amancio Ortega Gaon',
   'type_of_clothes': ['men', 'women', 'children', 'home'],
   'international_competitors': ['Gap', 'H&M', 'Benetton'],
   'number_stores': 7000,
   'major_color': {
      'France': 'blue',
      'Spain': 'red',
      'US': ['pink', 'green']
   }
}

brand['number_stores'] = 2

clients = brand['type_of_clothes']
print(f'Zara\'s clients are: {clients[0]}, {clients[1]} and {clients[2]}')

brand['country_creation'] = 'Spain'

if 'international_competitors' in brand.keys():
	brand['international_competitors'].append('Desigual')

brand.pop('creation_date')

print(brand['international_competitors'][-1])

print(brand['major_color']['US'])

print(len(brand))

[print(key, end='; ') for key in brand.keys()]

more_on_zara = {
	'creation_date': 1975,
	'number_stores': 10000
}

brand.update(more_on_zara)

print(brand['number_stores'])
print(brand)

# Exercise4
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
#1/
disney_users_A = {}
for x, name in enumerate(users):
	disney_users_A[name] = x
print(disney_users_A)

disney_users_A = {}
for x, name in enumerate(users):
	if name[0] == "M" or name[0] == "P" or 'i' in name:
		disney_users_A[name] = x
	else:
		continue
print(disney_users_A)
#2/
disney_users_B = {}
for x, name in enumerate(users):
	disney_users_B[x] = name
print(disney_users_B)
#3/
disney_users_C = {}
users.sort()
for x, name in enumerate(users):
	disney_users_C[name] = x
print(disney_users_C)