from infrastructure.database.connection import SessionLocal
from infrastructure.models.pedido_model import PedidoModel

from domain.interfaces.pedido_repository_interface import (
    PedidoRepositoryInterface
)


class PedidoRepository(PedidoRepositoryInterface):

    def salvar(self, cliente, pizza, quantidade):

        db = SessionLocal()

        pedido = PedidoModel(
            cliente=cliente,
            pizza=pizza,
            quantidade=quantidade
        )

        db.add(pedido)
        db.commit()
        db.refresh(pedido)
        db.close()

        return pedido

    def listar(self):

        db = SessionLocal()

        pedidos = db.query(PedidoModel).all()

        db.close()

        return pedidos

    def buscar_por_id(self, id):

        db = SessionLocal()

        pedido = db.query(PedidoModel).filter(
            PedidoModel.id == id
        ).first()

        db.close()

        return pedido

    def atualizar(self, id, cliente, pizza, quantidade):

        db = SessionLocal()

        pedido = db.query(PedidoModel).filter(
            PedidoModel.id == id
        ).first()

        if pedido:
            pedido.cliente = cliente
            pedido.pizza = pizza
            pedido.quantidade = quantidade

            db.commit()
            db.refresh(pedido)

        db.close()

        return pedido

    def deletar(self, id):

        db = SessionLocal()

        pedido = db.query(PedidoModel).filter(
            PedidoModel.id == id
        ).first()

        if pedido:
            db.delete(pedido)
            db.commit()

        db.close()

        return pedido