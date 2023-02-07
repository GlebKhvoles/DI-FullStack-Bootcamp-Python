#Exercise1
print(('Hello world\n') *5)

#Exercise2
print((99*99*99)*8)

#Exercise3
#5 < 3
#False
#3 == 3
#True
#3 == "3"
#True
#"3" > 3
#TypeError
#"Hello" == "hello"
#False

#Exercise4
computer_brand = '"Apple"'
print(f'I have an {computer_brand} computer')

#Exercise5
name = 'Gleb'
age = 27
shoe_size = '42.5'
info = f'My name is {name}, i am {age} years old and my shoe size is EU {shoe_size}'
sentence = print(info)
sentence

#Exercise6
a = 2
b = 4
if a > b:
    print('Hello World')
else:
    print('a is not bigger than b')

#Exercise7
number = input('Write a random number: ')
if int(number) % 2 == 0:
    print('Odd')
else:
    print('Even')

#Exercise8
my_name = 'Gleb'
your_name = input('Please enter your name: ')

if my_name == your_name:
    print('Surprise! We have exactly the same name with you!')


#Exercise9
height = input('Enter your height in inches: ')

if float(height) * 2.54 >= 145:
    print('You are tall enough, get in, please!')
else:
    print('You need to grow some more to ride')
