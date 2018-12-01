import unittest
from xplor import XPLOR


class TestXPlor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.inst1 = XPLOR('')

    def test_read_discon(self):
        pass

    def test_read_dihcon(self):
        pass


if __name__ == '__main__':
    unittest.main()
