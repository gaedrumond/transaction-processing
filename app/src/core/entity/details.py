from dataclasses import dataclass
from decimal import Decimal
from datetime import datetime

from app.src.core.exceptions.empty_exception import EmptyException
from app.src.core.exceptions.invalid_amount import InvalidAmountValue
from app.src.utils.logger_mixin import logger


@dataclass(init=False)
class Details:
    def __init__(self, amount:Decimal, currency:str, transaction_date:str, description:str):
        if  amount <= Decimal('0.00'):
            logger.error(f"valor da transacao ({amount}) e invalido")
            raise InvalidAmountValue(amount)
        elif transaction_date.strip() == '':
            logger.error("data da transacao nao informado")
            raise EmptyException("data da transacao")
        logger.info("criando objeto detalhes da transacao")
        self._amount:Decimal = amount
        self._currency:str = currency
        self._transaction_date:str = transaction_date
        self._description:str = description

    @property
    def amount(self) -> Decimal:
        return self._amount

    @amount.setter
    def amount(self, amount:Decimal):
        self._amount = amount
        self._currency = 'BRL'

    @property
    def currency(self) -> str:
        return self._currency

    @property
    def date(self) -> str:
        return self._transaction_date

    @date.setter
    def date(self, date: str):
        self._transaction_date = date

    @property
    def description(self) -> str:
        return self._description