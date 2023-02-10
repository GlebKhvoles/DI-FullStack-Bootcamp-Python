#Exercise1
number = int(input('Enter a number: '))
length = int(input('Enter a length: '))
new_list = []
if length > 0:
    for i in range(1, length):
        new_list.append(number * i)
    print(new_list)
else:
    print('Please enter length more than 0')

#Exercise2
string = input('Write a string with duplicate consecutive letters: ')
string_arr = list(string)
string_arr2 = []

for el in string_arr:
    if len(string_arr2) == 0 or string_arr2[-1] != el:
        string_arr2.append(el)

print("".join(string_arr2))