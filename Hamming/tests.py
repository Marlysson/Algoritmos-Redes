# # -*- coding:utf-8 -*-

import unittest
from hamming import Hamming , Frame

class TestFrame(unittest.TestCase):

	def setUp(self):
		self.frame1 = Frame("01011")
		self.frame2 = Frame("01012")

	def test_frame_value_should_be_valid(self):

		self.assertTrue(self.frame1.is_valid())
		self.assertFalse(self.frame2.is_valid())

	def test_frame_should_return_equals_object_comparison_by_value(self):
		self.assertEqual(Frame("0101"),Frame("0101"))

	def test_frame_should_return_different_frames(self):
		self.assertNotEqual(Frame("010101"),Frame("0101"))


class TestHamming(unittest.TestCase):

	def setUp(self):
		self.hamming = Hamming("par")
	
	def test_power_positive_numbers(self):
		data_tests = []

		power_two =   { 2 : [ 2, 4, 8, 16, 32, 64] }
		power_three = { 3 : [ 3, 9, 27, 81] }
		power_four =  { 4 : [ 4, 16, 64] }
		power_ten =   { 10: [10, 100, 1000] }

		data_tests.extend([power_two,power_three,power_four,power_ten])

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

	def test_frame_encoded_should_be_correct(self):
		frame1 = Frame("011")
		frame2 = Frame("11100101010110")
		frame3 = Frame("0100")

		frame1_encoded = self.hamming.encode(frame1)
		frame2_encoded = self.hamming.encode(frame2)
		frame3_encoded = self.hamming.encode(frame3)

		self.assertEqual(Frame("110011"),frame1_encoded)
		self.assertEqual(Frame("1110110101010100110"),frame2_encoded)
		self.assertNotEqual(Frame("1100110"),frame3_encoded)

	def test_calculate_parity_of_dataset_bits(self):
		dataset = [0,1,1,0] #Global parity : par

		parity = self.hamming.calculate_parity(dataset)

		self.assertEqual(parity,0)

	def test_calculate_parity_of_dataset_changing_parity(self):

		dataset = [0,1,1,1] #With global parity : par

		parity_par = self.hamming.calculate_parity(dataset)

		self.hamming.parity = "impar"

		parity_impar = self.hamming.calculate_parity(dataset)

		self.assertEqual(1,parity_par)
		self.assertEqual(0,parity_impar)

	@unittest.skip("not implemented")
	def test_frame_check_should_be_correct(self):

		frame = Frame("0001111")

		check = self.hamming.check(frame)

		self.assertTrue(check)

if __name__ == "__main__":
	unittest.main(verbosity=2)