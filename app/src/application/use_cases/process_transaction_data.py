from datetime import datetime

from app.src.application.dto.payload_dto import PayloadDto
from app.src.application.ports.currency_port import CurrencyPort
from app.src.application.ports.data_store_port import DataStorePort
from app.src.application.ports.secrets_port import SecretsPort
from app.src.utils.logger_mixin import logger


class ProcessTransactionData:
    def __init__(self, currency_port: CurrencyPort, data_store:DataStorePort):
        self._currency_port = currency_port
        self._data_store = data_store


    def process_data(self, payload: PayloadDto):
        transaction = payload.to_transaction()
        try:
            logger.info("iniciando processamento da transacao")
            date = transaction.details.date
            transaction.details.date=datetime.isoformat(datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.000Z"))

            currency = transaction.details.currency
            if currency != 'BRL':
                amount = transaction.details.amount
                transaction.details.amount = self._currency_port.convert_to_brl(currency, amount)

            self._data_store.save_transaction(transaction)
        except Exception as exp:
            raise