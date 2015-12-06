# for any pair of number x, y

class ModularArithematic(object):
	def __init__(self, modulus):
		self.modulus = modulus

	def addition(self, num1, num2):
		return (num1 + num2) % self.modulus

	def substraction(self, num1, num2):
		return (num1 + self.modulus - num2) % self.modulus

	def multiplication(self, num1, num2):
		return (num1 * num2) % self.modulus

	def division(self, num1, num2):
		inverse_num2 = self.get_inverse(self.modulus, num2)
		return (num1 * inverse_num2) % self.modulus

	def get_inverse(self, mod, num):
		inverse = self.extended_gcd(mod, num)
		if inverse[0] != 1:
			return None
		return inverse[2] % mod

	# implementing extended euclidean algorithm:
	# for two numbers 567 and 88:
	#     their GCD = 
	#     567 = 88 * 6 + 39
	#     88 = 39 * 2 + 10
	#     39 = 10 * 3 + 9
	#     10 = 9 * 1 + 1
	#     9 = 1 * 9 + 0
	#     therefore the GCD of 567 and 88 = 1
	#
	# now to find the inverse of a number we use extended euclidean algorithm:
	# from the extended euclidean algorithm we can deduce that in an equation:
	# we can represent a gcd of x and y as: a * x + b * y = gcd(x,y)
	# now if the gcd was 1 then b * y would be 1 meaning that b would be the inverse of y
	# and in programming, it can be written as:
	def extended_gcd(self, mod, num):
		if num == 0:
			return mod, 1, 0
		else:
			g, itr_mod, itr_num = self.extended_gcd(num, mod % num)
			return g, itr_num, itr_mod - (mod // num) * itr_num

a = ModularArithematic(37)
c =a.get_inverse(37, 23)
print (c)
