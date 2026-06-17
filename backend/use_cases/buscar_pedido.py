from domain.interfaces.pedido_repository_interface import (
    PedidoRepositoryInterface
)


class BuscarPedido:

    def __init__(
            self,
            repository: PedidoRepositoryInterface):

        self.repository = repository


    def executar(self, id):

        return self.repository.buscar_por_id(id)