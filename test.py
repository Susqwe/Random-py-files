from unittest import TestCase

from solver import add


class TestAddCase(TestCase):
	def test_ok(self):
		res = add(1, 2)
		self.assertEqual(res, 3)