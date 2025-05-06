from decimal import Decimal

from app.src.core.exceptions.transaction_exception import TransactionException


class InvalidAmountValue(TransactionException):
    def __init__(self, value: Decimal):
        super().__init__(f"o valor {value} e invalido")