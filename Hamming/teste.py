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
		self.hamming = Hamming()

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

	@unittest.skip("Test of a dependence ( private method )")
	def test_create_list_with_spaces_to_power_of_two(self):
		frame1 = Frame("011")
		frame2 = Frame("10101101011100110")

		return_frame_1 = ["","",0,"",1,1]
		return_frame_2 = ["","",1,"",0,1,0,"",1,1,0,1,0,1,1,"",1,0,0,1,1,0]

		self.assertEqual(return_frame_1,self.hamming.encode(frame1))
		self.assertEqual(return_frame_2,self.hamming.encode(frame2))


	@unittest.skip("skipped")
	def test_frame_encoded_should_be_correct(self):
		frame = Frame("0111")

		encoded = self.hamming.encode(frame)

		self.assertEqual(Frame("0001111"),encoded)

	@unittest.skip("skipped")
	def test_frame_check_should_be_correct(self):

		frame = Frame("0001111")

		check = self.hamming.check(frame)

		self.assertTrue(check)


if __name__ == "__main__":
	unittest.main(verbosity=2)