from anagram_checker import AnagramChecker

def main():
	checker = AnagramChecker.init_anagram_checker()
	while True:
		usr_inp = input(f'Write your word or q to exit: ').strip()
		if len(usr_inp.split(' ')) > 1:
			print('Invalid input')
			continue
		if not usr_inp.isalpha():
			print('Invalid input')
			continue
		if usr_inp == 'q':
			break
		print(f'\nYOUR WORD: ”{usr_inp.upper()}”')
		print('This is a valid input.')
		print(f'Anagrams for your word: {", ".join(checker.get_anagrams(usr_inp))}')



if __name__ in '__main__':
	main()