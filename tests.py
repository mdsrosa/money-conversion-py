from money_conversion.money import Money
import unittest


class MoneyClassTest(unittest.TestCase):
    def setUp(self):
        self.twenty_euro = Money(20, 'EUR')

    def test_convert_euro_to_usd(self):
        twenty_usd = self.twenty_euro.to_usd()

        self.assertIsInstance(twenty_usd, Money)
        self.assertEqual('USD', twenty_usd.currency)
        self.assertEqual(21.8, twenty_usd.amount)

    def test_convert_euro_to_brl(self):
        twenty_brl = self.twenty_euro.to_brl()

        self.assertIsInstance(twenty_brl, Money)
        self.assertEqual('BRL', twenty_brl.currency)
        self.assertEqual(85, twenty_brl.amount)


if __name__ == '__main__':
    unittest.main()