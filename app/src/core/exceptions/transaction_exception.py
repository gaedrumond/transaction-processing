class TransactionException(Exception):
    def __init__(self, message: str= "nao foi possivel processar os dados da transacao"):
        super().__init__(message)