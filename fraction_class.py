class Fraction:
	# This is the constructor which defines the way in which data objects are created
	def __init__(self, top, bottom):
		# isinnstance(<var>, int) checks to see whether the variable is an integer or not
		if isinstance(top, int) & isinstance(bottom, int):
			self.num = top
			self.den = bottom
			if self.den < 0:
				self.num *= -1
				self.den *= -1
			common = gcd(self.num, self.den)
			self.num = self.num // common
			self.den = self.den // common
		else:
			raise RuntimeError("Both the numerator and denominator need to be integers")

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
		return Fraction(new_num, new_den)

	# Reedefining the method for deep equality
	def __eq__(self, other_fraction):
		first_num = self.num * other_fraction.den
		second_num = self.den * other_fraction.num
		return first_num == second_num

	# To do: multiplication, division, subtraction
	# multiply: __mul__
	def __mul__(self, other_fraction):
		first_num = self.num * other_fraction.num
		second_num = self.den * other_fraction.den
		return Fraction(first_num, second_num)

	# division: __trudiv__
	def __truediv__(self, other_fraction):
		first_num = self.num * other_fraction.den
		second_num = self.den * other_fraction.num
		return Fraction(first_num, second_num)

	# subtraction: __sub__
	def __sub__(self, other_fraction):
		new_num = self.num * other_fraction.den - self.den * other_fraction.num
		new_den = self.den * other_fraction.den
		return Fraction(new_num, new_den)

	# greater than
	def __gt__(self, other_fraction):
		first_num = self.num / self.den
		second_num = other_fraction.num / other_fraction.den
		return first_num > second_num

	#less than
	def __lt__(self, other_fraction):
		first_num = self.num / self.den
		second_num = other_fraction.num / other_fraction.den
		return first_num < second_num

	def __ge__(self, other_fraction):
		first_num = self.num / self.den
		second_num = other_fraction.num / other_fraction.den
		return first_num >= second_num

	def __le__(self, other_fraction):
		first_num = self.num / self.den
		second_num = other_fraction.num / other_fraction.den
		return first_num <= second_num

	def __ne__(self, other_fraction):
		first_num = self.num / self.den
		second_num = other_fraction.num / other_fraction.den
		return first_num != second_num

	# defining simple methods to return the numerator and denominator of the fractions
	def get_num(self):
		return self.num

	def get_den(self):
		return self.den

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

f4 = Fraction(1, 2)

f5 = Fraction(3, 4)

print(f4 * f5)

print(f4 / f5)

print(f4 - f5)