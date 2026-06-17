from abc import ABC, abstractmethod


class PedidoRepositoryInterface(ABC):

    @abstractmethod
    def salvar(
            self,
            cliente,
            pizza,
            quantidade):
        pass


    @abstractmethod
    def listar(self):
        pass


    @abstractmethod
    def buscar_por_id(self, id):
        pass


    @abstractmethod
    def atualizar(
            self,
            id,
            cliente,
            pizza,
            quantidade):
        pass


    @abstractmethod
    def deletar(self, id):
        pass