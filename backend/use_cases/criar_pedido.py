from domain.interfaces.pedido_repository_interface import (
    PedidoRepositoryInterface
)


class CriarPedido:

    def __init__(
            self,
            repository: PedidoRepositoryInterface):

        self.repository = repository


    def executar(
            self,
            cliente,
            pizza,
            quantidade):

        return self.repository.salvar(
            cliente,
            pizza,
            quantidade
        )