from dataclasses import dataclass

from app.src.utils.logger_mixin import logger


@dataclass(init=False)
class Partner:
    def __init__(self, name:str, email:str):
        logger.info("criando objeto de parceiros")
        self._name:str = name
        self._email:str = email

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email