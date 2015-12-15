
class Money(object):

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency.upper()

    def __repr__(self):
        return "%.2f %s" % (self.amount, self.currency)
