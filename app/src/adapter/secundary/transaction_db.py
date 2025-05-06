from dataclasses import dataclass

import boto3

from app.src.application.ports.data_store_port import DataStorePort
from app.src.core.entity.transaction import Transaction

@dataclass
class TransactionDB(DataStorePort):
    _client: boto3.client
    _table: str

    def save_transaction(self, transaction: Transaction) -> None:
        self._client.put_item(
            TableName=self._table,
            Item={
                "transaction_id": {'S': transaction.id},
                "account": {
                    'M': {
                        "account_id": {'S': transaction.account.id},
                        "holder_name": {'S': transaction.account.holder.name},
                        "holder_email": {'S': transaction.account.holder.email},
                        "holder_document": {'S': transaction.account.holder.document},
                    },
                },
                "transaction_details": {
                    'M': {
                        "amount": {'S': transaction.details.amount},
                        "currency": {'S': transaction.details.currency},
                        "transaction_date": {'S': transaction.details.date},
                        "description": {'S': transaction.details.description},
                    },
                },
                "third_party": {
                    'M': {
                        "name": {'S': transaction.partner.name},
                        "contact_email": {'S': transaction.partner.email},
                    },
                },
            }
        )