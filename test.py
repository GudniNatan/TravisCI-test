from my_math_lib import *
import unittest

class TestStringMethods(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(4, 6), 10)

    def test_sub(self):
        self.assertTrue(sub(10, 4))

    def test_multiply(self):
        s = 'hello world'
        self.assertEqual(multiply(5, 5), 25)
        # check that multiply fails when multiplying together strings
        with self.assertRaises(TypeError):
            multiply("ab" * "cd")

if __name__ == '__main__':
    unittest.main()
