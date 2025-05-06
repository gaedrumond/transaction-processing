import unittest
from decimal import Decimal
from unittest.mock import MagicMock

from app.src.application.dto.payload_dto import PayloadDto
from app.src.application.ports.currency_port import CurrencyPort
from app.src.application.ports.data_store_port import DataStorePort
from app.src.application.use_cases.process_transaction_data import ProcessTransactionData
from app.src.core.exceptions.currency_conversion_exception import CurrencyConversionException


class ProcessTransactionDataTestCase(unittest.TestCase):
    def setUp(self):
        self._payload = PayloadDto({'transaction_id': 'txn12345',
                          'account': {'account_id': 'acc67890', 'holder_name': 'John Doe',
                                      'holder_email': 'john.doe@example.com', 'holder_document': '123.456.789-00'},
                          'transaction_details': {'amount': 500.0, 'currency': 'USD',
                                                  'transaction_date': '2023-10-01T14:48:00.000Z',
                                                  'description': 'Payment for invoce #789'},
                          'third_party': {'name': 'Payment Processor Inc.',
                                          'contact_email': 'support@paymentprocessor.com'}})

    def test_processing_transaction_data(self):
        mock_convert = MagicMock(spec=CurrencyPort)
        mock_store = MagicMock(spec=DataStorePort)
        mock_convert.convert_to_brl.return_value = Decimal('2500.00')

        process = ProcessTransactionData(mock_convert, mock_store)
        process.process_data(self._payload)

        mock_convert.convert_to_brl.assert_called()
        mock_store.save_transaction.assert_called()

if __name__ == '__main__':
    unittest.main()
