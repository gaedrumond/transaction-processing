from app.src.core.exceptions.transaction_exception import TransactionException

class InvalidDocumentException(TransactionException):
    def __init__(self, message:str= "documento invalido"):
        super().__init__(message)