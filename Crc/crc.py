# -*- coding : utf-8 -*-

__author__ = "Marlysson Silva"
__contacts__ =  { "email"  : "marlysson5@gmail.com" , 
                  "social_network" : "facebook.com/marlysson7",
                  "github": "github.com/Marlysson"
                }


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

    def change_bit(self,position):

        if position <= 0 or position > len(self.value):
            raise ValueError("Invalid position, insert a valid position")
        else:
            frame_converted = list(map(int,self.value))
            position_readable = position - 1 

            frame_converted[position_readable] = 1 ^ frame_converted[position_readable]

            formated = "".join(map(str,frame_converted))

		#To return a immutable object, each modification
        # at object create a new.
        return Frame(formated) 

    def __eq__(self,other_frame):

        if self.value == other_frame.value:
            return True
        return False

    def __repr__(self):
        return "<Frame [{}]>".format(self.value)


class CRC:
	def __init__(self,generator):
		self.generator = generator

	def xor_division(self,value_one,value_two):

		mapped_to = lambda type,sequence : map(type,sequence)

		conditions = []
		conditions.append( type(value_one) == str)
		conditions.append( type(value_two) == str)
		conditions.append( len(value_one) == len(value_two) )

		if not all(conditions):
			raise Exception("They need have same length and same type")
		else:

			new_list = []

			for index,value in enumerate(value_one):
				# ^ -> bitwise operation XOR
				new_list.append(int(value) ^ int(value_two[index]))

			'''
			OR MAKING SO
			for index, value in enumerate(mapped_one):
				if value == mapped_two[index]:
					new_list.append(0)
				else:
					new_list.append(1)
			'''

		str_converted = mapped_to(str,new_list)

		return "".join(list(str_converted))

	def encode(self,frame):

		level_generator = len(self.generator) - 1

		mx_r_bits = frame.value + level_generator*"0"

		current_index = 0
		data_to_process = ""

		while current_index < len(mx_r_bits) - 1:

			#To generate value that will be processed together with generator
			while len(data_to_process) < len(self.generator):
				data_to_process += mx_r_bits[current_index]

				current_index += 1	

			result_operation = self.xor_division(data_to_process,self.generator)

			data_to_process = result_operation.lstrip("0")
			
	def check(self,frame):
		pass

c =   CRC("101101")
f = Frame("111100101")

print(c.encode(f))
