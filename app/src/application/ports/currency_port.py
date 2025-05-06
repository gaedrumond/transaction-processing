from abc import ABC, abstractmethod
from decimal import Decimal


class CurrencyPort(ABC):

    @abstractmethod
    def convert_to_brl(self, base_currency:str, value:Decimal) -> Decimal:
        pass
