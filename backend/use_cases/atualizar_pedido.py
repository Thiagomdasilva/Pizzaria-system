from domain.interfaces.pedido_repository_interface import (
    PedidoRepositoryInterface
)


class AtualizarPedido:

    def __init__(
            self,
            repository: PedidoRepositoryInterface):

        self.repository = repository


    def executar(
            self,
            id,
            cliente,
            pizza,
            quantidade):

        return self.repository.atualizar(
            id,
            cliente,
            pizza,
            quantidade
        )