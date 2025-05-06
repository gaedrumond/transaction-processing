from dataclasses import dataclass

from app.src.core.entity.account import Account
from app.src.core.entity.details import Details
from app.src.core.entity.third_party import Partner
from app.src.core.exceptions.empty_exception import EmptyException
from app.src.utils.logger_mixin import logger


@dataclass(init=False)
class Transaction:
    def __init__(self, id:str, account: Account, details: Details, partner: Partner):
        if id.strip() == '':
            logger.error("id da transacao vazio")
            raise EmptyException('id da transacao')
        logger.info("criando objeto da transacao")
        self._id:str = id
        self._account:Account = account
        self._details:Details = details
        self._partner:Partner = partner


    @property
    def id(self) -> str:
        return self._id

    @property
    def account(self) -> Account:
        return self._account

    @property
    def details(self) -> Details:
        return self._details

    @property
    def partner(self) -> Partner:
        return self._partner