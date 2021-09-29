import unittest

from sales_taxes import round_up_tax, get_tax_rate_by_description, read_line


class MyTestCase(unittest.TestCase):
    def test_read_line(self):
        self.assertTupleEqual((1, "imported box of chocolates", 10.00),
                              read_line("1 imported box of chocolates at 10.00"))
        self.assertEqual((None, None, None), read_line("1.2 imported box of chocolates at 10.00"))
        self.assertEqual((None, None, None), read_line("1 imported box of chocolates at 10.00 10"))
        self.assertEqual((None, None, None), read_line("xxxx"))


    def test_get_tax_rate(self):
        # books
        self.assertEqual(0.0, get_tax_rate_by_description("Harry Potter BOOK"))
        self.assertEqual(0.0, get_tax_rate_by_description("Harry Potter books"))
        # food
        self.assertEqual(0.0, get_tax_rate_by_description("lindt chocolates white"))
        # medicine
        self.assertEqual(0.0, get_tax_rate_by_description("aspirin pills"))
        # others
        self.assertEqual(0.1, get_tax_rate_by_description("blue car"))
        # duty
        self.assertEqual(0.15, get_tax_rate_by_description("imported blue car"))
        self.assertEqual(0.05, get_tax_rate_by_description("imported chocolate"))

    def test_round_up_tax(self):
        self.assertEqual(0.05, round_up_tax(0.02))
        self.assertEqual(0.05, round_up_tax(0.05))
        self.assertEqual(0.05, round_up_tax(0.0001))
        self.assertEqual(1.15, round_up_tax(1.14))


if __name__ == '__main__':
    unittest.main()
