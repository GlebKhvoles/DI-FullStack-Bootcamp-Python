#Exercise1
my_fav_numbers = {7, 10, 23, 6}

my_fav_numbers.update([11, 3])

my_fav_numbers.discard(23)

friend_fav_numbers = {4, 19, 17, 33}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(my_fav_numbers)
print(our_fav_numbers)

#Exercise2
# NO

#Exercise3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.pop()
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket.count("Apples"))
basket.clear()
print(basket)

#Exercise4
float_numbers = []
x = 1.5

for i in range(1, 9):
    float_numbers.append(x)
    x += 0.5

print(float_numbers)

#Exercise5
for numbers in range(1, 21):
    print(numbers)

for numbers in range(1, 21):
    if numbers % 2 == 0:
        print(numbers)

#Exercise6
name = ''
# while name != 'Gleb':
    # name = input('Write your name: ')

#Exercise7
# str_fav_fruits = input('Write your favorite fruit(s) (please separate fruits by space): ')
# fav_fruits = str_fav_fruits.split(' ')

# fruits = input('Enter a fruit: ')

# if fruits in fav_fruits:
   # print('You chose one of your favorite fruits! Enjoy!')
# else:
    # print('You chose a new fruit. I hope you enjoy')

#Exercise8
list_toppings = []
#while True:
    # topping = input('Enter a series of pizza toppings you want: ')
    # if topping == 'quit':
       # break
   # else:
     #   list_toppings.append(topping)
      #  print('We\'ll add this one to your pizza!')

# print('All your toppings ' + ' '.join(list_toppings) + f'. Total price: {10 + len(list_toppings) * 2.5}')

#Exercise9
# str_family_age = input('Enter your age separated by space: ')
# family_age = str_family_age.split(' ')
total_cost = 0
#for i in family_age:
   # if 12 >= int(i) >= 3:
       # total_cost += 10
  # elif int(i) > 12:
        # total_cost += 15

# print(f'Total cost: {total_cost}')

# list_teens = ['Roy', 'Alice', 'Katty']

# for x in reversed(range(len(list_teens))):
   # age = int(input(f'{list_teens[x]} enter your age: '))
   # if 16 >= age <= 21:
       # list_teens.remove(list_teens[x])

# print(list_teens)

#Exercise10
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []

for i in sandwich_orders:
    finished_sandwiches.append(i)
sandwich_orders.clear()

for i in finished_sandwiches:
    print(f'I made your {i}')

#Exercise11
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []

print('Sorry, we run out of pastrami!')
while sandwich_orders.count('Pastrami sandwich') > 0:
    index = sandwich_orders.index("Pastrami sandwich")
    sandwich_orders.pop(index)

for i in sandwich_orders:
    finished_sandwiches.append(i)
sandwich_orders.clear()

for i in finished_sandwiches:
    print(f'I made your {i}')
