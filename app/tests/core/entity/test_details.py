import unittest
from decimal import Decimal

from app.src.core.entity.details import Details
from app.src.core.exceptions.empty_exception import EmptyException
from app.src.core.exceptions.invalid_amount import InvalidAmountValue


class DetailsTestCase(unittest.TestCase):

    def setUp(self):
        self._amount = Decimal('50.00')
        self._currency = 'BRL'
        self._transaction_date = '2023-10-01T14:48:00.000Z'
        self._description = 'some transaction'

    def test_create_transaction_details_object(self):
        try:
            details = Details(self._amount, self._currency, self._transaction_date, self._description)
            self.assertEqual(self._amount, details.amount)
            self.assertEqual(self._currency, details.currency)
            self.assertEqual(self._transaction_date, details.date)
            self.assertEqual(self._description, details.description)
        except Exception as exp:
            self.assertFalse(exp)

    def test_create_transaction_details_with_negative_amount(self):
        try:
            Details(-Decimal('4.00'), self._currency, self._transaction_date, self._description)
        except Exception as exp:
            self.assertRaises(InvalidAmountValue)

    def test_create_transaction_details_with_zero_amount(self):
        try:
            Details(-Decimal('0.00'), self._currency, self._transaction_date, self._description)
        except Exception as exp:
            self.assertRaises(InvalidAmountValue)

    def test_create_transaction_details_with_no_amount(self):
        try:
            Details(currency=self._currency, transaction_date=self._transaction_date, description=self._description)
        except Exception as exp:
            self.assertRaises(InvalidAmountValue)

    def test_create_transaction_details_with_empty_date(self):
        try:
            Details(self._amount, self._currency, '      ', self._description)
        except Exception as exp:
            self.assertRaises(EmptyException)

    def test_create_transaction_details_with_no_date(self):
        try:
            Details(amount=self._amount, currency=self._currency, description=self._description)
        except Exception as exp:
            self.assertRaises(EmptyException)

if __name__ == '__main__':
    unittest.main()
