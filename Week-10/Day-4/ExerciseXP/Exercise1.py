import random
def get_words_from_file():
	with open("sowpods.txt", mode = 'r') as words:
		w = words.read()
		return w.split('\n')

def get_random_sentence(length):
	words_list = get_words_from_file()
	sentence = []
	for x in range(0, length):
		if length == 0:
			return False
		else:
			sentence.append(random.choice(words_list))
	return ' '.join(sentence).lower()

#print(get_random_sentence(5))

def main():
	print('Hello! You have to enter the amount of words, you want to have in your sentence.')
	length = int(input('Enter a number: '))
	if 2 < length < 20:
		print(get_random_sentence(length))
	else:
		raise ValueError('Invalid length!')

main()