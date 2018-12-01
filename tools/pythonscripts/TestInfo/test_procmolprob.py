import unittest
from NMRFxMolProbTools import NMRFxMolProbTools as pmp


class TestProcessMP(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.inst1 = pmp()

    def test_organize_mpout(self):
        """Check if the output of method is empty or not by describing and asserting its bool() value"""
        result = self.inst1.org_molprobity_output('cy_tests_fa.txt')
        self.assertTrue(result, True)

    def test_org_mpout_itype(self):
        """Make sure to check input type and raise an error if necessary"""
        self.assertRaises(TypeError, pmp.org_molprobity_output, 123)


if __name__ == '__main__':
    unittest.main()
