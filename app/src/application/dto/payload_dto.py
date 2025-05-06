from dataclasses import dataclass
from decimal import Decimal

from app.src.core.entity.account import Account
from app.src.core.entity.details import Details
from app.src.core.entity.holder import Holder
from app.src.core.entity.third_party import Partner
from app.src.core.entity.transaction import Transaction
from app.src.utils.logger_mixin import logger


@dataclass
class PayloadDto:
    _content: dict

    @property
    def content(self)-> dict:
        return self._content

    @content.setter
    def content(self, *kwargs):
        self._content.update(kwargs)

    def to_transaction(self) -> Transaction:
        logger.info("iniciando a transformacao do payload em transacao")
        account = self._content.get('account', {})
        details = self._content.get('transaction_details', {})
        partner = self._content.get('third_party', {})
        return Transaction(self._content.get('transaction_id', ''),
                           Account(account.get('account_id', ''), Holder(account.get('holder_name', ''), account.get('holder_email', ''), account.get('holder_document', ''))),
                           Details(Decimal(details.get('amount', '')), details.get('currency', ''), details.get('transaction_date', ''), details.get('description', '')),
                           Partner(partner.get('name', ''), partner.get('contact_email','')))