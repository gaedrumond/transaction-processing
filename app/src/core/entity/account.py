from dataclasses import dataclass

from app.src.core.entity.holder import Holder
from app.src.core.exceptions.empty_exception import EmptyException
from app.src.utils.logger_mixin import logger


@dataclass(init=False)
class Account:
    def __init__(self, id: str, holder: Holder):
        if id.strip() == '':
            logger.error("id da conta esta vazio")
            raise EmptyException("conta")
        logger.info("criando objeto da conta")
        self._id:str = id
        self._holder:Holder = holder

    @property
    def id(self) -> str:
        return self._id

    @property
    def holder(self) -> Holder:
        return  self._holder