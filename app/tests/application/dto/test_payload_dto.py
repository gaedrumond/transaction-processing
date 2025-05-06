import unittest

from app.src.application.dto.payload_dto import PayloadDto
from app.src.core.entity.account import Account
from app.src.core.entity.details import Details
from app.src.core.entity.holder import Holder
from app.src.core.entity.third_party import Partner
from app.src.core.entity.transaction import Transaction


class PayloadDtoTestCase(unittest.TestCase):

    def setUp(self):
        self._payload = PayloadDto({'transaction_id': 'txn12345',
                          'account': {'account_id': 'acc67890', 'holder_name': 'John Doe',
                                      'holder_email': 'john.doe@example.com', 'holder_document': '123.456.789-00'},
                          'transaction_details': {'amount': 500.0, 'currency': 'USD',
                                                  'transaction_date': '2023-10-01T14:48:00.000Z',
                                                  'description': 'Payment for invoce #789'},
                          'third_party': {'name': 'Payment Processor Inc.',
                                          'contact_email': 'support@paymentprocessor.com'}})
        self._transaction = Transaction('txn12345',
                                        Account('acc67890', Holder('John Doe', 'john.doe@example.com', '016.603.130-58')),
                                        Details(500.0, 'USD', '2023-10-01T14:48:00.000Z', 'Payment for invoce #789'),
                                        Partner('Payment Processor Inc.', 'support@paymentprocessor.com'))


    def test_map_payload_to_transaction(self):
        transaction = self._payload.to_transaction()
        self.assertEqual(self._transaction, transaction)

if __name__ == '__main__':
    unittest.main()
