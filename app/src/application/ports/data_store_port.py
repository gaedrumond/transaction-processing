from abc import ABC, abstractmethod

from app.src.core.entity.transaction import Transaction


class DataStorePort(ABC):

    @abstractmethod
    def save_transaction(self, transaction: Transaction) -> None:
        pass