from currency_rates import rates


class Money(object):

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency.upper()

    def __repr__(self):
        return "%.2f %s" % (self.amount, self.currency)

    def __getattr__(self, currency):
        def convert():
            return self.to_currency(currency)
        return convert

    def to_currency(self, currency):
        currency = currency.split('_')[1].upper()
        amount = self.amount
        base_currency_rates = rates.get(self.currency)

        new_amount = amount * base_currency_rates.get(currency)

        return Money(new_amount, currency)
