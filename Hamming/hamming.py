# -*- coding:utf-8 -*-

'''

	API of Frame

	- is_valid()   # Verify whether bits of frame has values values not accepted.

	API of methods hamming algorithms

	- check()      # Calculate parity of bits and verify whether frame came 
	- encode()     # Put inside of frame the verification bit, in the positions of power of two.
	- decode()     # Verify whether the frame sent has bits wrong

	To use a dictionary to mark the positions of frame, as such as:

	>> frame = {'1':0,'2':1,'3':1,'4':1,'5':0,'6':1}
	>> position_two = frame.get(2,None)
	>> print(position_two)
	1

'''

class Frame:

	def __init__(self,value):
		self.value = value

	def is_valid(self):

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
		return "<Frame {}>".format(self.value)


class Hamming:
	def __init__(self):
		self.parity = "par"

	def is_power(self,value,power):

		results = []
		divisor = power

		while True:

			if value % divisor == 0:
				results.append(divisor)
				value /= divisor
			else:
				divisor += 1

			if value == 1:
				break

		if results.count(power) < len(results):
			return False
		return True

	def parities(self,position):
		pass

	def calculate_bit_parity(self,set_data):
		pass

	def encode(self,frame):

		original_list = list(frame.value)
		list_with_power_two = []

		position_new_list = 0

		if not frame.is_valid():

			return False

		else:

			while original_list:

				actual_position = len(list_with_power_two) + 1

				# Then it's position power of two
				if self.is_power(actual_position,2): 

					list_with_power_two.append("")

					position_new_list += 1

				else:

					element_original_list = int(original_list.pop(0))

					list_with_power_two.append(element_original_list)

		return list_with_power_two
				
	def check(self,frame):
		return frame

# Paridade : par
# 0 1 1
#  (1) (0) 0 (0) 1 1

h = Hamming()
print(h.encode(Frame('011')))