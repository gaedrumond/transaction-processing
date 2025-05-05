from dataclasses import dataclass
from re import match

from app.src.core.exceptions.invalid_document_exception import InvalidDocumentException
from app.src.utils.logger_mixin import logger


@dataclass(init=False)
class Holder:
    def __init__(self, name: str, email: str, document: str):
        if match(r'[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}', document):
            self._document_type = 'cpf'
        elif match(r'[0-9]{2}[.][0-9]{3}[.][0-9]{3}/[0-9]{4}-[0-9]{2}', document):
            self._document_type = 'cnpj'
        else:
            logger.error("nao foi possivel criar a transacao pois o documento eh invalido")
            raise InvalidDocumentException()
        logger.info("criando holder da transacao")
        self._name = name
        self._email = email
        self._document = document

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def document(self):
        return self._document

    @property
    def document_type(self):
        return self._document_type