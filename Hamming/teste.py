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

	@unittest.skip
	def test_create_list_with_spaces_to_power_of_two(self):
		frame1 = Frame("011")
		frame2 = Frame("10101101011100110")

		return_frame_1 = ["","",0,"",1,1]
		return_frame_2 = ["","",1,"",0,1,0,"",1,1,0,1,0,1,1,"",1,0,0,1,1,0]

		self.assertEqual(return_frame_1,self.hamming.encode(frame1))
		self.assertEqual(return_frame_2,self.hamming.encode(frame2))

	@unittest.skip
	def test_frame_encoded_should_be_correct(self):
		frame = Frame("0111")

		encoded = self.hamming.encode(frame)

		self.assertEqual(Frame("0001111"),encoded)

	@unittest.skip
	def test_frame_check_should_be_correct(self):

		frame = Frame("0001111")

		check = self.hamming.check(frame)

		self.assertTrue(check)


if __name__ == "__main__":
	unittest.main()