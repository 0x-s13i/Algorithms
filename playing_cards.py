import random

class random_playing_card:
	def __init__(self):
		numbers_to_choose_from = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
		suits_to_choose_from = ["Spades", "Clubs", "Hearts", "Diamonds"]
		
		rand_number = numbers_to_choose_from[random.randrange(len(numbers_to_choose_from))]
		rand_suit = suits_to_choose_from[random.randrange(len(suits_to_choose_from))]

		self.num = rand_number
		self.suit = rand_suit

	def __str__(self):
		return str(self.num) + " of " + str(self.suit)

class card:
	def __init__(self, num, suit):
		self.num = num
		self.suit = suit

	def __str__(self):
		return str(self.num) + " of " + str(self.suit)

class deck_of_cards:
	# a deck of cards has 52 cards from 2 of diamonds to a of spades
	def __init__(self):
		# card_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty-one", "twenty-two", "twenty-three", "twenty-four", "twenty-five", "twenty-six", "twenty-seven", "twenty-eight", "twenty-nine", "thirty", "thirty-one", "thirty-two", "thirty-three", "thirty-four", "thirty-five", "thirty-six", "thirty-seven", "thirty-eight", "thirty-nine", "forty", "forty-one", "forty-two", "forty-three", "forty-four", "forty-five", "forty-six", "forty-seven", "forty-eight", "forty-nine", "fifty", "fifty-one", "fifty-two"]

		numbers_to_choose_from = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
		suits_to_choose_from = ["Spades", "Clubs", "Hearts", "Diamonds"]

		deck = []

		for number in numbers_to_choose_from:
			for suit in suits_to_choose_from:
				deck.append(card(number, suit))

		self.deck = deck


test_random = random_playing_card()
print(test_random)
test_card = card(2, "Diamonds")
print(test_card)
test_deck = deck_of_cards()
for i in test_deck.deck:
	print(i)