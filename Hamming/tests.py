# # -*- coding:utf-8 -*-

import unittest
from hamming import Hamming , Frame

class TestFrame(unittest.TestCase):

	def setUp(self):
		self.frame1 = Frame("01011")
		self.frame2 = Frame("1234")

	def test_frame_value_should_be_valid(self):

		self.assertTrue(self.frame1.is_valid())
		self.assertFalse(self.frame2.is_valid())

	def test_frame_should_return_equals_object_comparison_by_value(self):
		self.assertEqual(Frame("0101"),Frame("0101"))

	def test_frame_should_return_different_frames(self):
		self.assertNotEqual(Frame("010101"),Frame("0101"))

	def test_change_bit_value_correct(self):
		frame1 = Frame("0101") 
		frame2 = Frame("01")

		new_frame1 = frame1.change_bit(1)
		new_frame2 = frame2.change_bit(2)

		self.assertEqual(new_frame1,Frame("1101"))
		self.assertEqual(new_frame2,Frame("00"))

	def test_change_wrong_position_should_raise_exception(self):

		frame = Frame("0101")

		self.assertRaises(ValueError,frame.change_bit,5)
		self.assertRaises(ValueError,frame.change_bit,-2)


class TestHammingAlgorithm(unittest.TestCase):

	def setUp(self):
		self.hamming = Hamming("pair")
	
	def test_valid_value_of_parity(self):
		with self.assertRaises(ValueError):
			hamming = Hamming("two")

	def test_power_positive_numbers(self):
		data_tests = []

		power_of_two =   { 2 : [ 2, 4, 8, 16, 32, 64] }
		power_of_three = { 3 : [ 3, 9, 27, 81] }
		power_of_four =  { 4 : [ 4, 16, 64] }
		power_of_ten =   { 10: [10, 100, 1000] }

		data_tests.extend([power_of_two,power_of_three,power_of_four,power_of_ten])

		for test in data_tests:
			for power_key, powers_values in test.items():
				for power in powers_values:
					self.assertTrue(self.hamming.is_power(power,power_key))

	def test_power_invalids(self):
		invalids_numbers = [ 0, -2, -4, -16 ]
		differents_powers = [10, 12, 20]

		with self.assertRaises(ValueError):
			for number in invalids_numbers:
				self.hamming.is_power(number,2)

		for value in differents_powers:
			self.assertFalse(self.hamming.is_power(value,3))


	def test_calculate_parity_of_dataset_bits(self):
		dataset = [0,1,1,0] #Global parity : par

		parity = self.hamming.calculate_parity(dataset)

		self.assertEqual(parity,0)

	def test_calculate_parity_of_dataset_changing_parity(self):

		hamming = Hamming("pair")

		dataset = [0,1,1,1] #With global parity : par
		parity_par = hamming.calculate_parity(dataset)

		hamming.parity = "odd"

		parity_impar = hamming.calculate_parity(dataset)

		self.assertEqual(1,parity_par)
		self.assertEqual(0,parity_impar)

	def test_frame_encoded_should_be_correct(self):
		frame1 = Frame("011")
		frame2 = Frame("11100101010110")
		frame3 = Frame("111")

		frame1_encoded = self.hamming.encode(frame1)
		frame2_encoded = self.hamming.encode(frame2)
		frame3_encoded = self.hamming.encode(frame3)

		self.assertEqual(Frame("110011"),frame1_encoded)
		self.assertEqual(Frame("1110110101010100110"),frame2_encoded)
		self.assertNotEqual(Frame("00101"),frame3_encoded)

	def test_frame_check_should_be_correct(self):

		frame1 = Frame("110011")
		frame2 = Frame("1110110101010100110")

		check_frame_1 = self.hamming.check(frame1)
		check_frame_2 = self.hamming.check(frame2)

		self.assertTrue(check_frame_1)
		self.assertTrue(check_frame_2)

	def test_frame_check_should_be_incorrect(self):

		frame1 = Frame("011")
		frame2 = Frame("11100101010110")

		frame1_encoded = self.hamming.encode(frame1).change_bit(1)
		frame2_encoded = self.hamming.encode(frame2).change_bit(5)

		check_frame_1 = self.hamming.check(frame1_encoded)
		check_frame_2 = self.hamming.check(frame2_encoded)

		self.assertFalse(check_frame_1)
		self.assertFalse(check_frame_2)

	def test_checks_vality_of_frame_changing_parity(self):
		hamming = Hamming("pair")

		frame = Frame("011")

		frame_encoded = hamming.encode(frame)

		hamming.parity = "odd"

		check_frame = hamming.check(frame_encoded)

		self.assertFalse(check_frame)

	def test_must_return_position_changed_from_frame(self):
		
		hamming = Hamming('pair')

		frame = Frame("001")

		encoded = hamming.encode(frame)

		changed = encoded.change_bit(6)

		wrong_position = hamming.wrong_position(changed)

		self.assertEqual(6,wrong_position)

	def test_must_fix_a_wrong_frame(self):

		hamming = Hamming('pair')

		frame = Frame("001")

		encoded = hamming.encode(frame)
		print(encoded)

		changed = encoded.change_bit(6)
		print(changed)
		self.assertFalse(hamming.check(changed))

		fixed = hamming.fix(changed)
		print(fixed)
		check = hamming.check(fixed)

		self.assertTrue(check)

if __name__ == "__main__":
	unittest.main(verbosity=2)