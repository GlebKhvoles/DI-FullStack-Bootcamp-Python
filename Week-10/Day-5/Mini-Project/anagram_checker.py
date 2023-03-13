import itertools
import requests
class AnagramChecker:
	@classmethod
	def init_anagram_checker(cls):
		response = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt')
		if not response.ok:
			return f'Sorry, come back later'
		words_list = response.text.split('\r\n')
		return cls(words_list)
	def __init__(self, words_list):
		self.words_list = words_list

	def	is_valid_word(self, word):
		if word in self.words_list:
			return True

	def get_anagrams(self, word):
		if not self.is_valid_word(word):
			print(f'The given word is not exist', word)
			return []
		else:
			anagrams = itertools.permutations(word)
			return [''.join(anagram) for anagram in list(anagrams)]

	def is_anagram(self, word1, word2):
		if word1 != word2:
			if word1 in self.get_anagrams(word2):
				return True

ana = AnagramChecker.init_anagram_checker()

