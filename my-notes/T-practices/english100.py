def sum_of_word(word):
	sum = 0
	for char in word:
		sum += ord(char) - 96
	return sum 

with open('results.txt', 'w') as results:
	with open('words_alpha.txt', 'r') as file:
		for word in file:
			if sum_of_word(word.strip()) == 100:
				results.write(word)
