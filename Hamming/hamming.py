# -*- coding:utf-8 -*-

'''

	API of Frame

	- is_valid()   # Verify whether bits of frame has values values not accepted.

	API of methods hamming algorithms

	- check()      # Calculate parity of bits and verify whether frame came 
	- encode()     # Put inside of frame the verification bit, in the positions of power of two.
	- decode()     # Verify whether the frame sent has bits wrong

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

	def encode(self,frame):

		original_list = list(frame.value)
		list_with_power_two = []

		index_original_list = 0
		position_new_list = 0

		while index_original_list < len(original_list):

			actual_position = len(list_with_power_two) + 1

			if actual_position == pow(2,position_new_list):

				list_with_power_two.append("")

				position_new_list += 1

			else:
				element_original_list = int(original_list[index_original_list])

				list_with_power_two.append(element_original_list)

				index_original_list += 1

		for position,element in enumerate(list_with_power_two,start=1):
			
			if element == "":
				

	def check(self,frame):
		return frame

# 0 1 1
#  _ _ 0 _ 1 1

h = Hamming()
print(h.encode(Frame("011")))