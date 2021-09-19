import unittest
from main import get_number_from_index

class Test_2048(unittest.TestCase):

	def test_1(self):
		self.assertEqual(get_number_from_index(1, 2), 8)

if __name__ == "main":
	unittest.main()

			