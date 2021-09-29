import unittest

from sales_taxes import round_up_tax


class MyTestCase(unittest.TestCase):
    def test_round_up_tax(self):
        self.assertEqual(0.05, round_up_tax(0.02))
        self.assertEqual(0.05, round_up_tax(0.05))
        self.assertEqual(0.05, round_up_tax(0.0001))
        self.assertEqual(1.15, round_up_tax(1.14))


if __name__ == '__main__':
    unittest.main()
