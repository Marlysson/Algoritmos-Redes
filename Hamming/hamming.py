# -*- coding:utf-8 -*-

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



class Hamming:
    def __init__(self,parity):
        if parity not in ["pair","odd"]:
            raise ValueError("Invalid Value")

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

        if results.count(power) != len(results):
           return False
        return True


    def divisors(self,position):
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

        if self.parity == "pair":
            if is_pair(count_one):
                value = 0
            else:
                value = 1

        elif self.parity == "odd":
            if is_pair(count_one):
                value = 1
            else:
                value = 0

        return value

    def bits_verified_by(self,sequence,power_two):

        dataset_bit = []

        for position,value in enumerate(sequence):
            position_readable = position + 1

            if not self.is_power(position_readable,2):
                divisors_position = self.divisors(position_readable)

                if power_two in divisors_position:
                    real_position = position_readable - 1

                    dataset_bit.append(sequence[real_position])

        return dataset_bit

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

        for position , actual_element in enumerate(list_with_power_two):

            position_readable = position + 1

            # Found parity position
            if self.is_power(position_readable,2):

                sequence_verified = self.bits_verified_by(list_with_power_two,position_readable)

                parity = self.calculate_parity(sequence_verified)

                # Minus 1(one) because the list original index begin in 0 , and position_readable
                # begin of 1(one) , human readable
                list_with_power_two[position_readable-1] = parity

        formated = "".join(map(str,list_with_power_two))

        return Frame(formated)
			
    def check(self,frame):
		
        original_frame = list(map(int,frame.value))

        bits_wrong = 0

        for index, value_position in enumerate(original_frame):

            position_readable = index + 1

            if self.is_power(position_readable,2):

                sequence_verified = self.bits_verified_by(original_frame,position_readable)
				
                parity = self.calculate_parity(sequence_verified)

                if parity != original_frame[position_readable-1]:
                    bits_wrong += 1

        if bits_wrong > 0:
            return False
        return True

    def __repr__(self):
        return "<Hamming: parity = ['{}']>".format(self.parity)