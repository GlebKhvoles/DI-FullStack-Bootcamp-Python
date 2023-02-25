import random


class Game:
	def get_user_item(self):
		items = ['Rock', 'Paper', 'Scissors']
		while True:
			value = input(f"Choose an item from {items}")
			if value in items:
				return value
			else:
				print('`You have enter an invalid value, please enter again')
	def get_computer_item(self):
		return random.choice(['Rock', 'Paper', 'Scissors'])
	def get_game_result(self, user_item, computer_item):
		if user_item == computer_item:
			return 'draw'
		if user_item == 'Rock' and computer_item == 'Paper':
			return 'loss'
		if user_item == 'Rock' and computer_item == 'Scissors':
			return 'win'
		if user_item == 'Paper' and computer_item == 'Rock':
			return 'win'
		if user_item == 'Paper' and computer_item == 'Scissors':
			return 'loss'
		if user_item == 'Scissors' and computer_item == 'Paper':
			return 'win'
		if user_item == 'Scissors' and computer_item == 'Rock':
			return 'loss'
	def play(self):
		user_item = self.get_user_item()
		computer_item = self.get_computer_item()
		result = self.get_game_result(user_item, computer_item)
		values = ['Rock', 'Paper', 'Scissors']
		results = {"win": "You win!", "loss": "You lose!", "draw": "It's draw!"}
		print(f'You selected {user_item}. The computer selected {computer_item}. {results}')
		return result
