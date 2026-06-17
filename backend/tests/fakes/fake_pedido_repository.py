from domain.entities.pedido import Pedido


class FakePedidoRepository:

    def __init__(self):

        self.pedidos = []

        self.id = 1


    def salvar(
            self,
            cliente,
            pizza,
            quantidade):

        pedido = Pedido(
            self.id,
            cliente,
            pizza,
            quantidade
        )

        self.pedidos.append(pedido)

        self.id += 1

        return pedido


    def listar(self):

        return self.pedidos


    def buscar_por_id(self, id):

        for pedido in self.pedidos:

            if pedido.id == id:

                return pedido

        return None


    def atualizar(
            self,
            id,
            cliente,
            pizza,
            quantidade):

        pedido = self.buscar_por_id(id)

        if pedido:

            pedido.cliente = cliente

            pedido.pizza = pizza

            pedido.quantidade = quantidade

        return pedido


    def deletar(self, id):

        pedido = self.buscar_por_id(id)

        if pedido:

            self.pedidos.remove(pedido)

        return pedido