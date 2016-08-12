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

class TestHamming(unittest.TestCase):

	def setUp(self):
		self.hamming = Hamming("par")

	def test_power_of_two_valids(self):
		valids = [1,2,4,8,16,32,64]

		for value in valids:
			self.assertTrue(self.hamming.is_power(value,2))

	def test_power_of_two_invalids(self):
		# Verify possibility of values are negatives. But the function is_valid()
		# Already to verify wheither frame is valid.

		invalids = [6,10,14,20,24]

		for value in invalids:
			self.assertFalse(self.hamming.is_power(value,2))

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
		#Global parity : par

		dataset = [0,1,1,0]

		parity = self.hamming.calculate_parity(dataset)

		self.assertEqual(parity,0)

	def test_calculate_parity_of_dataset_changing_parity_of_hamming(self):

		dataset = [0,1,1,1]

		parity_par = self.hamming.calculate_parity(dataset)

		self.hamming.parity = "impar"

		parity_impar = self.hamming.calculate_parity(dataset)

		self.assertEqual(1,parity_par)
		self.assertEqual(0,parity_impar)

	@unittest.skip("skipped")
	def test_frame_check_should_be_correct(self):

		frame = Frame("0001111")

		check = self.hamming.check(frame)

		self.assertTrue(check)


if __name__ == "__main__":
	unittest.main(verbosity=2)