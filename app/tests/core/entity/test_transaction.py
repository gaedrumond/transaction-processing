import unittest

from app.src.core.entity.account import Account
from app.src.core.entity.details import Details
from app.src.core.entity.holder import Holder
from app.src.core.entity.third_party import Partner
from app.src.core.entity.transaction import Transaction
from app.src.core.exceptions.empty_exception import EmptyException


class TransactionTestCase(unittest.TestCase):
    def setUp(self):
        self._transaction_id = "txn12345"
        self._account = Account('acc67890', Holder('John Doe', 'john.doe@example.com', '82.725.494/0001-36'))
        self._details = Details(500.00, 'USD', '2023-10-01T14:48:00.000Z', 'Payment for invoce #789')
        self._partner = Partner('Payment Processor Inc.', 'support@paymentprocessor.com')

    def test_create_transaction_object(self):
        transaction = Transaction(self._transaction_id, self._account, self._details, self._partner)
        self.assertEqual(self._transaction_id, transaction.id)
        self.assertEqual(self._account, transaction.account)
        self.assertEqual(self._details, transaction.details)
        self.assertEqual(self._partner, transaction.partner)

    def test_create_transaction_with_empty_id(self):
        try:
            Transaction('            ', self._account, self._details, self._partner)
        except Exception as exp:
            self.assertRaises(EmptyException)


    def test_create_transaction_with_no_id(self):
        try:
            Transaction(account=self._account, details=self._details, partner=self._partner)
        except Exception as exp:
            self.assertRaises(EmptyException)

if __name__ == '__main__':
    unittest.main()

