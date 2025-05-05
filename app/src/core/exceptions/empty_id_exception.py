from app.src.core.exceptions.transaction_exception import TransactionException


class EmptyIdException(TransactionException):
    def __init__(self, obj: str):
        super().__init__(f"id da {obj} vazio")