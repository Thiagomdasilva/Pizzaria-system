from repositories.pedido_repository import PedidoRepository


class RepositoryFactory:

    @staticmethod
    def criar_repository():

        return PedidoRepository()