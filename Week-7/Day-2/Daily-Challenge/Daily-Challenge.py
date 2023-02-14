matrix = [
	['7', 'i', '3'],
    ['T', 's', 'i'],
    ['h', '%', 'x'],
	['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!'],
]

final_sentence = []
for column in range(len(matrix[0])):
	for row in range(len(matrix)):
		if matrix[row][column].isalpha():
			final_sentence.append(matrix[row][column])
		elif len(final_sentence) > 0 and final_sentence[-1] != " " and row > 0:
			final_sentence.append(" ")

print(''.join(final_sentence))
