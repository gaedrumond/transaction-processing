from abc import ABC, abstractmethod

class SecretsPort(ABC):

    @abstractmethod
    def get_secret(self, key:str):
        pass