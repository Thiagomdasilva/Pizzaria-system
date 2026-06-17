from domain.interfaces.pedido_repository_interface import (
    PedidoRepositoryInterface
)


class ListarPedidos:

    def __init__(
            self,
            repository: PedidoRepositoryInterface):

        self.repository = repository


    def executar(self):

        return self.repository.listar()