import unittest

from sales_taxes import round_up_tax, get_tax_rate_by_description, read_line, basket2receipt, main


class MyTestCase(unittest.TestCase):
    def test_basket2receipt(self):
        input_1 = "1 book at 12.49\n1 music CD at 14.99\n1 chocolate bar at 0.85"
        input_2 = " 1 imported box of chocolates at 10.00\n1 imported bottle of perfume at 47.50"
        input_3 = "1 imported bottle of perfume at 27.99 \n1 bottle of perfume at 18.99 \n" \
                  "1 packet of headache pills at 9.75 \n1 box of imported chocolates at 11.25"
        input_4 = "1 imported bottle of perfume at 27.99 \n1 bottle of perfume at 18.99 \n" \
                  "2 packet of headache pills at 9.75 \n1 box of imported chocolates at 11.25"  # like #3 but 2 packets
        output_1 = "1 book: 12.49\n1 music CD: 16.49\n1 chocolate bar: 0.85\nSales Taxes: 1.50\nTotal: 29.83"
        output_2 = "1 imported box of chocolates: 10.50\n1 imported bottle of perfume: 54.65\nSales Taxes: 7.65\n" \
                   "Total: 65.15"
        output_3 = "1 imported bottle of perfume: 32.19\n1 bottle of perfume: 20.89\n" \
                   "1 packet of headache pills: 9.75\n1 box of imported chocolates: 11.85\nSales Taxes: 6.70\n" \
                   "Total: 74.68"
        output_4 = "1 imported bottle of perfume: 32.19\n1 bottle of perfume: 20.89\n" \
                   "2 packet of headache pills: 19.50\n1 box of imported chocolates: 11.85\nSales Taxes: 6.70\n" \
                   "Total: 84.43"
        self.assertEqual(output_1, basket2receipt(input_1.splitlines()))
        self.assertEqual(output_2, basket2receipt(input_2.splitlines()))
        self.assertEqual(output_3, basket2receipt(input_3.splitlines()))
        self.assertEqual(output_4, basket2receipt(input_4.splitlines()))

    def test_main(self):
        self.assertRaises(AttributeError, main, ["one"])  # must have at least 2 args
        self.assertRaises(ValueError, main, ["me", "fail_test.txt"])

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
