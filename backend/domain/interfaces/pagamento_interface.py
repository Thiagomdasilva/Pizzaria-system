from abc import ABC, abstractmethod

class PagamentoInterface(ABC):

    @abstractmethod
    def pagar(self, valor):
        pass