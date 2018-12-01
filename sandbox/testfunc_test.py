import unittest
from mock import patch, Mock
import testfunc


class TestCalculator(unittest.TestCase):

    @patch('testfunc.Calculator.multiply', return_value=4)
    def test_multiply(self, multiply):
        self.assertEqual(multiply(), 4)


if __name__ == '__main__':
    unittest.main(verbosity=2)
