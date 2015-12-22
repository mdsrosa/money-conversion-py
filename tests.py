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

    def test_invalid_method_pattern_call(self):
        with self.assertRaises(AttributeError):
            twenty_brl = self.twenty_euro.batman()

    def test_sum_operation_between_eur_and_dollar(self):
        fifty_eur = Money(50, 'EUR')
        twenty_dollars = Money(20, 'USD')

        money = fifty_eur + twenty_dollars

        self.assertEqual(money.amount, 68.2)
        self.assertEqual(money.currency, 'EUR')

        # test if a new object is returned
        self.assertNotEqual(id(fifty_eur), id(money))

    def test_sum_operation_between_dollar_and_eur(self):
        fifty_eur = Money(50, 'EUR')
        twenty_dollars = Money(20, 'USD')

        money = twenty_dollars + fifty_eur

        self.assertEqual(money.amount, 74.5)
        self.assertEqual(money.currency, 'USD')

        # test if a new object is returned
        self.assertNotEqual(id(fifty_eur), id(money))

if __name__ == '__main__':
    unittest.main()