inp_str = input('Enter a string of words: ')
str = [str for str in inp_str.split(',')]
str.sort()
print(', '.join(str))
