from app.src.core.exceptions.transaction_exception import TransactionException


class EmptyException(TransactionException):
    def __init__(self, obj: str):
        super().__init__(f"{obj} vazio")