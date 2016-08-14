# -*- coding:utf-8 -*-

'''

	API OF FRAME

	- is_valid() Boolean
		# Verify whether bits of frame has values values not accepted.

	API OF METHODS HAMMING ALGORITHM

	- encode() Object ( Frame )
		# Put inside of frame the verification bit, in the positions of power of two. (  add internaly to frame )

	- decode() Object ( Frame )
	    # Verify whether the frame sent has bits wrong  ( add internaly to frame )

	- check() Boolean
		# Calculate parity of bits and verify whether frame came ( add internaly to frame)

	- change_bit(position) Void
		# Swap bit

	API UTILS

	- calculate_parity(dataset) Integer
	- is_power(num,power) Boolean

'''

class Frame:

	def __init__(self,value):
		self.value = value

	def is_valid(self):
		#To implement REGEX = r'[01]

		count_wrong = 0

		for char in self.value:
			if int(char) not in [0,1]:
				count_wrong += 1

		if count_wrong > 0:
			return False
		return True


	def __eq__(self,other_frame):
		
		if self.value == other_frame.value:
			return True
		return False

	def __repr__(self):
		return "<Frame [{}]>".format(self.value)


class Hamming:
	def __init__(self,parity):
		if parity not in ["par","impar"]:
			raise ValueError("Incorrect Value")

		self.parity = parity

	def is_power(self,value,power):

		results = []
		divisor = power

		if value <= 0:
			raise ValueError("Invalid Value")
		else:
			while True:
				if value >= divisor:
					if value % divisor == 0:
						results.append(divisor)
						value //= divisor
					else:
						divisor += 1
				else:
					break

		print(results)
		if results.count(power) != len(results):
			return False
		return True


	def divisors(self,position):

		'''
			Return divisors which are power of two
		'''

		from math import sqrt , floor

		powers = []
		total = position

		find_floor_root = lambda x : floor(sqrt(x))

		while total > 1:
			max_power = pow(2,int(find_floor_root(total))) # Obtain closest power

			total -= max_power
			powers.append(max_power)

			if total == 1:
				powers.append(total)

		return powers

	def calculate_parity(self,dataset):
		count_one = dataset.count(1)

		is_pair = lambda value : value % 2 == 0

		if self.parity == "par":
			if is_pair(count_one):
				value = 0
			else:
				value = 1

		elif self.parity == "impar":
			if is_pair(count_one):
				value = 1
			else:
				value = 0

		return value

	def encode(self,frame):

		original_list = list(frame.value)
		list_with_power_two = []

		position_new_list = 0

		if not frame.is_valid():

			return False

		else:

			while original_list:

				actual_position = len(list_with_power_two) + 1

				if self.is_power(actual_position,2): 

					list_with_power_two.append("")

					position_new_list += 1

				else:

					element_original_list = int(original_list.pop(0))

					list_with_power_two.append(element_original_list)

		data_bits = {}

		#Generating dict with position and yours divisors
		for position,value_position in enumerate(list_with_power_two,start=1):
			if not self.is_power(position,2):
				data_bits[position] = self.divisors(position)

		for position,actual_element in enumerate(list_with_power_two,start=1):

			# Found parity position
			if self.is_power(position,2):

				position_bit_verified = []
				dataset_bit = []

				for position_list , divisors in data_bits.items():
					if position in divisors:
						position_bit_verified.append(position_list)

				for value in position_bit_verified:
					dataset_bit.append(list_with_power_two[value-1])

				parity = self.calculate_parity(dataset_bit)

				list_with_power_two[position-1] = parity

		formated = "".join(map(str,list_with_power_two))

		return Frame(formated)
			
	def check(self,frame):
		return frame

# Paridade : par impar
# 0 1 1
# _ _ 0 _ 1 1
#  (1) (1) 0 (0) 1 1
# Frame('110011')

l = range(1,20)
h = Hamming("par")

print(h.encode(Frame("11100101010110")))
print(h.is_power(10,3))
# for i in l:
# 	if not h.is_power(i,2):
# 		d = h.divisors(i)
# 		print("number:{} = {}".format(i," + ".join(map(str,d))))