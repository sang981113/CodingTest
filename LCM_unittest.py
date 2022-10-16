import LCM

import unittest

class LCM_test(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(LCM.gcd(10, 5), 5)

    def test_gcd2(self):
        self.assertEqual(LCM.gcd(99, 45), 9)

    def test_lcm(self):
        self.assertEqual(LCM.lcm(8, 14), 56)

if __name__ == '__main__':
    unittest.main()