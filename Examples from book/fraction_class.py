class Fraction:
	# This is the constructor which defines the way in which data objects are created
	def __init__(self, top, bottom):
		self.num = top
		self.den = bottom

	# Defining a method called show that will allow the Fraction object to print itself as a string
	def show(self):
		print(self.num, "/", self.den)

	# Redefine the behaviour of the __str__ method and give it a new implementation
	def __str__(self):
		return str(self.num) + "/" + str(self.den)

	# Redefine the behaviour of the __add__ method and give it a new implementation so that we can add two fractions
	def __add__(self, other_fraction):
		new_num = self.num * other_fraction.den + self.den * other_fraction.num
		new_den = self.den * other_fraction.den
		common = gcd(new_num, new_den)
		# // is for integer division
		return Fraction(new_num // common, new_den // common)

	# Reedefining the method for deep equality
	def __eq__(self, other_fraction):
		first_num = self.num * other_fraction.den
		second_num = self.den * other_fraction.num
		return first_num == second_num

	# To do: multiplication, division, subtraction

# This is a GCD (Greatest Common Divisor algorithm) - Implementation of Euclid's Algorithm
def gcd(m, n):
	while m % n != 0:
		old_m = m
		old_n = n

		m = old_n
		n = old_m % old_n
	return n


my_fraction = Fraction(3, 5)

my_fraction.show()

print(my_fraction)

f2 = Fraction(1,2)

print(my_fraction + f2)

print(gcd(20, 10))

f3 = Fraction(6, 10)

print(my_fraction + f3)

print(my_fraction == f2)

print(my_fraction == f3)