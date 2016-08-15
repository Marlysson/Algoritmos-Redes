# -*- coding:utf-8 -*-

import unittest
from crc import CRC , Frame

class TestCRC(unittest.TestCase):

	def setUp(self):
		self.crc = CRC("101101")

	def test_should_return_correctly_xor_division(self):
		bits_one = "010"
		bits_two = "100"

		division = self.crc.xor_division(bits_one,bits_two)

		self.assertEqual(division,"110")

	def test_should_return_false_parameters_invalids(self):

		bit_one = "0101"
		bit_two = "01010"

		bit_three = [1, 0, 1]

		self.assertRaises(Exception,self.crc.xor_division,bit_one,bit_two)
		self.assertRaises(Exception,self.crc.xor_division,bit_one,bit_three)

	@unittest.skip("After")
	def test_frame_encoded_correctly(self):

		frame = Frame("111100101")
		encoded = self.crc.encode(frame)

		self.assertEqual(encoded,Frame("11110010101010"))

	@unittest.skip("Execute after")
	def test_should_return_frame_checked_correctly(self):
		
		frame = Frame("111100101")
		encoded = self.crc.encode(frame)

		check = self.crc.check(encoded)

		self.assertTrue(check)

if __name__ == "__main__":
	unittest.main(verbosity=2)