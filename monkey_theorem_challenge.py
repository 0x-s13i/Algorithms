import random

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

def choose_initial_characters():
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

def improve():
	print("generating random string...")
	correct = "methinks it is like a weasel"
	best_string = choose_initial_characters()
	print("random string: %s" %(best_string))
	best_score = compare_strings(best_string)
	print("initial score is: %.2f%%" %(best_score))
	print("reworking random string...")	
	string_copy = []
	for k in range(len(best_string)):
		string_copy.append(best_string[k])
	m = 0
	for j in range(len(best_string)):
		while string_copy[j] != correct[j]:
			string_copy[j] = alphabet[random.randrange(len(alphabet))]
			score = compare_strings(string_copy)
			if score > best_score:
				best_string = string_copy
				best_score = score
			m += 1
	if score == 1:
		string2 = ""
		for l in range(len(best_string)):
			string2 += best_string[l]
		print("random string is now: %s" %(string2))
		print("it took %d random guesses to rewrite shakespeare" %(m))

improve()