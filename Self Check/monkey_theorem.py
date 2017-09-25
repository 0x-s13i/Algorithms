import random

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

def choose_characters():
	string = ""
	for i in range(28):
		rand = alphabet[random.randrange(len(alphabet))]
		string += rand
	return string

def compare_strings(string):
	correct = "methinks it is like a weasel"
	score = 0
	for i in range(len(string)):
		if string[i] == correct[i]:
			score += 1
	return score / 28

def generate():
	i = 0
	best_string = choose_characters()
	best_score = compare_strings(best_string)
	while i >= 0:
		rand_string = choose_characters()
		score = compare_strings(rand_string)
		if score > best_score:
			best_string = rand_string
			best_score = score
		if i % 1000 == 0:
			print("methinks it is like a weasel")
			print(best_string)
			print(best_score)
		if score == 1:
			print("methinks it is like a weasel")
			print(best_string)
			print(best_score)
			print(i)
			break 
		i += 1

generate()