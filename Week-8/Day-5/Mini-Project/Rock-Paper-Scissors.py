from Game import Game

def get_user_menu_choice():
	while True:
		value = input('Enter "P" to play a new game, "S" to show scores, or "Q" to quit: ')
		if value == 'P' or value == "S" or value == "Q":
			break
	return value
def print_results(results):
	print('Game results')
	print(f' You won: {results["win"]} times')
	print(f' You lost: {results["loss"]} times')
	print(f' You drew: {results["draw"]} times')
	print('Thank you for playing!')
def main():
	results = {'win': 0, 'loss': 0, 'draw': 0}
	while True:
		choice = get_user_menu_choice()
		if choice == 'P':
			new_game = Game()
			result = new_game.play()
			results[result] += 1
		elif choice == 'S':
			print_results(results)
		elif choice == 'Q':
			print(f'Bye bye now!\n{print_results(results)}')
			break

main()